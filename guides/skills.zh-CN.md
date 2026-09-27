# 使用项目自带的学习 Skills

简体中文 · [English](skills.md)

Skill 把 Agent 反复执行的任务整理成按需加载的流程。你描述学习目标，Agent 选择对应流程并使用现有本地工具。它不替换 Agent、不安装额外服务，也不连接 Anki。

## 你可以怎么说

| 你的请求 | 对应流程 |
|---|---|
| “准备这份课件，先给我笔记框架。” | `sts-course-setup`：课程档案、来源检查、单元划分、框架验证 |
| “继续 K03”或“修改笔记里这部分讲解。” | `sts-study-session`：恢复上下文、讲解指定单元、更新和核验笔记 |
| “抽问我”或“结束今天的学习，记录下次起点。” | `sts-study-session`：实际练习与有证据的会话记录 |
| “根据这些笔记制卡并导出。” | `sts-export-cards`：核验来源、整理制卡输入、导出 TSV 与图片 |

上下文不明确时指出文件或单元即可。STS 不要求特殊调用语法，默认用自然语言表达；也可以明确让 Agent 使用某个 Skill。

## Agent 如何发现它们

在 Agent 中打开 STS 目录本身。文件位于 `.agents/skills/<名称>/SKILL.md`；目录前面的点不代表可以删除。下载或复制模板时保留 `.agents/`。

Codex 文档列出 `.agents/skills/` 作为仓库发现位置，OpenCode 文档也列出相同的兼容位置；两者均支持按需加载 Skill 正文。这是宿主文档描述的能力，不保证所有版本和配置每次都自动选对。依据见 [OpenAI 官方文档](https://learn.chatgpt.com/docs/build-skills)和 [OpenCode 文档](https://opencode.ai/docs/skills)。

增加或更新后，可以问 Agent：“当前有哪些 `sts-` Skills？”如果没有出现，重新打开项目或新建会话，检查项目目录和宿主的 Skill 权限，不要为了绕过限制擅自修改全局配置。

## Agent 没有自动发现时

可以直接让它读取文件：

> 阅读 AGENTS.md，再读取 .agents/skills/sts-course-setup/SKILL.md，按其中流程准备 materials/【我的课件.pdf】。

讲解或制卡时替换成相应名称。这要求 Agent 确实能读取项目文件，不意味着发生了原生 Skill 加载。如果它不会自动加载 AGENTS.md，也要明确提供该文件。

## 各类信息放在哪里

`AGENTS.md` 保留长期教学与安全原则；Skills 负责任务步骤；[工具参考](tools.zh-CN.md)负责命令和格式；`scripts/` 负责确定性操作。Skill 引用这些文件，不另存一套容易漂移的副本。

机器入口使用英文，但 Agent 仍按课程选定的语言教学；本指南与用户教程提供中英版本。加载 Skill 本身不代表授权安装、公开资料、每课自动制卡或修改掌握状态。
