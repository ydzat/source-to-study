# 示例来源：集中趋势

简体中文 · [English](README.md)

这是外部公有领域材料，不是 STS 原创课程，也不是学习者的私人课件。按[简短跟练教程](../../guides/first-session.zh-CN.md)，让自己的 Agent 生成并逐步完善笔记即可，不要求或附带预写的参考 Notebook。

## 来源与再利用

- 作品：*Online Statistics Education: A Multimedia Course of Study*，第 3 章 *Summarizing Distributions*。
- 项目负责人：Rice University 的 David M. Lane。选定小节署名 David M. Lane 和 Heidi Ziemer（按本章印刷拼写）。
- [官方章节页面](https://onlinestatbook.com/2/summarizing_distributions/summarizing_distributions.html)、[原始 PDF](https://onlinestatbook.com/2/summarizing_distributions/summarizing_disributions.pdf)、[官方公有领域声明](https://onlinestatbook.com/lms/)。
- 本地文件：[summarizing_distributions.pdf](summarizing_distributions.pdf)。下载日期 2026-09-27，共 41 页、695,407 字节。原始 URL 确实拼作 `disributions`。
- SHA-256：`a4aad77d737740d76b1a0e4c8106a4aeb2ddb536c7fa9c50551f407ea5a62170`。
- 修改：无，逐字节保留原 PDF，未裁剪、翻译或删除页面。其公有领域地位来自发布方声明，不来自 STS 的 MIT 许可证；不暗示原作者为 STS 背书。

## 首次跟练范围

只使用 **PDF 第 2–13 页**，共 12 页、三个完整小节。对应书内印刷页码 124–135；引用时应使用下表的 PDF 页号。

| 单元 | PDF 页号 | 学习目标 |
|---|---|---|
| K01：什么是集中趋势 | 2–8 | 理解为什么要概括数据，以及“中心”的不同定义。 |
| K02：集中趋势的度量 | 9–11 | 定义符号，计算均值、中位数和众数。 |
| K03：中位数与均值 | 12–13 | 将绝对偏差、平方偏差和平衡点与相应度量串联起来。 |

前置知识：数字排序、加法、除法、绝对值和平方。按需补充数据集/分布、PDF 第 4 页的茎叶图以及中位数/百分位的含义。不预设统计学、微积分或 Python 编程基础；代码由 Agent 提供并解释。

建议首次跟练预算 **45–60 分钟**，这是设计估计，不是实测完成时间。时间少时先完成 K01，再续学。不要因为文件包含整章就把剩余内容一起教完。

## 为什么适合

选定范围同时具有文字、公式、表格、插图和小规模数值例题。后续 Notebook 可以沿用原文的五个数字 `2, 3, 4, 9, 16`：先手算，再画数据点和候选中心，比较偏差，最后改变一个极端值。新增计算和图应标为 STS 对来源的讲解，不冒充原书插图或新实验数据。

学习范围足够小，同时能够展示来源核验、直观讲解、代码验证、追问后重组笔记、回忆练习和按需制卡。原始 PDF 为英文；Agent 可用学习者选择的语言讲解和制作笔记。

## 后续教程的准备约束

- 保留这份原 PDF。若制作 12 页节选，必须另存文件，说明原页号到节选页号的映射并保留署名。
- 当前 Notebook 构建器要求输入 PDF 的每页恰好归入一个单元。不得把范围外的页面伪装成 recap，也不得削弱校验。制作限定范围的教程前，应先准备有来源记录的节选，或者明确保留未教学的范围外单元。
- 已用 Poppler 渲染并逐页检查第 2–13 页。公式文本提取不完全可靠；第 9–10 页的均值公式须看页图。
- 讲中位数时说明重复值的排序规则：原文“上下数量相同”不能理解为有重复值时严格大于/小于的数量相同。第 11 页分组数据的众数采用组中点约定，不代表任意连续数据的精确众数。
- 部署或生成示例不代表学习者掌握，不预填学习记录。

如果想先用自己的课程，可按[入门教程](../../guides/getting-started.zh-CN.md)操作。
