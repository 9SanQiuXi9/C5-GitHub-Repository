# 教学说明

## 快速上手

### 第一步：确认环境

需要 Python 3.10+。运行 `python --version` 确认。

### 第二步：运行评审

```bash
python scripts/main.py <提交文件夹路径>
```

### 第三步：查看报告

默认在终端显示 Markdown 格式报告。

## 进阶用法

### 输出 Excel 报告

```bash
python scripts/main.py ./submissions --output excel --report-path ./reports/
```

### 自定义评审标准

编辑 `references/rubric.json`，修改信号列表和阈值。

### 运行基准测试

```bash
python scripts/benchmark.py --verbose
```
