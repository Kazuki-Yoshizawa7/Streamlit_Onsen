import streamlit as st
import pandas as pd
from components.clustering import Taishitsu 

st.title("体質診断 Constitution Analysis Page")

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
# 質問データの定義
questions = [
    {
        "id": 1,
        "question": "胸やおなかが張って苦しくなることが多い",
        "options": ["Yes", "No"]
    },
    {
        "id": 2,
        "question": "イライラしやすく怒りっぽい",
        "options": ["Yes", "No"]
    },
    {
        "id": 3,
        "question": "不眠になりやすい",
        "options": ["Yes", "No"]
    },
    {
        "id": 4,
        "question": "皮膚に吹き出物や化のうがよくできる",
        "options": ["Yes", "No"]
    },
    {
        "id": 5,
        "question": "よく尿が濃い黄色になる",
        "options": ["Yes", "No"]
    },
    {
        "id": 6,
        "question": "肩がこりやすい",
        "options": ["Yes", "No"]
    },
    {
        "id": 7,
        "question": "唇や歯ぐきの色が紫に近い",
        "options": ["Yes", "No"]
    },
    {
        "id": 8,
        "question": "頭が重く感じられることが多い",
        "options": ["Yes", "No"]
    },
    {
        "id": 9,
        "question": "雨の日や湿度の高い日は体調が悪くなりがち",
        "options": ["Yes", "No"]
    },
    {
        "id": 10,
        "question": "皮膚が乾燥してカサカサしている",
        "options": ["Yes", "No"]
    },
    {
        "id": 11,
        "question": "舌のふちがギザギザになっている",
        "options": ["Yes", "No"]
    },
    {
        "id": 12,
        "question": "舌苔（舌のコケ）がびっしりついていて厚みがある",
        "options": ["Yes", "No"]
    },
    {
        "id": 13,
        "question": "舌の裏側の静脈が太くふくらんで見える",
        "options": ["Yes", "No"]
    },
    {
        "id": 14,
        "question": "食欲がなく胃もたれしやすい",
        "options": ["Yes", "No"]
    },
    {
        "id": 15,
        "question": "下痢や軟便になることがよくある",
        "options": ["Yes", "No"]
    },
    {
        "id": 16,
        "question": "よく腰やひざに疲れや脱力感を感じる",
        "options": ["Yes", "No"]
    },
    {
        "id": 17,
        "question": "むくみを感じることが多い",
        "options": ["Yes", "No"]
    },
    {
        "id": 18,
        "question": "髪の毛が細くパサつきやすい",
        "options": ["Yes", "No"]
    },
    {
        "id": 19,
        "question": "目の疲れや乾燥を感じやすい",
        "options": ["Yes", "No"]
    },
    {
        "id": 20,
        "question": "筋肉がけいれんしたり、つりやすい",
        "options": ["Yes", "No"]
    },
    {
        "id": 21,
        "question": "ほてりやのぼせを感じる",
        "options": ["Yes", "No"]
    },
    {
        "id": 22,
        "question": "疲労時や夜に、よく手のひらや足の裏が熱くなる",
        "options": ["Yes", "No"]
    }
]

st.title("体質診断 / Constitution Analysis")

# 現在の質問番号
current_q = st.session_state.current_question

# 全質問が終了した場合
if current_q >= len(questions):
    st.success("すべての質問に回答しました！")
    
    # DataFrameに変換
    df = pd.DataFrame(st.session_state.answers)
    
    



    st.subheader("回答結果")
    st.dataframe(df)
    
    # -> ここで分類アルゴリズムをかけて体質を最後に表示したいな
    Taishitsu_instance=Taishitsu(df)
    result = Taishitsu_instance.calculate_result()
    st.subheader('Score')
    st.dataframe(result)

    top = Taishitsu_instance.type_classify(result)
    st.subheader("Your Body Type")
    st.write(f"Type: {top}")

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