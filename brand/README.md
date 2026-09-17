# AlexisSantos.dev brand kit

This folder is the reusable source of truth for the studio identity. Version 2, September 2026. It follows the website's approved pearl-and-charcoal direction with the selected direction 04: a custom forward-leaning AS monogram with a diagonal cut.

## Start here

Open `index.html` for the visual overview, or `brand-guide.pdf` for the six-page guide. `alexissantos-brand-kit.zip` is the portable handoff.

- `logos/`: 12 outlined SVG variants. `logo-*` pairs symbol and name; `wordmark-*` is the name alone; `symbol-*` is the AS monogram; `stacked-*` is for covers and card fronts. Charcoal, white and black versions. PNG exports have transparent backgrounds.
- `fonts/`: Manrope and DM Sans, variable fonts plus static print weights, with original SIL Open Font Licences.
- `tokens.json`: colour values, typography, logo paths and ES/EN taglines for future design work.
- `templates/`: four editable business-card SVGs and two editable A5 flyer SVGs. Install the bundled fonts before editing live text. Logo lettering is already outlined.
- `print/business-cards-es-en.pdf`: Spanish front/back followed by English front/back. Finished size 85 × 55 mm, 3 mm bleed on each edge, 91 × 61 mm page size.
- `print/flyers-a5-es-en.pdf`: Spanish then English. Finished size 148 × 210 mm, 3 mm bleed, 154 × 216 mm page size.
- `source/build-brand.py`: generates the vector artwork, tokens, fonts and PDFs. Dependencies: fonttools, brotli, reportlab, svglib, pypdf and qrcode. It also publishes the website's logo, favicon and self-hosted fonts to `assets/studio/`.

## Rules to keep it recognisable

Use the supplied logos instead of typing a replacement. Keep a clear margin of at least one quarter of the symbol height. Full logo minimum: 180 px or 38 mm. Symbol minimum: 32 px or 8 mm. Use the supplied favicon for browser tabs.

Charcoal `#20242B`, pearl `#F5F6F8`, slate `#606977`, blue `#496F99`, mist `#DCE0E6`. Blue is an accent; the boldness comes from scale and typography. Charcoal or black on light backgrounds; white on dark backgrounds. Do not stretch, outline, add a drop shadow, or recolour the symbol arbitrarily.

Headlines: Manrope ExtraBold. Body and contact details: DM Sans. The AS silhouette can become an oversized cropped background motif; never crop the primary logo.

ES: Diseño con intención. Tecnología con impacto.
EN: Design with purpose. Technology with impact.

Write in Alexis's first-person voice. Explain business outcomes without promises of guaranteed results. Never invent customers, team size, phone numbers or an address. Breathe Now and Lean Cam retain their own product identities.

## Print handoff

The PDFs include TrimBox and BleedBox. Print at 100%. Fonts are embedded or outlined. They use RGB master colours and are not certified PDF/X. Before a production run, the printer should supply its ICC profile, stock and export requirements. Keep the 3 mm bleed and 5 mm inner safe margin. The QR codes lead to the Spanish or English website; use the appropriate language pages. The English destination requires publishing the new /en/ site before distributing the printed material.

## Website relationship

The website uses copies of the primary logo and favicon under `assets/studio/`, plus the same locally hosted fonts. The `brand/` source folder is excluded from public Cloudflare assets. Updating the brand source does not deploy the website.

Font sources: https://github.com/google/fonts/tree/main/ofl/manrope and https://github.com/google/fonts/tree/main/ofl/dmsans. Preserve the licence files when redistributing fonts.
