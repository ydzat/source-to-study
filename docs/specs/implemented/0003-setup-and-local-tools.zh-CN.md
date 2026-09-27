# 安装教程与本地学习工具

Status: implemented

## 问题

现有入口无法让学习者从安装 Python 一路操作到可见的 Notebook。私人流程脚本绑定机器与课程；制卡不应要求运行 Anki 或连接服务。

## 决定

guides/ 提供双语 Windows 安装与学习教程。uv 通过 pyproject.toml、uv.lock 和 .python-version 管理项目环境。本地脚本负责 PDF 页预处理、声明式 Notebook 构建、干净内核检查和文件制卡。Agent 操作文件，JupyterLab 展示和运行；先生成框架，再逐单元完善。[工具参考](../../../guides/tools.zh-CN.md)负责命令与格式。

导出 UTF-8 TSV、平铺图片资产和导入说明。稳定笔记 ID 放在用户创建的 STS 笔记类型的首字段。用户自行导入并检查小批次。不连接 Anki、不安装 MCP、不同步或删除卡片。

## 考虑过的替代方案

直接复制私人脚本会带入固定路径和课程假设。Anki 包可方便地包含图片，但需要更多格式专属工具；TSV 加图片需要手动复制，却便于检查且不依赖 Anki。CSV 也能使用，选择制表符是为方便检查包含逗号的正文。完整示例课程继续延后。

## 验证

在 Windows 上使用 uv 0.12.19 建立 Python 3.12.14 隔离环境。`uv run --locked python -m unittest discover -s tests -v` 通过 17 项测试，覆盖文档链接和 JSON 示意、空白页页号、来源保留、覆盖失败、学习者单元保留、编辑冲突与合并、本地资产、真实内核执行与失败、TSV/媒体导出、命令行调用，以及 JupyterLab 启动和根目录定位。测试输入为合成技术夹具，不使用私人课件摘录。不含 Anki API、数据库访问或同步依赖。Anki 桌面端导入及其他操作系统不在本轮验收范围内。

## 影响

提取文本无法证明视觉或公式正确。运行 Notebook 会执行任意代码，不等于安全沙箱。文本导入需要首次设置笔记类型并另行复制媒体。安装教程以 Windows 为目标；导出器交付由用户自行导入的文件，不集成应用。

## 依据

设计参考 [uv 项目管理](https://docs.astral.sh/uv/guides/projects/)、[JupyterLab 启动](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)、[nbclient 执行](https://nbclient.readthedocs.io/en/latest/client.html)、[Anki 文本导入](https://docs.ankiweb.net/importing/text-files.html)及 [Anki 包](https://docs.ankiweb.net/exporting.html)。
