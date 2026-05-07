#!/usr/bin/env python3

import argparse
import re
from collections import defaultdict
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def extract_first(pattern: str, text: str):
    m = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else None


def extract_all(pattern: str, text: str):
    return re.findall(pattern, text, flags=re.IGNORECASE | re.DOTALL)


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def get_meta_content(text: str, key: str, prop=False):
    if prop:
        pattern = rf'<meta[^>]+property=["\']{re.escape(key)}["\'][^>]*content=["\']([^"\']*)["\']'
    else:
        pattern = rf'<meta[^>]+name=["\']{re.escape(key)}["\'][^>]*content=["\']([^"\']*)["\']'
    v = extract_first(pattern, text)
    return normalize_space(v) if v else None


def audit_file(path: Path, text: str, domain: str):
    issues = []

    title = extract_first(r"<title[^>]*>(.*?)</title>", text)
    title = normalize_space(title) if title else None

    description = get_meta_content(text, "description")
    canonical = extract_first(r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', text)
    canonical = normalize_space(canonical) if canonical else None

    robots = get_meta_content(text, "robots")
    noindex = robots is not None and "noindex" in robots.lower()

    og_title = get_meta_content(text, "og:title", prop=True)
    og_desc = get_meta_content(text, "og:description", prop=True)
    og_image = get_meta_content(text, "og:image", prop=True)
    og_url = get_meta_content(text, "og:url", prop=True)
    og_type = get_meta_content(text, "og:type", prop=True)

    tw_card = get_meta_content(text, "twitter:card")
    tw_title = get_meta_content(text, "twitter:title")
    tw_desc = get_meta_content(text, "twitter:description")
    tw_image = get_meta_content(text, "twitter:image")

    h1_count = len(extract_all(r"<h1\b", text))

    if not title:
        issues.append(("error", "Missing title tag"))
    else:
        if len(title) < 30:
            issues.append(("warn", f"Title too short ({len(title)} chars)"))
        if len(title) > 60:
            issues.append(("warn", f"Title likely too long ({len(title)} chars)"))

    if not description:
        issues.append(("error", "Missing meta description"))
    else:
        if len(description) < 70:
            issues.append(("warn", f"Meta description too short ({len(description)} chars)"))
        if len(description) > 158:
            issues.append(("warn", f"Meta description likely too long ({len(description)} chars)"))

    if not canonical:
        issues.append(("error", "Missing canonical link"))
    else:
        if not canonical.startswith("https://"):
            issues.append(("error", f"Canonical is not HTTPS: {canonical}"))
        if domain and not canonical.startswith(domain):
            issues.append(("warn", f"Canonical outside configured domain: {canonical}"))

    if h1_count == 0:
        issues.append(("error", "Missing H1"))
    elif h1_count > 1:
        issues.append(("warn", f"Multiple H1 tags found ({h1_count})"))

    if not noindex:
        if not og_title:
            issues.append(("warn", "Missing og:title"))
        if not og_desc:
            issues.append(("warn", "Missing og:description"))
        if not og_image:
            issues.append(("warn", "Missing og:image"))
        if not og_url:
            issues.append(("warn", "Missing og:url"))
        if not og_type:
            issues.append(("warn", "Missing og:type"))

        if og_url and canonical and og_url.rstrip("/") != canonical.rstrip("/"):
            issues.append(("warn", "og:url does not match canonical"))

        if not tw_card:
            issues.append(("warn", "Missing twitter:card"))
        if not tw_title:
            issues.append(("warn", "Missing twitter:title"))
        if not tw_desc:
            issues.append(("warn", "Missing twitter:description"))
        if not tw_image:
            issues.append(("warn", "Missing twitter:image"))

    img_tags = extract_all(r"<img\b[^>]*>", text)
    missing_alt = 0
    empty_alt = 0
    missing_w = 0
    missing_h = 0

    for img in img_tags:
        has_alt = re.search(r"\balt=", img, flags=re.IGNORECASE)
        if not has_alt:
            missing_alt += 1
        else:
            val = extract_first(r"\balt=[\"\']([^\"\']*)[\"\']", img)
            if val is not None and val.strip() == "":
                empty_alt += 1

        if not re.search(r"\bwidth=[\"\']?\d+", img, flags=re.IGNORECASE):
            missing_w += 1
        if not re.search(r"\bheight=[\"\']?\d+", img, flags=re.IGNORECASE):
            missing_h += 1

    if missing_alt:
        issues.append(("warn", f"Images missing alt attributes: {missing_alt}"))
    if empty_alt:
        issues.append(("warn", f"Images with empty alt text: {empty_alt}"))
    if missing_w:
        issues.append(("warn", f"Images missing width attribute: {missing_w}"))
    if missing_h:
        issues.append(("warn", f"Images missing height attribute: {missing_h}"))

    return {
        "path": str(path),
        "title": title,
        "description": description,
        "canonical": canonical,
        "noindex": noindex,
        "issues": issues,
    }


def render_report(results):
    errors = 0
    warns = 0
    lines = ["# SEO Audit Report", ""]

    for row in results:
        row_errors = [i for i in row["issues"] if i[0] == "error"]
        row_warns = [i for i in row["issues"] if i[0] == "warn"]
        errors += len(row_errors)
        warns += len(row_warns)

    lines.append(f"Total files audited: {len(results)}")
    lines.append(f"Errors: {errors}")
    lines.append(f"Warnings: {warns}")
    lines.append("")

    for row in results:
        lines.append(f"## {row['path']}")
        lines.append("")
        lines.append(f"- Canonical: {row['canonical'] or 'MISSING'}")
        lines.append(f"- Noindex: {'yes' if row['noindex'] else 'no'}")
        lines.append(f"- Title: {row['title'] or 'MISSING'}")
        lines.append("")

        if not row["issues"]:
            lines.append("- PASS: No issues detected by local checks.")
        else:
            for severity, msg in row["issues"]:
                lines.append(f"- {severity.upper()}: {msg}")
        lines.append("")

    return "\n".join(lines), errors, warns


def main():
    parser = argparse.ArgumentParser(description="Audit local HTML files for basic SEO rules.")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--domain", default="", help="Expected canonical domain prefix")
    parser.add_argument("--output", default="reports/seo-audit.md", help="Markdown report output path")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    html_files = sorted(root.glob("**/*.html"))

    results = []
    title_index = defaultdict(list)
    desc_index = defaultdict(list)

    for f in html_files:
        text = read_text(f)
        row = audit_file(f.relative_to(root), text, args.domain.rstrip("/"))
        results.append(row)
        if row["title"]:
            title_index[row["title"]].append(row["path"])
        if row["description"]:
            desc_index[row["description"]].append(row["path"])

    # Duplicate checks should only flag cross-canonical collisions.
    for title, files in title_index.items():
        if len(files) > 1:
            canonical_set = {
                (row["canonical"] or row["path"])
                for row in results
                if row["path"] in files
            }
            if len(canonical_set) <= 1:
                continue
            for row in results:
                if row["path"] in files:
                    row["issues"].append(
                        ("warn", f"Duplicate title across canonical URLs ({len(canonical_set)} canonicals)")
                    )

    for desc, files in desc_index.items():
        if len(files) > 1:
            canonical_set = {
                (row["canonical"] or row["path"])
                for row in results
                if row["path"] in files
            }
            if len(canonical_set) <= 1:
                continue
            for row in results:
                if row["path"] in files:
                    row["issues"].append(
                        (
                            "warn",
                            f"Duplicate meta description across canonical URLs ({len(canonical_set)} canonicals)",
                        )
                    )

    report, errors, warns = render_report(results)
    out_path = Path(args.output)
    if not out_path.is_absolute():
        out_path = root / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")

    print(f"Audited {len(results)} files")
    print(f"Errors: {errors}")
    print(f"Warnings: {warns}")
    print(f"Report: {out_path}")

    # Fail CI only for hard errors.
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
