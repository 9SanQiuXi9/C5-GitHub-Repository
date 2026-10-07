# 使用教程

## 快速上手

### 第一步：确认环境

需要 Python 3.10 或更高版本。打开终端运行：

```bash
python --version
```

如果显示 3.10+ 即可。无需安装任何第三方包。

### 第二步：获取工具

```bash
git clone https://github.com/your-username/skill-evaluator.git
cd skill-evaluator
```

目录结构：

```
skill-evaluator/
├── scripts/          # 核心代码（7 个 Python 文件）
├── references/       # 评审标准配置
│   └── rubric.json
├── benchmark/        # 基准测试（黄金集样本）
│   └── golden_set/
├── docs/             # 文档
├── examples/         # 示例
└── tests/            # 测试
```

### 第三步：准备提交文件夹

将待评审的提交文件放入一个文件夹。文件命名规则：

```
作者名_C4_文件描述.ext
```

示例：

```
张三_C4_skill说明.md
张三_C4_skill.py
张三_C4_demo.mp4
张三_C4_教学说明.md
张三_C4_AI日志.md
```

支持的文件类型：`.md`, `.py`, `.js`, `.skill`, `.txt`, `.json`, `.yaml`, `.sh`, `.mp4`, `.png`, `.jpg` 等。

### 第四步：运行评审

```bash
python scripts/main.py <提交文件夹路径>
```

例如提交文件夹在桌面的 `submissions` 目录：

```bash
python scripts/main.py ~/Desktop/submissions
```

默认输出 Markdown 格式报告到终端。

### 第五步：查看报告

#### Markdown 报告（默认）

直接在终端显示，包含：
- 班级总览（提交人数、完整率、平均质量分）
- 每位作者的完整性检查表和质量评审表
- 排名（按综合分降序）
- 全班改进建议

#### Excel 报告

```bash
python scripts/main.py ./submissions --output excel --report-path ./reports/
```

生成 `C4A_评审报告.xlsx`，包含两个工作表：
- **评审总览**：排名、完整性、质量分、综合分、缺失文件
- **质量详情**：每人四维度的评级和得分

#### JSON 报告

```bash
python scripts/main.py ./submissions --output json --report-path report.json
```

## 进阶用法

### 自定义评审标准

编辑 `references/rubric.json` 可以调整：

- **信号列表**：在对应检查项的 `positive_signals` 或 `negative_signals` 中添加/删除关键词
- **阈值**：`min_hits`（正向信号最少命中数）、`max_hits`（负向信号最多允许命中数）
- **权重**：综合分计算公式（当前默认：完整性 40% + 质量 60%）

### 运行基准测试

```bash
python scripts/benchmark.py --verbose
```

### 评审标准适配不同课程

1. 复制 `references/rubric.json` 为 `my_course_rubric.json`
2. 修改配置
3. 运行时指定：`python scripts/main.py ./submissions --rubric my_course_rubric.json`

## 常见问题

### Q: 文件名不符合命名规则怎么办？

工具会尝试使用父文件夹名作为作者标识。如果文件夹名也无法识别，文件会被归入 "Unknown" 类别。

### Q: Excel 输出报错？

Excel 生成依赖 `openpyxl` 库。安装方式：

```bash
pip install openpyxl
```

其他格式（Markdown、JSON）不依赖任何第三方库。

### Q: 如何判断评审结果是否准确？

运行基准测试：`python scripts/benchmark.py --verbose`。12 组黄金集样本的标注答案已知，基准测试会计算评审结果与标注答案的一致性。

### Q: 二进制文件（图片、视频）怎么处理？

对于完整性检查，二进制文件通过文件名和扩展名匹配。对于质量评审，二进制文件的内容不参与信号匹配，但文件名中的关键词（如 "demo"）会被识别。

### Q: 如何新增一个检查项？

在 `rubric.json` 的对应维度的 `check_items` 数组中添加新项：

```json
{
  "id": "unique_check_id",
  "label": "检查项显示名称",
  "positive_signals": ["关键词1", "关键词2"],
  "min_hits": 1
}
```
