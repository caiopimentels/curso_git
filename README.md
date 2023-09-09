# Curso de Git
Este repositório foi criado para hospedar o esqueleto do projeto que será utilizado para explicar e ensinar o uso básico do Git dentro da Comunidade DS

# 1. Problema de négocios
Xtreme Groovy Bikes Sales é uma empresa de revenda de motocicletas. Seu modelo de nogócio é revender motocicletas usadas. Com a crescente do valor dos veículos usados, a XGB Sales, como é conhecida, deseja expandir os seus negócios. Você foi contratado como cientista de dados pela empresa XGB Sales para ajudá-los a encotrar as melhores motocicletas para revenda. 

Para isso, o CEO da empresa fez um estudo de mercado lhe entregou uma base de dados, obtida através desse estudo, para que você consiga auxiliá-lo a encontrar as melhores motocicletas para revenda, aumentando assim o lucro da empresa.

Dessa forma, o CEO da XGB Sales lhe fez as seguintes perguntas:

## 1. Primeira rodada
    1. Quantas motos temos dentro do Dataset?
    2. Qual é o ano da moto mais antiga da base de dados?
    3. Qual é o ano da moto mais nova da base de dados?
    4. Qual é o valor da moto mais cara da base de dados?
    5. Qual é o valor do hodômotro da moto com a maior quilometragem?
    6. Qual é o valor do hodômotro da moto com a menor quiilometragem?
    7. Das motocicletas que estão sendo expostas dentro de um Show Room, qual é o maior valor registrado na base de dados?
    8. Das motocicletas que estão sendo expostas dentro de um Show Room, qual é o menor valor registrado na base de dados?
    9. Quantas motocicletas estão sendo vendidades pelos seus donos e quantas estão sendo vendidas por outros revendedores?
    10. Qual é a média de valores das motos na base de dados?
    11. Qual é a média de ano das motos cadastradas dentro da base de dados?
    12. Qual é a média de quilometragem das motos cadastradas dentro da base de dados?
    13. Existem quantas motos dentro da base de dados que são motos de um único dono?
    14. As motos com menor quilometragem são as motos mais baratas do Dataset?

## 2. Segunda rodada
    1. As motos que possuiram somente 1 dono são as motos mais caras na média que as motos que tiveram mais donos?
    2. As motos que possuiram mais donos são as motos que possuem quilometragem média maior que as motos que possuiram menos donos?
    3. As motos que possuiram mais donos são as motos mais velhas na média?
    4. As motos que são vendidas por revendedores são as motos mais caras na média do que as motos vendidas pelos seus donos?
    5. O CEO lhe entregou um novo dataset chamado companies.csv, onde estão todas as fabricantes de motocicletas. Adicione uma coluna no DataFrame com o nome de company. Essa coluna deve possuir o nome do fabricante de cada moto do DataFrame.
    6. Crie um novo dataset chamado bikes_completed.csv a partir do DataFrame com a coluna company preenchida.
    7. Quais são so fabricantes que mais possuem motos cadastradas na base de dados completa?

## 3. Terceira rodada
    1. Ajustar a coluna `name` para que ela fique somente com o nome da moto.
    2. Qual das fabricantes possui o maior preço médio de suas motos?
    3. Qual o fabricante que possui a moto com o maior quilometragem?
    4. Qual o fabricante que possui a moto mais velha?
    5. O fabricante que possui a moto mais cara do Dataset é também o fabricante que possui menos motos cadastradas?
    6. Qual o fabricante que possui a menor variação de valor de venda?
    7. Quais motos eu devo comprar? 
    - Levando em conta que eu desejo motos com no máximo 3 anos de uso; no máximo 40 mil quilometros rodados; que sejam de um único dono; que estejam sendo vendidas por possoas físicas e que tenham o valor pretendido de venda menor que o valor do showroom. Envie um relatório contendo o modelo, preço de venda, quilometro rodado e ano, ordenado por valor de venda de forma decrescente para o meu e-mail.

# 2. Premissas assumidas
    1. A empresa XGB é uma empresa de revenda de motocicletas
    2. As visões geradas no dashboard foram de acordo com as perguntas de négocios do CEO
    3. A análise apresentada não dispõe de um período para análise.

# 3. Estratégias da solução
Criação de um dashbord online que mensura as principais metricas solicitadas pelo CEO, divido por cada rodada de perguntas.

# 4. Top 3 insgths de dados
    1. A maior parte das motos cadastradas vieram de donos pessoa física
    2. O número de donos que uma moto teve não tem ligação direta com a sua faixa de preço
    3. O ano da moto não significa que a mesma é a mais rodada, tendo motos mais velhas com quilometragem mais baixa

# 5. O produto do projeto
Um dashbord hospedado em cloud apresentando as principais dúvidas do CEO que pode ser acessado por qualquer dispositivo conectado a internet.

O dashbord pode ser acessado através do link: https://curso-git-cp.streamlit.app/

# 6. Conclusão
O objetivo foi criar um dashbord aonde o CEO pudesse verificar as principais metricas de négocio para uma tomada de decisão mais acertiva.  