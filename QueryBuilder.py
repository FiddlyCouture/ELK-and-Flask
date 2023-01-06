from elasticsearchquerygenerator.elasticsearchquerygenerator import ElasticSearchQuery
import json

def queryBuilder(log, token, time, limit):
    helper = ElasticSearchQuery(size=limit, BucketName="Kibana", min_score=0.2)

        # match phrase
    query=helper.match(field="app", value=log, operation='must')

        #Match
    for  i in token.items():
        query=helper.match(field=i[0], value=i[1], operation='filter')
    

    if time:
        # add time range filter to the query
        query['query']['bool'] = {'filter': {'range': {'@timestamp': {'gte': time['gte'], 'lte': time['lte']}}}}

    # queries = (json.dumps(query, indent = 3))
    # print(query)
    
    return  query


    # log = "istio_proxy"
    # token = [('msg', 'msge'),('loc', 'locs')]
    # queryBuilder(log, token)

    
