# 真实透明度与纯色抠除

这是素材分离的检查步骤，不是用棋盘格预览判断透明度。

## 选择纯色底

内置图片编辑可能输出 RGB 棋盘格，甚至带有看似透明的白色残影。遇到这种输出先检查文件，不把它叠进 PPT。请求纯色 RGB 底，不再请求透明：

- 底色优先选择素材中不存在的高饱和颜色，如绿色 `#00FF00`。
- 绿色植物素材不要用绿底；换用不与主体冲突的品红等颜色。
- 强调完全平坦、不带纹理、渐变或棋盘格，主体外不留残影。
- 保留源画布大小及主体位置，方便按同一坐标放回原页面。若单独裁切主体，记录原画布中的位置和尺寸。

## 实际抠除

`<skill-dir>` 是本 SKILL.md 所在目录。用能导入 Pillow 的现有 Python；优先查询桌面 `load_workspace_dependencies` 提供的运行时，不修改其捆绑依赖。若无可用 Pillow，在任务自己的虚拟环境中安装。

```sh
python <skill-dir>/scripts/remove_chroma_key.py \
  --input /absolute/task/assets/paper-green.png \
  --out /absolute/task/assets/paper.png \
  --key-color '#00ff00' \
  --soft-matte --transparent-threshold 70 --opaque-threshold 145 --despill
```

这组阈值适用于本次中性色纸张素材的起点，不能机械用于所有图片。实际生成绿色往往不是准确色值，可先读取背景空白区域像素来确定 key；背景占多数边缘时可用 `--auto-key border`。主体占满边缘时不要自动估色。

低阈值以下透明，高阈值以上不透明，中间保留抗锯齿。检查浅色主体是否被削弱、轮廓是否残留底色。颜色与主体重叠时重新选底色，不靠放宽阈值硬抠。脚本拒绝默认覆盖已有文件；输出新版本而非使用 `--force` 覆盖用户资产。

## 文件检查

以下检查只验证透明结构，不证明抠图边界正确。将 `FILE` 改为实际文件路径，传给已有 Python 运行：

```python
from PIL import Image
im = Image.open(FILE).convert('RGBA')
alpha = im.getchannel('A')
hist = alpha.histogram()
print({
    'alpha_range': alpha.getextrema(),
    'fully_transparent': hist[0],
    'fully_opaque': hist[255],
    'partial': sum(hist[1:255]),
    'total': im.width * im.height,
})
assert hist[0] > 0, '没有完全透明像素：可能是假透明或全不透明'
assert hist[255] > 0, '没有不透明主体：可能误抠除了整个素材'
```

RGBA 本身不够：整张 Alpha=255 仍是不透明。RGB 转 RGBA 后会是全 255，上述检查会拒绝。调色板 PNG 若用 tRNS 表示透明，转换 RGBA 后可正确检查。

另外检查至少一个已知背景点 Alpha=0、一个已知主体点 Alpha 接近255，确认空白区域不是棋盘格位图。分布必须符合本页的实际主体大小；不设通用的“合格透明比例”。纯半透明玻璃等没有不透明主体的特殊素材，按物理含义调整第二个断言并明确记录。

最后在 PPT 的实际底图上确认纸张边缘、细线和阴影正常。遇到预览器把透明显示为黑色时以 Alpha 数值和叠加结果判断，不把黑色本身当成失败或成功。
