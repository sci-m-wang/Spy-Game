import streamlit as st
from random import choices

state = st.session_state

# title
st.title("谁是卧底😎")
st.caption("人与AI的“谁是卧底”游戏平台，由东北大学数据挖掘实验室、书生·浦语、LangGPT开源社区等提供支持。")

# define the avatar dict for the players
avatar_dict = {
    "host": "🐼",
    "P1": "🚀",
    "P2": "🚄",
    "P3": "🚁",
    "P4": "🚂",
    "P5": "🚢",
    "P6": "🚤",
    "P7": "🚙",
    "P8": "🚠",
    "P9": "🚲",
    "P10": "🚜",
    "A1": "♈",
    "A2": "♉",
    "A3": "♊",
    "A4": "♋",
    "A5": "♌",
    "A6": "♍",
    "A7": "♎",
    "A8": "♏",
    "A9": "♐",
    "A10": "♑"
}

# define the state of the game and save some data
if "messages" not in state:
    state.messages = []
    pass
if "players" not in state:
    state.players = [{"id":"host", "dignity":"system", "is_live":True}]
    pass

with st.sidebar:
    st.write("游戏设置")
    with st.form(key="game_setting"):
        spy_word = st.text_input("卧底关键词", "黄桃")
        civilian_word = st.text_input("平民关键词", "黄瓜")
        total_num = st.number_input("总人数", 5, 10, 5)
        spy_num = st.number_input("卧底人数", 1, total_num//3, 1)
        ai_num = st.number_input("AI人数", 1, total_num, 4)
        
        submitted = st.form_submit_button("保存设置")
        if submitted:
            st.success("游戏设置保存成功")
            if "settings" not in state:
                state.settings = {}
                pass
            state.settings["spy_word"] = spy_word
            state.settings["civilian_word"] = civilian_word
            state.settings["total_num"] = total_num
            state.settings["spy_num"] = spy_num
            state.settings["ai_num"] = ai_num
            pass
    # voting area
    message_container = st.sidebar.container()
    with message_container:
        player_id = st.selectbox("选择你的身份", [a["id"] for a in state.players])
        vote_id = st.selectbox("投票", [a["id"] for a in state.players].remove(player_id))
        if st.button("投票"):
            state.messages.append({"id":"host", "message":f"玩家{player_id}投票给玩家{vote_id}"})
        pass

## initialization the players
spy_id = choices(range(1, state.settings["total_num"]+1), k=state.settings["spy_num"])
if len(state.players) == 1 and "settings" in state:
    for i in range(state.settings["total_num"]):
        if i < state.settings["ai_num"]:
            if i+1 in spy_id:
                state.players.append({"id":f"A{i+1}", "dignity":"spy", "is_live":True})
            else:
                state.players.append({"id":f"A{i+1}", "dignity":"civilian", "is_live":True})
                pass
            pass
        else:
            if i+1 in spy_id:
                state.players.append({"id":f"P{i+1-state.settings["ai_num"]}", "dignity":"spy", "is_live":True})
            else:
                state.players.append({"id":f"P{i+1-state.settings["ai_num"]}", "dignity":"civilian", "is_live":True})
                pass
            pass
        pass
    pass

message  = st.chat_input("输入你的消息")
if message:
    state.messages.append({"id":player_id, "message":message})

    pass

for message in state.messages:
    st.chat_message(message["id"], avatar=avatar_dict[message["id"]]).write(message["message"])
    pass

