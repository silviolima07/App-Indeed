import streamlit as st

from bokeh.models.widgets import Div

import pandas as pd

from PIL import Image

pd.set_option('precision',2)

import base64


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

   
    aguia1 = Image.open("Images/aguia1.jpg")
    aguia2 = Image.open("Images/aguia2.jpg") 
    aguia3 = Image.open("Images/aguia3.jpg")
    aguia4 = Image.open("Images/aguia4.jpg")
    aguia5 = Image.open("Images/aguia5.jpg")
    scrap  = Image.open("Images/scrap.png")

    activities = ["Home",'Cientista de Dados', 'Analista de Dados', 'Engenheiro de Machine Learning', 'Engenheiro de Dados',"About"]
    file_csv = ['CSV/indeed_Cientista_de_dados.csv','CSV/indeed_Analista_de_dados.csv', 'CSV/indeed_Engenheiro_de_machine_learning.csv',
                'CSV/indeed_Engenheiro_de_dados.csv']
    choice = st.sidebar.selectbox("Escolher",activities)

    if choice == 'Home':
        st.sidebar.image(scrap,caption="", width=300)
        st.subheader("Selecione o cargo")
        st.subheader(" - Cientista de Dados")
        st.subheader(" - Analista de Dados")
        st.subheader(" - Engenheiro de Machine Learning")
        st.subheader(" - Engenheiro de Dados")
        
    elif choice == activities[1]:
        st.sidebar.image(aguia1,caption="", width=300)
        df = pd.read_csv(file_csv[0])
        total = str(len(df))
        st.title(activities[1])
        st.subheader("Total de vagas: "+total)
        st.table(df)
        if st.button('Download Dataframe as CSV'):
            cargo = activities[1].replace(' ', '_')
            filename = 'indeed_'+cargo+'.csv'
            tmp_download_link = download_link(df, filename, 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)
        
    elif choice == activities[2]:
        st.sidebar.image(aguia2,caption="", width=300)
        df = pd.read_csv(file_csv[1])
        total = str(len(df))
        st.title(activities[2])
        st.subheader("Total de vagas: "+total)
        st.table(df)
        if st.button('Download Dataframe as CSV'):
            cargo = activities[2].replace(' ', '_')
            filename = 'indeed_'+cargo+'.csv'
            tmp_download_link = download_link(df, filename, 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)     
   
    elif choice == activities[3]:
        st.sidebar.image(aguia3,caption="", width=300)
        df = pd.read_csv(file_csv[2])
        total = str(len(df))
        st.title(activities[3])
        st.subheader("Total de vagas: "+total)
        st.table(df)
        if st.button('Download Dataframe as CSV'):
            cargo = activities[3].replace(' ', '_')
            filename = 'indeed_'+cargo+'.csv'
            tmp_download_link = download_link(df, filename, 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)

    elif choice == activities[4]:
        st.sidebar.image(aguia4,caption="", width=300)
        df = pd.read_csv(file_csv[3])
        total = str(len(df))
        st.title(activities[4])
        st.subheader("Total de vagas: "+total)
        st.table(df)
        if st.button('Download Dataframe as CSV'):
            cargo = activities[4].replace(' ', '_')
            filename = 'indeed_'+cargo+'.csv'
            tmp_download_link = download_link(df, filename, 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)

  
    elif choice == 'About':
        st.sidebar.image(aguia5,caption="", width=400)
        st.subheader("Built with Streamlit")
        st.write("Dados coletados via scrap usando: Selenium e BeautifulSoup.")
        st.write("As 10 primeiras páginas apenas.")
        st.subheader("by Silvio Lima")
        
        if st.button("Linkedin"):
            js = "window.open('https://www.linkedin.com/in/silviocesarlima/')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    

       

   
    
    
if __name__ == '__main__':
    main()
