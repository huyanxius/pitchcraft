# Slide Generation and QA — Image Draft Stage

This reference governs only the RW image-draft stage. Read `rw-consulting-ppt/SKILL.md` and its applicable references before generation. After approved PNGs exist, the separate editable stage follows [editable-handoff.md](editable-handoff.md); its native objects do not violate this image-stage contract.

## Full-slide image contract

Generate one native 16:9 image per complete slide. If delivered as PPTX, each page contains exactly one full-slide image.

Do not create the designed slide with HTML/CSS/React, SVG/canvas, Python/Pillow, browser screenshots, or editable PowerPoint objects. Code may scan repositories, prepare manifests, create contact sheets, validate images, and package accepted PNGs.

## Slide brief

Include:

- Slide number and story role.
- Spoken job.
- Action title.
- Subtitle only when it adds reasoning.
- Proof object.
- Visual mother concept.
- 3-6 evidence anchors.
- Product assets and their purpose.
- Evidence status: demonstrated, implemented, documented, planned, or hypothesis.
- Unsupported implications to avoid.
- Speaker time and transition.
- Must-keep text and numbers.
- Omit list.
- Rejection risks.

Do not prompt a page whose main visual is merely `cards`, `three columns`, or `a table` unless that structure is the real proof object.

## Product-native style master

Lock the whole-page rhythm, not only the palette:

- Title scale and top alignment.
- Subtitle proximity and weight.
- Product motif.
- Proof-object dominance.
- Screenshot treatment.
- Evidence-label treatment.
- Page marker and source note.
- Material and depth.

If the user supplies an approved sample or previous deck, treat it as the style master unless explicitly told otherwise. Reconcile it with the Product & Visual DNA Contract instead of silently choosing one.

## Prompt shape

Use this order:

1. Slide role and spoken job.
2. Action title.
3. Subtitle if required.
4. Main proof object.
5. Product-native visual mother concept.
6. Evidence anchors attached to the proof object.
7. Product assets.
8. Deck System Contract.
9. Text budget and exclusions.
10. Output: one complete 16:9 slide PNG.

## Sample selection

Test:

- One opening/thesis page for memorability and brand translation.
- One product/evidence page for screenshot treatment, Chinese text, and information density.

Emergency mode may proceed after internal review only when the user explicitly authorized uninterrupted work. Do not call internal review user approval or bypass an explicit sample gate.

## Hard rejection checks

Reject when any applies:

- Generic AI technology style: blue-purple gradients, glowing blobs, random circuits, or generic robots unrelated to the product.
- Generic SaaS dashboard: equal-weight cards and icons with no proof object.
- Product style reduced to logo plus brand color.
- Tiny or broken Chinese text.
- Multiple title-like conclusion zones.
- Screenshot used as decoration without proving workflow.
- Unsupported visual semantics: arrows, checks, gates, rings, or green status imply unproven success.
- Legacy/demo UI shown as the current product.
- Detached large numbers compete with the title.
- Slide cannot be understood from presentation distance.
- Page style drifts from the approved sample.

## Text-accuracy pass

For every generated page:

1. Compare visible required text and numbers against the brief.
2. Correct only the affected image/page when a required word, name, number, or unit is wrong; reuse accepted content and composition.
3. If exact rendering remains unstable, revise wording or move text to notes only when it preserves the agreed content and density; keep mandatory names, numbers, units and claims exact.
4. Never silently replace product names or metrics with approximate wording.

## Local revision rule

When the user changes one page:

- Resolve the actual page number and current file first.
- Preserve the Deck System Contract.
- Regenerate only the affected PNG.
- Replace only that PPTX page image.
- Rebuild the contact sheet and revalidate slide order/count.

Do not overwrite the accepted previous version unless the user explicitly requests it.

After editable conversion has begun, choose the minimum revision path in [editable-handoff.md](editable-handoff.md), rather than automatically regenerating an image for every text edit. Existing interface images may be reused as evidence; do not capture or upload screenshots.
