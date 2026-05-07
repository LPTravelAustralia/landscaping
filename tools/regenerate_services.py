from pathlib import Path
from textwrap import dedent


SITE_ROOT = Path(__file__).resolve().parents[1]
DEVICE_DIRS = ["desktop", "tablet", "mobile"]
SITE_URL = "https://www.betterthanbeforelawncareandlandscaping.com"
PHONE = "(616) 821-6876"
PHONE_LINK = "tel:(616)821-6876"
LOGO_PATH = "/Resources/images/imgi_2_573064202_17847239943596787_1118510838133176993_n-1920w.jpg"
HERO_IMAGE = "/Resources/images/shutterstock_1789023152-2880w.jpg"
SERVICE_TITLE_SUFFIX = "Better Than Before"

SERVICES = [
    {
        "slug": "lawn-turf-care",
        "title": "Lawn & Turf Care",
        "summary": "Weekly mowing, edging, fertilization, and seasonal turf health programs tailored to your yard.",
        "detail": "Reliable weekly maintenance, turf feeding plans, and proactive clean edging that keep the property looking sharp from curb to backyard.",
        "points": [
            "Recurring mowing and trimming schedules built around growth rate and property layout.",
            "Seasonal turf treatments that support density, color, and long-term lawn health.",
            "Clean-up passes after each visit so the finished result looks intentional, not rushed.",
        ],
    },
    {
        "slug": "seasonal-cleanup-specialty-services",
        "title": "Seasonal Cleanup & Specialty Services",
        "summary": "Spring and fall cleanups, mulch refreshes, pruning, and one-time property reset services.",
        "detail": "Ideal for bringing order back to the landscape after winter, storm activity, or an overgrown stretch of the season.",
        "points": [
            "Leaf removal, bed clean-outs, and debris hauling that reset the property quickly.",
            "Mulch and pruning work timed to improve appearance without stressing plant material.",
            "One-time cleanups for listings, events, or properties that need a fast visual upgrade.",
        ],
    },
    {
        "slug": "full-landscape-design",
        "title": "Full Landscape Design",
        "summary": "Concept-to-install plans with plant selection, grading strategy, and phased implementation options.",
        "detail": "We turn rough ideas into a buildable plan that balances curb appeal, maintenance demands, drainage, and budget.",
        "points": [
            "Layout planning for beds, screening, circulation, and focal points.",
            "Plant and material recommendations that fit the site and maintenance expectations.",
            "Phased planning when the full project needs to be installed in deliberate stages.",
        ],
    },
    {
        "slug": "patios-outdoor-living",
        "title": "Patios & Outdoor Living",
        "summary": "Patio installation, outdoor gathering spaces, and practical upgrades that extend living outdoors.",
        "detail": "Outdoor spaces should feel useful and durable, not just decorative, so we prioritize layout, flow, and longevity.",
        "points": [
            "Patio and seating layouts sized for real use and comfortable circulation.",
            "Material selections that fit the house style and expected wear.",
            "Add-on features that make the space easier to use through more of the year.",
        ],
    },
    {
        "slug": "retaining-walls-hardscaping",
        "title": "Retaining Walls & Hardscaping",
        "summary": "Retaining walls, paver paths, and hardscape elements engineered for durability and curb appeal.",
        "detail": "These projects have to look finished and stay stable, so grading, base prep, and drainage matter as much as the surface materials.",
        "points": [
            "Wall and paver work designed around elevation change and daily use.",
            "Structural prep that helps prevent movement, washout, and premature failure.",
            "Hardscape details that connect cleanly into beds, lawns, and entry points.",
        ],
    },
    {
        "slug": "drainage-grading",
        "title": "Drainage & Grading",
        "summary": "Water management and grading solutions to protect foundations and eliminate standing water issues.",
        "detail": "When runoff is controlled correctly, the rest of the landscape performs better and the property stays usable after weather events.",
        "points": [
            "Drainage corrections for low spots, pooling water, and soft turf areas.",
            "Grading improvements that move water away from structures and hardscapes.",
            "Practical solutions sized for the site instead of overbuilding the fix.",
        ],
    },
    {
        "slug": "tree-shrub-care",
        "title": "Tree & Shrub Care",
        "summary": "Plant health care, strategic trimming, and seasonal maintenance for long-term growth and structure.",
        "detail": "Healthy structure and predictable growth come from trimming with a purpose, not just cutting things back.",
        "points": [
            "Selective trimming to preserve shape, visibility, and plant health.",
            "Seasonal maintenance to keep shrubs tidy without over-pruning.",
            "Care recommendations that support screening, curb appeal, and long-term vigor.",
        ],
    },
    {
        "slug": "residential-snow-removal",
        "title": "Residential Snow Removal",
        "summary": "Dependable residential snow clearing and de-icing for safe winter access.",
        "detail": "Fast, clear response matters in winter, especially for driveways, walks, and high-use access points around the home.",
        "points": [
            "Driveway and walkway clearing focused on safe daily access.",
            "De-icing support where slip risk or refreeze is a recurring concern.",
            "Residential service designed for consistency through Michigan winter conditions.",
        ],
    },
    {
        "slug": "commercial-snow-contracts",
        "title": "Commercial Snow Contracts",
        "summary": "Priority winter response, plowing, and ice management for commercial properties.",
        "detail": "Commercial winter work depends on response planning, clear scopes, and dependable site access when conditions change fast.",
        "points": [
            "Plowing and ice-management plans sized to property access and traffic flow.",
            "Priority service expectations established before the season begins.",
            "Winter support for businesses that need dependable entrances, lots, and walkways.",
        ],
    },
]


def minify_html(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines()) + "\n"


def nav_links(prefix: str, active: str) -> str:
    links = [
        (f"{prefix}home/", "Home", False),
        (f"{prefix}about-us/", "About Us", False),
        (f"{prefix}services/", "Our Services", active == "services"),
        (f"{prefix}gallery/", "Gallery", False),
        (f"{prefix}contact/", "Contact Us", False),
    ]
    items = []
    for href, label, selected in links:
        klass = "nav-link is-active" if selected else "nav-link"
        items.append(f'<a class="{klass}" href="{href}">{label}</a>')
    return "".join(items)


def service_cards(prefix: str) -> str:
    cards = []
    for service in SERVICES:
        cards.append(
            f"<article class=\"service-card\"><h2><a href=\"{prefix}{service['slug']}/\">{service['title']}</a></h2><p>{service['summary']}</p><a class=\"service-link\" href=\"{prefix}{service['slug']}/\">Explore service</a></article>"
        )
    return "".join(cards)


def service_list(prefix: str, current_slug: str) -> str:
    items = []
    for service in SERVICES:
        klass = "service-list-link is-current" if service["slug"] == current_slug else "service-list-link"
        items.append(f'<a class="{klass}" href="{prefix}{service["slug"]}/">{service["title"]}</a>')
    return "".join(items)


def shared_styles() -> str:
    return dedent(
        f"""
        :root {{
          --brand-green: rgba(40, 102, 18, 1);
          --brand-orange: rgba(248, 111, 4, 1);
          --brand-orange-dark: rgba(205, 75, 14, 1);
          --brand-cream: rgba(244, 244, 244, 1);
          --brand-ink: rgba(36, 36, 36, 1);
          --brand-white: rgba(255, 255, 255, 0.97);
          --brand-shadow: 0 22px 60px rgba(36, 36, 36, 0.12);
          --content-width: 1180px;
        }}
        * {{ box-sizing: border-box; }}
        html {{ scroll-behavior: smooth; }}
        body {{
          margin: 0;
          font-family: Arial, Helvetica, sans-serif;
          color: var(--brand-ink);
          background:
            radial-gradient(circle at top left, rgba(248, 111, 4, 0.12), transparent 28%),
            linear-gradient(180deg, #fff 0%, #fbf8f2 52%, #f3efe7 100%);
        }}
        a {{ color: inherit; }}
        img {{ display: block; max-width: 100%; height: auto; }}
        .page-shell {{ min-height: 100vh; }}
        .wrap {{ width: min(var(--content-width), calc(100vw - 32px)); margin: 0 auto; }}
        .site-header {{
          position: sticky;
          top: 0;
          z-index: 20;
          background: rgba(255, 255, 255, 0.96);
          backdrop-filter: blur(12px);
          border-bottom: 1px solid rgba(36, 36, 36, 0.08);
        }}
        .site-header .wrap {{
          display: grid;
          grid-template-columns: auto 1fr auto;
          align-items: center;
          gap: 24px;
          padding: 18px 0;
        }}
        .brand-mark {{ display: inline-flex; align-items: center; }}
        .brand-mark img {{ width: clamp(140px, 14vw, 170px); }}
        .site-nav {{ display: flex; justify-content: center; flex-wrap: wrap; gap: 24px; }}
        .nav-link {{
          text-decoration: none;
          color: var(--brand-ink);
          font-size: 0.98rem;
          transition: color 160ms ease;
        }}
        .nav-link:hover,
        .nav-link.is-active {{ color: var(--brand-orange); }}
        .call-button {{
          display: inline-flex;
          align-items: center;
          justify-content: center;
          min-width: 196px;
          padding: 14px 20px;
          border-radius: 8px;
          background: var(--brand-orange);
          color: #23160a;
          text-decoration: none;
          font-weight: 700;
          box-shadow: 0 10px 24px rgba(248, 111, 4, 0.24);
        }}
        .hero {{
          position: relative;
          overflow: hidden;
          background: linear-gradient(90deg, rgba(36, 36, 36, 0.74), rgba(40, 102, 18, 0.66)), url('{HERO_IMAGE}') center/cover no-repeat;
          color: white;
        }}
        .hero::after {{
          content: "";
          position: absolute;
          inset: auto 0 0;
          height: 120px;
          background: linear-gradient(180deg, rgba(255,255,255,0), rgba(243,239,231,1));
          pointer-events: none;
        }}
        .hero .wrap {{ position: relative; z-index: 1; padding: 88px 0 112px; }}
        .eyebrow {{
          display: inline-block;
          margin-bottom: 18px;
          padding: 7px 12px;
          border-radius: 999px;
          background: rgba(255, 255, 255, 0.14);
          border: 1px solid rgba(255, 255, 255, 0.24);
          font-size: 0.84rem;
          letter-spacing: 0.08em;
          text-transform: uppercase;
        }}
        .hero h1 {{
          margin: 0;
          max-width: 14ch;
          font-size: clamp(2.2rem, 5.8vw, 4.3rem);
          line-height: 0.95;
          text-transform: uppercase;
        }}
        .hero p {{ max-width: 62ch; font-size: 1.06rem; line-height: 1.7; }}
        .hero-actions {{ display: flex; flex-wrap: wrap; gap: 14px; margin-top: 28px; }}
        .button {{
          display: inline-flex;
          align-items: center;
          justify-content: center;
          min-height: 48px;
          padding: 0 20px;
          border-radius: 10px;
          text-decoration: none;
          font-weight: 700;
        }}
        .button.primary {{ background: var(--brand-orange); color: #20150b; }}
        .button.secondary {{ background: rgba(255, 255, 255, 0.94); color: var(--brand-ink); }}
        main {{ padding: 0 0 72px; }}
        .content-grid {{
          display: grid;
          grid-template-columns: minmax(0, 1.6fr) minmax(260px, 0.9fr);
          gap: 26px;
          margin-top: -44px;
          position: relative;
          z-index: 2;
        }}
        .panel {{
          background: rgba(255, 255, 255, 0.96);
          border: 1px solid rgba(36, 36, 36, 0.08);
          border-radius: 22px;
          box-shadow: var(--brand-shadow);
          padding: 30px;
        }}
        .panel h2,
        .panel h3 {{ margin-top: 0; }}
        .intro-copy {{ font-size: 1.02rem; line-height: 1.75; color: rgba(36, 36, 36, 0.84); }}
        .feature-list {{ display: grid; gap: 16px; margin-top: 24px; }}
        .feature-item {{
          padding: 18px 18px 18px 22px;
          border-left: 4px solid var(--brand-orange);
          background: linear-gradient(90deg, rgba(248, 111, 4, 0.08), rgba(248, 111, 4, 0));
          border-radius: 12px;
          line-height: 1.65;
        }}
        .service-grid {{
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
          gap: 18px;
          margin-top: 8px;
        }}
        .service-card {{
          border-radius: 18px;
          background: white;
          border: 1px solid rgba(36, 36, 36, 0.08);
          padding: 22px;
          box-shadow: 0 10px 30px rgba(36, 36, 36, 0.06);
        }}
        .service-card h2 {{ margin: 0 0 12px; font-size: 1.18rem; }}
        .service-card h2 a {{ text-decoration: none; color: var(--brand-green); }}
        .service-card p {{ margin: 0 0 18px; line-height: 1.65; color: rgba(36, 36, 36, 0.84); }}
        .service-link {{ color: var(--brand-orange-dark); font-weight: 700; text-decoration: none; }}
        .sidebar-stack {{ display: grid; gap: 18px; }}
        .service-list {{ display: grid; gap: 8px; }}
        .service-list-link {{
          text-decoration: none;
          padding: 12px 14px;
          border-radius: 12px;
          background: var(--brand-cream);
          color: rgba(36, 36, 36, 0.86);
        }}
        .service-list-link.is-current {{ background: rgba(40, 102, 18, 0.12); color: var(--brand-green); font-weight: 700; }}
        .note-box {{
          border-radius: 18px;
          background: linear-gradient(155deg, rgba(40, 102, 18, 0.96), rgba(205, 75, 14, 0.92));
          color: white;
          padding: 26px;
        }}
        .note-box p {{ margin: 0 0 16px; line-height: 1.65; }}
        .site-footer {{ padding: 0 0 46px; }}
        .footer-bar {{
          display: flex;
          justify-content: space-between;
          align-items: center;
          gap: 18px;
          border-top: 1px solid rgba(36, 36, 36, 0.08);
          padding-top: 24px;
          color: rgba(36, 36, 36, 0.72);
          font-size: 0.95rem;
        }}
        .footer-links {{ display: flex; flex-wrap: wrap; gap: 16px; }}
        .footer-links a {{ text-decoration: none; }}
        @media (max-width: 960px) {{
          .site-header .wrap {{ grid-template-columns: 1fr; justify-items: center; }}
          .content-grid {{ grid-template-columns: 1fr; }}
          .hero .wrap {{ padding: 68px 0 98px; }}
          .hero h1 {{ max-width: none; }}
        }}
        @media (max-width: 640px) {{
          .wrap {{ width: min(var(--content-width), calc(100vw - 20px)); }}
          .site-nav {{ gap: 14px; }}
          .panel {{ padding: 22px; border-radius: 18px; }}
          .footer-bar {{ flex-direction: column; align-items: flex-start; }}
        }}
        """
    ).strip()


def render_header(prefix: str, active: str) -> str:
    return dedent(
        f"""
        <header class="site-header">
          <div class="wrap">
            <a class="brand-mark" href="{prefix}home/" aria-label="Better Than Before home">
              <img src="{LOGO_PATH}" alt="Better Than Before Lawn Care & Landscaping logo" width="320" height="90">
            </a>
            <nav class="site-nav" aria-label="Primary">
              {nav_links(prefix, active)}
            </nav>
            <a class="call-button" href="{PHONE_LINK}">{PHONE}</a>
          </div>
        </header>
        """
    ).strip()


def render_footer(prefix: str) -> str:
    return dedent(
        f"""
        <footer class="site-footer">
          <div class="wrap footer-bar">
            <div>Better Than Before LawnCare & Landscaping serving Sparta, Rockford, and nearby West Michigan communities.</div>
            <div class="footer-links">
              <a href="{prefix}areas-we-serve/">Areas We Serve</a>
              <a href="{prefix}resources/">Resources</a>
              <a href="{prefix}contact/">Request Service</a>
            </div>
          </div>
        </footer>
        """
    ).strip()


def render_index(device: str) -> str:
    prefix = "../"
    title = f"Landscaping Services | {SERVICE_TITLE_SUFFIX}"
    description = "Browse our full landscaping and seasonal service lineup for Sparta and Rockford, MI."
    canonical = f"{SITE_URL}/services/"
    body = dedent(
        f"""
        <div class="page-shell">
          {render_header(prefix, 'services')}
          <section class="hero">
            <div class="wrap">
              <span class="eyebrow">Outdoor Care Catalog</span>
              <h1>Landscaping & Outdoor Services</h1>
              <p>From weekly turf care to hardscaping and winter response, these pages now sit inside the same branded experience as the rest of the site instead of dropping visitors into a detached layout.</p>
              <div class="hero-actions">
                <a class="button primary" href="{prefix}contact/">Request an Estimate</a>
                <a class="button secondary" href="{prefix}gallery/">See Project Gallery</a>
              </div>
            </div>
          </section>
          <main>
            <div class="wrap content-grid">
              <section class="panel">
                <h2>Built Around Real Property Needs</h2>
                <p class="intro-copy">Better Than Before LawnCare & Landscaping works across lawn maintenance, cleanup, design, drainage, hardscaping, plant care, and snow response. Use this hub to move into a specific service without losing the site header, navigation, or brand styling.</p>
                <div class="service-grid">{service_cards('./')}</div>
              </section>
              <aside class="sidebar-stack">
                <section class="panel">
                  <h3>Need Help Choosing?</h3>
                  <p class="intro-copy">If the property needs more than one improvement, start with an estimate request and we can scope the work in the right order.</p>
                  <div class="hero-actions">
                    <a class="button primary" href="{prefix}contact/">Get a Quote</a>
                    <a class="button secondary" href="{prefix}about-us/">About the Team</a>
                  </div>
                </section>
                <section class="note-box">
                  <h3>Seasonal Planning</h3>
                  <p>Spring cleanup, summer turf work, drainage corrections, and winter contracts all have different lead times. Early planning usually gives the cleanest scheduling options.</p>
                  <a class="button secondary" href="{prefix}resources/">Read Resources</a>
                </section>
              </aside>
            </div>
          </main>
          {render_footer(prefix)}
        </div>
        """
    ).strip()
    return render_document(title, description, canonical, description, body)


def render_detail(device: str, service: dict[str, object]) -> str:
    prefix = "../../"
    service_prefix = "../"
    title = f"{service['title']} | {SERVICE_TITLE_SUFFIX}"
    description = f"{service['title']} in Sparta and Rockford, MI. {service['summary']}"
    canonical = f"{SITE_URL}/services/{service['slug']}/"
    point_markup = "".join(f'<div class="feature-item">{point}</div>' for point in service["points"])
    body = dedent(
        f"""
        <div class="page-shell">
          {render_header(prefix, 'services')}
          <section class="hero">
            <div class="wrap">
              <span class="eyebrow">Service Detail</span>
              <h1>{service['title']}</h1>
              <p>{service['summary']}</p>
              <div class="hero-actions">
                <a class="button primary" href="{prefix}contact/">Get a Quote</a>
                <a class="button secondary" href="../">All Services</a>
              </div>
            </div>
          </section>
          <main>
            <div class="wrap content-grid">
              <section class="panel">
                <h2>How We Approach This Service</h2>
                <p class="intro-copy">{service['detail']}</p>
                <div class="feature-list">{point_markup}</div>
              </section>
              <aside class="sidebar-stack">
                <section class="panel">
                  <h3>All Services</h3>
                  <div class="service-list">{service_list(service_prefix, service['slug'])}</div>
                </section>
                <section class="note-box">
                  <h3>Next Step</h3>
                  <p>Tell us about the property, the timeline, and any problem spots. We can scope whether this service stands alone or should be bundled with related work.</p>
                  <a class="button secondary" href="{prefix}contact/">Request Service</a>
                </section>
              </aside>
            </div>
          </main>
          {render_footer(prefix)}
        </div>
        """
    ).strip()
    return render_document(title, description, canonical, description, body)


def render_document(title: str, description: str, canonical: str, social_description: str, body: str) -> str:
    html = dedent(
        f"""
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>{title}</title>
          <meta name="description" content="{description}">
          <link rel="canonical" href="{canonical}">
          <meta property="og:type" content="website">
          <meta property="og:url" content="{canonical}">
          <meta property="og:title" content="{title}">
          <meta property="og:description" content="{social_description}">
          <meta property="og:image" content="{SITE_URL}{HERO_IMAGE}">
          <meta name="twitter:card" content="summary_large_image">
          <meta name="twitter:title" content="{title}">
          <meta name="twitter:description" content="{social_description}">
          <meta name="twitter:image" content="{SITE_URL}{HERO_IMAGE}">
          <style>{shared_styles()}</style>
        </head>
        <body>
          {body}
        </body>
        </html>
        """
    )
    return minify_html(html)


def write_pages() -> None:
    for device in DEVICE_DIRS:
        base = SITE_ROOT / "Pages" / device / "services"
        (base / "index.html").write_text(render_index(device), encoding="utf-8")
        for service in SERVICES:
            target = base / service["slug"] / "index.html"
            target.write_text(render_detail(device, service), encoding="utf-8")


if __name__ == "__main__":
    write_pages()