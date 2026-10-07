# 演示说明

## 演示一：基本评审流程

### 输入

准备一个包含 3 位同学提交的文件夹 `examples/sample_submissions/`：

```
sample_submissions/
├── Alice_C4_skill说明.md
├── Alice_C4_skill.py
├── Alice_C4_demo.md
├── Alice_C4_教学说明.md
├── Alice_C4_AI日志.md
├── Bob_C4_skill说明.md
├── Bob_C4_skill.skill
├── Bob_C4_demo.png
├── Bob_C4_教学说明.md
├── Carol_C4_skill说明.md
└── Carol_C4_skill.py
```

- Alice：5 项齐全，质量良好
- Bob：5 项齐全，有硬编码路径
- Carol：缺少 Demo 和 AI 日志

### 运行命令

```bash
python scripts/main.py ./examples/sample_submissions
```

### 预期输出

报告将显示：
- 班级总览：3 位作者，11 个文件
- Alice：完整性 5/5，质量优秀，综合分 100%
- Bob：完整性 5/5，可复用维度因硬编码路径被扣分，综合分约 82%
- Carol：完整性 3/5，缺失 Demo 和 AI 日志，综合分约 53%

---

## 演示二：Excel 报告输出

### 运行命令

```bash
python scripts/main.py ./examples/sample_submissions --output excel --report-path ./reports/
```

### 预期结果

生成 `./reports/C4A_评审报告.xlsx`，包含：
- **评审总览**工作表：排名、完整性、质量分、综合分、缺失文件、质量评级
- **质量详情**工作表：每人四维度的评级和得分

---

## 演示三：基准测试

### 运行命令

```bash
python scripts/benchmark.py --verbose
```

### 预期输出

```
============================================================
BENCHMARK RESULTS
============================================================
样本数: 12
完全匹配率: 100.0%
完整性匹配率: 100.0%
平均精确率: 1.000
平均召回率: 1.000
平均保守率: 0.000

各维度指标:
  reusable: P=1.000 R=1.000 F1=1.000 保守率=0.000
  executable: P=1.000 R=1.000 F1=1.000 保守率=0.000
  verifiable: P=1.000 R=1.000 F1=1.000 保守率=0.000
  clear_io: P=1.000 R=1.000 F1=1.000 保守率=0.000
```

---

## 演示四：对抗样本检测

### 输入

一个包含"看起来完整但实际质量差"的提交：

```
adversarial/
├── User_C4_skill说明.md    # 内容充实
├── User_C4_skill.py        # 包含 TODO: implement later
├── User_C4_demo.md         # 写着"待补充截图"
├── User_C4_教学说明.md      # 内容充实
├── User_C4_AI日志.md        # 内容充实
```

### 运行结果

- 完整性：5/5（5 项文件都存在）
- 可执行：失败（负向信号检测：代码中包含 "TODO"、"待实现"）
- 可验证：失败（零正向证据：无测试、无预期输出、无成功标准）
- 可复用：通过（安装说明和环境要求都存在）
- IO 明确：通过（输入输出描述清晰）

这展示了负向信号检测和零正向证据检测的作用——文件"存在"不等于内容"合格"。
