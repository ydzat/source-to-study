# 工作区架构

简体中文 · [English](architecture.md)

## 公开模板

| 位置 | 职责 |
|---|---|
| 根目录 README 双语文件 | 学习者初始化与学习流程 |
| 根目录 AGENTS 双语文件 | AI 导师的常驻规则 |
| `templates/` | 中英字段空表单，用学习者选定语言填写一份 |
| `examples/` | 学习流程的原创样例 |
| `docs/` | 维护约定与设计记录 |

## 本地学习工作区

助手根据课程表单创建 `study/COURSE.md`。课程档案负责目标与来源索引，并链接笔记、复习问题和最新会话。笔记位于 `study/notes/`，复习材料位于 `study/review/`，日期化会话位于 `study/sessions/`。这些是直接维护的学习真源，不是生成的导出物。

原始材料保留在 `materials/` 或学习者指定位置。衍生缓存与导出物放入[发布约定](conventions.zh-CN.md)规定的忽略目录。使用这些表单无需命令行管线或 UI 框架。

结构决定记录在[此处](specs/implemented/0001-learning-workspace.zh-CN.md)。自动化提案与当前工作区约定分开。
