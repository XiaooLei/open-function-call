# Open Function Call Assistant

The Open Function Call Assistant is a Python-based tool that allows users to interact with various functions through a conversational interface. This example includes integration with a web browser function.

## Getting Started

### Prerequisites

- Python 3.x
- Dependencies: `glm_client`, `web_brower` (custom module, assumed to be available in your project)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/XiaooLei/open-function-call.git
   cd open-function-call

### Usage

1. Import the necessary modules in your script:

```python
from open_function_call import Assistant
from glm_client import GLMHttpClient
from web_brower import baidu_search
```

2. Define your tool list with functions:
```python
tool_list = [
    {
        "type": "function",
        "function": {
            "name": "browser",
            "description": "search information from the internet",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "the query you need to search",
                    },
                },
                "required": ["query"],
            },
        }
    }
]
```
3. Create instances of necessary classes and run the assistant:

```python
glm = GLMHttpClient()
assistant = Assistant(tool_list=tool_list, llm=glm)

user_input = input(">> ")
while True:
    assistant.human_ask(user_input)
    cur = assistant.run()
    if cur["type"] == "function_call":
        if cur["function_name"] == "browser":
            print("call function..., args:", cur["arguments"])
            arguments = cur["arguments"]
            browser_output = baidu_search(arguments["query"])
            assistant.submit_function_res(browser_output)

    elif cur["type"] == "reply":
        print("AI:", cur["ai_msg"])
        user_input = input(">> ")

```

### Contributing
If you'd like to contribute to this project, please follow the contribution guidelines.


