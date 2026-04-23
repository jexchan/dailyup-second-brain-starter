# 贡献指南

> 欢迎为 DailyUp Second Brain Starter 做贡献！本指南帮你快速找到合适的贡献方式。

---

## 贡献方式

### 1. 提 Issue

- **Bug**：结构/模板/Skill 里的问题
- **Feature**：缺少的模板类型、缺少的 Skill、缺少的规则
- **Question**：使用过程中的疑问，反馈能帮我们改进文档

### 2. 提 PR

非常欢迎以下类型的 PR：

#### 新的卡片模板

如果你在使用中发现现有 22 种卡片不够用：

1. 在 `04_Knowledge/00_Cards/.templates/` 新建 `Your_Card.md`
2. 参考现有模板的 frontmatter + 区块结构
3. 同时在 `04_Knowledge/00_Cards/` 根目录加一张 `_EXAMPLE_your_xxx.md`
4. 更新 `04_Knowledge/00_Cards/README.md` 的表格

#### 新的 AI Skill

1. 在 `.claude/skills/<your-skill>/SKILL.md` 写 skill 定义
2. Skill frontmatter 需要：
   ```yaml
   name: <your-skill>
   description: <20–40 字描述，说明什么时候应该触发>
   ```
3. 写清楚 **什么时候用**、**读什么**、**产出什么**、**风格要求**
4. 如果需要，在 `.agents/skills/` 同步一份（或用硬链接）

#### 翻译

目前文档以中文为主。欢迎贡献英文版：
- `README.md` → `README.en.md`
- `QUICK_START.md` → `QUICK_START.en.md`

#### 改进规则文档

`00_System/` 下的规则是活文件，欢迎补充细节、修正不清晰的地方。

---

## 贡献原则

### 保持通用

本模板的目标是"**任何人都能用**"，请避免：

- 引入特定领域（如某个具体行业）的强假设
- 绑定某个闭源工具（除 Obsidian 本身外）
- 加入带个人偏好的内容（特定博客、特定品牌、特定观点）

### 保持轻量

- 不要新增需要编译/构建步骤的东西
- 不要引入 node_modules 级别的依赖
- 保持 Vault 可以"下载 → 打开 → 就能用"

### 保持一致

- 目录命名沿用 `{编号}_{名称}/` 的约定
- 卡片类型命名沿用 `snake_case`
- 示例文件统一带 `_EXAMPLE_` 前缀
- 模板文件统一放在 `.templates/`

### 文件与命名

- 日期文件：`YYYY-MM-DD.md`
- 卡片文件：`{type}_{主题}.md`
- 项目目录：`PascalCase` 或 `snake_case`
- 规则文件：`PascalCase_Name.md`

详见 `00_System/Naming_Conventions.md`。

---

## PR 流程

1. Fork 本仓库
2. 新建 feature 分支：`git checkout -b feat/your-feature`
3. 提交：`git commit -m "feat(cards): add new diagram card type"`
4. 推送：`git push origin feat/your-feature`
5. 在 GitHub 上发起 PR，描述中包括：
   - 做了什么
   - 为什么这么做
   - 用什么场景验证过

---

## Commit Message 规范

使用 Conventional Commits：

- `feat:` 新功能（新模板、新 Skill、新规则）
- `fix:` 修复 Bug
- `docs:` 只改文档
- `refactor:` 结构重构，不改功能
- `chore:` 杂项（gitignore、license 等）

范围（scope）建议：
- `cards` — 卡片模板相关
- `skills` — AI Skills
- `system` — 00_System/ 下的规则
- `obsidian` — .obsidian 配置
- `docs` — README / QUICK_START 等

示例：
```
feat(cards): add `experiment` card type for A/B tests
fix(skills): correct path in card-creator for Windows
docs(quick_start): add instruction for Obsidian Sync
```

---

## 行为准则

参见 [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)。简而言之：互相尊重，就事论事。

---

## 有疑问？

- 提 Issue：你的问题很可能其他人也有
- Star 本仓库让我们知道它有价值

Thanks for contributing ✨
