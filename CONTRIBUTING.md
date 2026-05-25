# Contributing to Embodied AI Paper Writer

Thanks for your interest in improving this skill. This project lives or dies by the accuracy of its corpus-derived rules, so contributions that **ground rules in observed paper patterns** are especially welcome.

## Ways to contribute

### 1. Report a wrong rule

If a rule in `SKILL.md` or `references/*.md` contradicts what you see in published papers — open a [Bug Report](.github/ISSUE_TEMPLATE/bug.yml).

**Good bug reports cite at least 2 counter-examples from the corpus** (or from comparable venues). "I disagree" is not a bug; "Paper X and Paper Y both violate this rule and were accepted at CoRL 2024" is.

### 2. Add a paper to the corpus

The corpus is 63 papers (see `references/research/_paper_roster.md`). Adding more papers strengthens every rule. Open a [Paper Addition](.github/ISSUE_TEMPLATE/paper-addition.yml) request with:

- Venue + year + arXiv ID
- Award or best-paper finalist status (if applicable)
- A 1-line note on what writing convention the paper exemplifies or breaks

### 3. Suggest a missing pattern

Found a recurring move, opener, transition, or anti-pattern not yet catalogued? Open a [Pattern Suggestion](.github/ISSUE_TEMPLATE/pattern-suggestion.yml) with:

- The pattern (verbatim or paraphrased)
- 3+ papers that use it
- Which playbook file it belongs in
- Whether it's a positive pattern or anti-pattern

### 4. Improve playbook prose

Typos, awkward phrasing, broken links, or unclear instructions in any reference file — PRs welcome. Keep edits surgical; don't restructure a playbook in a single PR.

## Editing workflow

1. Fork the repo and create a feature branch: `git checkout -b improve-figures-playbook`.
2. Make your changes. Keep each PR focused on one playbook or one rule.
3. **Run a sanity check**: open `SKILL.md` and any modified `references/*.md` side-by-side and verify they don't contradict each other (the routing table in SKILL.md is the source of truth).
4. Commit with a descriptive message: `figures-playbook: clarify F6 plot statistical disclosure`.
5. Open a PR using the PR template.

## What we won't merge

- Rules added without corpus evidence ("I think papers should…").
- Stylistic rewrites that don't change the rule (churn without value).
- New playbook files unless there's a clear gap not covered by the existing 8.
- Anything that adds technical-content judgement (this skill is writing-craft only — see the boundaries in `SKILL.md`).

## Voice and style of the playbooks

The playbooks read as **operational** rather than **discursive**:

- Numbered Steps, not prose paragraphs.
- Quantified rules (`120–250 words`, `5–7×`, `mean ± StdErr`).
- Anti-pattern tables with rewrites.
- Construction workflows with verbatim-copyable templates.

When in doubt, mimic the existing playbook style.

## Code of Conduct

Be kind. See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Questions

Open a [Discussion](https://github.com/OpenGHz/embodied-ai-paper-writer/discussions) (preferred for design questions) or an issue (preferred for bugs and concrete proposals). See [`SUPPORT.md`](SUPPORT.md).
