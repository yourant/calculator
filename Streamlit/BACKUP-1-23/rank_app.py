#Core
import streamlit as st
import streamlit.components.v1 as components

#EDA
import time
import pandas as pd
import numpy as np
import plotly_express as px
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://chencheng:iKWz@4*7W55@10.1.1.202:3306')
catelist=pd.read_csv('files/category__.csv')

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







def run_rank():
    st.title('当月排名进度')
    category = st.selectbox('品类名称:',catelist['category_name'])
    catid=catelist[catelist['category_name']==category]['category_id'].values[0]
    st.markdown(f'#### 已选中 **{category}** ,  品类ID: **{catid}**')
    data = None
    while data is None:
        data_load_state=st.text('正在加载数据')
        data=load_data(catid)
    table=data.groupby(['asin','date'])['ranking'].agg('median').apply(lambda x:int(x))
    t1=table.unstack(level=1)
    st.write(t1)
    data_load_state.success('✔️ 数据加载完成')
    time.sleep(1)
    data_load_state.text('')
    chosed_asin = st.selectbox('Asin',data.asin.unique())
    a1=pd.DataFrame(t1.loc[f'{chosed_asin}',:].dropna()).transpose()
    a1_rank=a1.apply(lambda x: int(np.median(x)),axis=1)[0]
    #画图模块   
    t2=pd.DataFrame(t1.loc[f'{chosed_asin}'])
    t2['date']=t2.index.get_level_values(0)
    t2.reset_index(drop=True)
    fig = px.line(t2, x=t2['date'], y=t2[f'{chosed_asin}'], title=f'{chosed_asin}的当月排名情况(红线为当月排名)')
    fig.add_shape(type='line',
                    x0=t2['date'].iloc[0],
                    y0=a1_rank,
                    x1=t2['date'].iloc[-1],
                    y1=a1_rank,
                    line=dict(color='Red'),
                    xref='x',
                    yref='y')
    st.plotly_chart(fig, use_container_width=True)
    #画图模块    
    st.info(f'ASIN {chosed_asin}的当月排名为:    {int(a1_rank)}')
    a2=t1.apply(lambda x: np.median(x),axis=1).sort_values()
    if int(a2[0])==1:
        st.success(f'当前品类下月排名最高的Asin为{a2.index[0]},  月排名为: {int(a2[0])}')
    elif int(a2[0])<=8:
        st.info(f'当前品类下月排名最高的Asin为{a2.index[0]},  月排名为: {int(a2[0])}')
    else:
        st.warning(f'当前品类下月排名最高的Asin为{a2.index[0]},  月排名为: {int(a2[0])}')
    d1,d2=st.beta_columns(2)
    with d1:
        start_time = st.date_input("根据日期查看",t2['date'].iloc[0])
    with d2:
        end_time = st.date_input("结束日期",t2['date'].iloc[-1])
    if str(start_time) in t1.columns:
        st.write(t1.loc[:,start_time:end_time])
        t2=t1[f'{start_time}'].sort_values()
        top1=t2[0]
        topn=t2.where(t2<=8).count()
        if top1==1:
            st.success(f'{start_time}日 {t2.index[0]} 的日排名为第一！')
        elif topn>=4:
            st.success('有四个个以上asin进入前八！')
        else:
            st.warning('没有排名靠前的Asin')

    else:
        st.write('数据缺失')

    with st.beta_expander('原始数据详情',expanded=False):
        i=st.number_input('输入你想要看到的条数',min_value=1,value=50,step=50)
        detail=data.iloc[:i,:]
        st.write(detail)
        

if __name__=='__main__':
    run_rank()
