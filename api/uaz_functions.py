from requests import get,post,put,delete
import json
import pandas as pd
from io import StringIO

def urlify(endpoint, keywords, maxHits=100):

    keywords = keywords.split(" ")
    amp_keywords=[]

    for words in keywords:
        new_word = words.replace(" ", "%20")
        amp_keywords.append(new_word)

    keyword_string ='%20'.join(amp_keywords)
    maxit = f'&maxHits={maxHits}'
    search_url = endpoint + keyword_string + maxit
    
    return search_url

#Format response result to swagger schema
def schema_results_uaz(raw_uaz):
    
    schema_results = []
    temp_dict = {}

    for result in raw_uaz:

        data_location = result.get('datamartId', "None")
        dataset_id = result.get('datasetId', "None")
        score = result.get('score', "None")
        variable_id = result.get('variableId', "None")
        descr = result.get('variableDescription', "None")
    
        temp_dict= {"data_location": data_location,
                    "dataset_id": dataset_id,
                    "variable_id": variable_id,
                    "description": descr,
                    "score": score}

        schema_results.append(temp_dict)
     
    return schema_results
