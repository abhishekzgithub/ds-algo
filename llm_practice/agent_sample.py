from typing import Optional, Type
from pydantic import Field, BaseModel
from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import tool
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain.agents import AgentExecutor
from langchain.llms.openai import OpenAIChat
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain_ollama.llms import OllamaLLM
from langchain_ollama.chat_models import ChatOllama
from langchain.agents import AgentExecutor, create_tool_calling_agent
import pyautogui
import time

model_name="llama-3.2-1b-instruct"
model_name="llama3.1:latest"
#model_name="llama-3-groq-8b-tool-use"
#llm = ChatOpenAI(model=model_name, base_url="http://localhost:1234/v1", api_key="not-needed")
llm = ChatOllama(
    model=model_name,  # Replace with your Ollama model name
    server_url="http://localhost:11434"  # Default Ollama local server URL
)

@tool
def get_code(text:str)->str:
    """Useful for when you need to get the code for a given text."""
    print("Using tool get_code")
    return text

@tool
def open_start_menu():
    """Simulate pressing the Windows key to open the Start menu."""
    pyautogui.press('win')
    time.sleep(1)  # Allow time for the menu to open

@tool
def search_in_start_menu(tool_input):#todo
    """Open the Start menu and type a tool_input."""
    pyautogui.press('win')
    pyautogui.typewrite(tool_input, interval=0.1)
    pyautogui.press('enter')

@tool
def open_file_explorer():
    """Open File Explorer using Windows+E shortcut."""
    pyautogui.hotkey('win', 'e')

@tool
def minimize_all_windows():
    """Minimize all windows using Windows+D shortcut."""
    pyautogui.hotkey('win', 'd')

@tool
def lock_computer():
    """lock the computer using Windows+L shortcut."""
    pyautogui.hotkey('win', 'x')
    time.sleep(1)
    for ele in ["up","up","right","down","enter"]:
        time.sleep(0.2)
        pyautogui.press(ele)
    time.sleep(1)
    pyautogui.press('enter')
    #pyautogui.hotkey()  # This sequence may vary depending on the system settings
    
    # pyautogui.keyDown()
    # time.sleep(0.3)
    # pyautogui.keyUp()
@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    print("Using tool")
    return len(word)

@tool
def lock_windows():
    """ Get the current working directory to check if we're on Windows and lock the windows"""
    import os
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.LockWorkStation()

tools = [lock_windows,get_code,open_file_explorer,minimize_all_windows,search_in_start_menu,open_start_menu,lock_computer,get_word_length]
llm_with_tools = llm.bind_tools(tools)



prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are very powerful assistant, but don't know current events",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are very great python developer.Develop the code based on the input provided and return only the code snippet in text format. Do not send it in markdown format ever.",
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
        

    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)


agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# response=agent_executor.invoke(
#     {"input": "what is the length of characters in the word eudca"})
while True:
    try:
        query = input("Enter your query: ")
        response=agent_executor.invoke(
            {"input": f"{query}"})
        print(response)
    except Exception as exc:
        print(exc)

#agent = create_tool_calling_agent(llm, tools, prompt)

# print(list(agent_executor.invoke(
#     {"input": "what is the length of characters in the word eudca"})))

# query = "What is 10*65?"
# #query="What is the length of elephant"

# reponse=llm_with_tools.invoke(query)

# print("Response\n", reponse)
# print("Reponse tool calls:\n\n",reponse.tool_calls)
