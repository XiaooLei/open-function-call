
from open_function_call import Assistant

from glm_client import GLMHttpClient
from web_brower import baidu_search

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

if __name__ == "__main__":
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
