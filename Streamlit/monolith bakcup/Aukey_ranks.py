import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly_express as px
import time
import spacy_streamlit
import spacy
import en_core_web_sm
import os
import matplotlib.pyplot as plt 
import matplotlib
from sqlalchemy import create_engine
from wordcloud import WordCloud
from textblob import TextBlob 
from PIL import Image
from datetime import datetime

st.set_page_config(
    page_title='Aukey 2.0 品类排名看板',
    page_icon=':shark:',
    initial_sidebar_state='expanded'
)

nlp = en_core_web_sm.load()

def main():
    menu=['主页','排名进度','合并查询','语义分析','物品识别','关于']
    choice = st.sidebar.selectbox('Menu',menu)
    engine = create_engine('mysql+pymysql://chencheng:iKWz@4*7W55@10.1.1.202:3306')
    catelist=pd.read_csv('Files/category__.csv')
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

    if choice == '主页':
        st.title('傲基2.0品类管理')
        st.header('品类详情')
        st.markdown('针对每个asin，日排名规则为：每日排名取当日排名的中位数值')
    
    elif choice == '排名进度':
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
        # with open('app.html') as f:
        #    t1= f.read()
        #    components.html(t1,height=800)
        st.write(t1)
        data_load_state.success('✔️ 数据加载完成')
        time.sleep(1)
        data_load_state.text('')
        chosed_asin = st.selectbox('Asin',data.asin.unique())
        a1=pd.DataFrame(t1.loc[f'{chosed_asin}',:].dropna()).transpose()
        a1_rank=a1.apply(lambda x: int(np.median(x)),axis=1)[0]
        st.dataframe(a1)
    
    
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

    elif choice == '合并查询':
        
        ci=st.multiselect('品类ID',data['category_id'].unique())           
        newdate=st.multiselect('日期',data[(data['category_id'].isin(ci))].date.unique())            
        asin=st.multiselect('ASIN',data[data['category_id'].isin(ci)&(data['date'].isin(newdate))].asin.unique())
        newtable=data[(data['category_id'].isin(ci))&(data['asin'].isin(asin))&(data['date'].isin(newdate))]

        st.write(newtable[['category_id','category_name','asin','ranking','date']])


    elif choice == '语义分析':
        st.subheader('亚马逊商品评论智能分析')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        engine = create_engine('mysql+pymysql://root:aukey@888@139.9.201.134:3306')
        sql1='''select distinct asin from amazon.asin_review
        '''
        asins = pd.read_sql(sql1,engine)
        chosedasin=st.selectbox('Asin:',asins['asin'].unique())
        
        sql=f'''
        select review_star_rating,review_info, right(review_date,17) 
        as review_date from amazon.asin_review 
        where asin='{chosedasin}'
        '''

        review = pd.read_sql(sql,engine)
        st.write(review)
        no=st.number_input('输入你想要看到的评论序号',min_value=1,value=1,step=1)
        ct=review.iloc[no,1]
        raw_text =st.text_area('选择序号自动引用评论，或在下框手动输入文本',f'{ct}')
        docx = nlp(raw_text)

        c_tokens = [ token.text for token in docx ]
        c_lemma = [token.lemma_ for token in docx]
        c_pos = [word.tag_ for word in docx]
        new_df = pd.DataFrame(zip(c_tokens,c_lemma,c_pos),columns=['Tokens','Lemma','POS'])
        adj=new_df[(new_df['POS']=='JJ')|(new_df['POS']=='NN')]['Lemma'].value_counts()
        wc=str(adj).replace('dtype','').replace('Lemma','').replace('int64','').replace('Name','')

        c1,c2,c3,c4=st.beta_columns(4)
        with c1:
            qf=st.button('开始切分')
        with c2:
            cy=st.button('生成词云')
        with c3:
            fx=st.button('情感分析')
        with c4:
            ck=st.button('查看动名词')
        if fx:
            blob = TextBlob(raw_text)
            sent_res=[]
            sent_res.append(blob.polarity)
            sent_res.append(blob.subjectivity)            
            st.success(f'该评论的偏向性为:{sent_res[0]},主观性为:{sent_res[1]}')
            if sent_res[0]>0.3:
                st.success('该客户颇为喜爱此商品！')
            elif sent_res[0]>=-0.3 and sent_res[0]<=0.3:
                st.info('该客户对此商品没有明显偏向')
            else:
                st.warning('该客户对产品很不满！')
        if cy:
            wordcloud =  WordCloud().generate(wc)
            plt.imshow(wordcloud,interpolation='bilinear')
            plt.axis("off")
            st.pyplot()
        if ck:
            st.write(pd.DataFrame(adj.rename('Count')).transpose()) 
        if qf:
            st.dataframe(new_df)

if __name__=='__main__':
    main()

