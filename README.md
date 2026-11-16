# Skill Evaluator — C4 技能提交自动评审工具

一句话描述：输入一个包含多人技能提交的文件夹，输出完整的评审报告（Markdown / Excel / JSON）。

---

## 解决什么问题

当老师或助教面对几十份甚至上百份学生技能提交时，逐份人工检查完整性、逐项打分、汇总排名——这个过程极其耗时且容易出错。没有这个工具之前，评审靠人工逐项对照清单，一份提交可能需要 5-10 分钟，全班 40 人就是 3-6 小时的重复劳动。

有了 Skill Evaluator，整个评审流程从文件扫描到报告生成全自动完成，**5 分钟内出结果**。

## 快速开始

### 安装

```bash
git clone https://github.com/9SanQiuXi9/C5-GitHub-Repository.git
cd C5-GitHub-Repository
```

无需安装任何第三方依赖。本工具纯 Python 标准库实现，支持 Python 3.10+。

如果需要 Excel 报告输出（可选）：

```bash
pip install openpyxl
```

### 使用

```bash
# 基本用法 — 输出 Markdown 报告到终端
python scripts/main.py <提交文件夹路径>

# 输出 Excel 报告
python scripts/main.py ./submissions --output excel --report-path ./reports/

# 输出全部格式（Markdown + Excel + JSON）
python scripts/main.py ./submissions --output all --report-path ./reports/

# 使用自定义评审标准
python scripts/main.py ./submissions --rubric my_rubric.json

# 运行基准测试（验证评审准确性）
python scripts/benchmark.py --verbose
```

## 示例

### 输入

准备一个包含多位同学提交的文件夹：

```
submissions/
├── 张三_C4_skill说明.md
├── 张三_C4_skill.py
├── 张三_C4_demo.md
├── 张三_C4_教学说明.md
├── 张三_C4_AI日志.md
├── 李四_C4_skill说明.md
├── 李四_C4_skill.skill
├── 李四_C4_demo.png
├── 李四_C4_教学说明.md
├── 王五_C4_skill说明.md
└── 王五_C4_skill.py
```

### 运行

```bash
python scripts/main.py ./submissions
```

### 输出

```
# C4 提交自动评审报告

生成时间：2026-10-07 14:30:00
扫描路径：./submissions
识别提交：3 位作者，11 个文件

## 一、班级总览

| 指标 | 数值 |
|------|------|
| 总提交人数 | 3 |
| 完整提交（5/5） | 2 |
| 部分提交 | 1 |
| 平均质量分 | 72.2% |

## 二、排名

| 排名 | 作者 | 完整性 | 质量分 | 综合分 |
|------|------|--------|--------|--------|
| 1 | 张三 | 5/5 | 100% | 100.0% |
| 2 | 李四 | 5/5 | 75% | 82.0% |
| 3 | 王五 | 3/5 | 75% | 53.3% |
```

完整的示例输出见 [reports/reports.md](./reports/reports.md)。

## 项目结构

```
skill-evaluator/
├── README.md
├── LICENSE
├── SKILL.md                    # 技能定义文件
├── CONTRIBUTING.md             # 贡献指南
├── CHANGELOG.md                # 版本更新记录
├── AI日志.md                   # AI 辅助开发日志
├── AAR.md                      # 项目复盘（After Action Review）
├── ATTRIBUTION.md              # 借鉴来源说明
├── .gitignore
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md       # Bug 报告模板
│       └── feature_request.md  # 功能请求模板
├── scripts/
│   ├── main.py                 # CLI 入口，串联完整评审流程
│   ├── scanner.py              # 文件扫描、作者识别、文件分组
│   ├── completeness.py         # 完整性检查（5 项交付物匹配）
│   ├── evaluator.py            # 质量评审（四维度信号匹配 + 评分）
│   ├── reporter.py             # 报告生成（Markdown / Excel / JSON）
│   ├── benchmark.py            # 黄金集基准测试
│   └── self_test.py            # 自测脚本
├── references/
│   ├── rubric.json             # 评审标准配置（信号列表、阈值、权重）
│   └── rubric.yaml             # 评审标准（YAML 格式参考）
├── benchmark/
│   ├── generate_golden_set.py  # 黄金集样本生成器
│   ├── results.json            # 基准测试结果
│   └── golden_set/             # 12 组标注样本
│       ├── labels.json         # 标注答案
│       ├── sample_01_perfect/  # 完美提交
│       ├── sample_02_missing_teaching/
│       ├── sample_03_hardcoded_paths/
│       ├── ...
│       └── sample_12_no_skill_doc/
├── docs/
│   ├── skill-doc.md            # 技能详细说明
│   ├── tutorial.md             # 使用教程
│   └── demo.md                 # 演示说明
├── examples/
│   └── sample_submissions/     # 示例提交文件夹
├── reports/
│   ├── reports.md              # 示例评审报告（Markdown）
│   └── reports.json            # 示例评审报告（JSON）
└── tests/
    └── test_evaluator.py       # 单元测试
```

## 核心架构

```
输入文件夹
    │
    ▼
scanner.py ── 递归扫描 → 文件名正则匹配 → 按作者分组
    │
    ▼
completeness.py ── 四级置信度匹配（文件名+扩展名 → 文件名 → 内容信号 → 未找到）
    │                对 5 项交付物逐一检测
    ▼
evaluator.py ── 正向信号计数 / 负向信号 veto / 条件检查 / 必填检查
    │             四维度评审：可复用 / 可执行 / 可验证 / IO明确
    ▼
reporter.py ── 汇总排名 → 生成 Markdown / Excel / JSON 报告
```

### 评审维度

| 维度 | 检查内容 | 示例信号 |
|------|----------|----------|
| **可复用** | 安装说明、无硬编码路径、环境要求、泛化说明 | 正向：`pip install`、`环境要求`；负向：`C:\Users`、`/home/xxx` |
| **可执行** | 可运行代码、.skill 包结构、YAML frontmatter | 正向：`def `、`import `、`name:`；负向：`TODO`、`待实现` |
| **可验证** | 测试用例、预期输出、Demo 证据、成功标准 | 正向：`单元测试`、`预期输出`、`测试结果` |
| **IO 明确** | 输入输出描述、类型格式、一句话功能说明 | 正向：`输入`、`输出`、`格式` |

### 配置驱动

所有评审标准由 `references/rubric.json` 驱动，不硬编码任何判断逻辑。修改信号列表、阈值、权重即可适配不同课程的评审标准，无需改动代码。

## 基准测试

内置 12 组黄金集标注样本，覆盖：完美提交、缺失各类文件、硬编码路径、弱 IO 描述、无代码、无 AI 日志、不可验证、对抗样本等场景。

```bash
python scripts/benchmark.py --verbose
```

当前版本基准指标：
- 12 样本 **100% 匹配率**
- 四维度精确率/召回率均 **1.000**
- 保守率 **0%**

## 技术栈

- 语言：Python 3.10+
- 依赖：零第三方依赖（纯标准库：pathlib, re, json, argparse, collections, datetime）
- 可选依赖：openpyxl（Excel 输出）
- AI 集成：Claude (Anthropic) + ChatGPT (OpenAI) 辅助开发

## AI 生成说明

本项目使用 AI 辅助开发，经历了 5 轮主要迭代（架构设计 → 核心实现 → 基准测试调优 → 报告生成 → 文档完善），详见 [AI日志.md](./AI日志.md)。项目复盘见 [AAR.md](./AAR.md)。

## 借鉴来源

本项目参考了多个来源的设计思路和最佳实践，详见 [ATTRIBUTION.md](./ATTRIBUTION.md)。

## License

[MIT](./LICENSE)
