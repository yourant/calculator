import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

import en_core_web_sm
import matplotlib.pyplot as plt 
from wordcloud import WordCloud
from textblob import TextBlob 
from sqlalchemy import create_engine
nlp = en_core_web_sm.load()

@st.cache
def load_data():
    sql1='''select distinct asin from amazon.asin_review'''
    engine = create_engine('mysql+pymysql://root:aukey@888@139.9.201.134:3306')
    asins = pd.read_sql(sql1,engine)
    return asins

def run_nlp():
    st.subheader('亚马逊商品评论智能分析')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    asins = load_data()
    chosedasin=st.selectbox('Asin:',asins['asin'].unique())
#用类把这个和load_data封装到一起
    sql=f'''
    select review_star_rating,review_info, right(review_date,17) 
    as review_date from amazon.asin_review 
    where asin='{chosedasin}'
    '''  
    engine = create_engine('mysql+pymysql://root:aukey@888@139.9.201.134:3306')
#
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
    wordcount=str(adj).replace('dtype','').replace('Lemma','').replace('int64','').replace('Name','')

    c1,c2,c3,c4=st.beta_columns(4)
    with c1:
        _token=st.button('开始切分')
    with c2:
        _wordcloud=st.button('生成词云')
    with c3:
        _sentiment_analysis=st.button('情感分析')
    with c4:
        _lemma=st.button('查看词频')
    if _sentiment_analysis:
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
    if _wordcloud:
        wordcloud =  WordCloud().generate(wordcount)
        plt.imshow(wordcloud,interpolation='bilinear')
        plt.axis("off")
        st.pyplot()
    if _lemma:
        st.write(pd.DataFrame(adj.rename('Count')).transpose()) 
    if _token:
        st.dataframe(new_df)

if __name__=='__main__':
    run_nlp()