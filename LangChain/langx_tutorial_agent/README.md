# LangChainを使ったAgentの作り方のチュートリアル

> チュートリアルでは、検索エンジンと対話できるエージェントを構築します。  
> このエージェントに質問したり、検索ツールを呼び出す様子を見たり、会話をしたりすることができます。

とのこと

# Execution

## chatgptとの相談

https://chatgpt.com/share/68454203-99bc-8007-9e97-69f5e99bbfee

## REF

https://python.langchain.com/docs/tutorials/agents/

## 時系列実行

Step1で行った時と同じようにLangChainをinstallする

```bash
cd LangChain
brew update && brew install uv
uv self version
uv init langx_tutorial_agent
cd langx_tutorial_agent
# https://pypi.org/project/langchain/0.3.25/
# 現在の最新は0.3.25
uv add -q "langchain[anthropic]"
# 間違えて入れたので以下を実行
uv remove "langchain[anthropic]"
uv add langchain-community \
  langgraph \
  langchain-anthropic \
  tavily-python \
  langgraph-checkpoint-sqlite
# 実行  
uv run main.py
# エラー発生
Value error, Did not find tavily_api_key, please add an environment variable `TAVILY_API_KEY` which contains it, or pass `tavily_api_key` as a named parameter. [type=value_error, input_value={}, input_type=dict]
# tavilyのAPIキーが必要と記載がある．持ってないので取りにいく
# [memo]tavilyは登録したら簡単にAPIキーを取得できた
# 実行  
uv run main.py
# エラー発生
anthropic.NotFoundError: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'model: claude-3-sonnet-20240229'}}
# モデルが存在しないというエラー．勘弁してくれ．
# 以下のページに存在するモデル一覧がある．参考にしてclaude-3-sonnet-20240229をclaude-3-5-sonnet-latestに変更する
# https://docs.anthropic.com/en/docs/about-claude/models/overview
# 実行
uv run main.py
# エラー発生
anthropic.APIConnectionError: Connection error.
# tavilyの検索回数の問題でした
#ここから次回やる
```
