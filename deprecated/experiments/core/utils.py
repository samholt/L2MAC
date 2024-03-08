from io import StringIO
import sys
from typing import Dict, Optional

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents.tools import Tool
from langchain.llms import OpenAI


class PythonREPL:
    """Simulates a standalone Python REPL."""

    def __init__(self):
        pass        

    def run(self, command: str) -> str:
        """Run command and returns anything printed."""
        # sys.stderr.write("EXECUTING PYTHON CODE:\n---\n" + command + "\n---\n")
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        try:
            exec(command, globals())
            sys.stdout = old_stdout
            output = mystdout.getvalue()
        except Exception as e:
            sys.stdout = old_stdout
            output = str(e)
        # sys.stderr.write("PYTHON OUTPUT: \"" + output + "\"\n")
        return output
      
llm = OpenAI(temperature=0.0)
python_repl = Tool(
        "Python REPL",
        PythonREPL().run,
        """A Python shell. Use this to execute python commands. Input should be a valid python command.
        If you expect output it should be printed out.""",
    )
tools = [python_repl]
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
agent.run("What is the 10th fibonacci number?")