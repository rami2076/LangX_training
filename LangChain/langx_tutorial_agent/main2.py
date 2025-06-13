import os
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage

# 環境変数から API キーを読み込む
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY is not set in the environment.")

# Claude モデル（例: claude-3-opus）を使用
llm = ChatAnthropic(model="claude-3-7-sonnet-latest", api_key=api_key)

while True:
    prompt = input("> ")
    if prompt == "":
        break
    response = llm.invoke([HumanMessage(content=prompt)])
    print(response.content)