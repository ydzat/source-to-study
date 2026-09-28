# Source to Study (STS)

简体中文 · [English](README.md)

**版本 1.1** · Windows 部署 · [MIT 许可证](LICENSE)

结合能操作文件的 AI Agent，复习你自己的课程材料。Agent 帮你整理和完善笔记；JupyterLab 用来阅读笔记、运行例子和作答。不绑定特定 Agent 服务商。

## 功能

- 提取 PDF 文字、渲染页图、核验页覆盖，生成知识单元框架。
- 根据来源撰写讲解，定义符号、逐步推理、图文相邻，提供完整核对答案。
- 按科目和考核采用 Predict → Run → Break it → Reproduce。
- 声明式 Notebook 生成、干净内核检查、备份与学习者单元保留。
- 分别记录材料就绪、自述完成、练习和独立展示能力。
- 按需导出 TSV 与图片，供手动导入 Anki。

## 环境要求

- Windows 与 PowerShell，用于文档规定的部署流程。
- 已安装、已登录，能够读写项目文件并执行获准命令的 AI Agent；服务商由你自行选择。
- 用于 JupyterLab 的浏览器，以及首次下载依赖所需的网络连接。
- 有权使用的课程材料；自动预处理目前接收 PDF。

uv 管理环境及 `.python-version` 指定的 Python 版本，目前为 Python 3.12。其他操作系统尚未完成文档所述部署验收。

## 快速开始

### 1. 部署工作区

在 Windows 上下载并解压本仓库。用已安装、已登录且能操作文件的 AI Agent（例如 Codex 或 OpenCode）打开解压后的目录，然后说：

> 阅读 AGENTS.md 和 .agents/skills/sts-setup/SKILL.md，按这个 Skill 安装并验证本项目。完成后简短报告结果和下一步。

Agent 会检查 uv、安装锁定的 Python 环境、准备目录，并实际测试 Notebook 内核和 JupyterLab。需要下载时按 Agent 提示批准；不用自己分别安装 Python、Jupyter。不支持自动发现 Skill 的 Agent 也可以直接读取这个文件。

部署成功后，**重启 Agent 软件，在同一目录开启新会话**，再用自带 PDF 跟着[简短跟练教程](guides/first-session.zh-CN.md)操作。重启是保守的入门步骤，不代表所有 Agent 都有这个技术要求。

想手动安装？请看[手动安装步骤](guides/getting-started.zh-CN.md)。已有 uv 时，可运行统一部署与验证入口：

```powershell
./scripts/setup.ps1
```

### 2. 打开 JupyterLab

在项目目录打开终端，运行：

```sh
uv run jupyter lab
```

uv 管理 Python 和项目的 `.venv`，无需另装 Python/Jupyter，也不用手动激活环境。使用 JupyterLab 时保持最后这个终端运行。

## 使用方式

### 准备与复习课程

项目自带按需加载的 [Skills](guides/skills.zh-CN.md)：环境部署、课程初始化、学习会话和按需制卡。你自然描述任务，Agent 按对应流程执行；指南也说明了无法自动发现时如何直接读取文件。

使用能操作文件的 Agent，例如 Codex 或 OpenCode，另行安装并登录。在 Agent 中打开本项目目录，把 PDF 放入 `materials/`，然后说：

> 帮我预处理 materials/【文件名.pdf】。我在学【科目】，目标是【目标】，目前会【已有基础】，用【语言】讲解。

在 JupyterLab 左侧文件浏览器进入 `study/notes/`，打开生成的 `.ipynb`。继续**在 Agent 中**对话，例如：

> 我们从 K01 开始吧。

疑问可直接在聊天中提出。需要把解释写进文件时，明确要求更新笔记。

Agent 重建前先保存并关闭 Notebook 标签页，完成后重新打开。在“我的作答”单元中填写答案。学习结束时让 Agent 记录实际表现和下次起点；新开聊天时，先让它读取课程档案和最新会话再继续。

[教学流程](guides/teaching.zh-CN.md)说明每个单元怎样连接源目标、对象定义、逐步推理、可观察结果和独立复现，并规定课程范围检查、完整笔记答案与现场测验的区别。

### 导出复习卡片

你提出要求后，Agent 可以基于指定的已完成笔记及源材料制卡。导出器生成 **TSV + 图片 + 导入说明**，同时提供便于搬运的 ZIP。由你手动导入 Anki，不需要 MCP、插件或 Anki 连接。详见[导入教程](guides/anki.zh-CN.md)。

## 项目结构

| 位置 | 内容 |
|---|---|
| `AGENTS.md`、`.agents/skills/` | 导师规则与专项任务流程 |
| `guides/`、`templates/` | 使用指南与学习空表单 |
| `examples/` | 原创样例及注明来源的外部学习材料 |
| `scripts/`、`tests/` | 本地工具与自动检查 |
| `docs/` | 维护文档与设计决定 |
| `materials/` | 原始课程文件 |
| `study/COURSE.md` | 学习目标、来源地图和学习文件链接 |
| `study/specs/`、`study/notes/` | 教学规格真源和学习 Notebook |
| `study/sources/` | 按页提取的文字及源课件页图 |
| `study/review/`、`study/sessions/` | 复习材料与真实学习进度 |
| `output/` | 你选择导出的文件 |
| `work/` | 本地中间产物 |

## 文档

- [安装与故障排查](guides/getting-started.zh-CN.md)
- [首次学习会话](guides/first-session.zh-CN.md)
- [教学流程与质量检查](guides/teaching.zh-CN.md)
- [可用 Skills](guides/skills.zh-CN.md)
- [命令与文件格式](guides/tools.zh-CN.md)
- [Anki 导入](guides/anki.zh-CN.md)
- [开发与维护](docs/README.zh-CN.md)

## 版本历史

### 1.1 — 当前版本

- 增加源步骤覆盖、最小必要例子和四项独立教学质量检查。
- 完善正式笔记答案要求，同时保留现场测验等待作答的规则。
- 补齐表达、证据、授权、安全编辑与验证要求，同步指令和教程。
- 明确疑问句不自动授权改笔记，分别记录自述完成、跳过与掌握证据。
- 重整双语 README，将项目元数据统一为 `1.1.0`。

### 1.0 — 此前基线

此前的模板追溯命名为 **1.0**，已具备 Windows/uv 部署、来源预处理、Notebook 生成与检查、学习会话流程及文件制卡导出。

这里记录项目版本，不表示已发布对应 Git tag 或 GitHub Release。1.1 沿用现有文件格式和运行依赖。

## 隐私与局限

个人材料、学习记录、中间文件和导出内容放在被忽略的 `materials/`、`study/`、`work/`、`output/` 目录中。Git 忽略规则不提供访问控制，公开前须检查文件和历史。提供材料前，确认 AI 服务商的数据政策及学校的 AI 使用规则。

Notebook 代码以执行进程的权限在本地运行，陌生代码须检查。执行成功只能验证对应技术性质；来源准确性、讲解完整性和学习者能力需要各自的证据。

## 支持与贡献

部署问题可参照故障排查指南，提供相关错误前移除敏感信息。修改仓库时遵循[维护文档](docs/README.zh-CN.md)，保持双语一致、保护个人数据，并运行与改动相关的检查。

## 许可证

模板采用 [MIT 许可证](LICENSE)，版权所有者为 Dongze Yang。课程材料保留各自权利，附带 PDF 的署名与再使用信息见[示例来源](examples/central-tendency/README.zh-CN.md)。
