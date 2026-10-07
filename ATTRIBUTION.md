# 借鉴来源说明

本项目的开发过程中参考了以下来源的设计思路、代码模式和最佳实践。

---

## 架构设计

### 配置驱动的评审标准

评审标准完全由 `references/rubric.json` 驱动，不硬编码任何判断逻辑。这一设计模式参考了：

- **ESLint 的规则配置系统**：通过 JSON/YAML 配置文件定义检查规则，而非在代码中硬编码
- **pytest 的 conftest.py 机制**：通过配置文件控制测试行为

### 四级置信度匹配策略

完整性检测采用的四级匹配策略（文件名+扩展名 → 文件名 → 内容信号 → 未找到），参考了：

- **MIME 类型检测**：先按扩展名判断，再按文件内容魔数判断的分层策略
- **Python pathlib 文档**：文件名模式匹配的方法论

## 代码实现

### 信号匹配机制

正向信号计数、负向信号 veto 的设计，参考了：

- **垃圾邮件过滤中的贝叶斯分类**：正向特征和负向特征分别计分
- **Claude 内置的 file-reading skill**：文件类型分发逻辑

### 报告生成

多格式报告输出（Markdown / Excel / JSON）的设计，参考了：

- **Python 标准库的 argparse 文档**：CLI 参数解析的最佳实践
- **openpyxl 官方文档**：Excel 格式化和样式设置

## 文档与社区要素

### README 结构

README 的结构参考了以下开源项目的最佳实践：

- [Make a README](https://www.makeareadme.com/) 的模板指南
- GitHub 官方文档中关于创建 README 的建议

### CONTRIBUTING.md

贡献指南的结构参考了：

- [Atom 项目的 CONTRIBUTING.md](https://github.com/atom/atom/blob/master/CONTRIBUTING.md)
- GitHub 的 [Setting guidelines for repository contributors](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions)

### CHANGELOG.md

变更日志格式遵循 [Keep a Changelog v1.1.0](https://keepachangelog.com/zh-CN/1.1.0/) 规范。

### Issue 模板

Issue 模板的设计参考了 GitHub 官方文档中关于 [Issue 模板](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests) 的最佳实践。

## 评审维度

四维度评审体系（可复用、可执行、可验证、IO 明确）的设计，参考了：

- **软件工程质量模型**：可维护性、可移植性、可测试性等 ISO 25010 质量特性
- **代码审查的标准实践**：review 时关注的代码质量维度
- **Claude skill-creator 的质量标准**：Skill 评审的维度设计

## AI 辅助说明

本项目使用 AI 辅助开发（详见 [AI_LOG.md](./AI_LOG.md)）。C4 阶段的原始开发使用了 Claude (Anthropic) 和 ChatGPT (OpenAI)；C5 阶段的仓库包装使用了 Qoder。所有 AI 生成的内容均经过人工审核和修改。
