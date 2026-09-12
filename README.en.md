<p align="center"><img src="docs/assets/pitchcraft-logo.svg" width="390" alt="Pitchcraft"></p>
<p align="center">Beautiful image decks. Refined editable slides when you need them.</p>
<p align="center"><a href="README.md">简体中文</a> · <a href="docs/USAGE.md">Usage guide</a> · <a href="docs/EXAMPLES.md">Gallery</a></p>

Pitchcraft turns product evidence and visual identity into presentation slides through two distinct stages. First, generate complete, carefully composed slide images and package them as a presentation-ready PPTX. Stop there, or convert the accepted design into visible editable text, appropriate native shapes, and independent image assets.

![Windup presentation example](docs/examples/windup-opening.png)

These are existing works supplied by the maintainer as visual references, not outputs of an end-to-end test of this public release. A preview image alone does not demonstrate editability.

## Choose your deliverable

| Image deck | Editable deck |
| --- | --- |
| Complete slide PNGs and one image per PPTX slide | A separate PPTX with visible editable text and meaningful assets |
| Ready to present without conversion | Built from the accepted image design |
| Review wording, evidence, hierarchy and consistency | Review text coverage, clean underlying images and layout fidelity |

This is a skill workflow for a capable assistant, not a standalone one-click converter. It combines `pitchcraft`, `rw-consulting-ppt`, and `image-ppt-to-editable`. The repository bundles all three skills, with upstream notices preserved.

## Install

```bash
git clone https://github.com/huyanxius/pitchcraft.git
cd pitchcraft
```

Install the three folders inside `skills/` into your assistant's skill directory. For Codex this is typically `~/.codex/skills/`, or `$CODEX_HOME/skills/` when customized. Back up and compare existing skills before replacing them. The [Chinese README](README.md#安装) includes an installation command that refuses to overwrite existing folders.

Refresh skills or start a new session as required by the host. Other assistants need equivalent file, image-generation, PPTX assembly and rendering tools; installing the Markdown does not supply those capabilities.

Requirements: Python 3.10+, Git for remote inputs, a native full-slide image-generation tool, and—for editable conversion—a Presentations skill with an available PPTX runtime and renderer. Pillow is used for chroma-key removal and optional contact sheets. Host plugins and model services are not bundled. Any service costs are charged by their providers.

## Use

```text
Use $pitchcraft to create an eight-minute product pitch from this repository.
Show two representative sample pages first. Deliver an image-only PPTX.
```

```text
Use $pitchcraft to create an RW image draft, then convert the accepted pages
into an editable PPTX. Preserve the design and save a separate file.
```

```text
Use $pitchcraft to clean residual image text in this partially editable deck.
Preserve existing picture counts, positions, sizes, crops and grouping.
```

## Quality and speed

Pitchcraft reuses approved copy and assets, learns the product's design language, and revises only affected pages. Speed comes from reducing avoidable work; there is no fixed completion-time guarantee.

Editable text must be visible. Underlying images must not duplicate it. Complex illustrations may remain grouped bitmaps, and charts are data-editable only when reliable source data exists. Artistic fonts may require an approximation. Structure checks do not replace visual and factual review.

See [validation status](docs/VALIDATION.md) for the checks actually performed. The public workflow has not yet been rerun end to end from fresh image generation through editable delivery.

## License

Original skill instructions and code: [MIT](LICENSE). Bundled RW material and the chroma-key utility retain their upstream licenses; see [third-party notices](THIRD_PARTY_NOTICES.md). Gallery works and brand assets are excluded from the code license. Third-party marks belong to their respective owners and do not imply endorsement.
