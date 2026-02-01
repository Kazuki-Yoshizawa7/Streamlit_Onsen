import streamlit as st
import datetime

# --- 設定: ページ設定など ---
st.set_page_config(layout="wide")

# --- カスタムCSS ---
st.markdown("""
<style>
    /* 検索バー全体（黄色い枠） */
    .search-container {
        background-color: #feba02;
        padding: 10px;
        border-radius: 4px;
        margin-bottom: 2rem;
    }

    /* 入力エリア（白背景）のスタイル調整 */
    /* Streamlitの列(stColumn)ごとの余白や背景を調整 */
    div[data-testid="stColumn"] > div > div > div {
        background-color: white;
        border-radius: 4px;
    }
    
    /* テキスト入力やセレクトボックスの微調整 */
    .stTextInput, .stDateInput, .stNumberInput, .stSelectbox {
        padding: 0px;
    }

    /* --- ボタンのスタイル設定 --- */

    /* 1. Searchボタン (type="primary") 専用スタイル */
    /* これで「Search」ボタンだけが青くなります */
    div.stButton > button[kind="primary"] {
        background-color: #0071c2 !important;
        border: none !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
        width: 100%;
        height: 55px; /* 高さを入力欄に合わせる調整 */
        margin-top: 0px; 
    }
    
    /* Searchボタンのホバー時 */
    div.stButton > button[kind="primary"]:hover {
        background-color: #005999 !important;
        color: white !important;
    }

    /* 2. その他のボタン (View Dealなど type="secondary") */
    /* 白背景に青文字のBooking.com風スタイル */
    div.stButton > button[kind="secondary"] {
        background-color: white !important;
        border: 1px solid #0071c2 !important;
        color: #0071c2 !important;
        font-weight: bold !important;
    }

    /* ヘッダー文字 */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.5rem;
        color: black;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8); /* 黒文字なので白縁取りに変更 */
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- 背景画像設定 (省略) ---

# --- メインコンテンツ ---

with st.container():
    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
    
    # 1. キャッチコピー
    st.markdown('<h1 class="hero-title">Find your perfect Onsen sanctuary</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Search deals on hot spring hotels, ryokans, and private retreats.</p>', unsafe_allow_html=True)

    # 2. 検索バー
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    
    # 1行目: 基本情報
    col1, col2, col3, col4, col5 = st.columns([2, 2, 1, 1.5, 1], gap="small")
    
    with col1:
        destination = st.text_input("Destination", placeholder="Where are you going?", label_visibility="collapsed")
        
    with col2:
        today = datetime.date.today()
        date_range = st.date_input(
            "Dates",
            (today, today + datetime.timedelta(days=1)),
            label_visibility="collapsed",
            format="MM/DD/YYYY"
        )

    with col3:
        guests = st.number_input("Guests", min_value=1, value=2, step=1, label_visibility="collapsed")
        
    with col4:
        filters = st.selectbox(
            "Filter",
            ["Any Price / Type", "Budget (<$100)", "Luxury (>$300)", "Private Onsen", "Tattoo Friendly", "Snow Monkey View"],
            label_visibility="collapsed"
        )
        
    with col5:
        # ここで type="primary" を指定しているため、CSSの button[kind="primary"] が適用され「青」になります
        # 縦位置を合わせるために独自のパディングなどを入れることもあります
        search_pressed = st.button("Search", type="primary", use_container_width=True)

    # 2行目: 詳細フィルター (2段組み風)
    st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True) # 少し隙間
    col6, col7, col8, col9 = st.columns([2,2,1,1], gap="small")

    with col6:
        st.selectbox(
            "Body Type",
            ["Body Type", "Type A", "Type B", "Type C", "Type D"],
            label_visibility="collapsed"
        )

    with col7:
        st.selectbox(
            "Preferred Water Type",
            ["Water Type", "Acidic", "Alkaline", "Sulfur", "Carbonated"],
            label_visibility="collapsed"
        ) 

    with col8:
        st.selectbox(
            "Scenery",
            ["Scenery", "Mountain View", "Ocean View", "Forest View", "Urban View"],
            label_visibility="collapsed"
        )
    
    with col9:
        # レイアウト調整用の空欄、あるいは追加ボタン
        st.empty()

    st.markdown('</div>', unsafe_allow_html=True) # コンテナ閉じ

# --- 検索結果の表示エリア ---
if search_pressed:
    st.write("---")
    st.subheader(f"Results for: {destination}")
    
    res_col1, res_col2, res_col3 = st.columns(3, gap="medium")

    # 結果カード1：露天風呂のイメージ
    with res_col1:
        # 確実に表示される温泉画像 (Outdoor Onsen)
        st.image("https://images.unsplash.com/photo-1576485290814-1c72aa4bbb8e?q=80&w=800&auto=format&fit=crop", use_container_width=True)
        st.markdown("### Tohoku Onsen A ")
        st.write("⭐ 4.8 (Exceptional) - 2.5km from center")
        st.markdown("#### $250 / night")
        # デフォルト(secondary)ボタン = 白背景・青文字
        st.button("View Deal", key="btn1", use_container_width=True)
    
    with res_col2:
        # 確実に表示される温泉画像 (Indoor Onsen)
        st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=800&auto=format&fit=crop", use_container_width=True)
        st.markdown("### Tohoku Onsen A with Special Meal-plan")
        st.write("⭐ 4.8 (Exceptional) - 2.5km from center")
        st.write("Includes traditional Yakuzen(薬膳) dinner and breakfast")
        st.markdown("#### $300 / night")
        st.button("View Deal", key="btn2", use_container_width=True)

    with res_col3:
        # 確実に表示される温泉画像 (Private Onsen)
        st.image("https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?q=80&w=800&auto=format&fit=crop", use_container_width=True)
        st.markdown("### Tohoku Private Onsen B")
        st.write("⭐ 4.9 (Exceptional) - 3.0km from center")
        st.write("Private onsen with japanese garden and local cuisine options")
        st.write("Includes packaged local trips and experiences")
        st.markdown("#### $700 / night")
        st.button("View Deal", key="btn3", use_container_width=True)