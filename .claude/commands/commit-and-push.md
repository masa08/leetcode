# Commit and Push

Commit changes to the LeetCode solutions repo and push to remote.

## Context

Current git status:

```bash
$(git status --short)
```

Current branch:

```bash
$(git branch --show-current)
```

Recent commits (note the commit style):

```bash
$(git log --oneline -5)
```

## Instructions

This repo follows a simple workflow: solve a problem, commit, push to main. No PRs.

1. Review the changes above. Identify which solution files (`solutions/<number>_*.py`) were added or modified.

2. **Group commits by problem number.** Each LeetCode problem gets its own commit, even if multiple files (e.g., the solution + a model/util update) are touched together. The default rule: one commit per `solutions/<number>_*.py` file plus any closely related files (e.g., updates to `model/`, `utils/`, `explore/` that support that solution).

3. **Commit message style** — match the existing pattern in `git log`:
   - New problem: `add <number>` (e.g., `add 704`)
   - Modification to existing solution: `update <number>` (e.g., `update 207`)
   - Repo-wide changes (model, utils, explore, CLAUDE.md, etc.): use a short descriptive message in lowercase (e.g., `add DoublyListNode to model`, `refactor list_node helpers`)
   - One-line, lowercase, no period.

4. Stage only the files belonging to each logical commit (avoid `git add -A` for grouped commits).

5. Push to `origin main` (the working branch). Do NOT create a PR — this repo commits directly to main.

6. After pushing, run `git log --oneline -5` and report the new commits to the user.
