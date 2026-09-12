<p align="center"><img src="docs/assets/pitchcraft-logo.svg" width="390" alt="Pitchcraft"></p>
<p align="center">路演构造术 · 高质量图片 PPT，按需转为精致可编辑 PPT。</p>
<p align="center"><a href="README.en.md">English</a> · <a href="#安装">安装</a> · <a href="docs/USAGE.md">使用指南</a> · <a href="docs/EXAMPLES.md">作品示例</a></p>

Pitchcraft 把内容判断、产品风格和 PPT 制作接成一个工作流。先用完整页面生成获得精致的图片 PPT，可以直接演示和交付；需要修改文字或移动素材时，再转换为可编辑 PPT。两个阶段独立可用，按需选择交付终点。

它面向比赛答辩、产品路演和需要视觉完成度的演示。目标是把商业演示所需的细节做到位：结论有证据、版式有层级、风格来自产品，文字和素材能够继续修改。

## 核心亮点

### 一次调用，从 GitHub 项目找到真实的产品与品牌

给出 GitHub 仓库、PR 链接或本地项目路径，Pitchcraft 自动读取对应源码与资料，定位产品文档、品牌素材、配色、字体和设计变量，再把这些线索组织成路演的内容与视觉方向。一次调用完成资料读取、素材定位与风格提炼，让路演建立在真实产品之上。

### 提取真实品牌风格，让 PPT 一眼属于你的产品

从项目本身提炼配色、字体、插画、材质与布局节奏，把真实的品牌语言延伸到整套路演中。纸感、像素、克制的科技感，都随产品特征展开，让每套 PPT 拥有鲜明、连贯的品牌个性。

### 直接调用生图模型，快速生成丰富、精致的完整页面

文字、视觉主体、构图与材质在整页生成时统一设计。生图模型能够呈现丰富的插画、产品意象、空间层次与细腻质感，让 PPT 具备完整的设计感和高级感。RW 方法同时约束结论、证据、信息层级和整套一致性，让高视觉完成度服务于内容表达。

图片版生成后即可演示和交付。认可的正文、样页与素材会继续复用，局部修改只处理受影响页面，以减少返工来提高速度。

### 从精致图片到可编辑素材，面向商业级交付

需要进一步使用时，可以把页面中的文字、插图和其他素材单独提取：文字恢复为原生文本框，合适的简单图形恢复为原生对象，复杂插图成为可单独移动的完整图片素材。同步清理底图残字，保留认可的版式，得到方便改文案、换素材和调整布局的可编辑 PPT。

交付标准覆盖商业演示实际关心的细节：文字准确、视觉精致、品牌一致、对象可用、后续易改。图片版可以直接用，可编辑版可以继续精修；两种形式服务于不同阶段的真实需求。

## 两个阶段，两个可用的终点

| | 图片 PPT | 可编辑 PPT |
| --- | --- | --- |
| 制作方式 | RW 方法组织文案与证据，原生图像生成完成整页 | 在认可页面上恢复原生文字、图形与独立素材 |
| 适合 | 快速获得风格完整、视觉精致的演示稿 | 后续改文案、移动素材、调整局部版式 |
| 交付 | 整页 PNG + 每页一张图的 PPTX | 另存可编辑 PPTX，保留图片版作为基准 |
| 验收重点 | 文字准确、证据关系、视觉层级、整套一致性 | 底图无重复字，文字真实可编辑，素材边界和版式稳定 |

图片版可以直接使用。第二阶段按需进行，也接受你已经做好的图片 PPT；如果文件已经拆好，只修漏字和残字，保持原图片组织。

## 安装

这是供具备技能加载能力的助手使用的技能包，通过一次调用串联完整制作流程。仓库包含三个配套技能：

- `pitchcraft`：统一入口，负责路演、来源、阶段交接与验收。
- `rw-consulting-ppt`：图片 PPT 制作方法。
- `image-ppt-to-editable`：可编辑转换与已有 PPT 修复。

以支持本地 skills 的 Codex 环境为例：

```bash
git clone https://github.com/huyanxius/pitchcraft.git
cd pitchcraft
```

把 `skills/` 下的三个目录安装到你的技能目录，通常为 `~/.codex/skills/`；自定义 `CODEX_HOME` 时使用 `$CODEX_HOME/skills/`。下面的命令会检查同名技能，保留已有修改：

```bash
python3 - <<'PY'
import os, shutil
from pathlib import Path
source = Path('skills')
assert (source / 'pitchcraft' / 'SKILL.md').is_file(), '请先进入克隆的 pitchcraft 目录'
target = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills'
names = ('pitchcraft', 'rw-consulting-ppt', 'image-ppt-to-editable')
conflicts = [str(target / name) for name in names if (target / name).exists()]
if conflicts:
    raise SystemExit('同名技能已存在，请先备份或比较：\n' + '\n'.join(conflicts))
target.mkdir(parents=True, exist_ok=True)
for name in names:
    shutil.copytree(source / name, target / name)
print('Installed: ' + ', '.join(names))
PY
```

安装后按宿主方式刷新技能或开始新会话。其他助手可手动安装相同目录，并配备对应的图像生成与 PPT 编辑工具。

### 运行条件

- 能读取本地文档与图片、调用原生图像生成的助手环境。
- 转换阶段需要可用的 Presentations 技能、PPTX 组装运行时与渲染工具；由宿主环境提供。
- Python 3.10+；确定性抠图和可选联系表使用 Pillow，可在任务虚拟环境中安装 `python -m pip install Pillow`。
- 读取远程仓库需要 Git；私有源使用你自己的授权。模型与工具服务及费用由对应提供方负责。

使用前可按指南检查宿主的图像生成与转换能力。[完整使用与排错指南](docs/USAGE.md)。

## 开始使用

**直接做图片 PPT：**

```text
用 $pitchcraft，根据这个产品仓库做一套 8 分钟答辩 PPT。
先给我两张代表样页，风格沿用产品；最终只要图片版 PPT。
```

**图片版加可编辑版：**

```text
用 $pitchcraft，按这份正文生成 RW 图片初稿，认可后转为可编辑 PPT。
保持原版式，清掉底图文字，另存并保留图片版。
```

**从已有文件继续：**

```text
用 $pitchcraft，把这份已认可的图片 PPT 按原版式转成可编辑版。
```

**只修残字：**

```text
用 $pitchcraft，只补这份 PPT 遗漏的可编辑文字并清除底图残字。
保留现有图片数量、位置、大小、裁切和组织。
```

## 工作流程

确认受众、时长与交付终点 → 核对内容和产品证据 → 确定逐页正文与视觉风格 → 生成并认可样页 → 完成图片 PPT → 按需转换 → 整页和文件检查 → 另存交付。

已经认可的正文、图片和素材直接复用。需要完整路演时，可以附讲稿、时间表、Demo 备用讲法和评委问答；只做 PPT 时按所选格式交付。

## 项目状态与贡献

这是从实际制作经验整理的可复用工作流。公开版已完成安装、技能结构与图片打包检查，详细范围见 [验证记录](docs/VALIDATION.md)。欢迎使用可公开分享的页面、预期行为和实际结果提交 Issue。

## 许可与致谢

原创技能与脚本采用 [MIT](LICENSE)。图片制作方法基于 [RW Consulting PPT](https://github.com/Pikapika260214/rw-consulting-ppt)，保留其 MIT 许可证；确定性纯色抠除脚本来自 [ningzimu/image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill)，保留原版权。完整来源见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

作品示例与品牌素材保留各自权利人的权利，使用范围见 [示例说明](docs/EXAMPLES.md)。

## 作品展示

以下四张既有作品展示了这套制作方法追求的构图、材质与品牌表达。[查看作品说明](docs/EXAMPLES.md)。

### 群学致知 · 产品入口

![群学致知产品入口](docs/examples/qunxue-product.png)

### Windup · 设计判断

![Windup 设计判断](docs/examples/windup-design.png)

### Windup · 开场

![Windup 开场](docs/examples/windup-opening.png)

### Windup · 收束

![Windup 收束](docs/examples/windup-closing.png)
