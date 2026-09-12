<p align="center"><img src="docs/assets/pitchcraft-logo.svg" width="390" alt="Pitchcraft"></p>
<p align="center">路演构造术 · 高质量图片 PPT，按需转为精致可编辑 PPT。</p>
<p align="center"><a href="README.en.md">English</a> · <a href="#安装">安装</a> · <a href="docs/USAGE.md">使用指南</a> · <a href="docs/EXAMPLES.md">作品示例</a></p>

Pitchcraft 把内容判断、产品风格和 PPT 制作接成一个工作流。先用完整页面生成获得精致的图片 PPT，可以直接演示和交付；需要修改文字或移动素材时，再转换为可编辑 PPT。两个阶段独立可用，不必每次都走到底。

它面向比赛答辩、产品路演和需要视觉完成度的演示。目标是把商业演示所需的细节做到位：结论有证据、版式有层级、风格来自产品，文字和素材能够继续修改。

## 作品一览

![Windup 开场页：产品风格与角色素材](docs/examples/windup-opening.png)

<table><tr><td><img src="docs/examples/windup-design.png" alt="Windup 设计判断页"></td><td><img src="docs/examples/qunxue-product.png" alt="群学致知产品页"></td></tr></table>

这些是维护者提供的既有作品参考，展示目标视觉质量；并非本次公开包的端到端测试输出。图片预览无法证明内部对象可编辑。[查看更多示例与说明](docs/EXAMPLES.md)。

## 两个阶段，两个可用的终点

| | 图片 PPT | 可编辑 PPT |
| --- | --- | --- |
| 制作方式 | RW 方法组织文案与证据，原生图像生成完成整页 | 在认可页面上恢复原生文字、图形与独立素材 |
| 适合 | 快速获得风格完整、视觉精致的演示稿 | 后续改文案、移动素材、调整局部版式 |
| 交付 | 整页 PNG + 每页一张图的 PPTX | 另存可编辑 PPTX，保留图片版作为基准 |
| 验收重点 | 文字准确、证据关系、视觉层级、整套一致性 | 底图无重复字，文字真实可编辑，素材边界和版式稳定 |

图片版可以直接使用。第二阶段按需进行，也接受你已经做好的图片 PPT；如果文件已经拆好，只修漏字和残字，保持原图片组织。

## 为什么用 Pitchcraft

**精致出图，也为后续修改留出路。** 整页图像生成先建立视觉完成度，再恢复可编辑对象；不从一套普通卡片模板开始拼。

**风格来自你的产品。** 从品牌素材、现有界面和认可样页提炼字体、配色、材质与页面节奏。纸感、像素、极简或其他风格都由项目决定，示例不是固定模板。

**速度来自少返工。** 复用已有正文与素材，样页确定后保持整套风格；生成后及时回装，局部问题只改局部。实际耗时受页数、模型速度、文字密度与转换复杂度影响，不承诺固定分钟数。

**可编辑有具体标准。** 文字必须可见且可编辑，底图不能仍留同一份字，复杂插图可作为完整组合素材。只有源数据可靠时，图表才称为数据可编辑；不会把隐藏文本或整页背景冒充转换完成。

## 安装

这是供具备技能加载能力的助手使用的技能包，不是独立的一键转换软件。仓库包含三个配套技能：

- `pitchcraft`：统一入口，负责路演、来源、阶段交接与验收。
- `rw-consulting-ppt`：图片 PPT 制作方法。
- `image-ppt-to-editable`：可编辑转换与已有 PPT 修复。

以支持本地 skills 的 Codex 环境为例：

```bash
git clone https://github.com/huyanxius/pitchcraft.git
cd pitchcraft
```

把 `skills/` 下的三个目录安装到你的技能目录，通常为 `~/.codex/skills/`；自定义 `CODEX_HOME` 时使用 `$CODEX_HOME/skills/`。下面的命令遇到同名技能会停止，避免覆盖已有修改：

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

安装后按宿主方式刷新技能或开始新会话。其他助手可手动安装相同目录，但需要自行提供等价工具，不能仅靠复制 Markdown 获得图像生成或 PPT 编辑能力。

### 运行条件

- 能读取本地文档与图片、调用原生图像生成的助手环境。
- 转换阶段需要可用的 Presentations 技能、PPTX 组装运行时与渲染工具；这些宿主能力不随仓库分发。
- Python 3.10+；确定性抠图和可选联系表使用 Pillow，可在任务虚拟环境中安装 `python -m pip install Pillow`。
- 读取远程仓库需要 Git；私有源使用你自己的授权。模型或工具的费用由提供方决定，本项目不提供模型服务。

图像生成或转换能力缺失时，技能会说明缺失项，不把提示词或图片版当成已完成的可编辑交付。[完整使用与排错指南](docs/USAGE.md)。

## 开始使用

**直接做图片 PPT：**

```text
用 $pitchcraft，根据这个产品仓库做一套 8 分钟答辩 PPT。
先给我两张代表样页，风格沿用产品；最终只要图片版 PPT。
```

**图片版加可编辑版：**

```text
用 $pitchcraft，按这份正文生成 RW 图片初稿，认可后转为可编辑 PPT。
保持原版式，清掉底图文字，另存，不覆盖图片版。
```

**从已有文件继续：**

```text
用 $pitchcraft，把这份已认可的图片 PPT 转成可编辑版，不重新设计。
```

**只修残字：**

```text
用 $pitchcraft，只补这份 PPT 遗漏的可编辑文字并清除底图残字。
现有图片数量、位置、大小、裁切和组织保持不变。
```

## 工作流程

确认受众、时长与交付终点 → 核对内容和产品证据 → 确定逐页正文与视觉风格 → 生成并认可样页 → 完成图片 PPT → 按需转换 → 整页和文件检查 → 另存交付。

已经认可的正文、图片和素材直接复用。需要完整路演时，可以附讲稿、时间表、Demo 备用讲法和评委问答；只做 PPT 时不强制增加材料。

## 项目状态与贡献

这是从实际制作经验整理的可复用工作流。公开版检查范围见 [验证记录](docs/VALIDATION.md)；模型输出仍需逐页审阅。欢迎带具体页面、预期行为和实际问题提交 Issue，请勿上传密钥、未授权材料或敏感信息。

## 许可与致谢

原创技能与脚本采用 [MIT](LICENSE)。图片制作方法基于 [RW Consulting PPT](https://github.com/Pikapika260214/rw-consulting-ppt)，保留其 MIT 许可证；确定性纯色抠除脚本来自 [ningzimu/image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill)，保留原版权。完整来源见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

作品示例与品牌标志不包含在代码的 MIT 授权中。示例中的品牌、人物及第三方标识归各自权利人，展示不表示其为本项目背书；详见 [示例使用边界](docs/EXAMPLES.md)。
