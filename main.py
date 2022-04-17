import streamlit as st
from app.src.common import load_data
from app.src.common import make_plot

st.set_page_config(
    page_title = 'Chocolate bar rating',
    layout = 'wide'
)

st.title('Chocolate bar rating')
st.write('App demo PBG')
st.image('/static/choco_bar.jpg',width=300)

df_choco = load_data.load_dataset()

anno = st.sidebar.selectbox('Anno',sorted(df_choco.review_date.unique()))

st.altair_chart(make_plot.make_heatmap(df_choco,anno),use_container_width=True)

