from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    msg: str

def echo(state: State) -> dict:
    # minimal node that just echoes the input
    return {"msg": state["msg"]}

def build():
    g = StateGraph(State)
    g.add_node("echo", echo)
    g.set_entry_point("echo")
    g.add_edge("echo", END)
    return g.compile()

# The symbol named here must match the one in langgraph.json (":graph")
graph = build()
