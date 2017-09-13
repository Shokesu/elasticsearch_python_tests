
# coding: utf-8

# In[36]:


from elasticsearch import Elasticsearch
hosts = [
    {'host':'localhost', 'port':'9220', 'use_ssl':False}
]
searcher = Elasticsearch(hosts = hosts)

result = searcher.get(index='shokesu', doc_type='posts', id=['58f948e85f57fe0ae467dd2d'])
mensaje = result['_source']['body']['es']
retweet_count = result['_source']['retweet_count']
print('----')
print(mensaje)
print('----')
print('Retwiteado {} veces'.format(retweet_count))


# In[43]:


result = searcher.info()
print('Status: {}'.format(result['status']))
print('Nombre del cluster: {}'.format(result['cluster_name']))


# In[62]:



ids = ['58f948ed5f57fe0ae467dd39', '58f8dfd25f57fe0b5bf7775c']
result = searcher.mget(index='shokesu', doc_type='posts',
                       body = {'ids':ids})

tweets = result['docs']

for tweet in tweets:
    print('----')
    print(tweet['_source']['body']['es'])

    

