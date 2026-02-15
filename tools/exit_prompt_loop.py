from google.adk.tools.tool_context import ToolContext
def exit_prompt_loop(tool_context: ToolContext):
    """Call this function ONLY when the prompt critic agent indicates no further changes are needed, signaling the iterative process should end."""
    print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
    tool_context.actions.escalate = True
    tool_context.actions.skip_summarization = True
    # Return empty dict as tools should typically return JSON-serializable output
    return {}