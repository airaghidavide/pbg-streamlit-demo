import streamlit as st
from app.src.common import load_data
from app.src.common import make_plot

st.set_page_config(
     page_title="Chocolate Bar Rating",
     layout="wide",
 )
st.title('Chocolate Bar Rating')
st.write('Chocolate is one of the most popular candies in the world. Each year, residents of the United States collectively eat more than 2.8 billions pounds. However, not all chocolate bars are created equal!')
st.image('./static/choco_bar.jpg',width=300)

#load data for the app (all in cache)
df_choco = load_data.load_dataset()

anno = st.sidebar.selectbox('Anno',sorted(df_choco.review_date.unique()))

#create plot
st.altair_chart(make_plot.make_heatmap(df_choco,anno), use_container_width=True)
