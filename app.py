import streamlit as st

from bokeh.models.widgets import Div

import pandas as pd

from PIL import Image

pd.set_option('precision',2)

import base64

import sys

import glob

def download_link(df):
    if isinstance(df,pd.DataFrame):
        object_to_download = df.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{texto1}">{texto2}</a>'

def get_table_download_link(df,file):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download= "{file}" >Download csv</a>'
    return href
    

def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link
    return f'<a target="_blank" href="{link}">Link da vaga</a>' # ou {text} e irá mostrar o link clicável
    

def main():

    """Indeed App """

    # Titulo do web app
    html_page = """
    <div style="background-color:blue;padding=30px">
        <p style='text-align:center;font-size:30px;font-weight:bold;color:white'>Indeed</p>
    </div>
              """
    st.markdown(html_page, unsafe_allow_html=True)
   
    html_page = """
    <div style="background-color:white;padding=20px">
        <p style='text-align:center;font-size:20px;font-weight:bold;color:blue'>Scrap de Oportunidades Abertas em Data Science</p>
    </div>
              """
    st.markdown(html_page, unsafe_allow_html=True)

   
    aguia1 = Image.open("Images/aguia1.png")
    aguia2 = Image.open("Images/aguia2.png") 
    aguia3 = Image.open("Images/aguia3.png")
    aguia4 = Image.open("Images/aguia4.png")
    scrap  = Image.open("Images/webscrap.jpeg")

    st.sidebar.image(scrap,caption="", width=300)

    activities = ["Home",'Cientista de Dados', 'Analista de Dados', 'Engenheiro de Machine Learning', 'Engenheiro de Dados',"About"]
    lista_CD= []
    lista_AD=[]
    lista_EML=[]
    lista_ED=[]
    lista_intervalo = []
    
    
    for f in glob.iglob("CSV/*.csv"): # generator, search immediate subdirectories
        st.write(f)

        if str(f).startswith('CSV/indeed_CD'):
            lista_CD.append(f)
            temp = f.replace('indeed_CD_','').replace('.csv','')
            lista_CD.append(temp)
         
        if f.startswith('CSV/indeed_AD'):
            lista_AD.append(f)
            temp = f.replace('indeed_AD_','').replace('.csv','')
            lista_AD.append(temp)

        if f.startswith('CSV/indeed_EML'):
            lista_EML.append(f)
            temp = f.replace('indeed_EML_','').replace('.csv','')
            lista_EML.append(temp)

        if f.startswith('CSV/indeed_ED'):
            lista_ED.append(f)
            temp = f.replace('indeed_ED_','').replace('.csv','')
            lista_ED.append(temp)

    st.write(lista_CD)
    st.write(lista_AD)
    st.write(lista_EML)
    st.write(lista_ED)

    choice = st.sidebar.selectbox("Selecione uma opção",activities)

    # Definir a data da última atualização


    f = open("update", "r")
    data_update = f.read()
   
    if choice != 'About':
        st.write('Última atualizacao: '+ data_update)

    if choice == activities[0]:
       
        col1, col2 = st.columns(2)
    
        col11, col22 = st.columns(2)
        
        col1.header("Cientista de Dados")
        col1.image(aguia1, width=300)
        
        col2.header("Analista de Dados")
        col2.image(aguia2, width=300)

        col11.header("Engenheiro de M.Learning")
        col11.image(aguia3, width=300)

        col22.header("Engenheiro de Dados")
        col22.image(aguia4, width=300)
        
    elif choice == activities[1]: # CD
        st.sidebar.image(aguia1,caption="", width=300)
        df = pd.read_csv(lista_csv[0])
        st.title(activities[1])
        st.subheader("Vagas: "+str(lista_intervalo[0]))
        st.table(df)
        file = lista_csv[0].replace('CSV/','')
        st.markdown(get_table_download_link(df, file), unsafe_allow_html=True)
        
    elif choice == activities[2]: # AD
        st.sidebar.image(aguia2,caption="", width=300)
        df = pd.read_csv(lista_csv[2])
        st.title(activities[2])
        st.subheader("Vagas: "+str(lista_intervalo[2]))
        st.table(df)
        file = lista_csv[2].replace('CSV/','')
        st.markdown(get_table_download_link(df, file), unsafe_allow_html=True)   
   
    elif choice == activities[3]: # EML
        st.sidebar.image(aguia3,caption="", width=300)
        df = pd.read_csv(lista_csv[1])
        st.title(activities[3])
        st.subheader("Vagas: "+str(lista_intervalo[1]))
        st.table(df)
        file = lista_csv[1].replace('CSV/','')
        st.markdown(get_table_download_link(df,file), unsafe_allow_html=True)

    elif choice == activities[4]: # ED
        st.sidebar.image(aguia4,caption="", width=300)
        df = pd.read_csv(lista_csv[3])
        st.title(activities[4])
        st.subheader("Vagas: "+str(lista_intervalo[3]))
        st.table(df)
        file = lista_csv[3].replace('CSV/','')
        st.markdown(get_table_download_link(df, file), unsafe_allow_html=True)
            
  
    elif choice == 'About':
        #st.sidebar.image(about,caption="", width=300, height= 200)
        st.subheader("Built with Streamlit")
        
        st.write("Dados coletados via scrap usando: request e BeautifulSoup.")
        #st.markdown("A coleta dos dados é feita às 9h, 12h, 15h e 18h")
        #st.write("Executados via crontab scripts realizam o scrap e atualização do app.")
        #st.write("Foram definidos 4 cargos apenas para validar o processo.")
        #st.write("O scrap para o cargo de Engenheiro de Machine Learning trouxe poucas linhas.")
        #st.write("Para os demais cargos, foram encontradas mais de 100 vagas, distribuídas em diversas páginas.")
        st.write("Esse app traz as 40 primeiras páginas apenas.")
        #st.subheader("Observacao:")
        #st.write("O codigo html da pagina muda ao longo do tempo e ajustes no scrap são necessarios.")
        #st.subheader("Versão 02")
        #st.write(" - incluído o link encurtado da vaga")
        st.subheader("by Silvio Lima")
        st.write('https://www.linkedin.com/in/silviocesarlima/')
        
        #if st.button("Linkedin"):
        #    js = "window.open('https://www.linkedin.com/in/silviocesarlima/')"
        #    html = '<img src onerror="{}">'.format(js)
        #    div = Div(text=html)
        #    st.bokeh_chart(div)
    

       

   
    
    
if __name__ == '__main__':
    main()
