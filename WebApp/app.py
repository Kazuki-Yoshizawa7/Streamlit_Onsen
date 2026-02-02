import streamlit as st
from components.img import ImgComponent

# --- ページ設定 ---
st.set_page_config(
    page_title="Onsen Journey Japan",
    page_icon="♨️",
    layout="wide" #centered
)

# --- CSSスタイル定義 (背景画像とデザイン) ---
# 露天風呂の画像 (Unsplash)

img_path = '/Users/yoshizawakazuki/Streamlit_Onsen/static/img2.jpg'
img_component = ImgComponent(image_path=img_path)
img_component.set_background_image(png_file=img_path, overlay_opacity=0.6)



# デザイン用のコンテナ開始
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# タイトルとキャッチコピー
st.markdown("# ♨️ ONSEN JOURNEY")
st.markdown("### Discover the Healing Art of *Toji*")
st.write("---")

# 説明文
st.markdown("""
<p style="font-size: 1.2rem; line-height: 1.8; margin-bottom: 3rem;">
    Immersion in nature. Relaxation for the soul.<br>
    Experience Japan's finest hot springs tailored to your needs.
</p>
""", unsafe_allow_html=True)

st.markdown("## What is Toji?", unsafe_allow_html=True)
st.markdown("""
<p style ="font-size: 1.2rem; line-height: 1.8; margin-bottom: 3rem;">
    Onsens have health benefits and each onsen has different characteristics. <br>)
</p>
""", unsafe_allow_html=True)

# --- 3枚の画像を並べるエリア ---
img_col1, img_col2, img_col3 = st.columns(3, gap="medium")

with img_col1:
        # 癒やし/入浴イメージ
    st.image("/Users/yoshizawakazuki/Streamlit_Onsen/static/OnsenA.png", use_container_width=True)
    st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 5px;'>Onsen A </p>", unsafe_allow_html=True)

with img_col2:
        # 自然/風景イメージ
    st.image("/Users/yoshizawakazuki/Streamlit_Onsen/static/OnsenB.png", use_container_width=True)
    st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 5px;'>Onsen B </p>", unsafe_allow_html=True)

with img_col3:
        # 文化/浴衣イメージ
    st.image("/Users/yoshizawakazuki/Streamlit_Onsen/static/OnsenC.png", use_container_width=True)
    st.markdown("<p style='text-align: center; font-size: 0.8rem; margin-top: 5px;'>Onsen C</p>", unsafe_allow_html=True)
    
st.write("") # スペーサー
st.write("")

# 2カラムレイアウトでボタンを配置
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("##### 🧘‍♀️ Personalize")
    st.write("Find your perfect Onsen match.")
    # type="primary" で色を変えて強調
    if st.button("Start Body Diagnosis", type="primary", use_container_width=True):
        st.switch_page("pages/type_clustering.py")

with col2:
    st.markdown("##### 🔍 Explore")
    st.write("Search Onsen-hotels & Ryokans.")
    if st.button("Search Onsen Deals", use_container_width=True):
        st.switch_page("pages/search.py")

st.markdown('</div>', unsafe_allow_html=True) # コンテナ終了


import pandas as pd
import altair as alt

# ... (これまでのコードの続き) ...

# === Editor's Choice セクション ===

with st.container():
    # CSS適用のためのマーカー (同じガラスデザインを適用)
    st.markdown('<div id="glass-card"></div>', unsafe_allow_html=True)
    
    st.markdown("### 🏆 Editor's Choice Rankings")
    st.markdown("""
    <p style="font-size: 1rem; margin-bottom: 2rem; opacity: 0.9;">
        Curated top picks based on traveler reviews and expert ratings.
    </p>
    """, unsafe_allow_html=True)

    # 1. ダミーデータの作成
    # 実際にはデータベースから取得しますが、ピッチ用に固定データを作ります
    df_ranking = pd.DataFrame({
        'Onsen Area': ['Hakone (Kanagawa)', 'Kusatsu (Gunma)', 'Beppu (Oita)', 'Ginzan (Yamagata)', 'Kurokawa (Kumamoto)'],
        'Overall Score': [98, 96, 94, 92, 90],
        'Healing': [90, 99, 95, 85, 92],
        'Views': [95, 85, 90, 99, 94],
        'Culture': [92, 94, 96, 95, 88]
    })

    # 2. タブでカテゴリ切り替え
    tab1, tab2, tab3 = st.tabs(["🔥 Overall Popularity", "🌿 Best for Healing", "🗻 Best Views"])

    # 共通のチャート設定関数 (修正版)
    def create_ranking_chart(column_name, color_hex):
        # ソート順: スコアが高い順
        sorted_df = df_ranking.sort_values(by=column_name, ascending=False)
        
        # ベースとなるバーチャート (設定はまだ適用しない)
        base_chart = alt.Chart(sorted_df).mark_bar(cornerRadiusTopRight=10, cornerRadiusBottomRight=10).encode(
            x=alt.X(f'{column_name}:Q', title='Score (out of 100)', scale=alt.Scale(domain=[0, 100])),
            y=alt.Y('Onsen Area:N', sort='-x', title=None, axis=alt.Axis(labelFontSize=12, labelColor='white')),
            color=alt.value(color_hex),
            tooltip=['Onsen Area', column_name]
        ).properties(
            height=250
        )
        
        # テキストレイヤー
        text = base_chart.mark_text(
            align='left',
            baseline='middle',
            dx=5,
            color='white'
        ).encode(
            text=f'{column_name}:Q'
        )
        
        # 【重要】結合した後に、configure系をまとめて適用する
        combined_chart = (base_chart + text).configure_axis(
            grid=False,
            domain=False
        ).configure_view(
            strokeWidth=0
        )
        
        return combined_chart

    # 各タブにチャートを表示
    with tab1:
        st.altair_chart(create_ranking_chart('Overall Score', '#ff6b6b'), use_container_width=True)
        st.write("Hakone remains the top choice for its accessibility and variety.")

    with tab2:
        st.altair_chart(create_ranking_chart('Healing', '#4ecdc4'), use_container_width=True)
        st.write("Kusatsu's highly acidic water offers the strongest detox effect.")

    with tab3:
        st.altair_chart(create_ranking_chart('Views', '#ffe66d'), use_container_width=True)
        st.write("Ginzan Onsen provides a nostalgic, snowy winter scenery like no other.")

# ... (この後にフッターが続きます) ...

# --- フッター ---
st.markdown("""
<div style="text-align: center; margin-top: 80px; color: rgba(255,255,255,0.7); font-size: 0.9rem;">
    <p>© 2026 Onsen&Toji Japan For demonstration purposes only.</p>
</div>
""", unsafe_allow_html=True)