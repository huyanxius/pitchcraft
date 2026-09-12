<p align="center"><img src="docs/assets/pitchcraft-logo.svg" width="390" alt="Pitchcraft"></p>
<p align="center">Beautiful image decks. Refined editable slides when you need them.</p>
<p align="center"><a href="README.md">简体中文</a> · <a href="docs/USAGE.md">Usage guide</a> · <a href="docs/EXAMPLES.md">Gallery</a></p>

Pitchcraft turns product evidence and visual identity into presentation slides through two distinct stages. First, generate complete, carefully composed slide images and package them as a presentation-ready PPTX. Stop there, or convert the accepted design into visible editable text, appropriate native shapes, and independent image assets.

## What makes Pitchcraft different

### One invocation, grounded in your GitHub project

Provide a GitHub repository, a pull-request URL or a local project path. Pitchcraft reads the corresponding source and materials, locates product documentation, brand assets, colors, fonts and design variables, then uses that evidence to shape the presentation. One invocation brings product evidence and brand references into the presentation workflow.

### A visual identity grounded in your product

The deck inherits your product's palette, typography, illustration language, materials and visual rhythm. Paper textures, pixel art or a restrained technical aesthetic come from the project and approved references, giving each deck a distinctive, coherent identity.

### Rich, refined slides generated as complete compositions

Native image generation creates the text, visual subject, composition and material treatment together. It supports expressive illustrations, product imagery, depth and fine visual detail beyond a conventional component layout. RW's method keeps the message, evidence, hierarchy and deck-wide consistency in focus.

The image deck is ready to present. Reusing approved copy and assets and revising only affected pages reduces avoidable work and helps reach a polished result quickly.

### Independent assets and editable text for professional delivery

When further editing is needed, extract text and meaningful visual assets from the accepted pages. Text becomes native text boxes, suitable simple graphics become native objects, and complex illustrations remain independently movable images. Remove duplicate text from the underlying assets while preserving the accepted composition.

The workflow targets the details expected in commercial presentation delivery: accurate copy, refined visuals, consistent branding, usable objects and practical revision. Present the image version directly or continue refining the editable version.

## Choose your deliverable

| Image deck | Editable deck |
| --- | --- |
| Complete slide PNGs and one image per PPTX slide | A separate PPTX with visible editable text and meaningful assets |
| Ready to present without conversion | Built from the accepted image design |
| Review wording, evidence, hierarchy and consistency | Review text coverage, clean underlying images and layout fidelity |

This skill workflow connects the complete production process through one assistant invocation. It combines `pitchcraft`, `rw-consulting-ppt`, and `image-ppt-to-editable`. The repository bundles all three skills, with upstream notices preserved.

## Install

```bash
git clone https://github.com/huyanxius/pitchcraft.git
cd pitchcraft
```

Install the three folders inside `skills/` into your assistant's skill directory. For Codex this is typically `~/.codex/skills/`, or `$CODEX_HOME/skills/` when customized. Back up and compare existing skills before replacing them. The [Chinese README](README.md#安装) includes an installation command that refuses to overwrite existing folders.

Refresh skills or start a new session as required by the host. Other assistants can use the same skill folders with equivalent file, image-generation, PPTX assembly and rendering tools.

Requirements: Python 3.10+, Git for remote inputs, a native full-slide image-generation tool, and—for editable conversion—a Presentations skill with an available PPTX runtime and renderer. Pillow is used for chroma-key removal and optional contact sheets. The host supplies plugins and model services; their providers determine service costs.

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

Pitchcraft reuses approved copy and assets, learns the product's design language, and revises only affected pages. This reduces avoidable work; completion time depends on page count, model latency and conversion complexity.

Editable delivery combines visible native text with clean underlying images. Complex illustrations may remain grouped bitmaps, and charts are data-editable only when reliable source data exists. Artistic fonts may require an approximation. Delivery includes structural, visual and factual review.

See [validation status](docs/VALIDATION.md) for the checks actually performed. The public release has passed installation, skill-structure and mechanical image-packaging checks; model-driven end-to-end validation remains a next step.

## License

Original skill instructions and code: [MIT](LICENSE). Bundled RW material and the chroma-key utility retain their upstream licenses; see [third-party notices](THIRD_PARTY_NOTICES.md). Gallery works, brand assets and third-party marks retain their respective owners’ rights; their usage terms are described in the gallery notes.

## Showcase

These four existing works illustrate the composition, materials and brand expression this workflow aims to achieve. See [example notes](docs/EXAMPLES.md).

### Qunxue · Product entry

![Qunxue product entry](docs/examples/qunxue-product.png)

### Windup · Design principles

![Windup design principles](docs/examples/windup-design.png)

### Windup · Opening

![Windup opening](docs/examples/windup-opening.png)

### Windup · Closing

![Windup closing](docs/examples/windup-closing.png)
