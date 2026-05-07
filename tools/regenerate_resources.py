#!/usr/bin/env python3
"""
Regenerate Resources pages with branded template header/footer.
Applies to desktop, mobile, and tablet variants.
"""

from pathlib import Path
from textwrap import dedent
import json

# Define resources content
RESOURCES = [
    {
        "title": "Seasonal Yard Checklist",
        "description": "A practical spring-to-winter checklist so your property stays healthy year-round."
    },
    {
        "title": "Lawn Health Basics",
        "description": "Simple watering, fertilization, and mowing patterns that prevent stress and bare patches."
    },
    {
        "title": "Drainage Warning Signs",
        "description": "How to spot pooling, runoff paths, and soft spots before they become expensive repairs."
    },
    {
        "title": "Outdoor Living Planning",
        "description": "Budget and phasing advice for patios, retaining walls, and usable gathering space."
    }
]

# Brand colors from CSS
COLORS = {
    "primary_green": "rgba(40, 102, 18, 1)",
    "primary_orange": "rgba(248, 111, 4, 1)",
    "secondary_orange": "rgba(205, 75, 14, 1)",
    "light_gray": "rgba(244, 244, 244, 1)",
    "dark_gray": "rgba(36, 36, 36, 1)",
    "white": "rgba(255, 255, 255, 1)",
}

def build_hero_section():
    """Build the hero/header section with branding."""
    return dedent(f"""
    <div class="flex-element group" data-auto="flex-element-group">
        <div class="flex-element group" data-auto="flex-element-group">
            <div class="flex-element widget-wrapper" data-auto="flex-element-widget-wrapper" data-widget-type="paragraph" data-external-id="1268622482">
                <div class="dmNewParagraph" data-element-type="paragraph" data-version="5" id="1268622482" style="">
                    <h1 class="m-text-align-left text-align-center" style="">
                        <span style="display: unset; color: var(--color_1);">Landscaping Resources</span>
                    </h1>
                    <p style="text-align: center; color: var(--color_7);">Useful planning references from Better Than Before LawnCare & Landscaping. Use these to budget projects, prep for seasonal changes, and avoid preventable yard issues.</p>
                </div>
            </div>
            <div class="flex-element widget-wrapper" data-auto="flex-element-widget-wrapper" data-widget-type="link">
                <a data-display-type="block" class="align-center dmButtonLink dmWidget dmWwr default dmOnlyButton dmDefaultGradient flexButton" href="../contact/">
                    <span class="iconBg" aria-hidden="true"><span class="icon hasFontIcon icon-star"></span></span>
                    <span class="text">Ask a Project Question</span>
                </a>
            </div>
            <div class="flex-element widget-wrapper" data-auto="flex-element-widget-wrapper" data-widget-type="link">
                <a data-display-type="block" class="align-center dmButtonLink dmWidget dmWwr default dmSecondaryButton flexButton" href="../services/">
                    <span class="iconBg" aria-hidden="true"><span class="icon hasFontIcon icon-star"></span></span>
                    <span class="text">Browse Services</span>
                </a>
            </div>
        </div>
    </div>
    """).strip()

def build_resources_grid():
    """Build the resources cards grid."""
    cards = []
    for resource in RESOURCES:
        cards.append(f"""
    <article class="card">
        <h2>{resource["title"]}</h2>
        <p>{resource["description"]}</p>
    </article>""")
    
    return dedent("""
    <div class="grid">""") + "".join(cards) + dedent("""
    </div>
    """).strip()

def build_resources_html(device_type="desktop"):
    """Build complete Resources page HTML."""
    
    # Determine relative paths based on device type
    if device_type == "desktop":
        relative_depth = "../"
    elif device_type in ["mobile", "tablet"]:
        relative_depth = "../../../"
    else:
        relative_depth = "../"
    
    # Check if we need simplified or full template
    # For now, use simplified custom HTML with branding colors
    html = f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Resources | Better Than Before Landscaping</title>
  <meta name="description" content="Landscaping guides, seasonal checklists, and practical planning resources for Sparta and Rockford homeowners.">
  <link rel="canonical" href="https://www.betterthanbeforelawncareandlandscaping.com/resources">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.betterthanbeforelawncareandlandscaping.com/resources">
  <meta property="og:title" content="Resources | Better Than Before Landscaping">
  <meta property="og:description" content="Landscaping guides, seasonal checklists, and practical planning resources for Sparta and Rockford homeowners.">
  <meta property="og:image" content="https://www.betterthanbeforelawncareandlandscaping.com/Resources/images/shutterstock_1463795483-1920w.jpg">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="Resources | Better Than Before Landscaping">
  <meta name="twitter:description" content="Landscaping guides, seasonal checklists, and practical planning resources for Sparta and Rockford homeowners.">
  <meta name="twitter:image" content="https://www.betterthanbeforelawncareandlandscaping.com/Resources/images/shutterstock_1463795483-1920w.jpg">
  <style>
    :root {{
      --earth: #3d2d22;
      --olive: #617e34;
      --accent: #d7872f;
      --ink: #1f1d1a;
      --color_1: rgba(40, 102, 18, 1);
      --color_2: rgba(248, 111, 4, 1);
      --color_7: rgba(36, 36, 36, 1);
      --color_8: rgba(255, 255, 255, 1);
    }}
    * {{ box-sizing: border-box; }}
    body {{ 
      margin: 0; 
      color: var(--ink); 
      font-family: Georgia, "Times New Roman", serif; 
      background: linear-gradient(180deg, #fbf7ef 0%, #f2ede3 100%);
    }}
    header.branded-header {{
      background: var(--color_8);
      border-bottom: 1px solid #e0e0e0;
      padding: 12px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .logo {{ height: 40px; }}
    .branded-header nav {{ display: flex; gap: 24px; align-items: center; }}
    .branded-header a {{ text-decoration: none; color: var(--color_7); font-size: 14px; }}
    .phone-btn {{
      background: var(--color_2);
      color: white;
      padding: 8px 16px;
      border-radius: 4px;
      text-decoration: none;
      font-weight: bold;
    }}
    .hero {{
      background: linear-gradient(120deg, rgba(61,45,34,.95), rgba(97,126,52,.9));
      color: #fff;
      padding: 70px 20px 52px;
    }}
    .wrap {{
      width: min(1020px, 92vw);
      margin: 0 auto;
    }}
    h1 {{
      margin: 0 0 10px;
      font-size: clamp(2rem, 4.5vw, 3.1rem);
    }}
    p {{ line-height: 1.6; }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 14px;
      margin: 24px 0 10px;
    }}
    .card {{
      background: #fff;
      border: 1px solid #e4dac9;
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 8px 22px rgba(40, 29, 20, .08);
    }}
    .card h2 {{
      margin: 0 0 8px;
      font-size: 1.08rem;
      color: var(--earth);
    }}
    .actions {{
      margin-top: 18px;
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .btn {{
      display: inline-block;
      text-decoration: none;
      border-radius: 999px;
      padding: 10px 15px;
      font-weight: 700;
      border: none;
      cursor: pointer;
    }}
    .btn.primary {{
      background: var(--color_2);
      color: #22170e;
    }}
    .btn.secondary {{
      border: 1px solid #d7ccb9;
      color: #2c2722;
      background: #fff;
    }}
    section {{ padding: 28px 20px 56px; }}
    footer {{
      background: var(--color_7);
      color: var(--color_8);
      text-align: center;
      padding: 32px 20px;
      font-size: 13px;
    }}
    footer a {{ color: var(--color_8); }}
  </style>
  <link href="/Style/{device_type}.css" rel="stylesheet" type="text/css"/>
</head>
<body data-page-alias="resources">
  <!-- Branded Header -->
  <header class="branded-header">
    <div class="wrap" style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
      <a href="../home/" style="text-decoration: none;">
        <img src="/Resources/images/imgi_2_573064202_17847239943596787_1118510838133176993_n-1920w.jpg" alt="Better Than Before Logo" class="logo">
      </a>
      <nav>
        <a href="../home/">Home</a>
        <a href="../about-us/">About Us</a>
        <a href="../services/">Our Services</a>
        <a href="../gallery/">Gallery</a>
        <a href="../contact/">Contact Us</a>
        <a href="tel:(616) 821-6876" class="phone-btn">(616) 821-6876</a>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="wrap">
      <h1>Landscaping Resources</h1>
      <p>Useful planning references from Better Than Before LawnCare & Landscaping. Use these to budget projects, prep for seasonal changes, and avoid preventable yard issues.</p>
      <div class="actions">
        <a class="btn primary" href="../contact/">Ask a Project Question</a>
        <a class="btn secondary" href="../services/">Browse Services</a>
      </div>
    </div>
  </section>

  <!-- Resources Content -->
  <section>
    <div class="wrap">
      <div class="grid">
        <article class="card">
          <h2>Seasonal Yard Checklist</h2>
          <p>A practical spring-to-winter checklist so your property stays healthy year-round.</p>
        </article>
        <article class="card">
          <h2>Lawn Health Basics</h2>
          <p>Simple watering, fertilization, and mowing patterns that prevent stress and bare patches.</p>
        </article>
        <article class="card">
          <h2>Drainage Warning Signs</h2>
          <p>How to spot pooling, runoff paths, and soft spots before they become expensive repairs.</p>
        </article>
        <article class="card">
          <h2>Outdoor Living Planning</h2>
          <p>Budget and phasing advice for patios, retaining walls, and usable gathering space.</p>
        </article>
      </div>
      <div class="actions" style="justify-content: center;">
        <a class="btn secondary" href="../areas-we-serve/">Areas We Serve</a>
        <a class="btn secondary" href="../gallery/">Project Gallery</a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="wrap">
      <p>&copy; 2026 Better Than Before LawnCare & Landscaping | All Rights Reserved</p>
      <p>Sparta, MI 49345 | <a href="tel:(616) 821-6876">(616) 821-6876</a></p>
    </div>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      const currentYear = new Date().getFullYear();
      document.querySelector('footer p').textContent = '\u00a9 ' + currentYear + ' Better Than Before LawnCare & Landscaping | All Rights Reserved';
    }});
  </script>
</body>
</html>
"""
    return html

def main():
    """Regenerate Resources pages for all device types."""
    base_path = Path("/workspaces/landscaping/Pages")
    
    device_types = ["desktop", "mobile", "tablet"]
    
    for device in device_types:
        output_path = base_path / device / "resources" / "index.html"
        
        # Create directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Generate and write HTML
        html_content = build_resources_html(device)
        output_path.write_text(html_content)
        
        print(f"✓ Regenerated {device} Resources page: {output_path}")
    
    print("\n✓ All Resources pages regenerated with branded header/footer!")

if __name__ == "__main__":
    main()
