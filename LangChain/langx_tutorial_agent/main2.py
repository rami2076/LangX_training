import os
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, AIMessage

# APIキー取得
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY is not set in the environment.")

llm = ChatAnthropic(model="claude-3-7-sonnet-latest", api_key=api_key)

# 会話履歴
messages = []

while True:
    prompt = input("> ")
    if prompt == "":
        break

    messages.append(HumanMessage(content=prompt))
    response = llm.invoke(messages)
    print(response.content)

    # Claudeの返答を履歴に追加
    messages.append(AIMessage(content=response.content))
