# Nexo Mantenimiento showcase design

## Goal

Add a bilingual, image-led showcase to AlexisSantos.dev that helps a small or medium-sized business understand what an integrated AI solution could do for its daily work. The first case is a fictional field-service company called Nexo Mantenimiento.

The case must demonstrate a complete business process rather than a generic chatbot. It should make the value clear to a plumber, electrician, facilities company, property manager, or larger field-service operation without claiming that Nexo is a real client.

## Experience structure

The website gains four public routes:

- `/showcase/`: Spanish showcase index.
- `/en/showcase/`: English showcase index.
- `/showcase/nexo-mantenimiento/`: Spanish Nexo case.
- `/en/showcase/nexo-maintenance/`: English Nexo case.

The main Spanish navigation uses `Demos`; the English navigation uses `Showcase`. The homepage gains a compact Nexo preview after the process section and before the existing product portfolio. The preview links to the relevant case page. The showcase index is designed as a reusable gallery even though the first release contains one published case.

## Fictional business

Nexo Mantenimiento is a fictional property-maintenance company with an office team and field technicians. It receives requests through WhatsApp, email, voice notes, and photographs. Its current administrative work includes understanding the request, recording the customer and location, assessing urgency, scheduling the visit, collecting evidence, preparing a completion report, and drafting an invoice.

Every Nexo page and preview must include a visible `Caso ficticio` or `Fictional case` label. The content must not imply a real engagement, testimonial, production deployment, or measured business result.

## Demonstrated workflow

The interactive case presents six stages:

1. **Request received**: a customer sends a WhatsApp message, a photograph, and a short voice note about a leak.
2. **Request understood**: the system transcribes the audio and extracts the customer, address, issue, and urgency.
3. **Job created**: the system prepares a work order with the extracted facts and flags uncertain details for review.
4. **Visit scheduled**: the office chooses from suggested appointment windows and assigns a technician.
5. **Work validated**: the technician uploads before-and-after photographs; the system checks that the required evidence and fields are present.
6. **Documents prepared**: the customer report and invoice draft are ready for a person to review and approve.

The flow always shows where a person reviews or approves the work. It does not suggest that AI makes unchecked operational or financial decisions.

## Visual direction

The showcase uses the existing AlexisSantos.dev identity: pearl background, charcoal text, restrained blue, Manrope display type, DM Sans body type, the AS wordmark, and the existing spacing rhythm.

The memorable visual is a large editorial mosaic inspired by image-led showcase galleries:

```text
┌───────────────────────────────────┬──────────────────┐
│                                   │ Incoming request │
│  Field-service photograph         ├──────────────────┤
│  Active-stage interface overlay   │ Work order       │
│                                   ├──────────────────┤
│                                   │ Report ready     │
└───────────────────────────────────┴──────────────────┘
```

The large panel combines an original monochrome or low-saturation field-service image with a precise interface mockup. The supporting tiles show the incoming WhatsApp request, the extracted job card, the evidence check, and the prepared documents. Blue is used for active states, extracted data, and human-review markers rather than decoration.

Images must be original generated assets or project-owned graphics. They must not copy OpenAI showcase artwork, third-party brands, real WhatsApp screenshots, or identifiable people. The message interface can use familiar messaging patterns without reproducing WhatsApp branding.

## Interaction

On pointer devices, hovering a stage tile makes it the active stage. Its image gains a restrained zoom, the corresponding interface layer appears in the large panel, and a short explanation becomes visible. Keyboard focus produces the same state.

The interaction does not auto-advance. It must remain understandable with JavaScript disabled: every tile keeps its image, title, and short explanation. On touch devices the text stays visible and tapping a tile selects it. Reduced-motion mode removes zoom and crossfade animation.

The active state must not rely on colour alone. It also uses a border, title treatment, and an accessible current-state description.

## Page content

### Homepage preview

- Section title: `Mira cómo funcionaría.` / `See how it could work.`
- One sentence explaining that the demos are fictional examples of integrated AI solutions.
- Large Nexo visual mosaic.
- Nexo title and one-line outcome: from customer request to completed job, report, and invoice draft.
- CTA: `Explorar la demo` / `Explore the demo`.

### Showcase index

- Short introduction to the purpose of the demonstrations.
- Featured Nexo case using the large mosaic.
- A restrained `Próximamente` / `Coming next` line naming future sectors: restaurant bookings, invoice processing, property management, and professional services. These are text only until their cases exist.

### Nexo case

- Hero with fictional-case label, Nexo name, and plain-language summary.
- Interactive six-stage workflow.
- `Antes` / `Before` section showing fragmented messages, manual copying, and missing evidence.
- `Con la solución` / `With the solution` section showing the connected flow and human checkpoints.
- Integration map showing messaging, calendar, job system, document storage, and accounting as generic systems.
- Closing prompt asking which process costs the visitor time and linking to the existing contact section.

Spanish and English copy must be written independently enough to sound natural. English must not be a word-for-word translation where the phrasing would feel awkward.

## Technical structure

`scripts/build-studio.py` remains the source of generated navigation and shared page chrome. A structured Nexo content object supplies Spanish and English labels, steps, descriptions, metadata, and routes.

Showcase presentation is isolated in:

- `assets/showcase/showcase.css`
- `assets/showcase/showcase.js`
- `assets/showcase/nexo/` for original images and interface artwork

Generated pages live in the four route directories. The homepage loads the showcase stylesheet and script because it contains the interactive preview. Article pages do not load showcase assets.

The JavaScript uses progressive enhancement. It binds hover, focus, and click events to stage controls, updates the active-stage attribute, and exposes the current state through accessible text. No framework, API, analytics service, or persistent state is required.

## Metadata and navigation

Each index and case page gets a localized title, description, canonical URL, language alternates, Open Graph image, and social description. Language switching preserves context between the Spanish and English showcase routes.

The existing Articles, Projects, About, and Contact links remain available. The mobile menu and footer include the showcase link.

## Validation

The implementation is complete when:

- All four routes build and all local assets resolve.
- Spanish and English navigation, metadata, labels, and CTAs match.
- Hover, keyboard focus, and touch selection expose the same six stages.
- The content remains readable without JavaScript.
- Desktop, tablet, 390 px, and 320 px layouts have no clipping or horizontal overflow.
- Reduced-motion mode removes non-essential animation.
- Generated images have useful alternative text where they communicate content; decorative layers use empty alternatives.
- The fictional-case label is visible on the homepage preview, index, and case page.
- No real-client claim or invented performance metric appears.
- Existing product dialogs, contact form, articles, protected routes, and excluded source directories continue to behave as before.
- The production deployment is made from the committed snapshot and live files match that snapshot.

## Future cases

Future demonstrations reuse the gallery card, case-page shell, localized metadata, active-stage interaction, and fictional-case labeling. Each case supplies its own industry vocabulary, workflow, images, and integration map. The system should not introduce empty cards or duplicate pages before a case is ready.
