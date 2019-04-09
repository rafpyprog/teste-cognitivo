import datetime

import pandas as pd
import sqlalchemy


def upload_data_to_db(
    df: pd.DataFrame,
    user: str,
    password: str,
    host="cognitivo.cfz4dq8w2iii.us-east-1.rds.amazonaws.com",
    dbname="cognitivo",
) -> None:
    """ Faz upload do dataframe no banco de dados. Caso a tabela já exista os
    dados serão sobrescritos. O nome da tabela gerada segue o padrão:
    citacao_AAAAMMDD """

    engine = sqlalchemy.create_engine(
        f"postgresql://{user}:{password}@{host}:5432/{dbname}"
    )

    table_name = f"citacoes_{datetime.date.today().strftime('%Y%m%d')}"
    dataset.to_sql(
        table_name, con=engine, if_exists="replace", schema="app", index=False
    )
