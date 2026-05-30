from deepagents import CompiledSubAgent
from langgraph.graph import StateGraph, END
from langgraph.graph import MessagesState
import agents.researcher.nodes as nodes


def should_continue(state: MessagesState):
    last_message = state["messages"][-1]
    if getattr(last_message, "tool_calls", None):
        return nodes.TOOL_NODE
    return END

graph = StateGraph(MessagesState)
graph.add_node(nodes.PLAN_NODE, nodes.call_llm_node)
graph.add_node(nodes.TOOL_NODE, nodes.tool_node)

graph.set_entry_point(nodes.PLAN_NODE)
graph.add_conditional_edges(
    nodes.PLAN_NODE,
    should_continue,
    {
        nodes.TOOL_NODE: nodes.TOOL_NODE,
        END: END,
    },
)
graph.add_edge(nodes.TOOL_NODE, nodes.PLAN_NODE)

compiled_graph = graph.compile()

research_agent = CompiledSubAgent(
    name="research-agent",
    description="Research agent to know what the homelab community is working on running on their own infrastructure. This is a ReAct agent with tools to perform research. You have access to tools to search different data sources. Always think step by step and use your tools when you need to perform specific tasks.",
    runnable=compiled_graph
)