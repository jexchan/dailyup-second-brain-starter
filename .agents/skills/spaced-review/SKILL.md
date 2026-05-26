---
name: spaced-review
description: Manage spaced repetition review for Obsidian knowledge cards. Use this skill when the user asks what to review today, wants to add cards to the review queue, or gives review feedback such as again/hard/good/easy for a card.
---

# Spaced Review

为 `04_Knowledge/00_Cards/` 中的知识卡片提供间隔重复复习机制。

这个技能的核心原则是：复习卡片不是重新阅读，而是先主动提取，再打开卡片校验，然后根据掌握情况更新下一次复习时间。

---

## Trigger

使用本技能处理以下请求：

- 今天该复习什么
- 今日复习 / 知识卡片复习
- 把这张卡片加入复习
- 我对这张卡片掌握得很好 / 一般 / 忘了
- 更新这张卡片的复习反馈
- 查看到期复习卡片

---

## Review Fields

复习状态写在卡片 frontmatter 中：

```yaml
srs_enabled: true
srs_status: learning
srs_due: 2026-05-26
srs_last_reviewed:
srs_interval: 1
srs_ease: 2.5
srs_reps: 0
srs_lapses: 0
srs_priority: core
```

字段含义：

- `srs_enabled`：是否进入复习系统。
- `srs_status`：`learning` / `review` / `suspended`。
- `srs_due`：下一次复习日期。
- `srs_last_reviewed`：上次复习日期。
- `srs_interval`：当前间隔天数。
- `srs_ease`：熟悉度系数，默认 `2.5`。
- `srs_reps`：成功复习次数。
- `srs_lapses`：遗忘/失败次数。
- `srs_priority`：`core` / `normal` / `low`。

---

## Workflow

### 1. 今日复习

运行：

```bash
python .agents/skills/spaced-review/scripts/spaced_review.py due --limit 20
```

输出按 `srs_due`、`srs_priority`、间隔长度排序。

### 2. 加入复习

运行：

```bash
python .agents/skills/spaced-review/scripts/spaced_review.py enroll "04_Knowledge/00_Cards/term_间隔重复SRS.md" --priority core
```

默认明天到期，初始间隔为 1 天。

### 3. 记录反馈

用户看完卡片后，先让用户给出掌握反馈：

- `again`：基本忘了，需要很快再看。
- `hard`：想起来一部分，但不稳。
- `good`：基本掌握。
- `easy`：很熟，可以拉长间隔。

运行：

```bash
python .agents/skills/spaced-review/scripts/spaced_review.py review "04_Knowledge/00_Cards/term_间隔重复SRS.md" --rating good
```

如果用户给了文字反馈，用 `--note` 记录：

```bash
python .agents/skills/spaced-review/scripts/spaced_review.py review "04_Knowledge/00_Cards/term_间隔重复SRS.md" --rating hard --note "能说出定义，但忘了主动提取这一层"
```

---

## Output Style

当用户问“今天该复习什么”时，按这个结构输出：

```markdown
# 今日复习

今天到期：N 张

1. [[card_name]] — 类型 / 优先级 / 上次复习 / 间隔
   - 提取提示：先不打开卡片，用 1-2 句话说出它的核心意思。
   - 反馈选项：again / hard / good / easy
```

如果没有到期卡片，说明当前没有需要复习的卡片，并建议加入 3-5 张核心卡片开始。

---

## Algorithm

使用轻量 SM-2 变体：

- `again`：间隔重置为 1 天，`ease - 0.2`，`lapses + 1`。
- `hard`：间隔约为原来的 `1.2` 倍，至少 1 天，`ease - 0.15`。
- `good`：间隔乘以 `ease`。
- `easy`：间隔乘以 `ease * 1.35`，`ease + 0.15`。

`ease` 下限为 `1.3`。所有下一次复习日期按天计算。

---

## Notes

- 默认只处理 `srs_enabled: true` 的卡片。
- 不要批量把所有卡片加入复习。优先加入真正需要长期掌握的核心概念、方法论、课程知识、重要洞察。
- 如果卡片本身太长，应在复习时要求用户先提取“一句话/核心结构/应用场景”，而不是逐字背诵。
