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

    min_year = int(df.loc[:,'year'].min())
    max_year = int(df.loc[:,'year'].max())

    year_selecao = st.sidebar.slider("Ano de fabricação", min_year, max_year, min_year)

    min_km = int(df.loc[:,'km_driven'].min())
    max_km = int(df.loc[:,'km_driven'].max())
    
    km_rodado = st.sidebar.slider("Quilometragem", min_km, max_km, min_km)
    
    fabricante = st.sidebar.multiselect("Fabricante",df.loc[:,'company'].unique(),df.loc[:,'company'].unique())

    selecao = df['company'].isin(fabricante)
    df = df.loc[selecao,:]

    selecao = df['year'].between(year_selecao.min(), year_selecao.max())
    df = df.loc[selecao,:]

    selecao = df['km_driven'].between(km_rodado.min(), km_rodado.max())
    df = df.loc[selecao,:]
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Nº de motos na base", df.shape[0],help="Com base no filtro aplicado")
    
    with col2:
        st.metric("Modelo mais novo",df.loc[:,'year'].max(),help="Com base no filtro aplicado")

    with col3:
        st.metric("Modelo mais velho",df.loc[:,'year'].min(),help="Com base no filtro aplicado")
    
    with col4:
        st.metric("Média de quilometragem", "{:,}".format(int(df.loc[:,'km_driven'].mean())).replace(",",".")+" km",
                  help="Com base no filtro aplicado")
    return df

def create_answers_section(df):
    st.markdown("---")
    st.header("Gráficos")
    st.subheader(
        "Distribuição das motos anunciadas"
    )
    asw.rd1_question_9(df)

    st.subheader("Motos por número de donos")
    asw.rd1_question_13(df)

    st.subheader(
        "Faixa de preço por quilometragem"
    )
    asw.rd1_question_14(df)

    st.subheader(
        "Faixa de preço por número de donos"
    )
    asw.rd2_question_1(df)

    st.subheader(
        "Quilometragem média por número de donos"
    )
    asw.rd2_question_2(df)

    st.subheader("Quantidade de motos por fabricante")
    asw.rd2_question_7(df)

    st.subheader("Preço médio por fabricante")
    asw.rd3_question_2(df)

    st.subheader(
        "Quantidade de motos por valor por fabricante"
    )
    asw.rd3_question_5(df)

    st.subheader("Data base com base nos paramentros selecionados")
    asw.rd3_question_7(df)


def create_main_layout():
    df = load_data()

    create_dataframe_section(df)

    create_answers_section(df)


if __name__ == "__main__":
    create_main_layout()