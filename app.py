import streamlit as st

from bokeh.models.widgets import Div

import pandas as pd

from PIL import Image

pd.set_option('precision',2)

import base64


#def my_widget(key):
#    st.subheader('Hello there!')
#    clicked = st.button("Click me " + key)


def download_link(df, texto1, texto2):
    if isinstance(df,pd.DataFrame):
        object_to_download = df.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{texto1}">{texto2}</a>'
    



def main():

    """Indeed App """

    # Titulo do web app
    html_page = """
    <div style="background-color:blue;padding=80px">
        <p style='text-align:center;font-size:30px;font-weight:bold;color:white'>Indeed<br>Scrap de Oportunidades Abertas</p>
    </div>
              """
    st.markdown(html_page, unsafe_allow_html=True)

    
    # This works in the main area
    #clicked = my_widget("first")

    # And within an expander
    #my_expander = st.beta_expander("Expand", expanded=True)
    #with my_expander:
    #    clicked = my_widget("second")

    # AND in st.sidebar!
    #with st.sidebar:
    #    clicked = my_widget("third")
    
    
    aguia2 = Image.open("aguia7.jpg")
    st.sidebar.image(aguia2,caption="", width=200)

    activities = ["Home",'Cientista de Dados', 'Analista de Dados', 'Engenheiro de Machine Learning', 'Engenheiro de Dados',"About"]
    file_csv = ['CSV/indeed_Cientista_de_dados.csv','CSV/indeed_Analista_de_dados.csv', 'CSV/indeed_Engenheiro_de_machine_learning.csv',
                'CSV/indeed_Engenheiro_de_dados.csv']
    choice = st.sidebar.selectbox("Escolher",activities)

    if choice == 'Home':
        st.subheader("Selecione o cargo")
        st.subheader(" - Cientista de Dados")
        st.subheader(" - Analista de Dados")
        st.subheader(" - Engenheiro de Machine Learning")
        st.subheader(" - Engenheiro de Dados")
        
    elif choice == activities[1]:
        df = pd.read_csv(file_csv[0])
        total = str(len(df))
        st.title(activities[1])
        st.subheader("Total de vagas:"+total)
        st.table(df)
        if st.button('Download Dataframe as CSV'):
            cargo = activities[1].replace(' ', '_')
            filename = 'indeed_'+cargo+'.csv'
            tmp_download_link = download_link(df, filename, 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)
        
    elif choice == activities[2]:
        df = pd.read_csv(file_csv[1])
        total = str(len(df))
        st.title(activities[2])
        st.subheader("Total de vagas:"+total)
        st.table(df)
        if st.button('Download Dataframe as CSV'):
            cargo = activities[2].replace(' ', '_')
            filename = 'indeed_'+cargo+'.csv'
            tmp_download_link = download_link(df, filename, 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)     
   
    elif choice == activities[3]:
        df = pd.read_csv(file_csv[2])
        total = str(len(df))
        st.title(activities[3])
        st.subheader("Total de vagas:"+total)
        st.table(df)
        if st.button('Download Dataframe as CSV'):
            cargo = activities[3].replace(' ', '_')
            filename = 'indeed_'+cargo+'.csv'
            tmp_download_link = download_link(df, filename, 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)

    elif choice == activities[4]:
        df = pd.read_csv(file_csv[3])
        total = str(len(df))
        st.title(activities[4])
        st.subheader("Total de vagas:"+total)
        st.table(df)
        if st.button('Download Dataframe as CSV'):
            cargo = activities[4].replace(' ', '_')
            filename = 'indeed_'+cargo+'.csv'
            tmp_download_link = download_link(df, filename, 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)

  
    elif choice == 'About':
        st.subheader("Built with Streamlit")
        st.write("Dados coletados via scrap usando: Selenium e BeautifulSoup.")
        st.write("Foram pesquisadas as 10 primeiras páginas retornadas apenas.")
        st.subheader("by Silvio Lima")
        
        if st.button("Linkedin"):
            js = "window.open('https://www.linkedin.com/in/silviocesarlima/')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    

       

    #html2_page = """
    #<div style="background-color:tomato;padding=50px">
    #    <p style='text-align:center;font-size:40px;font-weight:bold'; font-color: white>Scrap de Oportunidades Abertas</p>
    #</div>
    #          """
    #st.markdown(html2_page, unsafe_allow_html=True)

    # Columns

    #col1, col2 = st.beta_columns(2)

    #aguia1 = Image.open("aguia6.jpg")
    #col1.header("Original")
    #col1.image(aguia1, use_column_width=True)

    #grayscale = aguia1.convert('LA')
    #col2.header("Grayscale")
    #col2.image(grayscale, use_column_width=False)

    # Table
    
    #st.title("Let's create a table!")
    #for i in range(1, 10):
    #    cols = st.beta_columns(4)
    #    cols[0].write(f'{i}')
    #    cols[1].write(f'{i * i}')
    #    cols[2].write(f'{i * i * i}')
    #    cols[3].write('x' * i)
   
    
        
     

    
   
    
    
if __name__ == '__main__':
    main()
