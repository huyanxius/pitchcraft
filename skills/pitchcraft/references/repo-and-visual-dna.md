# Repository and Visual DNA

## Purpose

Convert repository evidence into a trustworthy product model and a reusable presentation style master.

## Source-of-truth audit

Record each important claim with one status:

- `demonstrated`: visible in the current product or verified output.
- `implemented`: supported by current code/tests but not demonstrated in the roadshow.
- `documented`: stated in maintained documentation but not independently verified.
- `planned`: explicitly future work.
- `hypothesis`: desired positioning without sufficient evidence.
- `legacy`: old or demo-only material that must not represent the current product.

Keep roadshow ambition, product facts, and future roadmap separate. A strong pitch can contain all three, but it must not visually present a plan as shipped capability.

## Repository scan targets

Inspect only the highest-value sources first:

1. Project instructions and handoff notes.
2. Current app entry points and visible product surfaces.
3. README, architecture, product, competition, and pitch documents.
4. Recent releases, PRs, issues, changelog, and tests.
5. Brand assets, screenshots, GIFs, videos, icons, fonts, and public images.
6. CSS variables, theme files, Tailwind configuration, design tokens, and component styles.

Exclude build output, dependencies, generated jobs, secrets, caches, large binary archives, and unrelated worktrees.

## Visual DNA dimensions

Extract and judge:

- Palette: base, text, primary anchor, secondary accent, status colors.
- Typography: families, display/body relationship, weight, scale, language fit.
- Geometry: corner radius, border weight, spacing rhythm, alignment behavior.
- Material: flat, paper, glass, pixel, hand-drawn, cinematic, tactile, technical.
- Density: sparse hero, medium presentation, dense report, editor/workbench.
- Image language: product screenshots, characters, diagrams, photographs, illustrations.
- Motion signature: reveal, generation, sequence, progress, transformation, feedback.
- Distinctive motif: the one visual idea that makes the product recognizable.

Token frequency is evidence, not a verdict. A common gray may be a neutral background rather than the brand anchor.

## Translation rule

Translate product language into deck language:

- Reuse product colors by role, not by raw surface area.
- Reuse interface geometry as an accent or proof-object grammar, not as generic card grids.
- Use real screenshots only where they prove workflow or product maturity.
- Use the product's distinctive motif as a repeated deck-level signature.
- Simplify interface density for distance viewing.

## Product & Visual DNA Contract template

```markdown
## Product & Visual DNA Contract

### Product truth
- Product:
- Target user:
- Core problem:
- Demonstrable workflow:
- Strongest evidence:
- Planned claims:
- Conflicts / gaps:

### Visual truth
- Approved assets:
- Base / text / anchor / accent colors:
- Typography mood:
- Geometry:
- Material:
- Density:
- Distinctive motif:
- Screenshot policy:

### Exclusions
- Legacy/demo material:
- Generic styles to avoid:
```

## Acceptance checks

- A reviewer can trace every major product claim to a source or status.
- The visual direction contains at least one product-specific motif beyond color and logo.
- Legacy/demo assets are explicitly separated.
- The contract is short enough to repeat in generation prompts.
