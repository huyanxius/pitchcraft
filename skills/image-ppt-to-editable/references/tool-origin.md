# 本地工具来源

`scripts/remove_chroma_key.py` 原样来自 ningzimu/image-to-editable-ppt-skill，提交 `b730e426ed5808c70b48ef7a3408db135341f571`。

源文件：<https://github.com/ningzimu/image-to-editable-ppt-skill/blob/b730e426ed5808c70b48ef7a3408db135341f571/skills/image-to-editable-ppt/cli/editppt/runtime/remove_chroma_key.py>

作者版权与 MIT 许可证完整保存在 `scripts/LICENSE-ningzimu.txt`。只内置这一份确定性纯色抠除工具，不依赖原仓库 CLI、OAuth、OCR Token、Agent 编排或配置文件。

运行依赖：Python 3 和 Pillow。脚本默认拒绝覆盖输出，不会联网。新增版本若修改源脚本，须注明变更并重新验证 Alpha 行为。
