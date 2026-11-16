# C5 交付物 · 仓库链接（repo链接）

## 仓库地址

- GitHub 仓库：**https://github.com/9SanQiuXi9/C5-GitHub-Repository**
- 默认分支：`main`（公开仓库，无需登录即可访问）
- 克隆命令：

```bash
git clone https://github.com/9SanQiuXi9/C5-GitHub-Repository.git
cd C5-GitHub-Repository
```

## 3 分钟验证路径（点开即可自查）

| 验证项 | 直达链接 |
|--------|----------|
| 项目主说明 | https://github.com/9SanQiuXi9/C5-GitHub-Repository/blob/main/README.md |
| 复盘报告 AAR | https://github.com/9SanQiuXi9/C5-GitHub-Repository/blob/main/AAR.md |
| AI 使用日志 | https://github.com/9SanQiuXi9/C5-GitHub-Repository/blob/main/AI日志.md |
| 借鉴来源与许可 | https://github.com/9SanQiuXi9/C5-GitHub-Repository/blob/main/ATTRIBUTION.md |
| 技能定义文件 | https://github.com/9SanQiuXi9/C5-GitHub-Repository/blob/main/SKILL.md |
| 源码目录 | https://github.com/9SanQiuXi9/C5-GitHub-Repository/tree/main/scripts |
| 单元测试 | https://github.com/9SanQiuXi9/C5-GitHub-Repository/blob/main/tests/test_evaluator.py |
| 基准样例与标签 | https://github.com/9SanQiuXi9/C5-GitHub-Repository/tree/main/benchmark |
| 示例评审报告 | https://github.com/9SanQiuXi9/C5-GitHub-Repository/blob/main/reports/reports.md |
| 本挑战的展示说明 | https://github.com/9SanQiuXi9/C5-GitHub-Repository/blob/main/拿来说明.md |

## 一句话说明

该仓库包含一个纯 Python 标准库实现的「技能提交自动评审工具」（Skill Evaluator）：
输入一个存放多人技能提交的文件夹，输出 Markdown / Excel / JSON 三种评审报告，
并可对照 rubric 的五个维度打分、识别红线违规。仓库同时满足 C5 要求的工程化配置：
LICENSE、CONTRIBUTING、CHANGELOG、`.github` 模板与工作流、`tests` 单元测试、`benchmark` 基准样例。
