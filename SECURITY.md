# Security Policy

## Scope

This repository contains documentation and prompt content (an agent skill — SKILL.md + reference playbooks). It does not ship executable code, network services, or compiled binaries. The realistic security surface is small but not zero — for example, malicious patterns added to the skill could mislead authors, and corpus content could plagiarize without attribution.

## Supported versions

The `main` branch is the only supported version. Patches are applied to `main` and tagged into the next release.

## Reporting a vulnerability or concern

Please report the following types of issues **privately**, not via a public GitHub issue:

- A prompt-injection pattern embedded in the skill that causes Claude to do something unsafe.
- Unauthorized reproduction of copyrighted prose from a source paper.
- Personal data accidentally included in any corpus file.
- Any other concern where public disclosure would amplify harm before a fix lands.

**How to report**: Open a [Security Advisory](https://github.com/OpenGHz/embodied-ai-paper-writer/security/advisories/new) in this repository. If you cannot use Security Advisories, open a confidential issue and request a private channel.

We aim to acknowledge within 5 working days and to publish a fix or mitigation within 30 days for confirmed issues.

## What is **not** in scope

- Generic concerns that LLMs may produce inaccurate writing advice (this is true of all LLM-based tools and is addressed in the skill's honest-boundaries section).
- Subjective disagreement with a rule (open a regular [Bug Report](.github/ISSUE_TEMPLATE/bug.yml) issue instead).
- General Claude / Anthropic API security questions (report to Anthropic directly).
