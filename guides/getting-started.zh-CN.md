# 从下载到第一次复习

简体中文 · [English](getting-started.md)

你会使用两个窗口：**AI Agent** 负责对话、查阅材料和修改文件，浏览器里的 **JupyterLab** 负责阅读笔记、运行代码和作答。JupyterLab 不是聊天窗口；两者访问的是电脑上的同一批文件。

## 推荐：让 Agent 完成部署

下载、解压仓库，用能操作文件的 Agent 打开项目目录，说：

> 阅读 AGENTS.md 和 .agents/skills/sts-setup/SKILL.md，按这个 Skill 安装并验证本项目。

检查通过后，重启 Agent 软件，在同一目录开启新会话。**跳过下面的手动步骤 1–3，从第 4 步开始。** 在此之前把第一份 PDF 放进 `materials/`。完整原创 PDF 示例课程尚未加入；当前[原创论证例子](../examples/README.zh-CN.md)展示讲解风格，本教程则带你处理自己的第一份课件。

部署不会开始学习会话，也不会留下运行中的 JupyterLab。可以让新会话中的 Agent 带你阅读本教程。部署失败时不能视为就绪：提供失败阶段和错误，不要提供私人令牌。最近的部署状态记录在 `work/setup/report.json`。

## 1. 手动备用方案：下载模板，安装 uv

在[仓库页面](https://github.com/ydzat/source-to-study)选择 **Code → Download ZIP**，解压到一个以后容易找到的文件夹。也可以使用 Git 克隆；下载 ZIP 不需要安装 Git 或注册 GitHub。

先安装一次 uv。它负责管理 Python 和项目隔离环境，不用分别安装 Python、JupyterLab 和科学计算依赖。下面的安装方式来自 [uv 官方说明](https://docs.astral.sh/uv/getting-started/installation/)。

Windows：打开 PowerShell，运行：

```powershell
winget install --id=astral-sh.uv -e
```

如果没有 WinGet，可按上述官方说明选择其他 Windows 安装方式。安装后关闭并重新打开终端，运行 `uv --version`。如果找不到命令，按安装提示处理 PATH，确认成功后再继续。

## 2. 在项目文件夹打开终端

正确的目录中应能看到 `README.md`、`AGENTS.md` 和 `pyproject.toml`，不是外层“下载”文件夹，也不是 `.venv`。

Windows 可以在文件资源管理器打开解压后的目录，右键选择“在终端中打开”。也可以输入 `cd` 和实际路径：

```powershell
cd "C:\your\folder\source-to-study-main"
```

上面是示意路径，必须换成你自己的。后续所有命令都在这个项目目录执行。

## 3. 安装环境，准备学习目录

```sh
uv sync --locked
uv run python scripts/init_workspace.py
uv run python scripts/check_setup.py
```

第一条命令会在需要时下载指定 Python，并将锁定依赖安装进项目的 `.venv`，首次需要联网，可能耗时数分钟。第二条创建学习目录和空课程档案，不覆盖已有文件。第三条检查真实内核，短暂启动并停止 JupyterLab，不开始学习会话。不需要手动激活虚拟环境。环境与锁文件机制见 [uv 项目指南](https://docs.astral.sh/uv/guides/projects/)。

把第一份 PDF 复制到 `materials/`。先从一份课件开始，不必一次处理整个学期。其他格式可让 Agent 读取，或另行转成 PDF；当前预处理脚本只接收 PDF，不改写原材料。

## 4. 打开 Agent，建立课程档案

仓库自带[学习 Skills](skills.zh-CN.md)，不用每次重复全部操作规则。在 Agent 中打开项目本身，兼容工具即可发现 `.agents/skills/`；无法发现时，按该指南直接读取文件。

你需要能操作文件的 Agent 程序，例如 Codex、OpenCode。这只是举例，不要求选择特定服务商。按你所选程序的官方说明安装和登录；它需要能读写项目文件、查看页面图片，并在获得授权后运行本地命令。无法访问文件的普通聊天窗口，不能独立完成这些操作。

在 Agent 中打开**同一个项目文件夹**，告诉它：

> 阅读 AGENTS.md 和 guides/tools.zh-CN.md。这个项目使用 uv。我的课程是【科目】，目标是【学习或考核目标】，用【语言】讲解。第一份来源是 materials/【文件名.pdf】。帮我完善 study/COURSE.md，查看来源并划分知识单元。先给我看单元划分和来源页码，不要一次写完全部讲解。

回答它关于前置知识、考核要求和 AI 使用规则的问题，确认它找到的是正确文件。能访问本地文件不代表模型在本地运行：提供私人材料前，检查所用服务的数据政策。

## 5. 让 Agent 生成笔记框架

确认来源范围和知识点划分后，说：

> 用 scripts/prepare_pdf.py 预处理 PDF，按 guides/tools.zh-CN.md 在 study/specs/ 创建教学规格，再用 scripts/nb_build.py 生成 study/notes/lecture01.ipynb。未讲单元保持 todo，检查框架。如果开头是上一讲的 recap，先与上一份材料核对，再保留回指，不删除任何源课件页。

脚本由 Agent 操作，你不必自己编写 JSON。框架包含来源地图和占位章节，**不是已经完成的讲解**。你应收到 Notebook 路径、覆盖范围和验证结果。

## 6. 启动 JupyterLab，找到笔记

在项目终端运行：

```sh
uv run jupyter lab
```

保持这个终端运行。JupyterLab 通常会自动在浏览器打开；没有打开时，复制终端中显示的本地网址到浏览器，不要分享其中的访问令牌。从项目目录启动，左侧文件浏览器就从该目录开始。依据见 [JupyterLab 启动说明](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)与 [uv 的 Jupyter 指南](https://docs.astral.sh/uv/guides/integration/jupyter/)。

在左侧依次打开 `study`、`notes`，双击 `lecture01.ipynb`。用来学习的是这个文件，不是 JSON 规格。若提示选择内核，选择项目的 Python 内核。`Shift+Enter` 运行当前单元格。只运行可信代码：它是本地 Python 执行，不是安全沙箱。

## 7. 一次完善一个知识点

回到 Agent 的聊天窗口：

> 现在只讲 K01。从源课件的目标出发，先解释新符号，再把中间步骤串到最终结果。尽量用同一个具体例子贯穿，插图紧跟知识点，图解紧跟插图。通过规格更新 Notebook 并运行检查，其余单元保持占位。聊天中简述改动，不重复整篇笔记。

在 JupyterLab 阅读更新后的笔记，先预测再运行实验。不理解时，在 Agent 窗口追问，例如：

> 我看不懂这个输入如何变成下一个对象。请展示中间结果，并修改 K01 对应章节，不要在末尾追加一段孤立问答。

理解后再让它继续 K02。对于不适合代码实验的学科，使用图解、具体推理和回忆练习，不硬凑代码。

Agent 重建已打开的笔记前，**先保存并关闭该标签页**，完成后重新打开。在“我的作答”或自己新增的单元格中写答案。生成的讲解单元来自规格；直接编辑它们会触发重建冲突，必须由 Agent 合并，不能强行覆盖。重建会备份原文件并保留学习者单元；生成的代码输出会清空，可重新运行。没有生成标记的新增单元会保留在末尾。

## 8. 结束、恢复，以及按需制卡

学习结束时说：

> 在 study/sessions/ 记录实际已学范围、我的表现证据、待解决问题和下次起点，更新课程档案中的链接。不要仅因生成笔记就标为掌握。

保存 Notebook。停止 JupyterLab 时回到终端，按 `Ctrl+C`，如有提示则确认关闭；只关浏览器不一定会停止服务。下次进入同一目录，运行 `uv run jupyter lab`，并让 Agent 先读 `study/COURSE.md`、最新会话及相关笔记，再继续。

卡片按需生成，不自动制卡：

> 基于这些已完成笔记【路径】，必要时结合这些源课件范围【路径及页码】，整理重点复习卡片。核验来源，加入有帮助的图，按 guides/anki.zh-CN.md 生成导入文件。不要连接或修改 Anki。

之后按独立的 [Anki 导入教程](anki.zh-CN.md)操作。生成文件本身不需要安装 Anki。

## 常见问题

| 现象 | 处理方法 |
|---|---|
| 找不到 `pyproject.toml` | 返回解压后的项目目录，不在 `study/` 或 `.venv/` 里运行。 |
| 提示缺包 | 运行 `uv sync --locked`；JupyterLab 和脚本都用 `uv run`。课程需要新依赖时先让 Agent 说明，再用 `uv add`。 |
| 检查提示内核错误 | 让 Agent 检查 `uv run jupyter kernelspec list`，选择或修正项目内核，不删除全局内核。 |
| PDF 没文字或公式缺失 | 检查渲染页图；文本提取不是 OCR，也可能漏公式。 |
| 仍显示旧笔记 | 重建前保存关闭，重建后重新打开，避免用浏览器旧副本覆盖外部更新。 |
| 脚本失败 | 把完整错误和命令交给 Agent，修复原因，不跳过失败检查。 |

自己的来源和学习产物默认私有；模板开源不意味着可以公开 `materials/`、`study/` 或 `output/`。
