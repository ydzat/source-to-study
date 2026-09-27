<!--
 * @Author: @ydzat
 * @Date: 2026-09-27 04:29:23
 * @LastEditors: @ydzat
 * @LastEditTime: 2026-09-27 04:37:43
 * @Description:
-->
# 跟练一次：从课件到自己的笔记

简体中文 · [English](first-session.md)

先完成 [README 中的部署](../README.zh-CN.md)，重启 Agent，并在同一项目目录开启新会话。下面的提示词都发送给 **Agent**；笔记在 **JupyterLab** 中阅读。你不必自己编写脚本或笔记规格。

## 1. 生成笔记框架

我们使用仓库自带的[集中趋势示例 PDF](../examples/central-tendency/README.zh-CN.md)，不需要准备自己的课件。发送：

> 帮我预处理 summarizing_distributions.pdf。

Agent 会按项目 Skill 处理课件、划分知识点并创建笔记框架。如果它询问你的学习目标或请你确认划分，正常回答即可。

在项目文件夹（包含 `pyproject.toml`）打开终端，运行：

```sh
uv run jupyter lab
```

保持终端运行。在 JupyterLab 左侧进入 `study/notes/`，打开 Agent 给出的笔记文件。先看一下知识点划分：例如 K01、K02，以及各自的标题和来源页码。现在是框架，讲解还没填入。

## 2. 让 Agent 讲解 K01

先保存并关闭这个 Notebook 标签页，再发送：

> 我们从 K01 开始吧。

Agent 完成后，重新打开同一个笔记，读一遍 K01 的讲解。

## 3. 随意提问，让笔记更适合你

哪里不明白，就用自己的话问，不必使用固定句式。例如：

> 为什么同一组数据可以有不同的“中心”？我没太理解。

也可以问“这个符号是什么意思？”“这一步怎么算出来的？”或“换一个数字会怎样？”。**发送会修改笔记的请求前，先保存并关闭 Notebook 标签页。**

Agent 会根据你的问题完善笔记。等它完成后，重新打开同一个文件，看看对应内容有哪些变化。

## 4. 运行笔记里的代码

点击代码单元，按 **Ctrl+Enter**，结果或图片会出现在下方。第一次按从上到下的顺序运行，看到 `[*]` 时等它结束。默认快捷键见 [JupyterLab 官方文档](https://jupyterlab.readthedocs.io/en/stable/user/commands.html)。

代码看不懂或报错，也可以直接问 Agent。只运行你信任的代码。

## 5. 理解后再进入下一知识点

还有不明白的地方就继续问，Agent 会不断完善笔记。觉得这部分已经学会后，保存并关闭笔记，再说：

> 这部分我明白了，继续 K02 吧。

以后每个知识点都这样推进，不需要一次生成整门课的讲解。换成自己的课件时，把文件放进 `materials/`，告诉 Agent 文件路径、学习目标和已有基础，再从生成框架开始即可。
