# Agents

A library of expert personas for Claude Code sessions: a design critic, a database expert, an API
designer, a microservices architect, or something much narrower. Each persona is a subagent that
you call in a session when you need that expertise.

A persona is only as good as what it knows. So each one rests on its own research, written down
here with its sources, and on a memory of what it learned while working.

## Personas

| Persona | What it does | Call it with |
|---|---|---|
| Loupe | Design critic for websites and apps: reviews, UX questions, design directions | `@agent-agents:loupe` |
| Vellum | Designer for websites and apps: several design directions as HTML prototypes | `@agent-agents:vellum` |

## Skills

| Skill | What it does | Call it with |
|---|---|---|
| think-first | Understand the person and the problem before acting, scaled to the size of the work | Loads by itself, or `/agents:think-first` |
| simple-english | Write or check technical text with ASD-STE100 Simplified Technical English | Loads by itself, or `/agents:simple-english` |
| concise | Rewrite each reply for the most information in the fewest words | A hook adds it to every prompt, or `/agents:concise` |
| design | Design a screen: the user first, versions, mocks of the real app, a checklist, a review | Loads by itself, or `/agents:design` |

## Install

This repo is a Claude Code plugin and its own marketplace. Add the marketplace from GitHub or
from a local clone, then install the plugin:

```
claude plugin marketplace add awalvie/agents
claude plugin install agents@awalvie-agents
```

Both installs copy the plugin into Claude Code's plugin cache. Claude Code uses that copy, not
your clone. After you change the repo, update the plugin and restart Claude Code:

```
claude plugin update agents@awalvie-agents
```

A general memory that a persona writes goes into the cached copy. After an update, Claude Code
uses a new copy, and the memory stays behind in the old one. To keep a memory, copy it into
`personas/<persona>/memory/` in the repo.

## Layout

```
.claude-plugin/        plugin and marketplace manifests
agents/<persona>.md    the persona: who it is, how it works, what it reads
skills/<skill>/        a skill: SKILL.md and anything it needs
hooks/hooks.json       hooks that run in every session with the plugin
personas/<persona>/
  memory/              general lessons, true in any project
  research/
    BRIEF.md           what the research set out to learn, and how
    notes/             the researchers' notes and sources, one pair per area
    synthesis/         the knowledge base, one folder per version (v1, v2, ...)
    prompts/           the prompts that produced the research
```

## Memory

A persona keeps two kinds of memory:

- General lessons, true for any product, live in `personas/<persona>/memory/` here (see Install).
- Lessons about one project live in that project, in `.claude/agent-memory/<persona>/`, so this
  repo stays general.

Ask for a "blind" review to run a persona without either memory.

## How a persona is built

1. Write a brief: what the persona must know, which sources count, and what to be skeptical of.
2. Research it with several agents in parallel, one area each. Each starts with no context beyond
   the brief, so no project or earlier conclusion biases it.
3. Synthesise the notes into a short core that the persona reads every time, plus topic files it
   reads when a task needs them.
4. Have a skeptic check the synthesis against its sources and cut weak claims.
5. Write the agent file on top of the synthesis, and review it with a second agent.

## Not in git

Screenshots of third-party pages taken during research (`*-shots/`) stay local.
