---
name: critical-check
description: 对观点、论证与证据进行建设性审查。Use when the user asks to critique, validate, red-team, or stress-test a claim, card, draft, course, or project judgment for assumptions, evidence gaps, reasoning errors, counterexamples, boundaries, and next validation steps.
---

# Critical Check

进行**建设性怀疑**：准确复述，再挑战高影响主张，并把每项挑战转化为可验证的下一步。

默认只读。用户明确要求记录、更新、写回或保存时，才依照 Vault 的既有写回规则修改文件。

## Select the Review Mode

- **Quick check**: 用于短观点、单个问题或用户要求快速反馈；覆盖最强部分、最大风险、待补证据和更稳妥的改写。
- **Full check**: 用于多主张内容、将发布的文稿、课程或项目判断，或用户要求深入审查；覆盖主张地图、证据、推理、反例、边界与迭代动作。

选择与材料范围和用户目标相称的模式；用户未指定时，短内容使用 Quick check，其他内容使用 Full check。

**Mode completion:** The review mode and material scope are explicit.

## Workflow

### 1. Locate the material and context

- 直接分析用户贴出的内容；读取用户提供的文件路径。
- 对 wikilink 或卡片名，先在 `04_Knowledge/00_Cards/` 搜索。
- 对仅有主题的请求，用 `rg` 搜索相关内容，并说明本次采用的材料范围。
- 仅当审查依赖用户方向、受众或写作标准时，读取对应的 Context 或 Writing Rules 文件。

把一次检索描述为“当前检索未发现”，不要外推为全库不存在。

**Completion:** The material source, review scope, and any missing context are explicit.

### 2. Build a claim map

识别 3–7 个最影响结论的主张，并为每项记录：

- 主张类型：事实、因果、价值、方法论、产品/课程判断或个人经验；
- 现有支撑：事实、案例、经验、引用、研究、数据或直觉；
- 隐含假设与目标对象：适用于谁、什么场景和阶段。

先复述中心主张，再开始质疑，避免把误读当作漏洞。

**Completion:** Every load-bearing claim has a type, available support, hidden assumption, and target object.

### 3. Verify evidence when needed

对时间敏感、可外部验证，或用户明确要求事实核查的决定性事实主张，检索一手或权威来源。为每条已验证的外部事实附上来源。

其余情况优先依据用户提供材料和 Vault 内容。把结论明确标记为：`材料证据`、`外部证据` 或 `推断`；未核查的信息标记为未核查。

**Completion:** Every decisive factual claim is either verified with an appropriate source or explicitly labeled as unverified.

### 4. Apply constructive skepticism

优先处理高影响主张，而不是机械覆盖全部检查项。按需检查：

- **证据强度**：支撑是否匹配结论强度，相关是否被说成因果；
- **推理链条**：概念层级、必要/充分条件、外推与归因是否成立；
- **替代解释**：是否遗漏变量、激励、环境或选择偏差；
- **反例与边界**：在哪些人、任务、阶段或条件下会失效；
- **表达清晰度**：概念、对象和语气是否可检验且有边界。

每个重要质疑都对应至少一项行动：补证据、找反例、限定边界、改写主张或设计验证。

**Completion:** Every high-impact challenge has an evidence target, boundary, rewrite, or validation action.

### 5. Report and route next actions

清楚区分原内容中的证据、基于材料的推断和你的建议。使用直接、建设性的语气，并将有价值但证据不足的观点处理为“保留但降级表达”。

读取 `references/output-formats.md`，选择 Quick 或 Full 格式。读取 `references/examples.md`，仅当用户的请求与示例场景相近且需要澄清执行方式。

用户明确要求沉淀稳定反思时，交给 `card-creator`；需要追踪观点演变时，使用 `trace`；需要连接两个主题时，使用 `connect`。

**Completion:** The report states the strongest support, highest-risk issue, evidence status, and the next validation action at the detail level required by the chosen mode.

## Writing Back

写回前，先展示拟写入内容和精确目标位置并取得确认。将项目判断写入对应 `Project.md`；将稳定知识交由 `card-creator`；其余情况遵循 Vault 的任务、命名和写作规则。

## Output Style

- 默认使用中文；除非用户要求，否则不为反对而反对。
- 让改写更准确、可检验且有适用边界。
- 说明具体需要补充的证据，而不是泛称“需要更多证据”。
