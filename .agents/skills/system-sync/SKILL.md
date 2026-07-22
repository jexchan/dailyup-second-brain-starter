---
name: system-sync
description: 将当前 Obsidian Vault 中新增、删除、迁移、重命名或结构变化后的信息，同步到系统级导航与说明文件中。适用于更新 `00_System/Vault_Map.md`、`CLAUDE.md`、根目录 `README.md`、目录级 `README.md`、`Skills_Manual.md`、MOC 内容地图，以及卡片数量、卡片类型数量、模板数量、技能数量、README 数量、Base 数量、附件迁移和目录结构变化等统计。Use this skill whenever the user says “同步系统信息”, “更新系统地图”, “同步 README / CLAUDE / Vault Map”, “统计新增卡片和技能”, “更新技能说明手册”, “sync vault metadata”, or asks to make the vault's documentation reflect recent migrations, new skills, new card types, new templates, moved content, or changed counts.
---

# System Sync: 系统信息同步器

本技能用于维护 Vault 的系统地图和说明文件，让它们持续反映当前文件系统的真实状态。

它不是内容创作技能，也不是项目规划技能。它只处理“系统说明是否过期”这件事：当目录、模板、技能、README、Base、MOC、附件、卡片统计或系统规则发生变化时，更新对应的导航文件和说明文件。

---

## 当前 Vault 基线

执行本技能时，应以文件系统实时扫描为准，不要只依赖下面的基线。下面信息反映当前模板库结构，用来帮助判断哪些说明可能过期。

当前核心目录：

- `00_System/` — 系统地图、任务管理、写作规范和命名规范
- `01_Context/` — 稳定全局上下文
- `02_Daily/` — 每日记录和模板
- `03_Projects/` — 项目资料和项目模板
- `04_Knowledge/` — 原子知识卡片和长期主题地图
- `05_References/` — 外部剪藏与参考资料
- `06_Tasks/` — Inbox 和任务管理
- `07_Bases/` — Obsidian Base 数据库视图
- `.agents/skills/` — 本地技能

当前系统文件重点：

- `AGENTS.md` — 指向 `CLAUDE.md` 的符号链接，是 AI 入口说明
- `CLAUDE.md` — 总导航和 AI 协作规则
- `00_System/Vault_Map.md` — Vault 结构地图
- `00_System/Writing_Rules.md` — 写作与附件规则
- `00_System/Naming_Conventions.md` — 命名规则
- `00_System/Task_Management_Rules.md` — 任务管理规则
- `README.md` — 面向使用者的项目说明
- `Skills_Manual.md` — 本地技能说明手册

当前目录级 README 通常包括：

- `03_Projects/README.md`
- `04_Knowledge/README.md`
- `04_Knowledge/00_Cards/README.md`
- `04_Knowledge/01_Topics/README.md`
- `05_References/README.md`

注意：不要假设存在 `20_Archive/`。只有实际扫描到该目录或用户明确新增时，才把它写入系统说明。

---

## 核心原则

### 1. 真实状态优先

涉及数量、清单、目录结构和文件存在性时，必须从文件系统计算，不要凭记忆或旧说明猜测。

必须动态计算的内容包括：

- 卡片数量
- 卡片类型分布
- 卡片模板数量
- 本地技能数量和技能清单
- README 清单
- Base 文件数量和清单
- MOC 文件数量和清单
- 附件数量或新增附件清单
- 关键目录和系统文件是否存在

写入统计时必须说明统计口径，例如：

- “按 `type: card` 统计”
- “按 `04_Knowledge/00_Cards/*.md` 中的示例卡片也纳入统计”
- “按 `.agents/skills/*/SKILL.md` 统计”
- “不含 `.git/` 和 `.obsidian/`”

### 2. 只同步系统信息

本技能只维护系统级说明、导航、统计和索引，不负责：

- 写文章
- 设计课程
- 创建具体知识卡片
- 制定项目计划
- 复盘每日进展
- 深度研究主题内容

如果发现内容本身需要沉淀，应建议使用当前 Vault 已有技能：

- `card-creator` — 创建知识卡片
- `brain-storming` — 发散主题想法并沉淀
- `connect` — 分析两个主题之间的连接
- `trace` — 追踪主题演变
- `closeday` — 每日复盘
- `weekly-review` — 周回顾

### 3. 避免重复记录

同一条系统信息应写到最合适的位置，不要整段复制到多个文件。

推荐落点：

- 全局结构、目录职责、系统文件清单 → `00_System/Vault_Map.md`
- AI 读写与协作原则 → `CLAUDE.md`
- 写作、附件、frontmatter 规则 → `00_System/Writing_Rules.md`
- 命名规则 → `00_System/Naming_Conventions.md`
- 总入口和协作规则 → `CLAUDE.md`
- 面向使用者的项目介绍 → `README.md`
- 目录内部说明 → 对应目录下的 `README.md`
- 本地技能总览 → `Skills_Manual.md`
- MOC 内容地图 → `04_Knowledge/00_Cards/moc_*.md`

其他文件中可以放短摘要和指向链接，但不要重复维护同一份长说明。

### 4. 先检查，再写入

更新前必须先读取目标文件，理解现有结构。

优先更新已有章节；只有没有合适章节时才新增小节。不要直接把同步结果追加到文件底部。

### 5. 尊重工作区状态

更新前查看 `git status --short`。

如果存在用户未提交改动：

- 不要回滚。
- 不要覆盖无关文件。
- 如果统计包含未提交文件，在报告中说明。
- 如果目标文件已有未提交改动，先读取并基于现状编辑。

---

## 触发场景

用户说以下内容时，使用本技能：

- “同步系统信息”
- “更新系统地图”
- “同步 README 和 CLAUDE”
- “更新 Vault_Map”
- “更新技能说明手册”
- “统计新增卡片和技能”
- “新增技能后同步说明”
- “新增卡片类型后同步系统”
- “迁移一批内容后更新目录说明”
- “把当前知识库结构同步到系统文件”

以下操作完成后，也适合主动建议使用本技能：

- 批量迁移旧 Vault 内容
- 新增或删除本地技能
- 新增卡片类型或模板
- 新建目录级 README
- 重命名关键目录
- 大量移动附件
- 修复大量 wikilink
- 新增 Base 文件
- 创建或更新 MOC 内容地图

---

## 工作流程

### Step 1: 读取系统导航和当前状态

先读取：

- `AGENTS.md`
- `CLAUDE.md`
- `00_System/Vault_Map.md`
- `00_System/Writing_Rules.md`
- `00_System/Naming_Conventions.md`
- `00_System/Task_Management_Rules.md`
- `README.md`
- `Skills_Manual.md`（如果存在，或任务涉及技能）

如果任务涉及某个目录，还要读取该目录下的 `README.md`。

同时运行：

```bash
git status --short
find . -maxdepth 3 -name README.md -not -path './.git/*' -print | sort
find .agents/skills -maxdepth 2 -name SKILL.md -print | sort
```

### Step 2: 判断同步范围

根据用户请求、git 状态和文件扫描结果，判断需要同步哪些方面：

- **目录结构**：新增、删除、重命名目录，或目录职责变化
- **系统文件**：新增或更新规则文件、导航文件、手册文件
- **README**：根目录 README 或目录级 README 是否过期
- **技能统计**：新增、删除或修改技能后，是否需要更新 `Skills_Manual.md`
- **卡片统计**：卡片总数、类型分布、模板数量是否变化
- **卡片类型**：模板清单、命名规则、卡片类型说明是否变化
- **Base 统计**：`07_Bases/` 下的 Base 文件是否变化
- **MOC 同步**：新增卡片是否需要加入相关 MOC
- **附件迁移**：附件目录规则或附件数量是否变化
- **总入口**：`CLAUDE.md` 是否需要新增重要入口或规则

不要因为某个文件存在就一定更新。只有信息缺失、过期、冲突或用户明确要求时才改。

### Step 3: 计算真实统计

优先使用以下命令。根据任务范围选择需要的统计，不必每次全部运行。

```bash
# 卡片总数：按 type: card 统计
rg -l '^type: card$' 04_Knowledge/00_Cards/*.md 2>/dev/null | wc -l

# 卡片类型分布
rg -n '^card_type: ' 04_Knowledge/00_Cards/*.md 2>/dev/null | sed 's/.*card_type: //' | sort | uniq -c

# 卡片模板数量
find 04_Knowledge/00_Cards/.templates -maxdepth 1 -type f -name '*_Card.md' | wc -l

# 卡片模板清单
find 04_Knowledge/00_Cards/.templates -maxdepth 1 -type f -name '*_Card.md' -print | sort

# 本地技能数量
find .agents/skills -maxdepth 2 -name SKILL.md | wc -l

# 本地技能清单
find .agents/skills -maxdepth 2 -name SKILL.md -print | sort

# README 清单
find . -maxdepth 3 -name README.md -not -path './.git/*' -print | sort

# Base 文件清单
find 07_Bases -maxdepth 1 -type f -name '*.base' -print | sort

# MOC 文件清单
find 04_Knowledge/00_Cards -maxdepth 1 -type f -name 'moc_*.md' -print | sort

# 附件清单
find . -path './.git' -prune -o -path './.obsidian' -prune -o -type f \( -path '*/Attachments/*' -o -path './Attachments/*' \) -print | sort
```

如果 glob 没有匹配文件，命令可能输出错误或空结果；报告中要说明“当前未发现对应文件”，不要编造数量。

### Step 4: 更新目标文件

#### `00_System/Vault_Map.md`

适合更新：

- 目录结构变化
- 系统文件清单变化
- 卡片类型和模板概览
- `07_Bases/` 文件变化
- `Skills_Manual.md` 作为系统入口的说明
- 新增目录级 README

不要把频繁波动的详细统计塞进 `Vault_Map.md`，除非用户明确要求或该统计是说明当前结构所必需。

#### `CLAUDE.md`

适合更新：

- 目录导航规则发生变化
- 新增必须优先读取的系统文件
- 默认工作流程或写回规则变化
- 新增重要系统入口，如 `Skills_Manual.md`

不适合写入：

- 频繁变化的数量统计
- 大段技能说明
- 某次迁移的临时报告

#### 根目录 `README.md`

适合更新：

- 项目定位
- 新用户入口
- 主要目录说明
- 技能说明手册入口
- 当前系统能力概览
- 快速开始流程

#### 目录级 `README.md`

适合更新：

- 目录新增子结构
- 新增重要文件或模板
- 使用流程变化
- 当前目录的入口说明

当前模板库中常见目录级 README：

- `03_Projects/README.md`
- `04_Knowledge/README.md`
- `04_Knowledge/00_Cards/README.md`
- `04_Knowledge/01_Topics/README.md`
- `05_References/README.md`

#### `Skills_Manual.md`

适合更新：

- 新增技能
- 删除技能
- 技能用途变化
- 技能触发词变化
- 技能读写边界变化
- 技能组合工作流变化

更新 `Skills_Manual.md` 时，应从 `.agents/skills/*/SKILL.md` 重新读取技能名称、描述和关键流程，不要只根据旧手册改。

### Step 5: 同步 MOC 内容地图

只有在新增或变更知识卡片，并且能确定合适 MOC 时，才更新 MOC。

MOC 文件通常位于：

```bash
04_Knowledge/00_Cards/moc_*.md
```

匹配建议：

| 新卡片类型 | 优先检查的 MOC |
|---|---|
| `mentalmodel_*` | 心智模型相关 MOC |
| `person_*` | 人物或主题相关 MOC |
| `book_*`, `book-note_*` | 书籍、主题或方法论相关 MOC |
| `tool_*`, `opensource_*`, `techstack_*` | 工具、技术或资源相关 MOC |
| `term_*` | 概念或主题相关 MOC |
| `insight_*`, `counterintuitive_*`, `paradox_*`, `question_*` | 主题相关 MOC |

MOC 更新流程：

1. 从 git diff 或文件列表中识别新增或变更的卡片。
2. 读取卡片 frontmatter，提取 `card_type`、`tags`、`related`、`source`。
3. 查找现有 MOC：
   ```bash
   find 04_Knowledge/00_Cards -maxdepth 1 -type f -name 'moc_*.md' -print | sort
   ```
4. 判断是否有明确匹配的 MOC。
5. 如果有，读取目标 MOC，找到合适章节，加入 `[[卡片名]] — 简短说明`。
6. 如果没有明确匹配，报告“未更新 MOC，原因是缺少合适目标”，不要硬塞。

MOC 不更新条件：

- 卡片是示例、草稿或临时状态。
- MOC 中已有该卡片链接。
- 无法确定合适 MOC。
- 用户明确表示不需要添加到 MOC。
- 新增内容还没有整理成稳定卡片。

### Step 6: 输出同步报告

同步完成后输出：

```markdown
# 系统同步完成

## 已更新文件
- `{{path}}` — {{更新内容}}

## 统计口径
- {{统计项}}：{{口径说明}}

## 统计结果
- 卡片数量：{{count}}
- 卡片类型：{{count}} 种
- 卡片模板：{{count}} 个
- 本地技能：{{count}} 个
- README：{{count}} 个
- Base：{{count}} 个
- MOC：{{count}} 个

## 未更新但建议关注
- `{{path}}` — {{为什么暂不更新}}

## 校验
- {{运行了哪些检查}}
```

如果没有修改文件，也要明确说“未写入文件”，并说明原因。

---

## 写入规则

允许写入：

- `00_System/Vault_Map.md`
- `00_System/Writing_Rules.md`
- `00_System/Naming_Conventions.md`
- `00_System/Task_Management_Rules.md`
- `CLAUDE.md`
- `README.md`
- 各目录 `README.md`
- `Skills_Manual.md`
- `04_Knowledge/00_Cards/moc_*.md`
- 与同步任务直接相关的系统规则文件

不要写入：

- Daily Note，除非用户明确要求把同步过程记录到当日记录
- 项目计划，除非用户明确要求同步项目结构规则
- 具体知识卡片正文，除非同步目标就是修正链接、类型或 MOC 关系
- 归档资料，除非用户明确要求整理归档目录说明

如果同步过程中发现内容需要知识化，应提出建议，不直接创建卡片。

---

## 与其他本地技能的边界

- `system-sync`：同步系统级导航、README、统计、技能手册和 MOC 内容地图。
- `card-creator`：创建具体知识卡片，不负责维护全局系统说明。
- `check-health`：检查失效链接、孤立卡片、观点矛盾；发现问题后，可再用 `system-sync` 更新系统说明。
- `closeday`：每日复盘，整理今日完成、洞察和明日延续。
- `weekly-review`：周回顾，整理一周项目和任务进展。
- `today`：生成今日计划，不写系统文件。
- `session-brief`：恢复当前工作上下文，不写系统文件。
- `brain-storming`：发散主题想法，确认后可沉淀到知识库。
- `connect`：分析两个主题之间的连接，不写系统文件。
- `trace`：追踪主题演变，不写系统文件。
- `random-thinking`：随机抽取知识内容获得灵感，不写系统文件。
- `spaced-review`：维护卡片复习字段，不写系统说明。

如果用户说“哪些内容值得写回系统”，先判断是否属于系统信息：

- 属于目录、规则、统计、技能、README、MOC 入口 → 使用 `system-sync`。
- 属于知识观点、概念、资源、案例 → 建议 `card-creator`。
- 属于日复盘或周复盘 → 使用 `closeday` 或 `weekly-review`。
- 属于主题演变或概念关系 → 使用 `trace` 或 `connect`。

---

## 校验要求

修改后至少运行：

```bash
git diff --check
git diff -- .agents/skills/system-sync/SKILL.md
```

如果目标文件尚未被 Git 跟踪，普通 `git diff -- path` 不会显示内容差异；此时应改用：

```bash
git diff --no-index /dev/null .agents/skills/system-sync/SKILL.md
```

如果更新了统计或系统说明，尽量同时运行对应统计命令，确认写入数字和真实结果一致。

最终回复应说明：

- 修改了哪些文件。
- 修正了哪些过期信息。
- 是否运行了校验。
- 是否存在未处理的工作区改动。
