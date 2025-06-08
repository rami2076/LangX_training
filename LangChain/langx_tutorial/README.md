# Tutorial for LangChain

## なにをするか？

- どこにチュートリアルがあるのか？
    - https://python.langchain.com/docs/introduction/
- どんなコマンドをすればいいのか？

# First Step

https://python.langchain.com/docs/introduction/

以下が公式が提供した手順書

```bash
pip install -qU "langchain[anthropic]"
```

以下の方がいい気がする

```bash
cd LangChain
brew update && brew install uv
uv self version
uv init langx_tutorial
cd langx_tutorial
# https://pypi.org/project/langchain/0.3.25/
# 現在の最新は0.3.25
uv add --verbose "langchain[anthropic]"
```
