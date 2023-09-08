import pandas as pd
import streamlit as st
import numpy as np

import src.answers as asw
from src.extraction import load_data

st.set_page_config(layout="wide")


def create_dataframe_section(df):
    st.title("XGB - Database")
    st.markdown("## Dashbord de acompanhamento de metricas")
    st.markdown("---")

    st.sidebar.image('image.jpg')
    st.sidebar.markdown("### Xtreme Groovy Bikes")
    st.sidebar.markdown("Sua melhor moto, você encontra aqui")

    year = st.sidebar.slider("Ano de fabricação",df.loc[:,'year'].min(),df.loc[:,'year'].max(),
                             value=[df.loc[:,'year'].min(),df.loc[:,'year'].max()])

    km_rodado = st.sidebar.slider("Kilometragem",value=[df.loc[:,'km_driven'].min(),df.loc[:,'km_driven'].max()])
    
    selecao = df['year'].between(*year)
    df = df.loc[selecao,:]

    selecao = df['km_driven'].between(*km_rodado)
    df = df.loc[selecao,:]
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Nº de motos na base", df.shape[0],help="Com base no filtro aplicado")
    
    with col2:
        st.metric("Modelo mais novo",df.loc[:,'year'].max(),help="Com base no filtro aplicado")

    with col3:
        st.metric("Modelo mais velho",df.loc[:,'year'].min(),help="Com base no filtro aplicado")
    
    with col4:
        st.metric("Média de kilometragem", "{:,}".format(int(df.loc[:,'km_driven'].mean())).replace(",",".")+" km",
                  help="Com base no filtro aplicado")

def create_answers_section(df):
    st.markdown("---")
    st.header("Gráficos")
    st.subheader(
        "Distribuição das motos anunciadas"
    )
    asw.rd1_question_9(df)

    st.subheader("Anúncios de unico dono")
    asw.rd1_question_13(df)

    st.subheader(
        "Faixa de preço por kilometragem"
    )
    asw.rd1_question_14(df)

    st.subheader(
        "Faixa de preço por número de donos"
    )
    asw.rd2_question_1(df)

    st.subheader(
        "Are the bikes that have more owners also the bikes with more kilometers traveled on avarege?"
    )
    asw.rd2_question_2(df)

    st.subheader("Which company has the most bikes registered?")
    asw.rd2_question_7(df)

    st.subheader("Which company has the most expensive bikes on avarege?")
    asw.rd3_question_2(df)

    st.subheader(
        "Are the company that has the most expensive bikes registered also the company with the most bikes registered?"
    )
    asw.rd3_question_5(df)

    st.subheader("Which bikes are good for buying?")
    asw.rd3_question_7(df)


def create_main_layout():
    df = load_data()

    create_dataframe_section(df)

    create_answers_section(df)


if __name__ == "__main__":
    create_main_layout()
