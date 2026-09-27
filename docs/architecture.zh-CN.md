# 工作区架构

简体中文 · [English](architecture.md)

## 公开模板

| 位置 | 职责 |
|---|---|
| 根目录 README 双语文件 | 学习者初始化与学习流程 |
| 根目录 AGENTS 双语文件 | AI 导师的常驻规则 |
| `.agents/skills/` | 按需加载的课程初始化、学习会话和制卡流程 |
| `guides/` | 学习者安装、本地工具约定和手动 Anki 导入 |
| `templates/` | 中英字段空表单，用学习者选定语言填写一份 |
| `scripts/` 与 `tests/` | 通用本地操作与行为测试 |
| `pyproject.toml`、`uv.lock`、`.python-version` | 直接依赖、解析锁与项目 Python 选择 |
| `examples/` | 学习流程的原创样例 |
| `docs/` | 维护约定与设计记录 |

## 本地学习工作区

初始化根据表单创建 `study/COURSE.md`，负责目标、来源索引及笔记、复习问题和最新会话链接。`study/specs/` 中的教学 JSON 生成 `study/notes/` 的 Notebook，其中学习者单元仍属于用户。PDF 页图和清单位于 `study/sources/`，复习/制卡输入位于 `study/review/`，日期化会话位于 `study/sessions/`。[工具参考](../guides/tools.zh-CN.md)负责格式与命令。

原始材料保留在 `materials/` 或指定位置，Anki 导出位于 `output/`，不连接 Anki。衍生产物存入[发布约定](conventions.zh-CN.md)规定的忽略目录。uv 管理 `.venv`；学习者使用独立的文件操作 Agent 与 JupyterLab。只用 Markdown 学习仍可不执行 Notebook 工具。

结构决定记录在[此处](specs/implemented/0001-learning-workspace.zh-CN.md)。自动化提案与当前工作区约定分开。
