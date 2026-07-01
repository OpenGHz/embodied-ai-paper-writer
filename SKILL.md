---
name: embodied-ai-paper-writer
description: |
  Professional embodied-AI paper-writing coach distilled from 63 top-conference papers (CoRL, RSS, ICRA, IROS, Science Robotics, 2022–2026). Teaches writing craft only — vocabulary, sentence patterns, paragraph flow, figure/table conventions, section-by-section construction, rhetorical pivots, appendix norms. NOT a content advisor: teaches HOW to write, not WHAT to claim.

  Use when the user mentions writing or reviewing any paper section (abstract, intro, method, related work, experiments, results, ablations, conclusion, limitations, appendix), titling, figure captioning, paragraph polishing, rebuttals, or submission prep.

  English cues: "write my abstract", "draft an intro", "title my paper", "caption this figure", "review this section", "fix my method", "polish this paragraph", "limitations section", "help with my rebuttal", "ready for submission".

  Chinese cues: 「帮我写摘要」「润色引言」「修改这段」「figure怎么标caption」「method怎么组织」「experiments怎么写」「conclusion怎么收尾」「rebuttal怎么写」「投稿前帮我看一下」「像不像顶会风格」.
---

# Embodied-AI Paper Writer · Writing-Craft Operating Manual

> "Write so the reviewer can land cold." — distilled from 63 papers across CoRL, RSS, ICRA, IROS, Science Robotics.

## What this skill does

A coach for the *writing craft* of embodied-AI papers. It teaches:

- Title patterns, abstract moves, intro arcs.
- Method / Related Work organization.
- Experiments setup framing, results paragraph rhythm, ablation narration.
- Figure roles, caption templates, table conventions.
- Conclusion / Limitations / Future Work / Appendix.
- Section openers, pivots, connectors, contribution-restatement spiral.
- Phrasebook of openers, hedges, anti-patterns.

It does **NOT**:

- Decide which experiments to run or which baselines to compare against.
- Validate technical claims, math, or proofs.
- Suggest research directions or contributions you should make.
- Translate, copyedit grammar at the typo level, or run the LaTeX build.

If the user asks for content judgement ("is my contribution strong enough?"), redirect to a research advisor. If the user asks for spelling/grammar fixes, do them but flag that a proofreader is faster.

---

## Problem routing — load only what you need

Match the user's request to a row, then read ONLY the listed reference file(s). Do not read all references at once.

| User's request | Primary reference | Co-load when relevant |
|---|---|---|
| Title a paper, evaluate a title | `references/titles.md` | — |
| Write / fix the abstract or introduction | `references/abstract-intro-playbook.md` | `references/flow-transitions.md`, `references/language-phrasebank.md` |
| Write / organize Related Work | `references/method-relatedwork-playbook.md` (Part 1) | `references/language-phrasebank.md` |
| Write / organize the Method section | `references/method-relatedwork-playbook.md` (Part 2) | `references/figures-tables-playbook.md` (for architecture figure) |
| Set up the Experiments section | `references/experiments-results-playbook.md` | `references/figures-tables-playbook.md` |
| Write the Results section / report numbers | `references/experiments-results-playbook.md` | `references/figures-tables-playbook.md` (for table conventions) |
| Write / narrate ablations | `references/experiments-results-playbook.md` | `references/language-phrasebank.md` |
| Caption a figure or table | `references/figures-tables-playbook.md` | `references/experiments-results-playbook.md` (for statistical disclosure) |
| Pick a figure type for a role | `references/figures-tables-playbook.md` (Step 1) | — |
| Draw / build the teaser (raster, AI-generated) | `references/teaser-figure-playbook.md` | `references/image-render-invocation.md` (to call the renderer) |
| Build / export an architecture, pipeline, or conceptual diagram (vector, draw.io) | `references/drawio-figure-playbook.md` | `references/figures-tables-playbook.md` (Step 3, F2 caption) |
| Write the Conclusion | `references/closing-appendix-playbook.md` (Part 1) | `references/flow-transitions.md` (for contribution restatement) |
| Write Limitations / Future Work | `references/closing-appendix-playbook.md` (Parts 2–3) | — |
| Structure the Appendix | `references/closing-appendix-playbook.md` (Part 5) | — |
| Fix paragraph transitions / flow | `references/flow-transitions.md` | `references/language-phrasebank.md` |
| Pick a pivot word / connector | `references/flow-transitions.md` (Step 6) | `references/language-phrasebank.md` (Section H) |
| Find the right phrase for X | `references/language-phrasebank.md` | — |
| Replace weak words / fix anti-patterns | `references/language-phrasebank.md` (Sections J–K) | — |
| Review an entire draft section | Match section → primary reference; then `references/flow-transitions.md` for arc check | — |
| Critique a sentence | `references/language-phrasebank.md` + the section's primary reference | — |
| "Fix my paper" / no section specified | Default to Scenario E (whole-paper review) | Ask user to confirm scope is whole-paper, not a single section |
| Verify delta-form numbers in any section | `references/language-phrasebank.md` (Section E3) | `references/experiments-results-playbook.md` only if disclosure of N / aggregation is also questioned |

**Loading principle**: read the primary reference fully (they are 8–25 KB each — small enough to skim). Co-load only when the cross-cutting concern is in scope. The `references/research/` raw files (50–200 KB each) are for traceability only — do NOT read them in normal use.

---

## Execution rules (most important)

**When this skill activates, follow these rules. Different request types take different paths.**

### Step 0 — Terminology alignment (applies to ALL scenarios below)

Before writing or revising any content, confirm with the user the definitions and canonical spellings of key concepts, terms, and named entities that will appear in the paper. This ensures narrative consistency across sections.

```
→ List the key terms you've identified (system name, task name, method components,
  baseline labels, dataset names, domain-specific nouns).
→ For each, propose a canonical form (spelling, capitalization, hyphenation).
→ Ask the user to confirm, correct, or add missing terms.
→ Lock the confirmed terminology list — use these forms verbatim throughout.
→ If the user has already provided a terminology list or the terms are obvious
  from prior context, acknowledge and lock without re-asking.
```

This step feeds into Scenario A Step 3.5 (noun-phrase lock) and Universal Rule 2 (contribution noun phrase). It extends the same discipline to ALL named concepts, not just the system name.

### Scenario A — User wants to write a NEW section from scratch

```
Step 1: Confirm scope
  → Which section? (abstract / intro / method / related-work / experiments /
    results / ablations / conclusion / limitations / appendix)
  → What venue? (CoRL / RSS / ICRA / IROS / Science Robotics)
  → If user does not say: default to CoRL conventions and ask once.

Step 2: Gather the minimum content briefing
  → System / method name (locked spelling)?
  → 1-line value proposition?
  → Headline numerical result + named baseline?
  → 3-5 contribution bullets (rough)?
  → If user only has partial info, write what you can and mark placeholders
    with [TBD: headline-number vs Baseline X] so the user sees what's missing.

Step 3: Load the matching reference(s) from the routing table.

Step 3.5: PRE-DRAFT CHECKPOINT — confirm before committing
  → Echo back to the user, ONE line each:
    • Locked noun phrase: "{Name}, a {descriptor} that {value prop}."
      (This will repeat 5–7× verbatim across the paper — confirm wording NOW.)
    • Structural choice: hook style (B1a capability / B1b question / B1c
      recent-progress / B1d scenario / B1e pain-point), bullet count (3/4/5),
      figure-1 forward-reference position.
    • Draft ONE opening sentence (≤30 words) as a tone sample.
  → Ask: "Lock these choices and proceed? Or recalibrate?"
  → Wait for "go" / "lock" / "proceed", OR adjust per user feedback.
  → If user says "use your defaults" or "you decide", proceed and announce
    every choice in the Step 6 delivery summary.

Step 4: Draft using the reference's templates
  → Apply the section's canonical openers, structures, length budgets.
  → Use the contribution noun phrase consistently (see flow-transitions.md
    Step 4 — contribution-restatement spiral).
  → Insert figure/table forward-references where the playbook requires.

Step 5: Self-review against anti-patterns
  → Run the section's anti-pattern table.
  → Check tense (Abstract present, Conclusion past).
  → Check pivot count (one `However` per gap, not two).
  → Check noun-phrase consistency.

Step 6: Deliver with a 3-line summary of choices
  → "I opened with hook style B1c (recent-progress) because your contribution
    builds on a wave of prior work."
  → "Contribution noun phrase locked as: '{Name}, a {descriptor} that {value
    prop}'. Re-use this verbatim in Method, Experiments, Conclusion."
  → "Marked [TBD] for the X numbers you haven't filled in."
```

### Scenario B — User wants to FIX / REVIEW an existing section

```
Step 1: Identify the section type and venue.

Step 2: Load the matching primary reference + flow-transitions.md.

Step 3: Diagnose using a 4-layer scan (in this order)
  → Layer 1 — Structure: Does the section have the right moves?
    (e.g., Abstract: does it hit Frame → Gap → Contribution → Method → Results?)
  → Layer 2 — Flow: Are transitions / pivots / connectors correct?
    (e.g., is there a `However` pivot? Is the contribution noun phrase consistent?)
  → Layer 3 — Sentence-level: Are openers, hedges, and anti-pattern phrases OK?
    (cross-check against language-phrasebank.md)
  → Layer 4 — Figure/Table coupling: Are figure references forward-positioned
    with the right specificity?

Step 4: Report findings as 3–6 numbered issues
  → For each issue: cite the playbook step, quote the offending sentence,
    propose a rewrite.

Step 5: Checkpoint
  → Show the diagnosis BEFORE rewriting. Some users want only the diagnosis,
    not the rewrite. Ask: "Want me to apply these fixes inline, or stop here?"

Step 6: If user wants fixes, produce the rewritten section
  → Track-change style: keep the user's structure where possible, swap
    sentences and connectors only at the diagnosed locations.
```

### Scenario C — User asks a writing-craft question (no draft to write/fix)

```
Step 1: Match the question to the routing table.

Step 2: Read the relevant reference (or section of a reference).

Step 3: Answer concisely
  → For "how long should X be?" → give the number + the rule.
  → For "what word should I use here?" → give 2–3 options + when each fits.
  → For "is this OK?" → cite the playbook step + verdict + minimal example.

Step 4: Only escalate to drafting if user asks
  → Do not volunteer to rewrite. The user asked a question, not for a draft.
```

### Scenario D — User wants a figure caption / table caption

```
Step 1: Identify the figure type (F1 teaser / F2 architecture / F3 hardware /
  F4 tasks / F5 rollouts / F6 plot / F7 ablation / F8 failures) using
  figures-tables-playbook.md Step 1.

Step 2: Confirm the role
  → What does the figure / table show? What's the takeaway claim?
  → For F6 plots: confirm sample size + aggregation method + variability.

Step 3: Draft using the matching template
  → F1: name + value prop + scale flex + (optional) novelty + (optional) URL
       (full teaser playbook: teaser-figure-playbook.md)
  → F2: 3-4 components with action verbs + data flow
  → F3: SKUs + dimensions + control rates
  → F4: task names locked (must match across figure / table / prose)
  → F5: row labels + frame-direction hint + color decode
  → F6: what's plotted + aggregation + sample size + takeaway
  → Tables: takeaway-bold caption + Ours-row marking + bold-best + ↑↓ arrows

Step 4: Verify panel notation consistency with rest of paper
  → If paper uses `(a)/(b)`, this caption uses `(a)/(b)` — never mix.

Step 4.5: Verify caption length against figure-type budget
  → F1 teaser / F2 architecture: 3–6 sentences (rich context)
  → F3 hardware / F4 tasks: 1 sentence (label-only)
  → F5 rollouts / F7 ablation: 2 sentences (row decode + takeaway)
  → F6 plot / F8 failures: 3–4 sentences (statistical disclosure + takeaway)
  → If your draft is over budget, cut adverbs and meta-commentary first.

Step 5: Verify task names match the rest of the paper
  → For F4 tasks and result tables, names MUST be identical across figure,
    table, and prose. Flag any drift.
```

### Scenario E — User wants the whole-paper arc reviewed

```
Step 1: Ask which sections are drafted.
  → If only some sections exist, scope the review to those.

Step 2: Read each drafted section through 4 lenses
  → Arc consistency: does the 6-move arc (HOOK → GAP → APPROACH → MECHANISM
    → EVIDENCE → IMPLICATION) flow from Abstract through Conclusion?
  → Contribution-restatement spiral: same noun phrase 5–7 times, identical
    spelling, expanding clause each time?
  → Tense correctness: Abstract present, Conclusion past?
  → Figure/table coupling: are all main-text figures referenced?

Step 2.5: Run the mandatory convention sweeps (rules 14 + 15 + 16 + 17 + 18 + 19 + 20 + 21 + 22 + standing rules)
  **Preferred path**: invoke the tool that automates these sweeps (resolve
  `$SKILL_DIR` per "Bundled tools — Path resolution"):
    `bash "$SKILL_DIR/tools/audit_conventions.sh" --strict`
  Run from the paper directory (with main.tex). The tool follows every
  `\input{...}` (including symlinked figure dirs via `find -L`), so it
  catches drift in `sections/*.tex`, `figures/*.tex`, `figures/*/*.tex`,
  and any other `\input`'d file. It auto-loads `audit_conventions.conf`
  from the paper dir if present (per-paper config for project-specific
  old labels, system names, scope-tag modifiers). See
  `$SKILL_DIR/tools/audit_conventions.example.conf` for the schema. Run
  `audit_conventions.sh --list` to list available sweeps.

  **Why automation matters**: manual grep over `sections/*.tex` only
  systematically misses figure/table captions in `figures/*.tex` —
  this happened to us and a reviewer would have flagged it. The tool's
  recursive `\input` discovery is the only robust way to enumerate
  everything the build pulls in.

  **Manual fallback** (if the tool is unavailable, or to spot-check a
  specific sweep):
  → Abstract self-containment + method-internal jargon: grep abstract for
    (a) `\ref`, `\autoref`, `\Cref`, `Section `, `Fig.`, `Table ` (rule 14
    — body-anchored cross-references); (b) `gate`, `commit`, `converge`,
    `epoch`, `early stopping`, `iteration` (training-loop control flow),
    plus the paper's specific hyperparameter names (e.g., `K=3`, `0.85`)
    that should live in Method, not Abstract. Flag every hit
    (abstract-intro-playbook.md Move 4 method-internal table).
  → Related-Work bucket-header audit: list every `\paragraph{...}` /
    `\subsection{...}` header in Related Work. Check each is (a) a pure noun
    phrase, (b) names the research class (not I/O, not technique, not a
    sentence with verb), (c) shares no redundant tail with other headers,
    (d) case-consistent with the other headers (rule 15).
  → Table-jargon-in-prose audit: grep Abstract / Intro / Method (conceptual
    paragraphs) / Conclusion / Limitations for `\brow\b`, `\brows\b`,
    `\bcolumn\b`, `\bcell\b`. Each hit MUST sit in a sentence that cites a
    table or figure in the same or immediately prior sentence; otherwise
    replace with `baseline` / `condition` / `setting` / `variant` (rule 16).
  → Config-dump-in-main-body audit (venue-gated, rule 17):
      (a) Confirm venue. If CoRL / RSS / NeurIPS / ICML / ICLR / Science
          Robotics → in-PDF appendix allowed. If ICRA / IROS / RA-L / T-RO →
          no in-PDF appendix.
      (b) Scan Method / Experimental Setup / Results for inline parentheticals
          listing hardware SKUs (`H200`, `A100`, `RTX`, `Jetson`), precision
          flags (`bfloat16`, `fp16`, `int8`), token caps (`new-token`,
          `context length`), learning rates (`2e-5`, `lr=`), batch sizes
          (`batch size`), control rates (`Hz`), random seeds.
      (c) For appendix-supporting venues: each hit becomes a pointer
          (`see Appendix~\ref{app:X}`); the full dense paragraph moves to
          the appendix.
      (d) For no-appendix venues: hits stay inline but compress to ONE
          tight sentence per category, or move to a `(code release at <url>)`
          pointer.
      (e) Flag any `see Appendix X` pointer in a no-appendix-venue paper —
          that's a dead reference.
  → Paired-condition-label-axis audit (rule 18): list every distinct label
    the paper uses for its main experimental conditions (e.g., `iteration row`,
    `no-prompt baseline`, `Ours`, `naked-modality`, `with X`, `without X`).
    For each comparison pair, ask: are the two labels on the same naming axis?
    If `Ours` partners with `Naked-Modality Baseline`, or `Iteration Row`
    partners with `No-Prompt Baseline`, rewrite both to share one axis
    (typically `{Adjective}-{condition} {ModelClass}` for an input-axis pair).
    Verify the canonical pair is used identically across Abstract / Intro /
    Method / Results / Conclusion (no drift to `our system` mid-paper).
  → Writing-process-archaeology audit (rule 19): scan appendix and footnotes
    for paragraphs describing dropped baselines, superseded comparators,
    internal experiment codenames (`E02`, `Phase 1`, `Attempt 001`), or
    candidate-Δ-that-was-changed explanations. These should be deleted; if
    the choice-of-baseline justification is needed, compress to ONE sentence
    in the main-body Baselines paragraph. If load-bearing, promote to a
    proper named ablation subsection + table — never an apologetic appendix
    paragraph.
  → Load-bearing-modifier audit (rule 20): identify the scope-tag modifiers
    the paper introduces in Problem Setup / Abstract / Intro (e.g.,
    `successful`, `exploratory`, `held-out`, `task-keyed`, `frozen`,
    `naked-modality`, `minimal-success`). For each, grep the rest of the
    paper for occurrences. The first definition site keeps the modifier;
    every subsequent occurrence outside a local-adjective use should drop it
    (`the exploratory trace` → `the trace`; `the held-out groups` → `the
    test groups`). Flag stacked redundancies like `successful exploratory`
    or `held-out test` when the second word already implies the first.
  → Concept-vs-instantiation audit (rule 21): identify any instantiation
    noun the paper might be leaking into conceptual framing positions
    (e.g., `demo`/`demos`/`demonstration` when the framework-level concept
    is `trace`; `controller` when the concept is `policy`; `trial` when the
    concept is `episode`). The `vocab-lock` sweep in
    `tools/audit_conventions.sh` (config field `VOCAB_LOCK_PATTERNS`) is
    the operational tool — every hit is listed for manual verification;
    the source-disclosure site (typically Experiments / Appendix dataset
    section) is expected to appear and is legitimate, but any occurrence in
    Abstract / Intro / Method / Results / Conclusion framing positions
    should be replaced with the conceptual noun.
  → New-task naming audit (rule 22): if the paper proposes a new QA task /
    benchmark / evaluation formulation, verify it has a named abbreviation
    with full expansion on first mention in Abstract, Intro, and Method.
    Grep for generic descriptors that signal an unnamed task: `\bour QA\b`,
    `\bthe QA task\b`, `\bour task\b`, `procedural[ -]?QA`, `manipulation
    reasoning task`. Each hit indicates the paper is leaning on a generic
    handle where a proper name is needed. Also verify: the abbreviation
    appears in `\keywords{...}`; the task name is consistent across
    Abstract / Intro / Method / figure & table captions / appendix; the
    `vocab-lock` config locks any legacy descriptors used in earlier
    drafts (e.g., `procedural-QA`) to prevent regression.
  → Teaser reference: grep Intro for `Figure 1` / `Fig. 1` / `\ref{fig:teaser}`
    — must appear in ¶1 or ¶2 (rule 7).
  → Limitation pairing: every `\textbf{...}` / `**...**` limitation label
    must have a `Future work could ...` sentence in the same paragraph (rule 8).
    Anti-pattern: a standalone `\textbf{Future work.}` block at section end —
    fold each direction into its source limitation paragraph instead.
  These eleven sweeps catch the high-frequency, low-effort misses that the
  4-lens scan tends to skip.

Step 3: Report the arc-level findings
  → Show the noun-phrase chain (or where it breaks).
  → Show the move map (which sections hit which moves).
  → Mark any anti-patterns at the cross-section level.

Step 4: Section-by-section diagnosis (concise)
  → 2–3 issues per section maximum.
  → Cite playbook steps for each.

Step 5: Prioritize fixes
  → "Highest leverage: lock the contribution noun phrase first — it cascades
    to 5+ places."
  → "Second: fix the missing `However` pivot in Abstract."
  → "Third: caption-level fixes."
```

---

## Universal rules (apply in every scenario)

1. **Match venue conventions**.
   - CoRL/RSS = arabic section numbers, lowercase panel labels `(a)(b)`, modal appendix 5–15 pages
   - ICRA/IROS = roman section numbers, all-caps APPENDIX, page-pressed limitations
   - Science Robotics = no section numbers, `Discussion` replaces Conclusion, Author Contributions + Model Card mandatory
   - When in doubt, ask the user.

2. **Lock the contribution noun phrase**.
   - First time you draft something with the system name, write it as `{Name}, a {descriptor}` and tell the user "this is the canonical phrase — re-use it verbatim in Method, Experiments, Conclusion."
   - When reviewing, flag any drift (`OpenVLA` vs `Openvla`, `our system` vs the actual name).
   - **Legacy-cleanup discipline when renaming a locked noun**: when the user upgrades a concept name mid-revision (e.g. `attempt-chain` → `exploratory chain` to anchor the task name's `Exploratory` root; or `\addprompt` → `DRH` after standardizing the artifact name), sweep ALL occurrences across main body, appendix, table captions, figure captions, and `math_commands.tex` (or equivalent macro file). Remove any legacy macros that expand to the old name. Reviewers who spot the legacy name in one caption assume mid-revision rot in the rest of the paper. Detection: after a rename, `grep -rn "{old_noun}"` over the whole paper tree must return zero hits in live (uncommented) prose.

3. **Tense rules**.
   - Abstract = present (`we introduce`).
   - Method = present + system-as-subject (`the model outputs ...`).
   - Experiments-as-completed = past (`we evaluated on ...`).
   - Conclusion = past (`we presented ...`).
   - When mixed, fix the tense to match the section's convention.

4. **Disclose deltas, not just absolutes**.
   - `87.3% success rate` alone = under-reported.
   - `87.3% (vs 61.4% for the strongest baseline, +25.9pp absolute / +42% relative)` = correct.
   - Never let an Abstract or Results paragraph claim a number without a comparison.

5. **One pivot per gap**.
   - Each section gets one `However` / `Yet` per gap-statement. Two `However`s in adjacent paragraphs = indecisive.
   - If the gap is bi-fold, enumerate as `(i) ... (ii) ...` within one pivot sentence.

6. **Statistical disclosure for every plot caption**.
   - Mean + variability measure + sample size. Always. Reviewers reject papers with naked plots.

7. **Forward-reference all main figures**.
   - The figure number appears in prose BEFORE the figure is described. Teaser is referenced in Intro paragraphs 1–2.

8. **Every limitation pairs with a future-work mitigation**.
   - Naked limitations read as defeatist. Each gets `Future work could ...` in the same paragraph.
   - **Anti-pattern**: a standalone `\textbf{Future work.}` paragraph at the end of the section. The default CoRL/RSS/ICRA pattern (D1 in `closing-appendix-playbook.md` Step 10) folds each direction into its source limitation paragraph. Reserve a standalone Future Work section for Science Robotics or heavy-page-budget submissions with 3+ unrelated directions that don't map onto existing limitation paragraphs.
   - **Name a mitigation mechanism as one example, not the sole path**: when the future-work clause cites a concrete mechanism, mark it as illustrative (`for example through a long-term memory`), not the mandated solution, unless it genuinely is the only option. Anti-pattern: "persistence requires tracking applied operations `through` a longer-horizon memory" (reads as the one fix). Fix: "letting the robot determine the state on its own, `for example through` a long-term memory of past interactions."

9. **Hedge first-claims and negative-existence claims with scope**.
   - Never write `We are the first to do X.` — write `To the best of our knowledge, we are the first to do X under constraint Y.`
   - The same hedge covers any **negative-existence claim about the literature** — `no benchmark isolates X`, `no prior method does Y`, `no dataset captures Z` — which is a disguised first-claim (it asserts you have surveyed the whole field). Prefix it with `To the best of our knowledge`. Anti-pattern: "no existing benchmark isolates whether models defer to feedback." Fix: "To the best of our knowledge, no existing benchmark isolates whether models defer to feedback." Detection: grep for `no existing`, `no prior`, `no benchmark`, `no method`, `none of`, `the first`, `has not been`; each must sit behind the hedge unless it cites the survey that establishes it.

10. **Cite the playbook step when the user pushes back**.
    - If the user argues against an edit, cite the specific Step from the relevant reference (e.g., "abstract-intro-playbook.md Step 5 — Move 5 mandates delta-form numbers"). Don't argue from authority — argue from observed corpus patterns.

11. **Roadmap paragraphs — one per paper, venue-gated**.
    - **Intro roadmap** (the "Section II describes ... Section III ..." paragraph): only for IEEE-style venues (ICRA / IROS / RSS) OR theory papers with unconventional section order. CoRL / NeurIPS-adjacent / Science Robotics = silent transition, NO Intro roadmap.
    - **Method-internal roadmap** (one sentence naming Method's own subsections): only when Method has 3+ subsections AND there is NO Intro roadmap already covering them. If both exist, delete the Intro one — the Method one is more useful.
    - **No double-roadmap**: a single paper has at most ONE roadmap paragraph. CoRL submission with both → flag and remove the Intro roadmap.

12. **Conflict-resolution precedence between playbooks**.
    - When two reference files disagree (e.g., Method tense rule, roadmap placement), apply in this order:
      1. SKILL.md Universal Rules (this list) win.
      2. Then the section's PRIMARY playbook (per routing table).
      3. Then cross-cutting playbooks (`flow-transitions.md`, `language-phrasebank.md`).
    - Never let a phrasebook entry override a section playbook's structural rule.

13. **Pushback escalation policy** (companion to rule 10).
    - If the user argues against an edit AND the issue is **stylistic** (word choice, sentence rhythm, "I prefer it this way"): cite once, then defer to the user. They're the author.
    - If the issue is a **convention violation** that will hurt review (missing pivot, naked plot, double-roadmap, fabricated number, tense mismatch in Abstract): cite once with a corpus-pattern reason, then if user still insists, leave it but record in the delivery summary: "Kept your phrasing per your call. Note: this departs from the corpus norm — flag to your advisor for sign-off."
    - Never argue past two exchanges. Capitulate to stylistic preferences immediately; flag-and-leave for convention violations.

14. **Abstract is self-contained — no body-anchored cross-references**.
    - The abstract appears in isolation (arXiv listings, search snippets, program books, citation indexes). `\S\ref{sec:X}`, `see Section 4`, `as in Fig. 2`, `Table 1 reports ...` render as noise or as "§ ??" to readers who haven't opened the PDF.
    - Allowed in abstract: numbers, named baselines, system name, dataset/model names, project URL in Move 6 coda.
    - Forbidden in abstract: any `\ref` / `\autoref` / `\Cref` to a section, figure, table, or equation in the body. Re-state the content; do not point at it.
    - When reviewing, grep abstract for `\ref`, `\autoref`, `\Cref`, `Section `, `Fig.`, `Table ` and flag every hit.

15. **Related-Work bucket headers carry only distinguishing information**.
    - Every bucket header is a pure noun phrase naming the **research class** (not the technique, not the I/O structure, not a complete sentence with verb).
    - Compute the longest common suffix across headers. If it's more than one word, that's the paper's universal scope — drop it from every header (it's implicit). Example: four headers ending in `... on Manipulation Traces` → drop the suffix; the section heading already establishes the domain.
    - Pick Title Case OR sentence-case and apply to **every** header in the section. Mixed case is a tell.
    - See method-relatedwork-playbook.md Step 2 for the full anti-pattern table.

16. **No table jargon (`row`, `column`, `cell`) in prose contexts**.
    - `row` / `column` / `cell` force the reader to picture a table that isn't on the page. They are legitimate only when the current paragraph just cited a specific table or figure (`Table~\ref{tab:X}` / `Fig.~\ref{fig:Y}` in the same or immediately prior sentence).
    - In **prose contexts** — Abstract, Introduction, Method conceptual paragraphs, Conclusion, Limitations — replace table jargon with experiment-condition vocabulary: `baseline`, `condition`, `setting`, `variant`, `system`. Specifically:
      - `no-prompt row` / `baseline row` → `no-prompt baseline` (drop redundant "row" — "baseline" already names the role)
      - `iteration row` / `our row` → `iteration condition` / `our system` / `{SystemName}`
      - `the X row from the modality ablation` → `the X baseline` (the table reference belongs in the cite, not the noun)
    - In **table-anchored contexts** — Results/Ablations paragraphs that just cited `Table~\ref{...}` or `Figure~\ref{...}` — `row` is fine and even preferred for precise reference (`row 8 (video + proprio)`, `the iteration row clears 0.93`).
    - When reviewing, grep prose-context files for `\brow\b`, `\brows\b`, `\bcolumn\b`, `\bcell\b`. Each hit must either sit inside a table-anchored sentence (one cite in the same or prior sentence) or be replaced.

17. **Config-parameter relegation is venue-gated**.
    - "Config-parameter dump" = hardware SKU, precision flags, token caps, batch sizes, optimizer hyperparameters, control rates, learning-rate schedules, random seeds — the stuff that doesn't change the paper's argument but is needed for reproducibility.
    - **Venues that support an in-PDF appendix (`\appendix` in the same compiled PDF)** — CoRL, RSS, NeurIPS, ICML, ICLR, AAAI, Science Robotics (Supplementary Materials), Nature Robotics (Methods + Extended Data): aggressively relegate. Main body keeps **only the pointer** (`hardware, precision, and token caps are in Appendix~\ref{app:identifiers}`); appendix carries the dense paragraph. Each main-text inline config detail you keep eats line budget that should go to argument.
    - **Venues with strict page limit and no in-PDF appendix** — IEEE RA-L (8 pages incl. refs), IEEE T-RO (limited supplementary), ICRA standard track, IROS, most IEEE Letters: cannot relegate to an in-PDF appendix because there isn't one. Either (a) keep the config compressed inline in one tight sentence, or (b) point to a separate supplementary PDF / code release (`full hyperparameters in the code release at <url>` / `see supplementary PDF`). DO NOT write `see Appendix X` if your venue does not allow `\appendix` — reviewers will flag a dead pointer.
    - **When in doubt**: read the venue's CFP for "supplementary materials" / "appendix" guidance. CoRL/RSS default = aggressive relegation. ICRA/IROS default = inline compression + code-release pointer.
    - See experiments-results-playbook.md Step 9 (hardware paragraph) and method-relatedwork-playbook.md Step 10 (appendix-relegation) for drafting guidance under each regime.

18. **Paired condition labels must share a naming axis**.
    - Whenever the paper compares two experimental conditions to each other (treatment vs. control, ablation vs. full, ours vs. baseline), the two labels must be on the **same naming axis** — so the reader sees the pair as a pair, not as two unrelated nouns.
    - **Same-axis examples (good)**:
      - `Distilled-Prompt VLM` vs. `Naked-Modality VLM` — axis = "what input the VLM gets" (`{Adjective}-{input-condition} VLM` template)
      - `With pretraining` vs. `Without pretraining` — axis = "ablation flag"
      - `Ours (RL)` vs. `Ours (BC)` — axis = "training paradigm"
      - `OpenVLA-7B` vs. `OpenVLA-13B` — axis = "scale"
    - **Mixed-axis anti-patterns (bad)**:
      - `Iteration row` vs. `No-prompt baseline` — one names a table position (`row`), the other names an experimental role (`baseline`); reader cannot tell they are the same pair
      - `Ours` vs. `Best naked-modality` — `Ours` is an authorship marker, `Best naked-modality` is a content descriptor
      - `With distilled prompt` vs. `Raw VLM` — one names the input intervention, the other names the model class
    - When reviewing, list the labels of every condition the paper compares. For each pair, ask: "Are these two labels on the same axis?" If not, rewrite both to share one axis.
    - When the label drifts (e.g., `iteration row` in §4, `iteration condition` in §3, `our system` in §1), lock to one canonical pair across the whole paper — first/last mention identical to middle mention.
    - See language-phrasebank.md Section J for axis-aligned substitution candidates.

19. **No "writing-process archaeology" in main body or appendix**.
    - "Writing-process archaeology" = paragraphs that describe how the paper's setup or claims evolved during drafting: dropped baselines, internal experiment codenames (`E02`, `Phase 1`, `Attempt 001`), candidate Δs that were superseded, justifications for why a comparator was changed from one to another.
    - These read as the author talking to themselves, not to the reader. Reviewers infer cherry-picking ("if you considered other baselines, why did you settle on these?"). Even when the choice is defensible, the archaeology paragraph creates the question.
    - **Fix**: state the baseline's positive identity in the main-body Baselines paragraph and stop there. The baseline's own definition does the anti-cherry-picking work:
      - ✓ `The Naked-Modality VLM is the strongest of {video, proprio, video+proprio} rows from the modality ablation (Table~X); the chain prompt and evaluation cap are identical to the Distilled-Prompt VLM.`
      - ✗ `... we considered several candidates and chose the most conservative one.` ← softer archaeology; still triggers "which candidates?"
      - ✗ `... originally we used X but switched to Y for fairness.` ← explicit archaeology
    - **Subtractive principle**: the cleanest defense against "you cherry-picked" is to define the baseline as the *maximum* over a named set (e.g., `strongest of {...}`, `best across modalities`). The reader sees the upper-bound construction and the question dissolves — without you having to comment on the construction.
    - No numbers from dropped baselines. No internal codenames. No "originally we used X but switched to Y" / "the most conservative of the candidates we considered" explanations — both forms trigger the same suspicion.
    - If the dropped-baseline information is load-bearing for the argument (e.g., showing robustness across baseline choices), promote it to a full ablation **with a proper subsection name and table**, not a hidden paragraph in the appendix.
    - See closing-appendix-playbook.md anti-patterns for the appendix-specific framing.

20. **Lock load-bearing modifiers, then drop them outside the definition**.
    - Many embodied-AI papers introduce a *modifier* that scopes the contribution: `successful` exploratory trace, `held-out` test groups, `task-keyed` prompt entry, `frozen` base VLM, `naked-modality` baseline, `minimal-success` action chain. Each such modifier is **load-bearing once** — at the place where the term is first defined or scoped — and then becomes wallpaper if repeated.
    - **Rule**: define the modifier exactly once (in Problem Setup / first introduction / Abstract), then drop it from every subsequent reference. The reader carries the modifier mentally; repeating it implies the author is afraid the reader will forget.
    - **Example (the `successful exploratory trace` case)**:
      - ✓ §3.1 Problem Setup: `We consider procedural reasoning over a successful exploratory manipulation trace ...` (definition; modifier carried by the reader)
      - ✓ §2/§4/§5/§7: `the exploratory trace`, `the trace`, `this trace` (modifier dropped — already in the reader's mental model)
      - ✗ §2 ¶1: `In contrast, we frame chain prediction over a successful exploratory trace ...` (redundant repetition)
      - ✗ §2 ¶2: `in a successful trace, the same first pull-failure is signal that ...` (the modifier is doing no new work here)
    - **Watch for stacked redundancy**: `the successful exploratory trace's probe segment` triple-loads `successful` + `exploratory` + `'s probe`. After the first definition, drop both `successful` and `exploratory` — `the trace's probe segment` is unambiguous.
    - **Exception**: when the modifier carries a *local* meaning (e.g., `the second, successful pull` describing the second drawer-pull attempt that succeeded after the first failed), keep it — here `successful` modifies `pull`, not the framework-level concept. The rule is about modifier-as-framework-scope-tag, not modifier-as-local-adjective.
    - When reviewing, grep prose for the load-bearing modifiers the paper introduces. Count occurrences. If a modifier appears in 3+ places outside its definition site, flag every redundant repetition.
    - This is the modifier analog of rule 2 (lock the contribution noun phrase): rule 2 keeps the *system name* identical across re-mentions; rule 20 keeps the *scope-tag modifier* in one place only.

21. **Lock the type-general noun; isolate the concrete instantiation to a source-disclosure site**.
    - For each data object the paper reasons about, pick the **most type-general noun** that names what the object *is* (a stream / a record / a measurement), not what it *came from* (a demonstration / a rollout / a replay buffer / a teleop session). Use that conceptual noun everywhere — Abstract, Intro, Method, Results, Conclusion — and reveal the concrete instantiation only at the source-disclosure site (typically Experiments setup or Appendix dataset section).
    - **Why**: instantiation-named nouns lock the contribution to one data regime. If the paper writes "iterates on demos" throughout, reviewers infer the method requires demonstrations and won't work on inference logs, replay-buffer entries, or live recordings — even when nothing in the method actually depends on the data being a demonstration. The conceptual noun keeps the contribution portable across sources.
    - **Example (the `trace` vs `demonstration` case)**:
      - ✓ Abstract: `iterates on traces with access to ground-truth chain labels`
      - ✓ Intro / Method / Results / Conclusion: `the task's traces`, `the agent reads the trace input`, `each trace`
      - ✓ Appendix `app:datasets`: `Each trace in this paper is a recorded demonstration (simulator: AdaManip rollout; real-robot: human teleoperation). The framework treats trace as a generic data type and is not demonstration-specific: alternative sources such as model inference logs or replay-buffer entries could compose unchanged.`
      - ✗ Abstract: `iterates on demos` (instantiation noun in conceptual framing position)
      - ✗ Method figure caption: `iterates on the task's demo data` (same — demo-bound framing)
    - **Other common concept/instantiation pairs in embodied-AI**:

      | Concept noun (use throughout) | Concrete instantiation (only at source-disclosure) |
      |---|---|
      | `trace` / `trajectory` | `demonstration`, `rollout`, `replay-buffer entry`, `teleop session`, `inference log` |
      | `policy` / `controller` | `transformer policy`, `diffusion policy`, `MLP controller` |
      | `episode` | `trial`, `attempt`, `run`, `recording` |
      | `observation` | `RGB frame`, `point cloud`, `joint encoder reading` |
      | `dataset` | `OpenX subset`, `BridgeData V2`, `our 60-demo collection` |
      | `reward signal` | `sparse +1`, `shaped potential`, `LLM-judged scalar` |
      | `latent` | `bottleneck`, `embedding`, `VAE z` |

    - **Exception (mirrors rule 20's local-adjective exception)**: when the instantiation noun appears at the source-disclosure site itself, or in a sentence whose specific purpose is naming the implementation (`we use the Unitree A1 robot`, `60 demonstrations collected on physical hardware`), keep it. The rule is about leakage of instantiation framing into the conceptual layer, not about banning the word.
    - **Detection**: the `vocab-lock` sweep in `tools/audit_conventions.sh` (config field `VOCAB_LOCK_PATTERNS`) is the operational tool. Add the instantiation noun(s) the paper should not leak into conceptual framing (e.g., `\bdemo\b`, `\bdemos\b`, `\bcontroller\b`); the sweep lists every occurrence for manual verification. The source-disclosure site will appear in the list — that's expected; the auditor's job is to surface, the reviewer's job is to verify each hit is legitimately at a disclosure site, not at a framing site.
    - This is the **noun analog** of rule 20 (which is about modifier-level scope tags). Rule 20 controls *adjective* leakage; rule 21 controls *noun* leakage. Together they form the "lock the abstraction layer; isolate concretizations to disclosure sites" pattern.

22. **A proposed new task must have a named abbreviation, defined once and locked everywhere**.
    - When the paper proposes a **new QA task / benchmark / evaluation formulation** (not just a new method on an existing task), the task **must** have a named abbreviation. Generic descriptors like `procedural QA`, `manipulation reasoning task`, `our QA task` are not citable, not memorable, and reviewers will not retain them. Named tasks survive in citation graphs; generic descriptors do not.
    - **Corpus naming pattern**: `{Domain}-QA` / `{Domain}-Bench` / `{Domain}Bench`. Examples reviewers expect to recognize: VQA, RoboVQA, ManipBench, EgoPlan-Bench2, OpenX, R2D2-VQA, HARMONIC-MM. The abbreviation expands to a noun phrase that reads naturally in the title and section openers.
    - **First-mention convention**: introduce the task with `{Full Expansion} ({Abbreviation})` exactly once per major section (Abstract, Intro ¶3, Method §3.1 / Problem Setup). After first mention in each section, use the abbreviation only.
    - **Definition site**: the formal definition (input → output → metric) lives in Method's Problem Setup subsection. The Abstract and Intro use the abbreviation + a one-line gloss ("the task of predicting the minimal-success action chain that explains a trace"); the Method section gives the full I/O spec.
    - **Example (the EMT-QA case)**:
      - ✓ Abstract S2: `... pipeline for *Exploratory Manipulation Trace QA* (EMT-QA): ...`
      - ✓ Intro ¶3: `... pipeline for *Exploratory Manipulation Trace QA* (EMT-QA), the task of predicting the minimal-success action chain that explains an exploratory manipulation trace.`
      - ✓ Method §3.1: `We introduce *Exploratory Manipulation Trace QA* (EMT-QA), a chain-prediction task over a successful exploratory manipulation trace. Given a synchronized stream of (i) ..., (ii) ..., (iii) ..., the system must output the *minimal-success action chain* ...`
      - ✓ §4/§5/§6/§7/Appendix: `EMT-QA chain accuracy`, `the EMT-QA target strings`, `the EMT-QA chain question`, `EMT-QA artifacts`
      - ✗ Anywhere: `procedural-QA`, `procedural multimodal QA`, `our QA task`, `the QA we propose` (generic descriptors with no abbreviation — reviewers won't remember or cite this)
    - **Title alignment** (optional but strong): if the task is a primary contribution, the title should signal the task domain. The expansion noun phrase should be parseable from the title without the abbreviation (`... for Exploratory Manipulation Trace QA` is fine; `... for EMT-QA` in a title is not — title readers don't have the expansion yet).
    - **Keywords entry**: the abbreviation belongs in the `\keywords{...}` list alongside the method name and domain (e.g., `EMT-QA, exploratory manipulation, prompt distillation`).
    - **Detection**: when reviewing, grep the paper for `\bQA\b` / `\bbenchmark\b` / `\btask\b` in framing positions (Abstract, Intro, Method opener). If the paper reaches for a generic descriptor where a proper name should be, flag it. The `vocab-lock` sweep can also lock legacy generic descriptors (`procedural-QA`, `our task`) once the proper name is chosen, preventing regression.
    - **Sibling to rule 2** (lock contribution noun phrase). Rule 2 locks the *system name* (`Closed-Loop Trace Distillation`); rule 22 locks the *task name* (`EMT-QA`). A paper that proposes a method + a task + a trained artifact needs all three names locked independently. Worked example of a fully-named triad: **EMT-QA** (task, rule 22) × **Closed-Loop Trace Distillation** (method, rule 2) × **Distilled Reading Heuristic / DRH** (artifact, rule 2 — same locking discipline as system names). Picking same-root abbreviations across the triad (here `Distill-` shared by method and artifact) makes the contribution scannable as a single citation entity.
    - **Choosing the right generic descriptor for the task abbreviation**: after locking `{Abbrev}`, the generic-noun descriptor that lives in `{Full Expansion} ({Abbrev}), a {descriptor}` must also lock across abstract / intro / method first-mentions. Anti-patterns:
      - *Too narrow* (descriptor names an implementation specific, not the task type): `chain-prediction task`, `phase-segmentation task`, `reward-classification task` — these read as method choices, not task definitions.
      - *Too generic* (drops the input modality that distinguishes the task): `QA task`, `reasoning task`, `prediction task`.
      - *Balanced* (acknowledges the abbreviation's structural suffix AND the input modality): `multimodal QA task` (matches the `QA` suffix in `{X}-QA`), `multimodal reasoning task`, `multimodal {domain} benchmark`.
      Worked example: for `Exploratory Manipulation Trace QA (EMT-QA)`, the locked descriptor is `multimodal QA task` — not `chain-prediction task` (too narrow, locks the framing to one prediction style) and not `QA task` (too generic, drops the video+proprio multimodal input).

23. **User edit instructions are intent specifications, not final prose** (companion to rule 10/13).
    - When the user describes a desired edit in colloquial language (often Chinese, often a single imperative — "拆出一节说明泛化性", "这一句优化下", "方法具有一定泛化性"), treat the message as **intent**, not as draft text. Parse the underlying paper-writing move (split a paragraph, fold a sub-clause, hedge a claim, re-sequence a list, credit-then-limit, swap a connector, rename a section) and realize it in the venue's published register using the relevant playbook step. Never transliterate.
    - **Anti-pattern**: copying the user's literal phrasing into the paper. "方法具有一定泛化性" rendered as "the method has a certain generalization" surfaces the user's voice, not the published voice. "这一段挺好的" rendered as "this paragraph is good" is not paper prose at all — it was metadata about the *previous* edit, not text for the *next* edit.
    - **How to apply**: (i) identify what paper-writing move the user is asking for; (ii) look up the canonical form for that move in the routed playbook step; (iii) write prose in that form. If the move is not obvious, ask one clarifying question rather than draft the literal translation.
    - **Same rule applies recursively to skill edits**. When the user says "将这点也写到 skill 中" / "skill 里没有说明吗", parse what *kind* of rule they want recorded — a paper-writing convention, a collaboration meta-rule, an anti-pattern entry, a routing-table row — and place it in the corresponding section. Do not paste the user's phrasing into the skill as if it were a rule statement, and do not promote a one-off paper edit into a paper-writing rule unless the user asked for a generalizable rule. When in doubt, ask which class.

24. **Generic-then-named first mention for new artifacts** (extends rule 22 from task names to non-task contribution nouns).
    - When introducing a new artifact noun (a heuristic, a prompt, an encoding, a layer, an intermediate object), the canonical first-mention form is `a {generic descriptor}, which we call the {Name} ({Abbr})`. Generic noun first, named noun second. Reader builds a picture from the generic noun, then caches the name as a handle for that picture.
    - The pattern repeats in EVERY major section's first mention — Abstract, Intro ¶3, Method §3.{problem-setup or pipeline}, and Conclusion. Reviewers may skip from abstract straight to method or to results; each major section's first-mention must be self-contained with both the gloss and the name.
    - **Anti-pattern (name-first)**: `We distill a *Distilled Reading Heuristic* (DRH) over the trace.` — name introduced without prior gloss; reader cannot picture what it is until they read further.
    - **Canonical form (generic-then-named)**: `We distill a one-line natural-language prompt over the trace, which we call the *Distilled Reading Heuristic* (DRH).` — generic descriptor first; the name caches the descriptor.
    - **Inline-gloss companion for non-abbreviated core nouns**: e.g., `minimal-success action chain`, `chain accuracy`. Use the same per-section first-mention discipline with a comma-appositive inline gloss: `the minimal-success action chain, the fewest actions that complete the task, follows from the precondition`. The appositive serves the same role as `which we call` does for abbreviated nouns.
    - **Detection**: grep abstract / intro / method for the first appearance of every emphasized (`\emph{...}`) or capitalized contribution noun. If the first appearance lacks a preceding generic noun + comma + `which we call` (or equivalent appositive gloss), flag it.
    - This is the **artifact analog** of rule 22 (which applies first-mention discipline to task names). Rule 22 = task name; rule 24 = artifact name + non-abbreviated core nouns.

25. **No engineering jargon in academic paper prose**.
    - Three classes of jargon to elide before submission:
      1. **Version-control / GitHub vocabulary**: `fork`, `branch`, `clone`, `PR`, `monorepo`. These are author-developer words; in published prose they read as engineering-shop talk, not academic claim. Use `built on`, `extends X's task suite`, `derived from`, `following X`. Anti-pattern: `Simulator traces are collected in IsaacGym on an AdaManip fork.` → Canonical: `Simulator traces are collected in IsaacGym building on the AdaManip task suite.`
      2. **Raw LaTeX macros that expand to implementation-level nouns**: macro names like `\langtmpl` (`the task-keyed prompt template`), `\addprompt` (legacy artifact name), `\confkey`, `\cfgflag` are author-only shorthand for internal abstractions. In the rendered PDF the reader sees a phrase the paper never defined, OR they see the macro name itself if the macro is missing — either way the reader is confused. Fix: (a) expand the macro inline to its conceptual phrase when short (`the task-keyed prompt template`), OR (b) replace with the contribution noun phrase already in scope (`a single line per task` → `the DRH`). If a macro expands to a legacy noun that has been renamed, delete the macro and replace all callers with the new noun.
      3. **Internal-system actors the paper does not formally introduce**: phrases like `the driver commits`, `the dispatcher dispatches`, `the orchestrator schedules`, `the runtime evaluates` introduce phantom actors. Reviewers cannot tell whether `driver` is a synonym for the named `agent` or a distinct component. Collapse to the actors the paper already defines (typically the named agent), and rephrase the action accordingly. Anti-pattern: `The agent proposes a candidate DRH; the closed-loop driver commits the candidate.` → Canonical: `The agent proposes a candidate DRH and commits it only when ...` (or, when the agent is grammatically inconvenient, use passive: `the candidate is committed only when ...`).
    - **Detection**: grep main body for `fork`, `branch`, `\\\\[a-z]+(?=[\s{}])` (raw macro tokens), and any noun ending in `-er` or `-or` that the paper has not introduced via `\textbf{}` / `\emph{}` definition. Flag each hit for elision or replacement.
    - This rule is the **prose analog** of rule 17 (config-parameter relegation). Rule 17 moves engineering specifics to the appendix; rule 25 removes engineering vocabulary from the prose itself even when the specifics are warranted.

26. **Method abstraction vs Experiment specifics — separation of duty**.
    - Method §3 paragraphs describe hyperparameter **semantics and trade-offs**, not specific values. The reader leaves §3 understanding what each hyperparameter controls; they look in §4 (Experimental Setup) for the values used.
    - **Method-side (semantics + trade-off)**: `The two hyperparameters K and the gate threshold jointly trade off per-round wall-clock, agent-token consumption, training-trace coverage (larger K samples more variety), and the committed artifact's robustness (stricter gates filter unreliable candidates at the cost of convergence speed). Specific values are documented in \S\ref{sec:setup_main}.`
    - **Experiment-side (values only, no trade-off re-explanation)**: `The closed-loop iteration uses K=3 and a chain-accuracy gate of 0.85.`
    - **Anti-pattern (mixed responsibilities)**: dumping `K=3`, `gate=0.85`, `per-group cap=21`, AND a `5–30-min budget` claim AND the trade-off explanation into a single method paragraph. The reader cannot tell where the method abstraction ends and the experiment specifics begin; the trade-off claim reads as a *justification for the specific values* rather than as method-level semantics.
    - **Range-reporting follows the same split**:
      - *Method-side ranges describe artifact constraints* — report **upper bound only**: `The committed DRH stays within 200 tokens.`, `Each iteration round completes in at most 30 minutes.`
      - *Experiment-side ranges describe what actually happened* — report **full range**: `Each task's iteration run converged in 1–5 candidate-DRH rounds; the committed DRH was 50–200 tokens across our 5 tasks.`
      - The semantic distinction is **constraint vs. observation**. Method paragraphs declare the upper limit the artifact is designed to respect; experiment paragraphs record the empirical distribution.
    - **Detection**: grep method paragraphs for specific numeric values (`K=`, `\bgate\s*=`, `\$[0-9]`). Each occurrence must justify itself as a method-essential constant (e.g., the value affects the reader's understanding of the trade-off itself, like a sigmoid temperature whose effect is non-linear). Otherwise relegate to §4.

27. **Section title and caption anti-colon-description**.
    - Section titles and table/figure captions should not pair the topic noun with a colon- or comma-introduced paraphrase of the same topic.
    - **Anti-pattern (section title)**: `\section{Main Results: Iteration Uplift on EMT-QA}` — `Main Results` already establishes the section's role; `Iteration Uplift on EMT-QA` paraphrases the paper's thesis without adding scope.
    - **Anti-pattern (table caption opener)**: `\caption{Main results: closed-loop uplift on EMT-QA chain accuracy. The Naked-Modality VLM is ...}` — the opener phrase doubles the section title; the body already specifies the comparison.
    - **Canonical form**: `\section{Main Results}` and `\caption{Main results. The Naked-Modality VLM is ...}`. The topic-noun stands alone; the body carries the specific information.
    - **When IS a colon legitimate?**: when the post-colon clause carries information the topic noun does NOT. Tests:
      - Scope-narrowing: `Limitations: known failure modes` (scope: we cover failure modes, not other limitation classes).
      - Comparison framing: `Ablation: with vs. without pretraining` (specific comparator pair).
      - Domain anchor on a generic topic: `Datasets: BridgeData V2 and OpenX` (names the actual datasets).
      - Question hook in display titles (mostly for sub-section-style display in posters / slides): `Why does the DRH transfer? Mechanism analysis` — only justified when reading the title alone (no body context) leaves ambiguity.
      - **The test**: would the section/caption be self-explanatory without the post-colon clause? If yes, drop the clause.
    - **Detection**: grep `\section{`, `\subsection{`, `\caption{` for `:` followed by a noun phrase. For each hit, ask whether the post-colon noun adds scope, comparator, or domain anchor — or merely paraphrases the topic.

28. **Opener variety across consecutive paragraphs in a cluster**.
    - When a section has 3+ consecutive paragraphs (typical in Limitations, Experimental Setup, multi-axis Ablations), DO NOT start all of them with the same syntactic frame.
    - **Anti-pattern**: three Limitations paragraphs all opening with `Our pipeline ...`, `Our traces ...`, `Our evaluation ...` — the possessive repetition reads as monotone and unrhythmic.
    - **Canonical alternation** — pick distinct opener patterns across the cluster:
      - *Possessive*: `Our pipeline assumes ...`
      - *Definite article*: `The reported traces come from ...`
      - *Universal quantifier*: `All evaluation traces come from ...`
      - *Locative PP*: `Across three simulator and two real-robot tasks on distinct embodiments, the DRH ...`
      - *Concession*: `Although the EMT-QA formulation admits ..., our evaluation covers only ...`
      - *`While X, Y` hedge*: `While our method achieves ..., its accuracy degrades in ...`
    - **Rule of thumb**: in a 3-paragraph cluster, use 3 distinct opener patterns. In a 4+ paragraph cluster, no opener pattern appears more than twice and never twice in adjacent paragraphs.
    - **Detection**: list the first 4 words of every paragraph in the cluster. If the first noun phrase repeats 3+ times in a row, rewrite the openers to diversify per the patterns above.
    - See `language-phrasebank.md` Section H for full opener inventory.

29. **One subsection, one topic**.
    - A `\subsection{...}` carries one distinct method or empirical topic. When the subsection title declares topic A but the prose mixes topics A and B, reviewers feel the cross-topic sentence is out of place and skim past it.
    - **Anti-pattern**: `\subsection{Incremental multi-task via prompt-only artifacts}` whose first sentence describes the multi-task scaling property (topic A) and whose second sentence describes the fairness controls for the Distilled-Prompt vs. Naked-Modality comparison (topic B). Topic B belongs in §3.2 (the inference protocol cluster), not in the multi-task section.
    - **Fix-in-place rule**: for every sentence in a subsection, ask "does this sentence's claim fall under the subsection title's noun phrase?" If not, the sentence belongs in a different subsection — typically a sibling `\textbf{Label.}` paragraph in the closest method-level cluster.
    - **Detection**: for each `\subsection{...}`, list the sentence-level claim of every sentence. Group by topic-noun. If two distinct topic-nouns appear, the subsection mixes topics — split or relocate.
    - This rule is the **section-level analog** of rule 5 (one pivot per gap). Rule 5 keeps a single paragraph's argument structurally clean; rule 29 keeps a single subsection's topical scope clean.

30. **Related Work buckets are `\subsection`s, not run-in `\paragraph`s**.
    - Each research class gets a `\subsection{...}` at the same heading level as the Method's subsections (IEEEtran renders these `A.`, `B.`, `C.` …); do not use `\paragraph{...}` run-in bold headers for Related Work families.
    - **Anti-pattern**: a Related Work made of four `\paragraph{Cross-episode memory…}` run-ins while the Method uses `\subsection` — inconsistent and harder to scan.
    - **Detection**: grep Related Work for `\paragraph{`; if the families are `\paragraph`, promote them to `\subsection`. The bucket-header noun-phrase audit still applies.

31. **Subject is the method, not the robot** (anti-anthropomorphism).
    - Claims about prior work, the gap, or failure modes take the method / system / memory as the grammatical subject, not "robots" generically. A robot may anchor a *motivating scenario*, but not statements about what approaches do.
    - **Anti-pattern**: "Most robots nonetheless do exactly that."
    - **Fix**: "Existing cross-episode memories nonetheless preserve that overhead."

32. **Do not coin a named principle you use once.**
    - If a capitalized "Principle / Property" earns a boxed definition and its own (sub)section but is referenced almost nowhere else, de-coin it: explain the idea inline in Intro / Related and keep only the descriptive term for the artifact it produces.
    - **Detection**: for each coined, capitalized concept, count uses outside its own definition; if ≤2, drop the coinage and fold the idea into running prose.

33. **Position differently-motivated work by objective, not artifact superiority.**
    - When prior work pursues a different goal than yours, frame the delta as *objective + organization*, not "our representation beats theirs" — claiming superiority on an axis the other work never optimized is a strawman reviewers will rebut.
    - **Anti-pattern**: "we store a procedure (which shortens) vs.\ they store a trajectory (which cannot)," when shortening was never their goal.
    - **Fix**: "they target success and organize memory around states; we are object-centric and target efficiency."

34. **Lock the general term in framing; use the instantiation term only at the disclosure site.**
    - Abstract / Intro / Method-general-form use the general module or concept name (e.g.\ `procedure-conditioned policy`, `identifiable features`); the specific realization (`language-conditioned policy`, `appearance`, a model identifier) appears only where the instantiation is described.
    - The noun analog of rules 20–21, applied to the **general-vs-instantiation** axis: do not let a basic implementation choice (e.g.\ a `frozen` policy) read as a core property in the framing.

35. **One running example, not an example list.**
    - Motivate with a single concrete instance threaded through the paper; do not open with a comma list of three illustrations.
    - **Anti-pattern**: "a latched microwave, a locked cabinet, a sprung door."
    - **Fix**: "such as a latched microwave," reused at later mentions.

36. **No defensive coda after the contributions; state contributions positively.**
    - Do not append a self-justifying paragraph after the contributions list that declares what is *not* a contribution or pre-defends the framing. Real papers end the Introduction on the contributions list (or a one-line roadmap), not on a disclaimer.
    - **Anti-pattern**: after the `\item` list, "The policy is deliberately *not* a contribution: we reuse an existing policy… The contribution is the framework…, on the axis of efficiency, not success rate, which serves as a guardrail…" — defensive over-explaining a reviewer never asked for.
    - **Fix**: delete it. State each contribution positively *in the list itself*, and convey positioning (e.g.\ efficiency-not-success) **implicitly** — lead with it and let the results carry it — never as an explicit "we position X, not Y, as the contribution" declaration. This applies to the **Abstract's closing too**: replace "We therefore position efficiency, not success rate, as the contribution…" with a natural statement of the result ("the benefit is purely one of efficiency: success never regresses, and on the real robot even improves"). If a fact like "the policy is reused" matters, state it once, matter-of-factly, at the Method instantiation, not as a disclaimer.
    - **Detection**: if the sentence after `\end{itemize}`, or the Abstract's last sentence, contains "not a contribution", "we position … not …", "we do not claim", or restates the contributions with a "not X" hedge, cut or rephrase it to a positive statement.
    - **The same positive-framing discipline applies mid-body, not only at the contributions coda**:
      - **Scope is a fork, not an apologetic assumption.** Present a studied regime as one branch of a neutral fork and name the branch you take, not as a precondition the method leans on. Anti-pattern: "This reuse assumes the instance returns to the same hidden state, the reset setting we study." Fix: "The hidden state may reset between encounters or persist; … our experiments use only the reset setting." Valid only when the other branch is a legitimate alternative (not a failure mode) and the contribution applies to both; if X is a fragile precondition, "we assume X" is the honest phrasing, not a hedge to launder.
      - **Name your method as the subject of its value claims.** Don't abstract the method's name out of a value statement to dodge a perceived overclaim; name it and let an adjacent clause carry the scope. Anti-pattern (timid circumlocution): "Both settings draw the same value from a first encounter's discovery…" Fix: "IOM provides the same value in both settings, so our experiments use only the reset setting" — the scope limit rides the next clause, not an abstracted-away subject.

37. **One home per claim — don't restate the narrative inside the contributions list.**
    - A point already made in the Intro's narrative paragraphs must not be repeated in a contribution `\item` (or vice versa). Each claim lives in exactly one place. Contribution bullets are crisp statements of *what is new + the headline evidence*, not a re-explanation of a mechanism the prose already covered.
    - **Anti-pattern**: ¶3 says "Because the procedure enters only as a soft bias, a wrong recollection falls back to exploration rather than to failure," and then the *Empirical efficiency* bullet appends "because the procedure is a soft bias on a feedback-driven policy, a wrong memory costs only operations, not success" — the same mechanism stated twice.
    - **Fix**: keep the mechanism in the narrative; let the bullet carry only its own headline (here, the efficiency numbers). Cut the restating clause.
    - **Detection**: for each contribution bullet, check whether its explanatory clause paraphrases a sentence already in the Intro prose or the Abstract; if so, delete the clause from the bullet. Generalize: this is the contributions-vs-narrative case of the broader rule that no claim should appear twice in nearby text (sibling to rule 29, one-topic-per-subsection).

38. **Report results statistically; don't recite the table row by row.**
    - Results prose *interprets* the table with ranges, factors, and aggregates; it does not restate each task's number — those live in the table, and re-listing them per task is the most common form of results-section bloat.
    - **Anti-pattern**: "cuts operations by 30.2\% on microwave and 16.2\% on door … and 26.8\% on bottle and 16.2\% on cabinet"; "captures 88\% on microwave, 69\% on door, 81\% on bottle, 77\% on cabinet."
    - **Fix**: "cuts operations by 16--30\% across the four tasks"; "recovers 69--88\% of the oracle reduction." Reserve specific numbers for the single headline figure and for analysis **not** in the table (a distribution shift, one illustrative example, a derived factor / multiple).
    - **Detection**: if a results sentence lists ≥3 task-keyed numbers that also appear in a table column, collapse them to a range or a factor; keep at most one concrete example per mechanism.

39. **Cut what a connective or an earlier passage already supplies.**
    - Three local-redundancy forms of "don't state what the reader already holds":
      - **Inferential bridge** — `A, so B, therefore C` collapses to `A, so C` when `B` is just the inference the connective already carries. Anti-pattern: "…the same value, so either one alone demonstrates the framework. Our experiments therefore use only reset." Fix: "IOM provides the same value in both settings, so our experiments use only the reset setting."
      - **Label glossed in place** — a one-off abstract label immediately renamed by a concrete appositive and never reused is redundant with its gloss; keep the description, drop the label. Anti-pattern: "the same value from `cross-encounter memory`, a first encounter's discovery sparing later exploration." Fix: "…from a first encounter's discovery sparing later exploration." (A *contribution* noun is the opposite case — it earns name+gloss in every section, rule 24.)
      - **Re-gloss of an established concept** — a concept defined earlier (Abstract / Intro / Problem Setup) is referred to plainly later, not re-explained. Anti-pattern: re-appending "a first encounter's discovery sparing later exploration" in a later paragraph when Problem Setup already established the amortization.
    - Generalizes rule 20 (modifier redundancy) and rule 37 (claim redundancy) to inferential and glossing redundancy; the inverse-positive case is rule 24 (contribution nouns DO get name+gloss every section).

40. **State a contrast as a plain antithesis, not a nominalized metaphor.**
    - Don't compress a contrast into a clever nominalization the reader must decode; write both sides directly (a `whereas` / `requires nothing further … additionally requires` antithesis).
    - **Anti-pattern**: "reset isolates this value, whereas persistence …" (the reader must reconstruct "isolates from what?").
    - **Fix**: "reset requires nothing further, whereas persistence additionally requires …".

41. **Open a Related-Work bucket on the work, not on "the Nth line of work".**
    - The `\subsection` header already labels the bucket (rule 15); the first sentence must not re-announce it with scaffolding like `The closest line …`, `A second line …`, `Another line of work …`, `A third direction …`. Name the research area as the grammatical subject and dive into the work.
    - **Anti-pattern**: `The closest line gives a policy a memory of past successes…` / `A second line resolves an object's hidden state…` — `line` is vague (the reader decodes "line of work" before learning the topic) and the ordinal re-narrates the header.
    - **Fix**: `Closest to our setting, a policy is given a memory of past successes…` (keeps the closest-work signal, drops `line`); `A separate body of work resolves an object's hidden state…`. A genuine ordering signal (which bucket is nearest your method) is worth keeping — carry it on the work, not on the word `line`.
    - **Consistency tell**: if some buckets open this way and others already dive in (`Retrieval has also been used for…`, `The store-abstract-retrieve loop is well established…`), the scaffolded ones are the defect — align them to the divers, not the reverse.
    - The **opener** sibling of rule 15 (which governs the bucket **header**): rule 15 keeps the header a distinguishing noun phrase; rule 41 keeps the first sentence from wasting itself re-announcing that header.

42. **A float's page placement is set by its declaration point, not its `\ref` — to fix placement, move only the environment, never the description.**
    - A LaTeX table/figure floats forward from where `\begin{table}`/`\begin{figure}` sits in the source but never before it. When one lands on the wrong page (classically, a setup table deferring onto the references page of a full paper), relocate the *declaration* earlier, to any point after its dependencies are defined (a $\mathcal{K}^\circ$ table must follow the section defining $\mathcal{K}^\circ$). The `\ref` and caption are independent and stay in their semantic home — moving the environment does not require moving them.
    - **Discipline**: when the task is a placement fix, edit only the float environment. Do not move, rewrite, add, or delete the `\ref` sentence or the caption to chase page position; that conflates layout with content and corrupts the prose (sibling to rule 23: a placement request is not licence to edit descriptions).
    - **Detection**: if a change aimed at a float's page position touched any `\ref` sentence or caption, revert those prose edits and keep only the moved environment. This is a table/figure placement convention, distinct from compile-error debugging (out of scope).

---

## When to ask vs. when to default

| Situation | Default | Ask only if |
|---|---|---|
| Venue not stated | CoRL conventions | User is writing a journal paper |
| Tense for Method | Present (system-as-subject) | — |
| Panel notation | `(a)(b)` lowercase | Paper is for Science (then use `(A)(B)`) |
| Caption length | Match figure role table (F1/F2: 3–6 sentences; F5/F7: 2; F3/F4: 1) | — |
| Bold-the-best in tables | Yes, per column | — |
| ↑/↓ arrows in headers | Yes | — |
| `Ours` row label | Last row, bold | User has a specific brand they've already established |
| Statistical aggregation | Mean ± StdErr | User has different convention in their group |
| Section opener for Intro | B1a (capability statement) | User wants a question (B1b) or scenario (B1e) hook |

**Rule**: take defaults silently and announce them in the 3-line summary at delivery time. Ask ONLY when the choice will materially change the structure (e.g., "are you writing for Science Robotics? If yes, the Conclusion becomes a Discussion section").

---

## Failure modes to refuse / redirect

| User asks | Response |
|---|---|
| "Is my technical contribution strong enough?" | "I coach writing, not research direction. For that, you want a domain advisor." |
| "Translate this section from Chinese to English" | "I can edit English writing once translated, but I'm not a translator. Use a translator first; I'll polish after." |
| "Fix my LaTeX compilation error" | "Outside scope — try a LaTeX-focused tool or check the log." |
| "Generate fake numbers for my table" | Refuse. Explain that fabricated results are research misconduct. |
| "Write my contributions list without me telling you what they are" | "I need 3–5 sentences from you about what your paper actually does. I can format and tighten, but I can't invent contributions." |
| "Make my method sound more novel than it is" | "I won't inflate novelty. I can sharpen the wording around what you actually did — share the concrete contribution and I'll frame it precisely." |
| "Write my rebuttal response" | "I'll apply the same playbooks, but first I need: (1) the reviewer comment verbatim, (2) the word/page limit the venue allows, (3) which option you want — concede + revise, push back with evidence, or propose a new experiment." |
| "Invent a baseline name for me / pick which baselines I should compare" | Refuse the invention. Mark `[TBD: baseline name]` in any draft and tell the user: "I won't pick or name baselines — that's research direction. Tell me which ones you ran and I'll frame them." |
| "Write my project-page copy / video script / website blurb" | "Out of scope for this skill — these have different conventions (more marketing, less rigor). I can adapt your Abstract for a project page if you ask, but flag it as a non-paper deliverable." |

---

## Reference index

| File | Covers | Size |
|---|---|---|
| **Operational layer (load on demand per routing table)** | | |
| `references/titles.md` | Title patterns, system-name conventions, colon-split, "X is all you need" templates | 8 KB |
| `references/abstract-intro-playbook.md` | 5-move abstract structure, 4-paragraph intro arc, hook taxonomy, contribution bullets | 14 KB |
| `references/method-relatedwork-playbook.md` | Related Work 3-act narrative, Method system-name commitment, equation sandwich, sub-corpus matching | 18 KB |
| `references/experiments-results-playbook.md` | Question-list opener, baseline framing, ablation pairwise narration, sim-vs-real tagging, hardware paragraph | 22 KB |
| `references/figures-tables-playbook.md` | 8 figure roles (F1–F8), teaser ingredients, table-caption-as-takeaway, panel notation, statistical disclosure | 19 KB |
| `references/teaser-figure-playbook.md` | F1 teaser / graphical abstract deep-dive: naming, 4 visual variants, image composition + conference visual-style standards, caption-as-promise, Intro reference, drawing-prompt artifact + approval gate, draw→review→refine loop, anti-patterns | 10 KB |
| `references/teaser-prompt.template.yaml` | Copy-to-`teaser-prompt.yaml` template: the single reference consolidating variant/layout/caption/style/generation-prompt/output-path/Intro-pointer/review-bar for the teaser | 2 KB |
| `references/image-render-invocation.md` | Renderer plumbing, self-contained: default REST adapter (`tools/images_api_render.py` → `images/generations`) with the Codex `codex-image2` MCP bridge as alternative; endpoint check → render → finalize/verify via `tools/figure_render_helper.py`, output structure, rules | 6 KB |
| `references/drawio-figure-playbook.md` | Vector diagrams (F2 architecture / pipeline / conceptual) in draw.io: PDF export (`--crop --border --page-index`), MathJax (`math=1` + `\(\)`), typography tiers, color-by-role palette, desktop-app pitfalls, design principles, 2px arrow conventions | 7 KB |
| `references/language-phrasebank.md` | Section A–K rhetorical phrasebook: openers, contributions, pivots, hedging, connectors, anti-patterns | 24 KB |
| `references/flow-transitions.md` | 6-move paper arc, section openers, contribution-restatement spiral, pivot family, inter-paragraph connectors | 22 KB |
| `references/closing-appendix-playbook.md` | Conclusion 3-move recap, Limitations admit-and-propose, Appendix TOC, hyperparameter conventions, Author Contributions | 25 KB |
| **Research layer (read only when traceability is needed)** | | |
| `references/research/00-titles.md` | Raw title pattern extraction across 63 papers | 27 KB |
| `references/research/01-abstract-intro.md` | Raw abstract + intro extraction | 41 KB |
| `references/research/02-method-related.md` | Raw method + related-work extraction | 87 KB |
| `references/research/03-experiments-results.md` | Raw experiments + results extraction | 47 KB |
| `references/research/04-figures-tables.md` | Raw figure / table caption extraction | 37 KB |
| `references/research/05-language-phrases.md` | Raw phrase corpus across sections | 102 KB |
| `references/research/06-flow-rhetoric.md` | Raw flow / transition extraction | 76 KB |
| `references/research/07-conclusion-limitations.md` | Raw closing sections extraction | 28 KB |
| `references/research/08-appendix.md` | Raw appendix extraction | 29 KB |

---

## Bundled tools — what they are and how to run them

This skill ships executable helpers under `tools/`. They are invoked by the scenarios above (or on request):

| Tool | Used by | Purpose |
|---|---|---|
| `tools/audit_conventions.sh` | Scenario E Step 2.5 (mandatory convention sweeps) | Recursively follows `\input{}` from `main.tex` and runs the rule 14–22 sweeps; `--strict`, `--list`. Reads per-paper `audit_conventions.conf` (schema: `tools/audit_conventions.example.conf`). |
| `tools/page_audit.sh` | On request / submission prep | Reports CoRL-style page-budget compliance of the built PDF (`--pdf`, `--limit`). |
| `tools/images_api_render.py` | `references/image-render-invocation.md` (teaser draw — **default renderer**) | `generate` an image via an OpenAI-compatible `images/generations` endpoint (`gpt-image-2`); `check` reports the config mode (env / codex / mixed / unavailable) before rendering; `endpoint` prints the resolved URL+auth. |
| `tools/figure_render_helper.py` | `references/image-render-invocation.md` (teaser draw) | Renderer-agnostic `finalize` / `verify` of figure artifacts (+ a Codex-bridge `preflight` for the alternative path). |
| `tools/task_gallery_figure.py` | On request (F4/F5 task gallery) | Build a per-task gallery figure (init + operation screenshots, grouped rows) from a YAML config — `--config` + `--workspace`. Template: `tools/task_gallery.example.yaml`. Needs matplotlib + Pillow + PyYAML. |

### Path resolution (applies to every bundled tool)

**The tools live in the skill's install directory, which is NOT your working directory once the skill is installed** — your CWD is the user's paper (where `main.tex` / `main.pdf` live). A bare `tools/...` path only works when you happen to be running from the skill repo root. So resolve the skill dir first, then call the tool by absolute path. The tool **reads from the skill dir but operates on the paper in your CWD**.

```bash
# Resolve this skill's dir. $CLAUDE_SKILL_DIR is set by Claude Code during a skill
# invocation; fall back to the repo root, else substitute the absolute skill path
# you know from where you read SKILL.md. (Bash tool calls don't share shell state —
# include this line in the SAME block as the tool call, or paste the absolute path.)
SKILL_DIR="${CLAUDE_SKILL_DIR:-$(pwd)}"
[ -f "$SKILL_DIR/tools/audit_conventions.sh" ] || SKILL_DIR="/abs/path/to/embodied-ai-paper-writer"

# Then invoke a tool by absolute path, run from the paper dir:
bash "$SKILL_DIR/tools/audit_conventions.sh" --strict
bash "$SKILL_DIR/tools/page_audit.sh" --pdf main.pdf --limit 8
python3 "$SKILL_DIR/tools/figure_render_helper.py" preflight --workspace "$(pwd)"
```

Every `<skill-dir>/tools/...` or `tools/...` reference elsewhere in this skill means `"$SKILL_DIR/tools/..."` resolved this way. `references/image-render-invocation.md` applies the same convention with its own `$HELPER` shorthand.

---

## Honest boundaries

1. **Sample**: 63 papers, 2022–2026, CoRL / RSS / ICRA / IROS / Science Robotics. NeurIPS / ICML robotics tracks under-represented. CVPR-adjacent robotics under-represented.

2. **Anglophone bias**: corpus is English-language. Patterns may differ for translated submissions or for venues with non-anglophone reviewer pools.

3. **Conventions evolve**: arc + caption norms shift on ~2-year timescales. Patterns extracted up to early 2026. After mid-2027, re-extract.

4. **Writing-craft only**: this skill cannot judge whether a paper is publishable, whether the contribution is strong, or whether the experimental design is sound. It can only judge whether the writing follows the conventions of papers that DID get published.

5. **No translation, no LaTeX debugging, no figure-rendering**: outside scope.

6. **Defaults are calibrated to CoRL**: when the user is writing for ICRA / IROS / Science Robotics, ask once to recalibrate venue-specific conventions (numbering, section names, appendix length).

---

## Created by

> This skill was generated by [Nuwa · Skill造人术](https://github.com/alchaincyf/nuwa-skill).
> Author: [花叔](https://x.com/AlchainHust)
