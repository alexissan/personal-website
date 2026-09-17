# Brand source of truth

The reusable brand kit now lives in `brand/`. Start with `brand/README.md`, `brand/index.html`, and `brand/brand-guide.pdf`. Logos, fonts, colours and printable templates are maintained there. The website uses its exported assets.

## Website implementation notes

Build: python3 scripts/build-studio.py regenerates the Spanish and English consultancy pages. The website leads with AI integration and process automation; websites and apps are supporting delivery capabilities. Styles and behaviour live in assets/studio/. The contact form opens a mail draft; it does not send or store submissions. Existing articles and standalone app pages retain their original language and URLs.

Verification covers Spanish and English navigation and metadata, desktop and mobile layouts, product dialogs, mobile menu behaviour, contact validation, local routes and assets, JavaScript syntax, and whitespace checks.

## Showcase system

`scripts/build-studio.py` contains the bilingual `SHOWCASE` content model and generates the showcase alongside the homepages. The public routes are `/showcase/`, `/en/showcase/`, `/showcase/nexo-mantenimiento/`, and `/en/showcase/nexo-maintenance/`. Showcase-specific layout, interaction, and images live in `assets/showcase/`.

Every concept without a real client engagement must be visibly labelled `Caso ficticio` or `Fictional case`. Do not add invented results, testimonials, deployment claims, or performance figures. Show human review whenever the proposed workflow affects scheduling, reporting, or invoicing.
