import time

import tweepy


class CitationsCounter(tweepy.API):
    """ Abstração da API Twitter utilizada para realizar a autenticação e a busca
    por citaçãoes na rede social. """

    def __init__(self, consumer_key: str, consumer_secret: str):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        super().__init__(self.auth())

    def auth(self) -> tweepy.AppAuthHandler:
        """ Realiza a autenticação na API"""
        auth = tweepy.AppAuthHandler(self.consumer_key, self.consumer_secret)
        return auth

    def count_citations(
        self, query: str, count: int = 100, result_type: str = "recent"
    ) -> int:
        """ Busca tweets dos últimos 7 dias (Api Standard) e realiza a
        contagem de itens encontrados com o termo buscado. Tendo em vista
        a limitação da API gratuita limitamos a busca a apenas 100 resultados."""
        results = self.search(q=query, count=count, result_type=result_type)
        count = len(results)
        return count

    @property
    def rate_limit_renew(self) -> str:
        """ Retorna o data de renovação dos limites de requisição da API"""
        rate_limit = self.rate_limit_status()
        reset_epoch = rate_limit["resources"]["search"]["/search/tweets"]["reset"]
        renew_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(reset_epoch))
        return renew_time

    @property
    def remaining_rate_limit(self) -> int:
        """ Retorna a quantidade de requisições restantes até a próxima renovação
        dos limites da API """
        rate_limit = self.rate_limit_status()
        rate_limit = rate_limit["resources"]["search"]["/search/tweets"]["remaining"]
        return rate_limit
