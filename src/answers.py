import pandas as pd
import plotly.expresss as px
import streamlit as st

def rd1_quetao_9(df):
    df_grouped = df1[['id', 'seller_type']].groupby('seller_type')

    df_grouped = df_grouped.count().reset_index()

    df_grouped = df_grouped.rename(columns={'id': 'count'})

    df_grouped

    print(f'Dessa forma, temos {df_grouped.loc[0, "count"]} motos sendo vendidas por revendedores')
    print(f'E temos {df_grouped.loc[1, "count"]} motos sendo vendidas por seus donos')

    ax = sns.barplot(
        data = df_grouped,
        x = 'seller_type',
        y = 'count'
    )

    ax.bar_label(ax.containers[0])

    ax.set(
        title = 'Quantidade de Tipos de Vendendores',
        xlabel = 'Tipos de Vendedores',
        ylabel = 'Quantidade'
    );

    return None

def rd1_questao13(df):
    unico_dono = df1[df1['owner'] == '1st owner'].shape[0]
    unico_dono

    print(f'A base de dados possui {unico_dono} motos de um único dono')

    df_grouped = df1.groupby('owner').agg(
        qty = pd.NamedAgg('id', 'count')
    ).sort_values('qty').reset_index()

    ax = sns.barplot(
        data=df_grouped,
        x = 'owner',
        y = 'qty'
    )

    ax.bar_label(ax.containers[0])

    ax.set(
        title = 'Quantidade de Motos por tipo de dono',
        xlabel = 'Tipo de Dono',
        ylabel = 'Quantidade de donos'
    );
    return None

def rd1_questao14(df):
    df1['km_class'] = df1['km_driven'].apply( lambda km_driven: create_km_class(km_driven) )
    len(df1['km_class'].unique())
    df_grouped = df1[['km_class', 'selling_price']].groupby('km_class')

    df_grouped = df_grouped.mean().sort_values('selling_price', ascending=False).reset_index()

    ax = sns.barplot(
    data = df_grouped,
    x = 'km_class',
    y = 'selling_price'
    )

    ax.set(
    title = 'Média de Preço das Motocicletas agrupadas por classe',
    xlabel = 'Classe de Quilemtros percorridos (5 mil Km percorrido por classe)',
    ylabel = 'Preço Médio de venda'
    )

    ax = sns.scatterplot(
    data = df1,
    x = 'km_driven',
    y = 'selling_price',
    )

    ax.set(
        title = 'Relação entre Preço de Venda e Quilemetros Percorridos',
        xlabel = 'Quilemetros Percorridos',
        ylabel = 'Preço de Venda'
    );

    print(f'Conforme podemos observar em ambos os gráficos, as motos que possuem mais quilometragem percorrida, são as mais baratas')

    return None