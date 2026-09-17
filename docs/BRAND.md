# Brand source of truth

The reusable brand kit now lives in `brand/`. Start with `brand/README.md`, `brand/index.html`, and `brand/brand-guide.pdf`. Logos, fonts, colours and printable templates are maintained there. The website uses its exported assets.

## Website implementation notes

Build: python3 scripts/build-studio.py regenerates the two studio pages. Styles and behaviour live in assets/studio/. The contact form opens a mail draft; it does not send or store submissions. Existing articles and standalone app pages retain their original language and URLs.

Verification completed: Spanish/English navigation and metadata; desktop and 390px/320px widths with no horizontal overflow; native dialog focus return and Escape dismissal; mobile menu closure; required contact fields; email recipient and subject plus accented characters and multiline content; all 43 local references in each document; JavaScript syntax; whitespace checks. No browser console errors observed. No messages sent and no production deployment performed.
