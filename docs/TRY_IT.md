# 两页试用 / Two-slide trial

用 Pitchcraft 自己的公开资料试做两页，无需提供私有项目或比赛材料。这是一份试用题，实际完成的验证范围见[验证记录](VALIDATION.md)。

## 中文

安装三个技能后，在支持技能的助手中粘贴下面的提示词。宿主需要读写文件、原生图像生成和图片 PPTX 打包能力；转换为可编辑版还需要 Presentations 技能、PPTX 运行时和可用的渲染器。Python 打包器需要 `python-pptx`；可选联系表需要 Pillow。模型和工具服务由宿主提供，按对应服务计费。

```text
用 $pitchcraft，只用 https://github.com/huyanxius/pitchcraft 的公开资料，
做两张 16:9 英文样页。先检查宿主是否具有读写文件、原生图像生成、
图片 PPTX 打包工具；缺什么就说清楚，先完成不依赖它的资料工作。

读取 README.en.md、docs/VALIDATION.md 和 pitchcraft 技能说明。
不要使用作品库中的品牌图片，不添加用户数、效果指标或未经验证的承诺。
沿用 Pitchcraft 自己的 Logo 与克制的视觉风格。

第 1 页：Pitchcraft — From product evidence to a presentation
主要流程：Repository or brief → Image deck → Optional editable PPTX
第 2 页：Choose where to stop
图片版：完整页面 PNG + 每页一张图的 PPTX，图片内文字不可直接编辑。
可编辑版：另存 PPTX，恢复可见原生文字、适当的简单图形和独立图片素材。
复杂插图可能仍为位图；图表只有源数据可靠时才称数据可编辑。

先给两张整页样图供我检查文字与版式。等我认可后，打包图片版 PPTX。
这次先交付图片版，不自动进入可编辑转换。
```

想继续测试转换，在认可样页后追加：

```text
用 $pitchcraft，将第 2 页另存为可编辑 PPTX。
保持认可的构图，真正清除底图中的目标文字，再恢复可见的原生文本框。
复杂插图可保留为独立位图。保留图片版，并检查文字覆盖、对象与整页效果。
```

检查时，图片版应为两页、每页一张完整图片；可编辑样页应有可选中并修改的可见文字，底图中不再重复出现同一文字。文件结构检查、在目标应用打开和人工认可视觉效果分别记录。

## English

Try two slides using Pitchcraft's own public repository. No private project or competition material is needed. This is a trial brief; [validation status](VALIDATION.md) lists what has actually been checked.

Your host needs file access, native image generation and image-to-PPTX packaging. Optional editable conversion also needs a Presentations skill, a PPTX runtime and a working renderer. The Python packager needs `python-pptx`; optional contact sheets need Pillow. Your host supplies model and tool services, whose own charges apply.

```text
Use $pitchcraft to make only two 16:9 English sample slides from
https://github.com/huyanxius/pitchcraft and its public materials.
First check file access, native image generation and image-PPTX packaging.
If a capability is missing, name it and complete the evidence work that can run.

Read README.en.md, docs/VALIDATION.md and the pitchcraft skill instructions.
Use Pitchcraft's own logo and a restrained visual style. Do not reuse gallery
brands or images. Do not add user counts, outcome metrics or unverified claims.

Slide 1: Pitchcraft — From product evidence to a presentation
Main flow: Repository or brief → Image deck → Optional editable PPTX
Slide 2: Choose where to stop
Image deck: complete PNGs and one image per PPTX slide; image text is not editable.
Editable deck: a separate PPTX with visible native text, suitable simple shapes
and independent image assets. Complex illustrations may remain bitmaps.
Charts are data-editable only when reliable source data is available.

Show the two complete sample images for my review. After I approve them,
package an image-only PPTX. Stop at the image deck for this trial.
```

After approving the sample, optionally test conversion:

```text
Use $pitchcraft to save slide 2 as a separate editable PPTX.
Preserve the accepted composition. Remove the target text from underlying images,
then restore visible native text boxes. Complex illustrations can remain
independent bitmaps. Keep the image deck and check text coverage, objects and
the complete slide.
```

The image deck should contain two slides, each with one full-slide picture. The editable sample should have visible text you can select and change, without the same text remaining in its underlying images. Record structural checks, opening in the target application and human visual approval separately.

## 反馈 / Feedback

在 [GitHub Issues](https://github.com/huyanxius/pitchcraft/issues/new) 提供：宿主与版本、使用的模型或工具、停在哪一阶段、预期和实际结果。可以附可公开的最小样页；私有正文、个人信息和凭证先移除。

In a [GitHub issue](https://github.com/huyanxius/pitchcraft/issues/new), include your host and version, model/tools, the stage reached, expected behavior and observed result. Share a small public or redacted sample if useful. Remove private copy, personal information and credentials before posting.
