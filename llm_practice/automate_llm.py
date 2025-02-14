#from langchain_community.chat_models import ChatOllama
from langchain_ollama.llms import OllamaLLM
#from langchain_ollama.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage
#from langchain_core.prompts import ChatPromptTemplate
from langchain.llms import OpenAI
model_name="codellama:7b"
model_name="llama-3.2-1b-instruct"
# Step 1: Set up Ollama client
# ollama_client = ChatOllama(
#     model="llama3.1:latest",  # Replace with your Ollama model name
#     server_url="http://localhost:11434"  # Default Ollama local server URL
# )
#ollama_client = OllamaLLM(model=model_name,base_url="http://localhost:11434")
ollama_client=OpenAI(model=model_name,base_url="http://localhost:1234/v1", api_key="not-needed")
# Step 2: Define memory for the conversation
memory = ConversationBufferMemory(return_messages=True)

# Step 3: Set up the conversational chain
conversation = ConversationChain(
    llm=ollama_client,
    memory=memory
)

import subprocess
script_path=r"C:\Users\abhi3\Documents\work\ds-algo\execute.py"
# Function to execute a Python script within another Python program
def execute_python_script():
    # Use the 'python' command to execute the Python script
    subprocess.run(['python', script_path])

# Call the function to execute a Python script

# Step 4: Chat with the agent
print("Welcome to LangChain-Ollama Chat!")
system_prompt="""You are brilliant python developer.
Give the code snippet without enclosing it in triple backticks or markdown-specific syntax.Only the code in text format.No explanantion.
Here is a simple code snippet:
import pyautogui
import keyboard
import time

def open_start_menu():
    "Simulate pressing the Windows key to open the Start menu."
    pyautogui.press('win')
    time.sleep(1)  # Allow time for the menu to open

def search_in_start_menu(query):
    "Open the Start menu and type a search query."
    open_start_menu()
    pyautogui.typewrite(query, interval=0.1)
    pyautogui.press('enter')

def open_file_explorer():
    "Open File Explorer using Windows+E shortcut."
    pyautogui.hotkey('win', 'e')

def minimize_all_windows():
    "Minimize all windows using Windows+D shortcut."
    pyautogui.hotkey('win', 'd')

def lock_computer():
    "Lock the computer using Windows+L shortcut."
    pyautogui.hotkey('win', 'l')

Here is the instruction:"""

#Provide the response in the form of code snippet, in plain text,in structured format, without markdown formatting.
#I want you to only write me a python script and avoid sending any EXTRA information.Just the code.

while True:
    user_input = input(": ")
    user_input=system_prompt + user_input
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = conversation.invoke(input=user_input)
    rs=response['response']
    print(rs)
    with open(f"{script_path}", "w") as file:
        file.write(rs)
    execute_python_script()
    print(f"Ollama: {response['response']}")
