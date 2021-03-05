import streamlit as st
import pandas as pd
import time
from sqlalchemy import create_engine

@st.cache
def load_data(category_id):
    data_sql=f'''
    select category_id,category_name,asin,ranking,snapshotted_at as date
    from mws_data.project_20_listings where category_id='{category_id}'
    '''
    data_engine = create_engine('mysql+pymysql://chencheng:iKWz@4*7W55@10.1.1.202:3306')
    data=pd.read_sql(data_sql,data_engine) 
    data['date']=pd.to_datetime(pd.to_datetime(data['date']).dt.date)
    return data

def run_search():
    st.title('多品类合并查询')
    catelist=pd.read_csv('files/category__.csv')
    category = st.selectbox('品类名称:',catelist['category_name'])
    catid=catelist[catelist['category_name']==category]['category_id'].values[0]
    st.markdown(f'#### 已选中 **{category}** ,  品类ID: **{catid}**')
    data = None
    while data is None:
        data_load_state=st.text('正在加载数据')
        data=load_data(catid)
    ci=data['category_id'].unique()     
    newdate=st.multiselect('日期',data[(data['category_id'].isin(ci))].date.unique())            
    asin=st.multiselect('ASIN',data[data['category_id'].isin(ci)&(data['date'].isin(newdate))].asin.unique())
    newtable=data[(data['category_id'].isin(ci))&(data['asin'].isin(asin))&(data['date'].isin(newdate))]
    st.write(newtable[['category_id','category_name','asin','ranking','date']])

    data_load_state.success('✔️ 数据加载完成')
    time.sleep(1)
    data_load_state.text('')    
    

if __name__=='__main__':
    run_search()
