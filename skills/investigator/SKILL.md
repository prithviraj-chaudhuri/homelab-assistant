---
name: investigator
description: Investigate and audit homelab infrastructure, delegating analysis to the investigator sub-agent for implementation and improvement insights.
---

# Analyze Skill (Homelab Infrastructure Investigation)

## Purpose

This skill handles requests to investigate, audit, and analyze the homelab infrastructure. It delegates execution to the `investigator` sub-agent when the user asks to inspect how the homelab is implemented, what components exist, or how to improve the current setup.

---

## Trigger Conditions

Activate this skill when the user request involves:

### Homelab investigation intent
- “investigate my homelab”
- “analyze the homelab infrastructure”
- “audit my home lab setup”
- “review my homelab architecture”
- “what is the current infrastructure for my homelab?”

### Infrastructure analysis / implementation discovery
- “what services are running in my homelab?”
- “how is my homelab implemented?”
- “explain the current homelab architecture”
- “find issues in my homelab configuration”
- “how is postgres deployed currently?”
- “what is the current Redis / database stack?”
- “how is the Kubernetes stack implemented?”

### Troubleshooting and improvement analysis
- “how can I improve my homelab stack?”
- “what should I change in my homelab infrastructure?”

---

## Non-Trigger Conditions

Do NOT use this skill when:
- the request is a generic tech definition, not tied to the user’s homelab
- the user asks only for abstract infrastructure concepts without any personal/homelab context
- the user explicitly wants research or community trends unrelated to the local infrastructure
- the task is limited to a single code snippet review outside the homelab context

---

## Inputs

- **subject** (string): the homelab infrastructure or deployment to inspect
- **scope** (optional string): specific area such as networking, services, containers, virtualization, backup, monitoring, or security
- **goal** (optional string): desired outcome such as audit, optimization, documentation, or explanation

---

## Execution Flow

### 1. Confirm intent
Detect if the user wants a local infrastructure investigation or an analysis of the existing homelab environment.

### 2. Route to `investigator`
When triggered, invoke the `investigator` agent to perform the analysis, using available tools and state to discover the current infrastructure and its implementation details.

### 3. Synthesize findings
Summarize the infrastructure, implementation patterns, and any recommended next steps.

---

## Output Format

### 1. Infrastructure Summary
Describe the detected homelab components and architecture.

### 2. Implementation Details
Explain how services are implemented and connected.

### 3. Observations and Risks
Note any obvious issues, gaps, or security concerns.

### 4. Recommendations
Offer actionable next steps for improvement, optimization, or clarification.

---

## Best Practices

- Use the `investigator` agent for actual homelab inspection and tool-driven analysis.
- Keep responses grounded in detected infrastructure and available context.
- Avoid speculative generalizations when the request is clearly about the user’s own setup.
- Ask a clarifying question if the homelab scope is ambiguous or too broad.

---

## Example Triggers

- “Investigate my homelab infrastructure and tell me what is running.”
- “Analyze the home server architecture and recommend improvements.”
- “Audit the current infrastructure for my homelab deployment.”
- “What is implemented in my homelab and how is it organized?”
- “How is postgres deployed currently?”
- “How is my database stack implemented?”
- “What is the current Kubernetes/service stack in my homelab?”

---

## Failure Handling

If the infrastructure is unclear or insufficient data is available:
- ask for the specific homelab context or files to inspect
- fallback to explaining what information is needed for a proper audit
- do not pretend to have performed a local investigation without evidence
