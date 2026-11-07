#!/usr/bin/env python3
"""Stop hook: block a reply that breaks the countable rules of the concise skill."""
import json
import os
import re
import sys

MAX_SENTENCE = 25


def turn_text(data):
    path = data.get("transcript_path")
    if not path or not os.path.exists(path):
        return data.get("last_assistant_message") or ""
    entries = []
    with open(path) as f:
        for line in f:
            try:
                entries.append(json.loads(line))
            except ValueError:
                pass
    start = 0
    for i, e in enumerate(entries):
        if e.get("type") != "user" or e.get("isMeta"):
            continue
        c = (e.get("message") or {}).get("content")
        if isinstance(c, str) or (
            isinstance(c, list) and not any(b.get("type") == "tool_result" for b in c)
        ):
            start = i
    parts = []
    for e in entries[start:]:
        if e.get("type") != "assistant":
            continue
        for b in (e.get("message") or {}).get("content") or []:
            if b.get("type") == "text":
                parts.append(b["text"])
    return "\n\n".join(parts)


def problems(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "CODE", text)
    text = re.sub(r"https?://\S+", "URL", text)
    found = []
    lines = text.splitlines()
    if any(re.match(r"\s*#{1,6}\s", l) for l in lines):
        found.append("It has a heading. Use flat bullets.")
    if re.search(r"\*\*[^*\n]+\*\*|__[^_\n]+__", text):
        found.append("It has bold text. Remove it.")
    if sum(1 for l in lines if re.match(r"\s*\|.*\|\s*$", l)) >= 2:
        found.append("It has a table. Use bullets.")
    long = []
    for l in lines:
        l = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", l)
        for s in re.sub(r"([.!?:;][\"'”’)\]]*)\s+", "\\1\n", l).split("\n"):
            n = len(s.split())
            if n > MAX_SENTENCE:
                long.append(f'{n} words: "{" ".join(s.split()[:8])} ..."')
    if long:
        found.append(f"Sentences over {MAX_SENTENCE} words:\n  " + "\n  ".join(long))
    limit = os.environ.get("CONCISE_MAX_WORDS")
    if limit and len(text.split()) > int(limit):
        found.append(f"The reply has {len(text.split())} words; the limit is {limit}.")
    return found


def main():
    data = json.load(sys.stdin)
    found = problems(turn_text(data))
    if not found:
        return
    if data.get("stop_hook_active"):
        print(json.dumps({"systemMessage": "Concise check still fails: " + " ".join(f.splitlines()[0] for f in found)}))
        return
    print(json.dumps({
        "decision": "block",
        "reason": "Your reply breaks the concise skill. Rewrite the whole reply, then send only the new version.\n- "
        + "\n- ".join(found),
    }))


main()
