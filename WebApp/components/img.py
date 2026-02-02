import streamlit as st
import pandas as pd
from components.clustering import Taishitsu 
import base64
import os
import plotly.express as px
import numpy as np  
from pycirclize import Circos


class ImgComponent:

    def __init__(self, image_path: str):
        self.image_path = image_path 


    def set_background_image(self,png_file, overlay_opacity=0.7):
    
        if not os.path.exists(png_file):
            st.error(f"エラー: 画像ファイルが見つかりません: {png_file}")
            return

        # バイナリ読み込みとBase64変換
        with open(png_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        
        # 画像タイプ判定
        _, ext = os.path.splitext(png_file)
        img_type = ext.lower().replace(".", "")
        if img_type == 'jpg':
            img_type = 'jpeg'

        # CSS生成
        # linear-gradient で半透明の白を重ねています
        css = f'''
        <style>
            .stApp {{
                background-image: 
                    linear-gradient(rgba(255, 255, 255, {overlay_opacity}), rgba(255, 255, 255, {overlay_opacity})),
                    url("data:image/{img_type};base64,{bin_str}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            .stApp > header {{
                background-color: transparent;
            }}
        </style>
        '''
        st.markdown(css, unsafe_allow_html=True)