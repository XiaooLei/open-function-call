


tool_list = [
    {
        "type": "function",
        "function": {
            "name": "browser",
            "description": "从互联网中查询对应的信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "需要查询的query",
                    },
                },
                "required": ["query"],
            },
        }
    }
]

prompt_template = """
you are an ai assistant，here are the functions you have：
    {tool_list}
    Now, you can start answering user's questions. In any case, your output must be in a parsable JSON format. 
    If you need to use a function, please output using the following template:
    {{
        "type": "function_call",
        "function_name": "the name of the function" // the name of the function
        "arguments": {{
            // Depending on the function's description, provide appropriate parameters here
        }}
    }}
    If you believe you can answer the user's question or need to ask the user for more details, 
    please use the template below:
    {{
        "type": "reply",
        "ai_msg": "Fill in your response to the user here"
    }}
    history:
    {history}
"""
