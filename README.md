# Open Function Call framework

The Open Function Call framework is a Python-based large language model function call framework that allows users to build ai assistant quickly and privide ability similar to OpenAI assistant function call api.
## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/XiaooLei/open-function-call.git
   cd open-function-call

### Usage

1. Import the necessary modules in your script:

```python
from open_function_call import Assistant
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
3. Create instances of necessary classes and run the assistant, demo:

```python
glm = GLMHttpClient() # this could be any llm interface like Llama, Chat-GLM...
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


