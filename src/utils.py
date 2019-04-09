import json
import os


def load_credentials(credentials_file: os.PathLike) -> dict:
    """ Carrega um arquivo .json contendo as credenciais de acesso da API Twitter e AWS RDS
    retorna como um dicionário """
    with open(credentials_file) as f:
        return json.load(f)


def quote(app_name: str) -> str:
    """ Retorna a string entre aspas para busca do termo extato na API """
    return f'"{app_name}"'
