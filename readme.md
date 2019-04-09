# Teste Cognitivo.ai

# Requerimentos
* Python >= 3.6 
* Instalar as dependências: pip install -r requirements.txt
* Arquivo credentials.json com as credenciais de acesso para a API Twitter e Amazon RDS

# Descrição
O código da rotina está no Jupyter Notebook [analise-explotoria.ipynb](https://github.com/rafpyprog/teste-cognitivo/blob/master/notebooks/analise-exploratoria.ipynb). Esta forma de apresentação
foi escolhida por permitir explicitar de forma mais clara o processo de desenvolvimento. O pacote /scr contém as principais funções
utilizadas, possibilitando a reutilização do código e a independência do ambiente de notebooks.

## Banco de Dados

![AWS RDS](https://1.bp.blogspot.com/-5HaWl2nXjtc/Vx9EPVBhwHI/AAAAAAAAEto/HffgsQazTgALl0MjjVE_pBaNX5QJjSN7ACLcB/s1600/Amazon-RDS%2B%25281%2529.png)

O banco de dados utilizado é uma instância do PostgreSQL hospedada na AWS RDS, ampliando as possibilidades de integração e escalabilidade do processo.


## API

![Heroku](https://duckduckgo.com/i/34840fda.png)

Para acesso aos dados em formato JSON, foi criada uma API utilizando Flask e hospedada no Heroku.

* Repositório: https://github.com/rafpyprog/topmobileapps
* Aplicação: https://topmobileapps.herokuapp.com/

## Limitações e possíveis melhorias
* Tratamento dos nomes dos aplicativos para aumentar o número de resultados encontrados, uma vez que nem sempre as citações utilizam
o nome completo do aplicativo. 
* Parametrização da API para receber o nome da tabela a ser buscada no banco de dados.
* Para implementação rápida foi utilizado apenas os limites disponíveis na API gratuita do Twitter, é possível obter mais dados
utilizando a API paga, ou ainda armazenando os dados utilizando o endpoint de streaming.
* Testes



