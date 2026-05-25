# Embodied AI Paper Writer

[English](README.md) | 简体中文

> 一个可移植的 agent 技能（SKILL.md + 参考手册），专门指导具身智能（Embodied AI）论文的**写作技艺**——从 2022–2026 年 CoRL、RSS、ICRA、IROS、Science Robotics 五大顶会的 63 篇论文中提炼而来。可被任何能加载 markdown 上下文的 LLM agent 使用。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Format: SKILL.md](https://img.shields.io/badge/format-SKILL.md-blue.svg)](SKILL.md)
[![Corpus: 63 papers](https://img.shields.io/badge/corpus-63%20papers-green.svg)](references/research/_paper_roster.md)
[![Venues: CoRL · RSS · ICRA · IROS · Sci. Robotics](https://img.shields.io/badge/venues-CoRL%20%C2%B7%20RSS%20%C2%B7%20ICRA%20%C2%B7%20IROS%20%C2%B7%20Sci.%20Robotics-purple.svg)](references/research/_paper_roster.md)

---

## 这是什么

一个开箱即用的 **agent 技能**，把任何现代 LLM agent —— Claude Code、Cursor、Continue、Cline、Aider、Anthropic / OpenAI SDK，或任何能加载 system prompt 的工具 —— 变成一位针对机器人 / 具身智能论文写作、基于语料调优的写作教练。它教你：

- 标题范式、摘要章法、引言脉络。
- 方法 / 相关工作的组织方式。
- 实验设置框架、结果段落节奏、消融实验叙述。
- 配图角色、图注模板、表格惯例。
- 结论 / 局限 / 未来工作 / 附录。
- 章节开头、转折、衔接、贡献的螺旋式重申（contribution-restatement spiral）。
- 包含开场句、学术缓和措辞与反模式的短语库。

它**不会**替你决定该做哪些实验、不会验证技术主张、不会建议研究方向、不会翻译、也不会跑你的 LaTeX 编译。完整的边界清单见 [`SKILL.md`](SKILL.md)。

## 为什么做成 skill，而不是教科书

大多数写作建议都很泛（"要清晰、要引用相关工作"）。这个 skill 的特点是**量化**和**基于语料调优**：

- "摘要 = 120–250 词，分 5 步推进（铺垫 → 缺口 → 贡献 → 方法 → 结果）。"
- "方法部分时态 = 一般现在时，以系统为主语。"
- "图表图注 = 始终包含 mean ± 标准误（StdErr）+ 样本量。"
- "贡献名词短语在全文中原样重复 5–7 次。"
- "F1 teaser 图的图注 = 3–6 句；F3 硬件图的图注 = 1 句。"

每条规则都能追溯回 63 篇论文语料库中观察到的规律。

## 快速上手

### 1. 安装

把 [`SKILL.md`](SKILL.md) 和 [`references/`](references/) 复制到你的 agent 加载 system prompt 或 skill 文件的位置。常见目标：

- **Claude Code** —— 用户级：`~/.claude/skills/embodied-ai-paper-writer/`
- **Claude Code** —— 项目级：`<your-project>/.claude/skills/embodied-ai-paper-writer/`
- **Cursor / Continue / Cline / Aider** —— 把 `SKILL.md` 贴进 custom rules / system prompt 面板，`references/` 放在旁边，按 routing 表按需附加。
- **自定义 agent（Anthropic / OpenAI / 本地模型 SDK）** —— 把 `SKILL.md` 作为 system message 加载，按 routing 表懒加载 `references/*.md`。
- **纯聊天** —— 把 `SKILL.md` 贴进对话，按 routing 表的提示再补充对应 playbook。

```bash
# 示例：作为用户级 skill 装到 Claude Code
SKILL_DIR="$HOME/.claude/skills/embodied-ai-paper-writer"
mkdir -p "$SKILL_DIR"
cp -r SKILL.md references "$SKILL_DIR/"
```

这个 skill 就是 markdown + frontmatter，运行时行为没有任何东西绑死在某一家厂商上。

### 2. 唤起它

加载好之后，agent 会在以下这类提问中开始工作：

- "Help me write the abstract for my CoRL submission."
- "Caption this figure — it's a 3-panel success-rate plot."
- "My Limitations section sounds defensive — fix it."
- "Review my paper's arc."
- 「帮我润色一下这段 Intro」
- 「rebuttal 怎么写」

完整的触发词列表见 [`SKILL.md`](SKILL.md) 的 frontmatter `description` 字段。

## 项目结构

```
embodied-ai-paper-writer/
├── SKILL.md                              # 操作手册（入口）
├── references/
│   ├── titles.md                         # 标题范式与结构
│   ├── abstract-intro-playbook.md        # 摘要 + 引言写法
│   ├── method-relatedwork-playbook.md    # 方法 + 相关工作
│   ├── experiments-results-playbook.md   # 实验、结果、消融
│   ├── figures-tables-playbook.md        # F1–F8 配图角色、图注模板
│   ├── language-phrasebank.md            # 修辞短语库（A–K）
│   ├── flow-transitions.md               # 论文 6 步行文脉络、转折、衔接
│   ├── closing-appendix-playbook.md      # 结论 / 局限 / 附录
│   └── research/                         # 原始抽取（需追溯时查阅）
│       ├── _paper_roster.md              # 63 篇语料索引
│       └── 00–08 + 专题抽取
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── SUPPORT.md
├── CHANGELOG.md
└── CITATION.cff
```

这个 skill 有两层：

| 层级 | 文件 | 用途 |
|---|---|---|
| **操作层** | `SKILL.md` + `references/*.md` 里的 8 个 playbook | 由 agent 通过 SKILL.md 中的路由表按需加载 |
| **研究层** | `references/research/` 下的 9 个文件 | 原始证据——仅在需要追溯时阅读 |

操作层的 playbook 每个 8–25 KB。研究层文件（50–200 KB）的作用是让任意一条规则都能追溯回源头规律，**正常使用时不会被加载**。

## 这个 skill 是怎么思考的

agent 遵循五种执行场景（在 [`SKILL.md`](SKILL.md) 中定义）：

| 场景 | 触发 | 行为 |
|---|---|---|
| **A** — 写新章节 | "draft my intro" | 确认范围 → 收集背景 → 加载参考 → **起草前对齐确认** → 起草 → 自检 → 交付时附 3 行总结 |
| **B** — 修改/审阅已有内容 | "fix my method" | 4 层诊断扫描 → 编号列出问题 → 改写前先做对齐确认 |
| **C** — 只回答问题 | "how long should X be?" | 简洁给出数值 + 规则；不主动揽下重写 |
| **D** — 配图图注 | "caption this plot" | 识别 F1–F8 类型 → 确认角色 → 套模板 → 核对分图标号、任务名一致性和字数预算 |
| **E** — 整篇论文行文脉络 | "review my paper" | 四视角检查（行文脉络 / 贡献螺旋 / 时态 / 图文配合）→ 按优先级列出修改项 |

外加 13 条通用规则，包括：锁定贡献名词短语、披露增量而非绝对值、每个缺口配一个转折、每条局限都搭配一条对应的未来工作改进方向、应对异议的升级策略等。

## 诚实的边界

- **样本**：63 篇论文，2022–2026 年，来自 CoRL / RSS / ICRA / IROS / Science Robotics。NeurIPS / ICML 的机器人方向覆盖不足，CVPR 周边的机器人方向也覆盖不足。
- **英语世界偏差**：语料全部为英文。
- **学术惯例会变**：建议 2027 年中以后重新提取语料。
- **只管写作技艺**：这个 skill 无法判断论文是否可发表、贡献是否够强、实验设计是否合理。它只能判断写作是否符合已发表论文的惯例。
- **默认参数按 CoRL 标定**：当目标投稿到 ICRA / IROS / Science Robotics 时，skill 会主动询问一次以重新标定该会场的特定惯例。

## 贡献

欢迎提交规则修正、新增语料、以及反例案例。详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

常见贡献方式：

- **添加论文** 到语料库 → 见 [Paper Addition](.github/ISSUE_TEMPLATE/paper-addition.yml) 模板。
- **报告错误规则** → 见 [Bug Report](.github/ISSUE_TEMPLATE/bug.yml) 模板。
- **建议缺失的范式** → 见 [Pattern Suggestion](.github/ISSUE_TEMPLATE/pattern-suggestion.yml) 模板。

## 引用

如果这个 skill 对你的写作有帮助，欢迎引用本仓库。见 [`CITATION.cff`](CITATION.cff)。

## 许可证

[MIT](LICENSE)——可自由使用、fork、改编、再分发。署名值得感激，但不强制。

## 致谢

本 skill 使用 [Nuwa · Skill造人术](https://github.com/alchaincyf/nuwa-skill) 方法论提炼而成——这是一套把专家语料转化为可操作 skill（SKILL.md + 参考层）的结构化流水线。这套方法论是"泛泛的写作建议"和"基于语料调优的量化规则"之间的分水岭。

语料库中的原始论文及作者保留其全部权益；本仓库仅抽取写作范式与惯例。
