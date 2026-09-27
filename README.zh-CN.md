# Source to Study

简体中文 · [English](README.md)

结合能操作文件的 AI Agent，复习你自己的课程材料。Agent 帮你整理和完善笔记；JupyterLab 用来阅读笔记、运行例子和作答。不绑定特定 Agent 服务商。

## 安装与启动

下载并解压本仓库，安装 [uv](https://docs.astral.sh/uv/getting-started/installation/)，然后在包含 `pyproject.toml` 的目录打开终端，运行：

```sh
uv sync --locked
uv run python scripts/init_workspace.py
uv run jupyter lab
```

uv 管理 Python 和项目的 `.venv`，无需另装 Python/Jupyter，也不用手动激活环境。使用 JupyterLab 时保持最后这个终端运行。

**第一次接触这些工具？请跟着[Windows 完整入门教程](guides/getting-started.zh-CN.md)操作。** 教程说明安装方法、在哪里打开终端、在哪个窗口聊天，以及怎样找到 Notebook。

## 和 Agent 一起复习

项目自带三个按需加载的[学习 Skills](guides/skills.zh-CN.md)：课程初始化、学习会话和按需制卡。你自然描述任务，Agent 按对应流程执行；指南也说明了无法自动发现时如何直接读取文件。

使用能操作文件的 Agent，例如 Codex 或 OpenCode，另行安装并登录。在 Agent 中打开本项目目录，把 PDF 放入 `materials/`，然后说：

> 阅读 AGENTS.md 和 guides/tools.zh-CN.md。我的课程是【科目】，目标是【目标】，教学语言是【语言】，来源是 materials/【文件名.pdf】。先建立课程档案、检查来源并提出知识点划分。等我确认后，在 study/notes/ 生成 Notebook 框架，不要一次写完所有讲解。

在 JupyterLab 左侧文件浏览器进入 `study/notes/`，打开生成的 `.ipynb`。继续**在 Agent 中**对话，例如：

> 现在只讲 K01。先解释符号，再从源课件的目标一步步推到结果，配图和具体例子。更新对应笔记并运行检查，等我提问后再推进。

Agent 重建前先保存并关闭 Notebook 标签页，完成后重新打开。在“我的作答”单元中填写答案。学习结束时让 Agent 记录实际表现和下次起点；新开聊天时，先让它读取课程档案和最新会话再继续。

## 按需生成复习卡片

你提出要求后，Agent 可以基于指定的已完成笔记及源材料制卡。导出器生成 **TSV + 图片 + 导入说明**，同时提供便于搬运的 ZIP。由你手动导入 Anki，不需要 MCP、插件或 Anki 连接。详见[导入教程](guides/anki.zh-CN.md)。

## 你的文件放在哪里

| 位置 | 内容 |
|---|---|
| `materials/` | 原始课程文件 |
| `study/COURSE.md` | 学习目标、来源地图和学习文件链接 |
| `study/specs/`、`study/notes/` | 教学规格真源和学习 Notebook |
| `study/sources/` | 按页提取的文字及源课件页图 |
| `study/review/`、`study/sessions/` | 复习材料与真实学习进度 |
| `output/` | 你选择导出的文件 |

这些目录已被 Git 忽略，但不是访问控制。提供材料前检查 AI 服务商的数据政策，公开工作区前检查文件和历史。[MIT 许可证](LICENSE)覆盖模板，不自动覆盖你的课程材料；学习时遵守学校的 AI 使用规则。

精确命令和文件格式见[工具参考](guides/tools.zh-CN.md)；维护 STS 本身则阅读[开发文档](docs/README.zh-CN.md)。
