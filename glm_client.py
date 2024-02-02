import json
import requests
import time
import jwt
api_key = ""

tools = [
        {
            "type": "function",
            "function": {
                "name": "query_train_info",
                "description": "根据用户提供的信息，查询对应的车次",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "departure": {
                            "type": "string",
                            "description": "出发城市或车站",
                        },
                        "destination": {
                            "type": "string",
                            "description": "目的地城市或车站",
                        },
                        "date": {
                            "type": "string",
                            "description": "要查询的车次日期",
                        },
                    },
                    "required": ["departure", "destination", "date"],
                },
            },
        },
        {
            "type": "function",
            "function":{
                "name": "book_ticket",
                "description": "订阅对应的车次的车票",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "train_id": {
                            "type": "string",
                            "description": "车次的名称",
                        },
                    },
                    "required": ["train_id"],
                },
            }
        }
    ]

def generate_token(apikey: str, exp_seconds: int):
    try:
        id, secret = apikey.split(".")
    except Exception as e:
        raise Exception("invalid apikey", e)

    payload = {
        "api_key": id,
        "exp": int(round(time.time() * 1000)) + exp_seconds * 1000,
        "timestamp": int(round(time.time() * 1000)),
    }

    return jwt.encode(
        payload,
        secret,
        algorithm="HS256",
        headers={"alg": "HS256", "sign_type": "SIGN"},
    )

class GLMHttpClient:
    token: str = ""
    tokenExp: int = 0

    def __init__(self, token: str = api_key):
        return
    def Call(self, model, messages, tools=None):
        url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
        params = {}
        params["model"] = model
        params["messages"] = messages
        params["tools"] = tools

        # print("call params:", params)
        ts = int(time.time())
        if ts > self.tokenExp:
            self.token = generate_token(apikey=api_key, exp_seconds=3600)
            self.tokenExp = ts + 3600

        headers = {
            "Content-Type": "application/json",
            "Authorization": generate_token(apikey=api_key, exp_seconds=10000)
        }
        data_json = json.dumps(params)
        response = requests.post(url=url, headers=headers, data=data_json)
        return json.loads(response.content)

    def predict(self, input: str) -> str:
        url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
        params = {}
        params["model"] = "glm-4"
        params["messages"] = [
            {
                "role": "user",
                "content": input
            }
        ]
        # print("call params:", params)
        ts = int(time.time())
        if ts > self.tokenExp:
            self.token = generate_token(apikey=api_key, exp_seconds=3600)
            self.tokenExp = ts + 3600

        headers = {
            "Content-Type": "application/json",
            "Authorization": generate_token(apikey=api_key, exp_seconds=10000)
        }
        data_json = json.dumps(params)
        response = requests.post(url=url, headers=headers, data=data_json)
        resp_dict = json.loads(response.content)
        msg = resp_dict["choices"][0]["message"]
        return msg["content"]




if __name__ == "__main__":
    client = GLMHttpClient()
    print(client.predict("你好"))