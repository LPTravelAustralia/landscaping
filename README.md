# landscaping
landscping web preview

## SEO workflow

This repository includes a baseline SEO governance setup for static page auditing.

### Files added

- `SEO_GUIDELINES_REFERENCE.md`: universal SEO standards reference used by this project.
- `tools/seo_audit.py`: local static audit for HTML metadata/indexability checks.
- `robots.txt`: crawler policy including major search and AI retrieval/training bots.
- `sitemap.xml`: canonical URL sitemap for public indexable routes.

### Run the audit

```bash
python3 tools/seo_audit.py \
	--root . \
	--domain https://www.betterthanbeforelawncareandlandscaping.com \
	--output reports/seo-audit.md
```

The script prints a summary and writes a markdown report with issues by file.
