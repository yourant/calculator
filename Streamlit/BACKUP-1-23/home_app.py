#Core
import streamlit as st
import streamlit.components.v1 as components


def run_home():
    st.title('傲基2.0品类管理')
    st.header('品类详情')
    st.markdown('针对每个asin，日排名规则为：每日排名取当日排名的中位数值')
    