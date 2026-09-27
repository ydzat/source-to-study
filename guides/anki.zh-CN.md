# 将 STS 卡片导入 Anki

简体中文 · English：仓库中查看 anki.md，导出包中查看 IMPORT.md。

STS 只导出文件，不读取 Anki 数据库、不启动 Anki、不安装插件，也不改变已有卡片。何时导入、导入哪里，由你决定。

## 你会得到什么

导出目录包含 `cards.tsv`、`media/`、清单、卡片模板片段和本说明。目录旁的 ZIP 是便于搬运的副本：**先解压，不要把 ZIP 直接导入 Anki**。

选择 UTF-8 TSV 是为了文本可检查、导出仅依赖标准库。Anki 也支持 CSV，但二者都不能嵌入图片，图片要另行复制，并由字段引用。`.apkg` 可以把媒体一起打包，但本项目当前没有实现该导出。依据见官方[文本导入](https://docs.ankiweb.net/importing/text-files.html)与[包格式说明](https://docs.ankiweb.net/exporting.html)。

## 让 Agent 制卡

告诉 Agent 使用哪些已完成笔记、需要哪些源课件范围、复习语言和范围。它应核验来源，围绕单一回忆目标出题，不把整段讲义塞进答案，并按工具参考生成 `study/review/cards.json`。先审阅拟生成内容，再要求导出。

```sh
uv run python scripts/export_cards.py study/review/cards.json output/anki-review-01
```

每次使用新的输出目录。稳定 ID 用来识别同一笔记的不同版本；加课程前缀，修改题目或答案时不改变 ID。

## 首次在桌面 Anki 设置

1. 打开“工具 → 管理笔记类型”，复制基础的单卡问答类型，命名为 `STS`。
2. 在“字段”中按顺序设置四个字段：`ID`、`Front`、`Back`、`Source`，确保 `ID` 在第一位。标签不是第五个自定义字段。
3. 在“卡片”中把正面模板替换为 `{{Front}}`，背面模板替换为：

```html
{{FrontSide}}<hr id="answer">{{Back}}<hr><small>{{Source}}</small>
```

4. 可在样式中加入 `img { max-width: 100%; height: auto; }`。导出包也提供模板和样式文件，可直接复制。

ID 用于匹配，不会显示在卡面。这种类型每条笔记生成一张问答卡，不选择自动反向卡或挖空类型。字段与模板操作见 Anki 的[编辑说明](https://docs.ankiweb.net/editing.html)和[字段替换说明](https://docs.ankiweb.net/templates/fields.html)。

## 先导入一小批

1. 更新已有笔记前先备份集合，创建或选择目标牌组。
2. 将导出 `media/` **内部的文件**复制到当前配置档案的 `collection.media`，不创建子目录。遇到不同内容的已有同名文件，不盲目覆盖。生成文件名含内容哈希，以减少冲突。Windows 的配置档案通常位于 `%APPDATA%\Anki2`，自定义安装可能不同。详见[文件位置](https://docs.ankiweb.net/files.html)。
3. “文件 → 导入”，选择 `cards.tsv`、`STS` 类型和目标牌组。在预览中确认分隔符为 Tab、允许 HTML，以及 `ID → ID`、`Front → Front`、`Back → Back`、`Source → Source`、`Tags → 标签` 的映射。现代 Anki 可读取文件头，但仍需检查预览。
4. 导入前检查重复项/更新设置。首字段和选择的匹配范围会影响已有笔记的更新；保留稳定 ID。后续导出中删除某行，**不会**删除 Anki 内对应笔记。详见[文本导入规则](https://docs.ankiweb.net/importing/text-files.html)。
5. 抽查题目、答案、图片、公式和来源，并对照 `manifest.json` 中的笔记数量，确认后再导入大批内容。

公式使用行内 `\(...\)` 或块级 `\[...\]`，不是 Notebook 中的 `$...$`。Anki 内置 MathJax 不要求另装 LaTeX，依据见[数学记号说明](https://docs.ankiweb.net/math.html)。

## 边界

导出器检查文件结构、标识、必填字段和引用图片，不证明知识讲解或来源引用正确。当前支持基础问答和 PNG/JPEG 图片，不支持挖空、图像遮挡、音频、复习调度或同步。文件导出成功不等于已在你的 Anki 版本中验证过导入，首次需自行检查。

缺图时检查当前配置档案、文件名和 HTML 选项；公式显示为文本时让 Agent 修正 MathJax 分隔符。STS 使用 MIT 许可证，不意味着你的私人制卡包可以公开上传。
