# 贡献指南

感谢你对 Skill Evaluator 的关注！以下是参与贡献的方式和流程。

## 如何贡献

### 报告 Bug

如果你发现了 Bug，请在 [GitHub Issues](https://github.com/9SanQiuXi9/C5-GitHub-Repository/issues) 中提交 Bug Report，并选择 "Bug Report" 模板。

提交前请确认：
- 使用最新的 main 分支版本
- 搜索过已有 Issue，确认没有重复报告
- 包含复现步骤、预期行为、实际行为

### 请求新功能

如果有改进建议或新功能需求，请在 Issues 中选择 "Feature Request" 模板。

请说明：
- 你遇到的问题或使用场景
- 你期望的解决方案
- 你考虑过的替代方案

### 提交代码

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feature/your-feature-name`
3. 编写代码并添加测试
4. 确保基准测试通过：`python scripts/benchmark.py --verbose`
5. 提交：`git commit -m "Add: your feature description"`
6. 推送：`git push origin feature/your-feature-name`
7. 提交 Pull Request

### 改进文档

文档错误、表述不清、缺少示例——这些都可以直接提 PR 修改。

## 开发规范

### 代码风格

- 使用 Python 3.10+ 语法
- 仅使用标准库（不引入新的第三方依赖）
- 函数和类添加类型注解
- 关键逻辑添加注释说明

### 评审标准修改

如果需要调整评审维度或检查项，修改 `references/rubric.json` 即可，无需改动代码。PR 中请说明修改理由。

### 测试

- 新增检查项后，在 `benchmark/golden_set/` 中添加对应的测试样本
- 更新 `benchmark/golden_set/labels.json` 中的标注答案
- 运行 `python scripts/benchmark.py --verbose` 确认 100% 匹配率

## 评审标准适配

本项目的评审标准可以通过 `rubric.json` 适配不同课程和场景。如果你为其他课程做了适配，欢迎分享你的 rubric 配置。

## 行为准则

- 尊重每一位贡献者
- 讨论聚焦技术和项目本身
- 对事不对人
