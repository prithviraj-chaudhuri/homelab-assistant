---
name: enhance
description: Handle requests to enhance or optimize the homelab setup by discovering current implementation, researching new service ideas from r/homelab and r/selfhosted, filtering suggestions to exclude already-running services, and providing step-by-step implementation guidance.
---

# Enhance Skill (Homelab Improvement)

## Purpose

This skill is responsible for recommending and implementing enhancements to the current homelab setup. It should:
- gather fresh ideas from the homelab and self-hosting community,
- present only new, no-hardware-required service options,
- ask the user to choose one option,
- discover only the infrastructure details needed to implement it,
- and deliver a repository layout with concrete file modifications, scripts, playbook roles, config files, and `docker-compose` definitions needed to realize the enhancement.

## Trigger Conditions

Activate this skill when the user asks to enhance, improve, expand, or add features to the current homelab setup.

### Typical triggers
- “enhance my homelab”
- “add a new service to my homelab”
- “improve the current homelab setup”
- “what can I add to my home lab without new hardware?”
- “suggest self-hosted services I can run with my existing homelab”

## Non-Trigger Conditions

Do NOT use this skill when:
- the user asks only for general technology definitions or comparisons,
- the request is about abstract design without a homelab enhancement goal,
- the user explicitly asks for hardware upgrades,
- the user only needs infrastructure auditing without adding a feature.

## Inputs

- **goal** (string): enhance the current homelab with a new service or feature.
- **constraint** (string): no new hardware required.
- **sources** (optional string): r/homelab and r/selfhosted community posts.

## Execution Flow

### 1. Confirm enhancement intent

Verify that the user wants a new homelab service or feature added, and that no hardware requirement is allowed.

### 2. Discover current homelab implementation

Invoke the `discovery` sub-agent to identify:
- all currently running services and applications,
- the container/orchestration stack in use,
- storage solutions and networking setup,
- any relevant monitoring, DNS, or middleware components.

Store this baseline for comparison against suggestions later.

### 3. Research community trends

Invoke the `research-agent` to read new posts from `r/homelab` and `r/selfhosted`.
- Identify only new services or tools.
- Filter out anything that requires additional hardware.
- Focus on services that can run on existing infrastructure (containers, VMs, or software-only stacks).

### 4. Filter suggestions against current implementation

Cross-reference all discovered services with the research findings.
- Exclude any service or tool already running in the current homelab.
- Remove duplicates or redundant suggestions.
- Keep only genuinely new enhancement ideas.

### 5. Present filtered options to the user

Offer a few clearly separated enhancement options, each with:
- a short description,
- why it fits the current homelab,
- why it works without new hardware,
- why it is not already deployed.

Ask the user to choose one option before proceeding.

### 6. Discover required implementation details

After the user selects an option, call the `discovery` sub-agent again if needed.
- Pull only the essential infrastructure information required to implement the selected enhancement.
- Avoid redundant broad discovery if step 2 provided sufficient detail.
- Target integration points with the current container/orchestration stack, storage, network, DNS, and any related service dependencies.

### 7. Provide implementation instructions

Deliver a step-by-step plan that:
- fits the existing homelab framework,
- references the discovered current setup,
- includes configuration and deployment guidance,
- highlights any follow-up validation or testing steps.

## Output Format

### Phase 1: Current infrastructure discovery
- Summary of all currently running services and infrastructure.
- Container/orchestration stack details.
- Storage, networking, and DNS configuration.

### Phase 2: Research and filtered options
- Summary of latest relevant posts or trends from the community.
- 2–4 candidate enhancements that are NOT already implemented.
- Clear statement of why each option is new and fits the homelab.
- A clear ask for which option the user wants to implement.

### Phase 3: Discovery summary (if needed)
- Required current infrastructure details for the chosen enhancement.
- Any assumptions or missing information.

### Phase 4: Repository layout and artifacts
- A repo-level directory structure for the enhancement.
- Specific files to add or modify, including scripts, playbook roles, config files, and Docker Compose files.
- Full contents for each recommended artifact.
- Clear labels for where new files belong in the current project.

### Phase 5: Implementation plan
- Use `git` commands to create a new branch, stage changes, and push to the target repository `https://github.com/prithviraj-chaudhuri/home-lab`.
- Create a new branch named `enhance/<feature-name>` for the enhancement.
- Create a Pull Request with a descriptive title and body explaining the enhancement and changes made.
- Provice the link to the created Pull Request for user review.

## Best Practices

- Use the `discovery` sub-agent first to establish a baseline of current services and infrastructure.
- Keep recommendations limited to new, no-hardware services.
- Filter all research suggestions against the current implementation before presenting to the user.
- Use the `research-agent` only for community trend discovery.
- Use the `discovery` sub-agent for infrastructure baseline and implementation-specific details.
- Ask the user to choose before consuming additional discovery or implementation effort.
- Align instructions with the user’s current homelab framework and environment.
- Return actionable repo layout output, not only prose: file paths, exact file contents, and the commands needed to create or modify them.
- If infrastructure details are incomplete, ask follow-up questions rather than guessing.

## Example Triggers

- “I want to enhance the current homelab setup.”
- “Give me new no-hardware services to add to my homelab.”
- “Read recent r/homelab posts and suggest improvements.”
- “What can I self-host without buying more hardware?”
- “Help me add a new service using my existing homelab.”

## Failure Handling

If discovery of current infrastructure fails or is incomplete:
- ask the user to share their homelab configuration or deployment details,
- proceed with available information and note assumptions clearly.

If the agent cannot obtain fresh subreddit information:
- explain the limitation,
- provide best-effort service ideas that still meet the no-hardware requirement and are not already deployed.

If infrastructure details for the selected enhancement are missing:
- ask for the specific files, runtime environment, or homelab components needed to complete implementation,
- avoid overcommitting to a precise step-by-step plan without validation.