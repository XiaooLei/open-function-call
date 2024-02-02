import json
from prompt import prompt_template

class Assistant:
    def __init__(self, tool_list, llm):
        self.tool_list = tool_list
        self.messages = []
        self.llm = llm

    def human_ask(self, input):
        self.messages.append(f"human ask:{input}")
    def run(self):
        output = self.llm.predict(prompt_template.format(tool_list=self.tool_list, history=self.messages))
        output = output.strip("```")
        output = output.strip("json")
        # print("output:", output)
        output_dict = json.loads(output)
        if not "type" in output_dict:
            return "internal error"
        if output_dict["type"] == "reply":
            self.messages.append(f"ai reply: {output_dict['ai_msg']}")
        elif output_dict["type"] == "function_call":
            self.messages.append(f"function call, function_name[{output_dict}], arguments:{output_dict['arguments']}")
        return json.loads(output)

    def submit_function_res(self, tool_res):
        self.messages.append(f"function return:{tool_res}")


