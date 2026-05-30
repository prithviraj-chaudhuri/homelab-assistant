# Research Skill (Improved Spec)

## Purpose

This skill handles **topic-driven research requests** that require gathering external or community-based information rather than answering from static knowledge alone. It delegates execution to a `research-agent`.

---

## Trigger Conditions

Activate this skill when the user request involves:

### Explicit research intent
- “research…”
- “investigate…”
- “find information about…”
- “what’s happening in…”
- “what are people saying about…”

### Community / trend exploration
- Emerging tools, workflows, or technologies
- “what’s the community doing with…”
- “best practices people use for…”

### Reddit / forum queries
- “latest posts on r/…”
- “what’s trending on r/…”
- “summarize discussions in r/…”

### Improvement / optimization queries
- “how can I improve my setup…”
- “what should I change in my stack…”
- “what are modern approaches to…”

---

## Non-Trigger Conditions

Do NOT use this skill when:
- The user asks a general factual question (no research intent)
- The request is purely definitional (“what is X?”)
- The answer can be fully provided from stable internal knowledge
- The user request is vague and unrelated to a specific topic (ask a clarifying question instead)

---

## Inputs

- **topic** (string): the main subject of research
- **source context** (optional):
  - subreddit name (e.g., `r/homelab`)
  - technology domain (e.g., “self-hosting”, “Kubernetes”, “AI agents”)
  - constraints (e.g., “latest tools”, “beginner-friendly”, “2026 trends”)

---

## Execution Flow

### 1. Extract research intent
Identify:
- primary topic
- desired depth (overview vs. deep dive)
- source type (Reddit, general community, mixed)

### 2. Choose data source

- If general tech/community research → use `research-agent`
- If specific data source is mentioned pass it to the research-agent (e.g., subreddit name)

---

### 3. Synthesize findings

The response should:
- Summarize key themes
- Highlight patterns or consensus
- Include relevant examples or references (when available)
- Clearly separate facts vs. community opinion
- Provide actionable insights or recommendations when relevant

---

## Output Format

### 1. Summary of Findings
### 2. Key Themes / Insights
### 3. Community Sentiment (if applicable)
### 4. Actionable Recommendations
### 5. Optional: Gaps or Uncertainty

---

## Best Practices

- Prefer external/community data over assumptions when available
- Keep results tightly focused on the requested topic
- Avoid overloading with raw data dumps
- Clearly distinguish:
  - observed patterns
  - anecdotal community opinions
- If the request is too broad, ask a targeted clarifying question before running research

---

## Example Triggers

### Reddit-specific
- “What are the latest posts on r/homelab?”
- “Summarize discussions in r/selfhosted this week”

### General research
- “Research modern self-hosted VPN setups”
- “What are people using instead of Docker Compose in 2026?”

### Improvement-focused
- “How can I improve my home server stack?”
- “What should I upgrade in a Kubernetes homelab?”

---

## Failure Handling

If:
- topic is unclear → ask a clarification question
- no relevant data is found → state that and provide best-effort general insight
- subreddit is invalid or empty → fall back to general community research via `research-agent`