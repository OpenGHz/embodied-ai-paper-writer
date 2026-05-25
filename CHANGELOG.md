# Changelog

All notable changes to this skill are documented here. Format inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project adheres to [Semantic Versioning](https://semver.org/) at the playbook-rule level: MAJOR for breaking rule changes, MINOR for added rules/playbooks, PATCH for clarifications and typo fixes.

## [Unreleased]

## [0.1.0] — 2026-05-25

Initial public release.

### Added

- `SKILL.md` operating manual with:
  - Problem-routing table mapping user requests → reference files
  - 5 execution scenarios (write / fix / question / caption / arc-review)
  - 13 universal rules (venue conventions, noun-phrase locking, tense, delta-form, pivot count, statistical disclosure, forward references, limitation-pairing, hedging, pushback, roadmap-gating, precedence, escalation)
  - When-to-ask-vs-default table
  - Failure-modes refusal/redirect table
  - Reference index + honest boundaries
- 8 operational reference playbooks:
  - `titles.md` — title patterns, 5 architectures, system-name conventions
  - `abstract-intro-playbook.md` — 5-move abstract, 4-paragraph intro arc, hook taxonomy
  - `method-relatedwork-playbook.md` — RW 3-act narrative, Method commitment, equation sandwich
  - `experiments-results-playbook.md` — question-list opener, baseline framing, ablation narration
  - `figures-tables-playbook.md` — 8 figure roles (F1–F8), caption templates, panel notation, statistical disclosure
  - `language-phrasebank.md` — rhetorical phrasebook (sections A–K)
  - `flow-transitions.md` — 6-move paper arc, pivot family, contribution-restatement spiral
  - `closing-appendix-playbook.md` — Conclusion 3-move recap, Limitations admit-and-propose, Appendix conventions
- 9 raw research files in `references/research/` (corpus traceability, ~870 KB)
- Open-source scaffolding: README, LICENSE (MIT), CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, CITATION, issue/PR templates, `.editorconfig`, `.gitignore`

### Corpus

- 63 papers, 2022–2026, across CoRL / RSS / ICRA / IROS / Science Robotics
- Majority are best-paper-award winners or finalists
- Index in `references/research/_paper_roster.md`
