---
description: Content style and formatting guidelines
tags: [system, writing, style]
---
# Writing Rules

## 总原则
- 可理解性优先于完整性
- 清晰优先于华丽
- 结构优先于堆砌
- 实用优先于空泛表达

## 表达风格
- 尽量使用中文
- 多用短段落
- 标题清楚
- 先给整体图景，再进入细节
- 避免故作高深
- 适合知识型、方法论型、教学型内容

## 面向初学者时
- 先解释“这是什么”
- 再解释“为什么重要”
- 再解释“怎么做”
- 适当给例子
- 语速感偏慢，循序渐进

## 方法论类内容
- 先提出核心问题
- 再给框架
- 再分步骤展开
- 最后给落地建议

## 课程类内容
- 目标明确
- 结构递进
- 每节课有输入、练习、输出
- 尽量让内容可执行

## 避免
- 空话套话
- 过度营销腔
- 没有信息密度的排比
- 只讲概念，不讲怎么用

---

## 附件管理规则

### 存放位置
> 所有 Markdown 文件的附件都存放到当前目录下的 `Attachments/` 文件夹

**附件类型**：
- 图片（PNG, JPG, GIF, SVG 等）
- PDF 文档
- 音频文件（MP3, WAV 等）
- 视频文件（MP4, MOV 等）
- 其他二进制文件

### 路径格式
```markdown
![[文件名.扩展名]]
```

**注意**：使用 Obsidian wikilink 格式，不需要 `Attachments/` 前缀

### 示例
```markdown
![[Skills 实战课01.pdf]]
![[diagram.png]]
![[intro.mp3]]
![[everything-claude-code.png]]
```

### 注意事项
- 每个目录的附件存放在该目录下的 `Attachments/` 文件夹
- 保持附件文件名清晰有意义
- 避免在文件名中使用特殊字符

---

## Obsidian Base 规则

### 存放位置
> 所有 Obsidian Base 文件统一存放到 `07_Bases/` 目录

**Base 类型**：
- 卡片合集（Persons, Books, Subscriptions 等）
- 任务管理
- 项目追踪
- 数据库视图

### 文件命名
```bash
07_Bases/Books.base
07_Bases/Persons.base
07_Bases/Subscriptions.base
```

### 使用方式
```markdown
![[07_Bases/Books.base]]
![[07_Bases/Books.base#封面墙]]
```

### 注意事项
- 创建新 Base 时自动放到 `07_Bases/` 目录
- Base 文件使用 `.base` 扩展名
- 命名使用 PascalCase（大驼峰）

---

## Git 提交规范

### 提交信息格式

> 使用 HEREDOC 格式，但**不包含** Claude 的 Co-Authored-By 声明

```bash
git commit -m "$(cat <<'EOF'
提交标题

详细说明（可选）

EOF
)"
```

### 错误示例
```bash
# ❌ 不要包含
git commit -m "feat: add new feature

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

### 正确示例
```bash
# ✅ 正确格式
git commit -m "feat: add new feature

详细说明（可选）"
```

### 注意事项
- 提交信息本身可以由 Claude 辅助生成
- 但最终提交时**去掉** `Co-Authored-By` 部分
- 保持提交信息简洁清晰

---

## YAML Frontmatter 规则

### 列表项禁止行内注释
> 在 frontmatter 的列表项（如 `related`）中，不能添加行内注释文字

### 错误示例
```yaml
# ❌ 会导致解析错误
related:
  - "[[book_卡片笔记写作法]]" — 关于 Zettelkasten 的书
  - "[[person_NiklasLuhmann]]" — 卡片盒笔记法创始人
```

### 正确示例
```yaml
# ✅ 正确格式
related:
  - "[[book_卡片笔记写作法]]"
  - "[[person_NiklasLuhmann]]"
```

### 注释的位置
> 关联说明应放在正文的"关联卡片"章节中

```markdown
## 关联卡片
- [[book_卡片笔记写作法]] — 关于 Zettelkasten 的书
- [[person_NiklasLuhmann]] — 卡片盒笔记法创始人
```

### 适用字段
此规则适用于所有 frontmatter 列表字段：
- `related`
- `tags`
- 自定义列表字段

### 原因
YAML 规范中，列表项内的 `—` 等字符会被当作值的一部分，导致 Obsidian 解析失败或产生意外结果。

### source 属性规则
> 当来源既有文字描述又有链接时，source 属性只保留可点击链接，文字部分移到正文"来源"章节

#### 错误示例
```yaml
# ❌ 不要把文字和 URL 混在一起
source: "杨振宁讲座《我的学习与研究经历》：http://example.com/article.htm"
```

#### 正确示例
```yaml
# ✅ source 只保留简洁名称或可点击链接
source: "杨振宁讲座《我的学习与研究经历》"
```

#### 正文处理
```markdown
## 来源
[杨振宁讲座《我的学习与研究经历》](http://example.com/article.htm)

杨振宁在回顾宇称不守恒实验时引用吴健雄的话...
```

#### 原因
- YAML 不支持 Markdown 链接语法，source 中的 URL 无法点击
- 正文中使用 `[文字](URL)` 格式可点击跳转
- 保持 frontmatter 简洁，链接放在正文更符合使用习惯