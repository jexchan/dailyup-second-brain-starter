---
description: Writing and Markdown conventions for vault content
tags: [system, writing, markdown]
---
# Writing Rules

## 表达原则

- 可理解性优先于完整性
- 清晰优先于华丽
- 结构优先于堆砌
- 实用优先于空泛表达
- 默认使用中文，必要时保留准确的英文术语
- 先给整体图景，再展开细节
- 多用短段落和明确标题，避免故作高深与过度营销

## 常用内容结构

### 面向初学者

1. 这是什么
2. 为什么重要
3. 怎么做
4. 给出一个具体例子

### 方法论内容

1. 核心问题
2. 方法框架
3. 执行步骤
4. 落地建议

### 课程内容

- 明确学习目标
- 按理解难度递进
- 每节包含输入、练习和输出
- 让学习结果可以验证

## Markdown 与 Frontmatter

- 内部笔记使用 `[[wikilink]]`，外部网页使用 `[文字](URL)`
- Frontmatter 保持简洁，只保存适合检索、筛选或自动处理的字段
- Frontmatter 列表项只填写值，不追加说明文字
- 关联说明放在正文的“关联卡片”章节

错误示例：

```yaml
related:
  - "[[book_卡片笔记写作法]]" — 关于 Zettelkasten 的书
```

正确示例：

```yaml
related:
  - "[[book_卡片笔记写作法]]"
```

正文中补充说明：

```markdown
## 关联卡片

- [[book_卡片笔记写作法]] — 关于 Zettelkasten 的书
```

## 来源字段

- 有原始 URL 时，`source` 只保存 URL
- 没有 URL 时，`source` 可以保存简洁的来源名称
- 标题、作者、背景和引用说明放在正文“来源”章节
- 不要把说明文字和 URL 混在同一个属性值中

```yaml
source: "https://example.com/article"
```

```markdown
## 来源

[杨振宁讲座《我的学习与研究经历》](https://example.com/article)
```

## 附件

- 附件放在所属内容目录下的 `Attachments/` 文件夹
- 文件名应清晰、稳定，避免无意义名称和特殊字符
- 在笔记中使用 Obsidian 嵌入语法，不写 `Attachments/` 前缀

```markdown
![[diagram.png]]
![[课程讲义.pdf]]
```

附件包括图片、PDF、音频、视频及其他二进制文件。若同名附件可能产生歧义，先重命名为可唯一识别的名称。

## 避免

- 空话、套话和低信息密度排比
- 只讲概念，不说明如何使用
- 为追求完整而制造不必要的层级
- 把未经整理的聊天原文直接写入正式知识库
