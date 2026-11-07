# Agents

Skills for Claude Code sessions.

| Skill | What it does | Call it with |
|---|---|---|
| think-first | Understand the person and the problem before acting, scaled to the size of the work | Loads by itself, or `/agents:think-first` |
| simple-english | Write or check technical text with ASD-STE100 Simplified Technical English | Loads by itself, or `/agents:simple-english` |
| concise | Rewrite each reply for the most information in the fewest words | A hook adds it to every prompt, or `/agents:concise` |
| design | Design a screen: the user first, versions, mocks of the real app, a checklist, a review | Loads by itself, or `/agents:design` |

## Install

This repo is a Claude Code plugin and its own marketplace:

```
claude plugin marketplace add awalvie/agents
claude plugin install agents@awalvie-agents
```

Claude Code runs a copy in its plugin cache, not your clone. After you change the repo, update the plugin and restart Claude Code:

```
claude plugin update agents@awalvie-agents
```

## Layout

```
.claude-plugin/    plugin and marketplace manifests
skills/<skill>/    a skill: SKILL.md and anything it needs
hooks/hooks.json   hooks that run in every session with the plugin
```
