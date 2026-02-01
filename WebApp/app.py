import streamlit as st



# def main():
#     st.write("Hello World!")


# if __name__ == "__main__":
#     main()

"""
ここで、まずユーザーの情報：体質診断を行うPageに移動させる
"""

st.title("Welcome to our ONSEN.APP!!")

col1,col2 = st.columns(2)

with col1:
    if st.button("体質診断へ",use_container_width = True):
        st.switch_page("pages/type_clustering.py")

with col2:
    if st.button("温泉検索へ",use_container_width = True):
        st.switch_page("pages/search.py")
    