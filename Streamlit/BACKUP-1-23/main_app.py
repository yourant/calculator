#Core
import streamlit as st
import streamlit.components.v1 as components

#Pages
from home_app import run_home
from rank_app import run_rank
from search_app import run_search
from nlp_app import run_nlp

st.set_page_config(
    page_title='Aukey 2.0 品类排名看板',
    page_icon=':shark:',
    initial_sidebar_state='expanded'
)

def main():
    menu=['主页','排名进度','合并查询','语义分析','物品识别','关于']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == '主页':
        run_home()
    
    elif choice== '排名进度':
        run_rank()
    
    elif choice == '合并查询':
        run_search()

    elif choice == '语义分析':
        run_nlp()

if __name__=='__main__':
    main()

