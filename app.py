import pandas as pd
import streamlit as st
import numpy as np

import src.answers as asw
from src.extraction import load_data

st.set_page_config(layout="wide")


def create_dataframe_section(df):
    st.title("XGB - Database")
    st.markdown("## Dashbord de acompanhamento de metricas")

    st.sidebar.image('image.jpg')
    st.sidebar.markdown("### Xtreme Groovy Bikes")
    st.sidebar.markdown("Sua melhor moto, você encontra aqui")
    year = st.sidebar.slider("Selecione o ano de fabricação",df.loc[:,'year'].min(),df.loc[:,'year'].max(),
                             value=[df.loc[:,'year'].min(),df.loc[:,'year'].max()])

    km_rodado = st.sidebar.slider("Qual a kilometragem",value=[df.loc[:,'km_driven'].min(),df.loc[:,'km_driven'].max()])
    
    selecao = df['year'].isin(year)

    df = df.loc[selecao,:]
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Nº de motos na base", df.shape[0])
    
    with col2:
        st.metric("Modelo mais novo",df.loc[:,'year'].max())

    with col3:
        st.metric("Modelo mais velho",df.loc[:,'year'].min())
    
    with col4:
        st.metric("Média de kilometragem", "{:,}".format(int(df.loc[:,'km_driven'].mean())).replace(",",".")+" km")

    # col_1.header("Database")
    # col_1.dataframe(df, height=530)

#    col_2.header("Data Description")

#     data_description = """
#                         | Coluna | Descrição |
#                         | :----- | --------: |
#                         | ID | Identificador da linha/registro |
#                         | name | Fabricante e Modelo da Moto |
#                         | selling_price | Preço de Venda |
#                         | year | Ano de Fabricação da Moto |
#                         | seller_type | Tipo de Vendedor - Se é vendedor pessoal ou revendedor |
#                         | owner | Se é primeiro, segundo, terceiro ou quarto dono da moto |
#                         | km_driven | Quantidade de Quilometros percorrido pela moto |
#                         | ex_showroom_price | Preço da motocicleta sem as taxas de seguro e registro |
#                         | age | Quantidade de anos em que a moto está em uso |
#                         | km_class | Classificação das motos conforme a quilometragem percorrida |
#                         | km_per_year | Quantidade de Quilometros percorridos a cada ano |
#                         | km_per_month | Quantidade de Quilometros percorridos por mês |
#                         | company | Fabricanete da Motocicleta |
#     """

#     col_2.markdown(data_description)
def create_answers_section(df):
    st.title("Main Questions Answers")

    st.header("First Round")
    st.subheader(
        "How many bikes are being sold by their owners and how many bikes are being sold by distributors?"
    )
    asw.rd1_question_9(df)

    st.subheader("How many bikes are being sold are bikes from a unique owner?")
    asw.rd1_question_13(df)

    st.subheader(
        "Are high kilometer bikes more expensive than bikes with lower kilometer?"
    )
    asw.rd1_question_14(df)

    st.subheader(
        "Are the bikes with a unique owner more expense on avarege than the other bikes?"
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
