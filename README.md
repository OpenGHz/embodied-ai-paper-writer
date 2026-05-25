# Embodied AI Paper Writer

English | [简体中文](README.zh-CN.md)

> A portable agent skill (SKILL.md + reference playbooks) that coaches the **writing craft** of embodied-AI papers — distilled from 63 top-conference papers across CoRL, RSS, ICRA, IROS, and Science Robotics (2022–2026). Works with any LLM agent that can load markdown context.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Format: SKILL.md](https://img.shields.io/badge/format-SKILL.md-blue.svg)](SKILL.md)
[![Corpus: 63 papers](https://img.shields.io/badge/corpus-63%20papers-green.svg)](references/research/_paper_roster.md)
[![Venues: CoRL · RSS · ICRA · IROS · Sci. Robotics](https://img.shields.io/badge/venues-CoRL%20%C2%B7%20RSS%20%C2%B7%20ICRA%20%C2%B7%20IROS%20%C2%B7%20Sci.%20Robotics-purple.svg)](references/research/_paper_roster.md)

---

## What this is

A drop-in **agent skill** that turns any modern LLM agent — Claude Code, Cursor, Continue, Cline, Aider, the Anthropic / OpenAI SDKs, or anything else that can load a system prompt — into a corpus-tuned coach for writing robotics / embodied-AI papers. It teaches:

- Title patterns, abstract moves, intro arcs.
- Method / Related Work organization.
- Experiments setup framing, results paragraph rhythm, ablation narration.
- Figure roles, caption templates, table conventions.
- Conclusion / Limitations / Future Work / Appendix.
- Section openers, pivots, connectors, the contribution-restatement spiral.
- A phrasebook of openers, hedges, and anti-patterns.

It does **not** decide which experiments to run, validate technical claims, suggest research directions, translate, or run your LaTeX build. See [`SKILL.md`](SKILL.md) for the full boundary list.

## Why a skill, not a textbook

Most writing advice is generic ("be clear, cite related work"). This skill is **quantified** and **corpus-tuned**:

- "Abstract = 120–250 words, 5 moves (Frame → Gap → Contribution → Method → Results)."
- "Method tense = present, system-as-subject."
- "Plot caption = mean ± StdErr + sample size, always."
- "Contribution noun phrase repeats 5–7× verbatim across the paper."
- "F1 teaser caption = 3–6 sentences; F3 hardware caption = 1 sentence."

Each rule traces back to observed patterns in the 63-paper corpus.

## Quick start

### 1. Install

Copy [`SKILL.md`](SKILL.md) and [`references/`](references/) into wherever your agent loads system prompts or skill files. Examples:

- **Claude Code** — user-level: `~/.claude/skills/embodied-ai-paper-writer/`
- **Claude Code** — project-level: `<your-project>/.claude/skills/embodied-ai-paper-writer/`
- **Cursor / Continue / Cline / Aider** — paste `SKILL.md` into the custom-rules / system-prompt panel; keep `references/` next to it and attach files on demand per the routing table.
- **Custom agent (Anthropic / OpenAI / local model SDKs)** — load `SKILL.md` as the system message; lazily read `references/*.md` based on the routing table.
- **Plain chat** — paste `SKILL.md` into the conversation; follow up with the relevant playbook when the routing table calls for it.

```bash
# Example: install as a user-level skill for Claude Code
SKILL_DIR="$HOME/.claude/skills/embodied-ai-paper-writer"
mkdir -p "$SKILL_DIR"
cp -r SKILL.md references "$SKILL_DIR/"
```

The skill is just markdown + frontmatter — nothing in the runtime behavior is locked to one vendor.

### 2. Invoke it

Once loaded, the agent will engage on phrases like:

- "Help me write the abstract for my CoRL submission."
- "Caption this figure — it's a 3-panel success-rate plot."
- "My Limitations section sounds defensive — fix it."
- "Review my paper's arc."
- 「帮我润色一下这段 Intro」
- 「rebuttal 怎么写」

See the full trigger list in [`SKILL.md`](SKILL.md) (frontmatter `description`).

## Project layout

```
embodied-ai-paper-writer/
├── SKILL.md                              # Operating manual (entry point)
├── references/
│   ├── titles.md                         # Title patterns and architectures
│   ├── abstract-intro-playbook.md        # Abstract + Intro construction
│   ├── method-relatedwork-playbook.md    # Method + Related Work
│   ├── experiments-results-playbook.md   # Experiments, Results, Ablations
│   ├── figures-tables-playbook.md        # F1–F8 figure roles, caption templates
│   ├── language-phrasebank.md            # Rhetorical phrasebook (A–K)
│   ├── flow-transitions.md               # 6-move paper arc, pivots, connectors
│   ├── closing-appendix-playbook.md      # Conclusion / Limitations / Appendix
│   └── research/                         # Raw extraction (read for traceability)
│       ├── _paper_roster.md              # 63-paper corpus index
│       └── 00–08 + topical extracts
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── SUPPORT.md
├── CHANGELOG.md
└── CITATION.cff
```

The skill has two layers:

| Layer | Files | Purpose |
|---|---|---|
| **Operational** | `SKILL.md` + 8 playbooks in `references/*.md` | Loaded by the agent on demand via the routing table in SKILL.md |
| **Research** | 9 files in `references/research/` | Raw evidence — read only when traceability is needed |

The operational playbooks are 8–25 KB each. The research files (50–200 KB) exist so any rule can be traced back to source patterns; they are **not** loaded during normal use.

## How the skill thinks

The agent follows five execution scenarios (defined in [`SKILL.md`](SKILL.md)):

| Scenario | Trigger | Behavior |
|---|---|---|
| **A** — Write new section | "draft my intro" | Confirm scope → gather briefing → load reference → **pre-draft checkpoint** → draft → self-review → deliver with 3-line summary |
| **B** — Fix/review existing | "fix my method" | 4-layer diagnostic scan → numbered findings → checkpoint before rewrite |
| **C** — Question only | "how long should X be?" | Answer concisely with the number + the rule; don't volunteer to rewrite |
| **D** — Caption a figure | "caption this plot" | Identify F1–F8 type → confirm role → template → verify panel notation + task-name consistency + length budget |
| **E** — Whole-paper arc | "review my paper" | 4-lens check (arc / spiral / tense / figure coupling) → prioritized fix list |

Plus 13 universal rules including: lock the contribution noun phrase, disclose deltas not absolutes, one pivot per gap, every limitation pairs with future-work mitigation, and pushback escalation policy.

## Honest boundaries

- **Sample**: 63 papers, 2022–2026, CoRL / RSS / ICRA / IROS / Science Robotics. NeurIPS / ICML robotics tracks are under-represented. CVPR-adjacent robotics is under-represented.
- **Anglophone bias**: corpus is English-language.
- **Conventions evolve**: re-extract after mid-2027.
- **Writing-craft only**: this skill cannot judge whether a paper is publishable, whether the contribution is strong, or whether the experimental design is sound. It can only judge whether the writing follows the conventions of papers that **did** get published.
- **Defaults calibrated to CoRL**: when writing for ICRA / IROS / Science Robotics, the skill asks once to recalibrate venue-specific conventions.

## Contributing

Pattern corrections, new corpus additions, and anti-pattern submissions are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

Common contributions:

- **Add a paper** to the corpus → see the [Paper Addition](.github/ISSUE_TEMPLATE/paper-addition.yml) template.
- **Report a wrong rule** → see the [Bug Report](.github/ISSUE_TEMPLATE/bug.yml) template.
- **Suggest a missing pattern** → see the [Pattern Suggestion](.github/ISSUE_TEMPLATE/pattern-suggestion.yml) template.

## Citation

If this skill helped your writing, please cite the repository. See [`CITATION.cff`](CITATION.cff).

## License

[MIT](LICENSE) — use, fork, adapt, redistribute. Attribution appreciated, not required.

## Acknowledgments

This skill was distilled using the [Nuwa · Skill造人术](https://github.com/alchaincyf/nuwa-skill) methodology — a structured pipeline for turning expert corpora into operational skills (SKILL.md + reference layer). The methodology made the difference between "generic writing advice" and "corpus-tuned quantified rules."

Original corpus papers and authors retain all rights to their work; only writing patterns and conventions are abstracted here.
