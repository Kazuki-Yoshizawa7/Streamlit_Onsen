import streamlit as st
import pandas as pd


st.title("体質診断Page")

st.write("ここでは体質診断を行う")

# ホームに戻るボタン
if st.button("🏠 Back to Home"):
    st.switch_page("app.py")




# セッションステートの初期化
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

# 質問データの定義
questions = [
    {
        "id": 1,
        "question": "好きな色は？",
        "options": ["赤", "青", "緑", "黄色"]
    },
    {
        "id": 2,
        "question": "好きな食べ物は？",
        "options": ["寿司", "ラーメン", "カレー", "パスタ"]
    },
    {
        "id": 3,
        "question": "好きなスポーツは？",
        "options": ["サッカー", "野球", "バスケ", "テニス"]
    }
]

st.title("アンケートフォーム")

# 現在の質問番号
current_q = st.session_state.current_question

# 全質問が終了した場合
if current_q >= len(questions):
    st.success("すべての質問に回答しました！")
    
    # DataFrameに変換
    df = pd.DataFrame(st.session_state.answers)
    
    # -> ここで分類アルゴリズムをかけて体質を最後に表示したいな



    st.subheader("回答結果")
    st.dataframe(df)
    
    # CSV出力
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="CSVダウンロード",
        data=csv,
        file_name="answers.csv",
        mime="text/csv"
    )
    
    # リセットボタン
    if st.button("最初からやり直す"):
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.rerun()
    
else:
    # 現在の質問を表示
    q = questions[current_q]
    
    st.progress((current_q + 1) / len(questions))
    st.write(f"質問 {current_q + 1} / {len(questions)}")
    
    st.subheader(q["question"])
    
    # ラジオボタンで選択肢を表示
    answer = st.radio(
        "選択してください",
        options=q["options"],
        key=f"q_{q['id']}"
    )
    
    # 次へボタン
    if st.button("次へ", type="primary"):
        # 回答を保存
        st.session_state.answers.append({
            "question_id": q["id"],
            "question": q["question"],
            "answer": answer
        })
        
        # 次の質問へ
        st.session_state.current_question += 1
        st.rerun()