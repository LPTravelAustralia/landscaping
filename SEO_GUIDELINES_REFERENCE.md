# SEO Guidelines Reference - Universal Standard

Last reviewed: May 2026
Applies to: All page types, all platforms
Sources: Google Search Central, Bing Webmaster Guidelines, Ahrefs Site Audit, schema.org

## Important framing

These are best-practice targets and audit-tool standards, not guaranteed ranking factors.
Google and Bing visibility depends on content usefulness, crawlability, indexability,
link authority, and freshness.

Priority: fix crawl/index conflicts first, metadata second, content quality always.

## 1) On-page targets

- Title: target 50-60 chars, unique per page.
- Meta description: target 120-158 chars, unique per page.
- H1: exactly one per page, aligned to topic.
- Heading structure: H1 -> H2 -> H3 without skipping.
- Images: descriptive alt text, explicit width and height.
- H1 and title should align closely but do not need to be identical.

## 2) Canonicals

Every indexable page needs a self-referencing canonical to clean production HTTPS URL.
Avoid staging domains, redirects, non-200 canonicals, and multiple canonicals.

Example:

```html
<link rel="canonical" href="https://yourdomain.com/page-slug" />
```

## 3) Robots rules

Critical rule: robots.txt and noindex must not conflict.

If a page is blocked in robots.txt, crawlers may not read its noindex tag.
Use noindex (with crawl allowed) for pages that should not be indexed.

Use robots.txt disallow only for resources that must not be crawled.

## 4) Sitemap rules

- Include only canonical, indexable, HTTP 200 URLs.
- Exclude noindex, redirects, parameter/faceted URLs, session/checkout pages.
- Keep one sitemap unless 50,000+ URLs.
- Reference sitemap in robots.txt.
- Update lastmod only when meaningful page changes occur.

## 5) Open Graph and social metadata

Required for all indexable pages:

- og:title
- og:description
- og:image (recommended 1200x630)
- og:url (must match canonical)
- og:type
- twitter:card
- twitter:title
- twitter:description
- twitter:image

## 6) Core Web Vitals targets

- LCP < 2.5s
- CLS < 0.1
- INP < 200ms
- TTFB < 800ms

Common fixes:

- set image width and height
- preload above-the-fold hero image
- defer non-critical JS
- use CDN caching and immutable cache headers for hashed assets

## 7) Structured data principles

- Use JSON-LD.
- Mark up only what is visibly present on the page.
- Keep schema type relevant to page type.
- Validate with Schema Validator and Google Rich Results Test.

Recommended by page type (examples):

- Homepage: Organization + WebSite
- Landing/category: WebPage + BreadcrumbList
- Article: Article/BlogPosting + BreadcrumbList
- FAQ: FAQPage + BreadcrumbList (answers must be visible)

## 8) Indexability standards by URL type

- Index static editorial, stable service, about/contact/legal, and article pages.
- Noindex search-result/filter/parameter pages.
- Noindex checkout, payment, confirmation, account, profile, dashboard.
- Keep duplicate URL variants canonicalized to preferred URL.

## 9) Dynamic rendering and parity

If bot rendering is used, bot HTML must match user-visible content.
Do not add bot-only keyword blocks, links, or schema not visible to users.

## 10) GSC and Bing operations

- Submit sitemap to Google Search Console and Bing Webmaster Tools.
- Resolve coverage conflicts (noindex-in-sitemap, duplicate without canonical, 5xx).
- Use URL inspection for critical templates.

## 11) AI crawler policy

Allow retrieval/indexing bots for citation visibility:

- Googlebot, Bingbot
- OAI-SearchBot, ChatGPT-User
- PerplexityBot, Perplexity-User
- Claude-User
- CCBot

Allow or block training bots based on content licensing policy:

- GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, Bytespider

Note: retrieval bots and training bots serve different purposes.

## 12) Priority order for fixes

P0 crawl/index conflicts:

- robots/noindex conflicts
- noindex URLs in sitemap
- invalid canonical targets
- bot/user content mismatch

P1 page integrity:

- broken links
- redirect chains
- duplicate clusters without canonical strategy
- non-200 key pages

P2 on-page quality:

- missing/duplicate titles, descriptions, H1
- thin important pages
- missing alt text
- missing image dimensions

P3 enhancement:

- schema improvements
- CWV optimization
- AI discovery files and AI citation monitoring

## 13) Programmatic page quality minimum

For any templated or generated page, require:

- unique title
- unique meta description
- unique H1
- substantial useful content
- real internal linking
- no pure boilerplate pages

If quality is not met, use noindex until improved.

## 14) Internal linking standards

- ensure each important page has multiple dofollow internal links
- avoid orphan pages
- use descriptive anchor text (avoid "click here")
- avoid nofollow on internal links

## 15) Monitoring cadence

Weekly:

- site audit issues
- coverage changes
- query/CTR regressions
- AI citation trends (if tracked)

Monthly:

- full crawl
- structured data revalidation
- backlink and ranking movement checks

## Quick per-page launch checklist

- unique title and description in target ranges
- one H1 aligned to topic
- clean self canonical
- correct robots meta for page type
- complete OG/Twitter tags
- valid relevant schema
- indexable pages present in sitemap
- noindex pages excluded from sitemap
- image alt + width + height
- internal links from relevant pages
- mobile render at 375px tested
