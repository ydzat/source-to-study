# 本地工具与文件约定

简体中文 · [English](tools.md)

本页供操作文件的 Agent 查阅。学习者可以沿[入门教程](getting-started.zh-CN.md)通过对话操作。所有命令从项目根目录使用 `uv run` 执行；下列输入路径是示意，实际使用学习者的文件。

## 环境与初始化

`pyproject.toml` 记录直接依赖，`uv.lock` 锁定解析版本，`.python-version` 选择 Python 3.12。先运行 `uv sync --locked`，然后：

```sh
uv run python scripts/init_workspace.py
```

它创建本地学习目录，仅在 `study/COURSE.md` 不存在时复制课程表单。不使用全局 pip，不安装 Anki 集成。课程确需新依赖时先获得授权，再用 `uv add` 更新项目依赖文件。

## PDF 预处理

```sh
uv run python scripts/prepare_pdf.py materials/lecture01.pdf study/sources/lecture01
```

新目录中包含 `manifest.json`、`p0001.txt`、`p0001.png` 及每页对应文件，包括空白页。清单记录来源相对路径、SHA-256、页数、渲染 DPI 和资产名称。已有输出目录会被拒绝；来源变化后使用新目录，再更新规格。

脚本使用 Python 环境提供的 PDFium 与 Pillow，不要求另装 TeX 或 Poppler。提取文字用于搜索，不是公式转录真源。不执行 OCR，也不自动判断知识点。应检查页图并与学习者确认单元划分；recap 中混入的新知识须保留。

## Notebook 真源与构建

创建 `study/specs/lecture01.json`。以下只展示结构，不代表一份真实的三页课程：

```json
{
  "version": 1,
  "title": "课程 — 第一讲",
  "language": "zh-CN",
  "manifest": "../sources/lecture01/manifest.json",
  "assets": [],
  "units": [
    {"id": "K01", "title": "第一个单元", "pages": [1, 2], "status": "todo"},
    {"id": "K02", "title": "第二个单元", "pages": [3], "status": "todo"}
  ]
}
```

英文框架标题使用 `language: "en"`。页列表必须恰好覆盖实际 PDF 一次。明确的背景单元可使用空页列表，但不能借此掩盖来源覆盖缺口。状态为 `todo`、`ready` 或 `recap`；`ready` 仅表示已撰写，不表示掌握或自动核验。recap 单元必须给出非空 `recap` 回指，不能包含教学单元格。

```sh
uv run python scripts/nb_build.py study/specs/lecture01.json study/notes/lecture01.ipynb
uv run python scripts/nb_check.py study/notes/lecture01.ipynb
```

`manifest` 相对规格文件定位。单元格内容和 `assets` 中的路径相对**输出 Notebook 所在目录**定位。代码读取的数据等本地依赖要列入 `assets`；检查器也解析 Markdown 和 HTML 图片引用，但无法推断 Python 任意拼接的路径。

讲解某单元时增加 `cells` 列表，每项含稳定 `id`、`type`（`markdown` 或 `code`）和字符串 `source`：

```json
{"id": "notation", "type": "markdown", "source": "### 符号\n\n在这里定义每个新对象。"}
```

该列表替换本单元默认六段占位。按教学约定组织：目标/来源、符号、推导、适用时的预测/运行/改变条件、独立复现、收口。图插在对应环节，不集中到末尾；学习者作答前不加入测验答案。`intro`、`response` 是保留生成后缀；其他单元格 ID 在本单元内唯一。实际讲解完成前保持 `todo`。

构建器检查来源哈希、页覆盖、单元格身份和清单资产，保留 `sts.owner=learner` 单元中的答案及输出，未知的用户新增单元追加在末尾。直接修改生成单元的正文或附件会被拒绝；先将改动合并进规格及保留的学习者单元，再重建，不能移除保护来覆盖。每次成功替换前保留同目录备份。重建清空生成代码的输出，避免展示过期结果。重建前必须保存并关闭笔记，脚本无法保护浏览器中未保存的状态。

## 执行检查

检查器通过 nbclient 在干净 Python 内核中执行可信代码，以 Notebook 所在目录为工作目录；不修改输入文件，遇错停止。另检查本地图片引用和声明的资产。预检查核验解释器，并把 NumPy 除零、溢出和非法操作警告升级为错误，下溢仍允许。它是验证，**不是副作用隔离**；运行陌生代码前先检查。

空框架没有可执行单元，仅获得结构检查。执行通过不能证明来源、数学、完整性或掌握程度正确。依据见 [nbclient 执行约定](https://nbclient.readthedocs.io/en/latest/client.html)。

## 只导出文件的制卡

仅在用户要求时制卡。在 `study/review/` 准备经过审阅的 JSON：

```json
{
  "version": 1,
  "cards": [{
    "id": "my-course.k01.q01",
    "front": "围绕单一目标的回忆问题",
    "back": "经过核验的答案。行内公式：\\(x^2\\)。",
    "source": "lecture01.pdf，PDF p.3；notes/lecture01.ipynb，K01",
    "front_images": [],
    "back_images": [{"path": "../notes/img/diagram.png", "alt": "这张图展示什么"}],
    "tags": ["my_course", "K01"]
  }]
}
```

`front`、`back` 和 `source` 是非空纯文本，不是 Markdown 或原始 HTML。导出器转义 HTML 字符并转换正文换行。公式明确使用 Anki MathJax 分隔符，反斜杠按 JSON 转义，每个公式保持在一条物理行。图片路径相对卡片 JSON，使用 PNG/JPEG 和有意义的替代文字；图片数组可省略，图片显示在对应面的文字之后。导出器记录来源，但不核验来源语义。

ID 稳定且唯一，使用字母、数字、`.`、`_`、`:`、`-`，带课程前缀。标签不含空白。导出器在创建输出前拒绝缺字段、重复 ID、非法图片签名和缺失媒体。

```sh
uv run python scripts/export_cards.py study/review/cards.json output/anki-review-01
```

输出含 UTF-8 `cards.tsv`，列为 `ID`、`Front`、`Back`、`Source`、`Tags`；还有平铺的内容哈希命名图片、模板、清单和双语说明，旁边生成 ZIP 搬运副本。不连接 Anki、不导入、不删除、不调度或同步。导入操作见[独立教程](anki.zh-CN.md)。
