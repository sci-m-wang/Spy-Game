# Spy-Game
利用大语言模型进行卧底游戏，包括谁是卧底及衍生的发现AI卧底游戏等。

## 模型部署

本项目以书生·浦语开源的InternLM2.5-chat-7b为例，利用LMDeploy将其部署为OpenAI格式的接口，可以迁移为OpenAI的GPT-3.5-turbo、GPT-4o等模型，也可以部署其他开源模型。

```bash
bash run_internlm2.5.sh
```

## 运行发现AI卧底游戏

```bash
python -m streamlit run find_the_spy.py
```



