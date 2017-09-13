
# coding: utf-8

# In[52]:


from elasticsearch import Elasticsearch
hosts = [
    {'host':'localhost', 'port':'9220', 'use_ssl':False}
]
client = Elasticsearch(hosts = hosts)

print('El cluster está {}'.format('activo' if searcher.ping() else 'inactivo'))


# In[79]:


# Permite realizar búsquedas usando el operador _search de elasticssearch
# La siguiente búsqueda busca tweets que son posts y no son retweets (límita la busqueda a 3 tweets)


from elasticsearch_dsl import Search, Q

searcher = Search(using = client)

result =searcher.query(Q('match', is_retweet = False)).execute()


tweets = result

for tweet in tweets:
    print('----')
    body = tweet.body
    texto = body[next(iter(body))]
    print(texto)


# In[78]:


# Esta es la misma consulta que la anterior, 
# solo que además se descartan los tweets que no son respuestas a otros tweets

from elasticsearch_dsl import Search, Q

searcher = Search(using = client)

# Se usan operadores para unir consultas
q1 = Q('match', is_retweet = False)
q2 = Q('match', is_reply = True)
q = q1 & q2
result =searcher.query(q).execute()


tweets = result

for tweet in tweets:
    print('----')
    body = tweet.body
    texto = body[next(iter(body))]
    print(texto)
    print('{}es un retweet'.format('' if tweet.is_retweet else 'no ')) 
    print('{}es una respuesta a otro mensaje'.format('' if tweet.is_reply else 'no ')) 

