#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:13:55 2020

@author: travishartman
"""

from itertools import chain
from requests import get,post,put,delete
import requests
import json
import copy


########### SEARCH FUNCTIONS ###########

# Search for keywords, temporal intervals, and/or geospatial areas
def nyu_search(body, nyu_url): 

    # Copy dict to maintain original user search BODY
    new_body = copy.deepcopy(body) 

    #init empty dicts to check if NOT {} --> add to search
    keywords = []
    checked = []

    #add search to relevant dict to be checked if null
    geo = {}
    time = {}
    keywords = {}

    # Run thru all BODY keys and build search dict which is sent to NYU server
    for key in new_body.keys():
        
        if key == "keywords":
            keywords = new_body["keywords"]

        # GEO search requires geo "variable"
        if key == "geo":
            geo_type = new_body["geo"]["type"]

            # BOUNDING BOX dict
            if geo_type == "bbox":
                geo = new_body["geo"]["value"]["bbox"]
                geo["type"] = "geospatial_variable"

            # PLACE search (wiki admin name)
            if geo_type == "place":
                geo = new_body["geo"]["value"]["place"]
                geo["type"] = "geospatial_variable"

        # Time search requires geo "variable"
        if key == "time":
            time = new_body["time"]  
            time["type"]= "temporal_variable"
              
    # Must have at least one search parameter beyond "data_location"
    null_check = [keywords, geo, time]
    tah = [x for x in null_check if x != {}]

    if len(tah) == 0:
        err = {"Search requires at least one parameter besides data_location"}
        return f'{err}', 405, {'x-error': 'method not allowed'}

    else:
        #check for data and format query key "variables" into list of dicts
        checker = [geo,time]
        checked = [x for x in checker if x != {}]
        
        all_keywords_nyu = []
        for words in keywords:
            query = [{
                    "keywords": words,
                    "variables": checked
                     }]

            #  call server
            #print(f'query: {query}')
            response = requests.post(nyu_url, data={'query': json.dumps(query[0])})
            response.raise_for_status()
            raw_results = response.json()['results']

            #format to schema
            nyu_results = schema_results(raw_results)
            all_keywords_nyu.append(nyu_results)

        all_keywords_nyu = list(chain.from_iterable(all_keywords_nyu))
        
        nyu_search_results = delete_min_score(all_keywords_nyu)
           
        return nyu_search_results


# delete duplicates returned from multiple keyword searches and return HIGHEST score
def delete_min_score(results):
    
    # list of dataset_ids
    ids = [_id["dataset_id"] for _id in results]

    # count occurences of each dataset_id and get index   
    occ = [(i, ids.count(i)) for i in ids]
    index_list = [ (occ[i][0], i) for i in range(len(occ)) if occ[i][1] >1 ]
    
    scored = []
    for duped in index_list:
        ind = duped[1]
        score = results[ind]['score']
        scored.append((ind, score))  
    
    if scored != []:
        #ridiculous
        score_min = 1000000

        #find min score
        for i in scored:
            ind_ = i[0]
            temp_score = i[1]
            if temp_score < score_min:
                score_min = temp_score
                min_ind = ind_

        print(f'Deleted Duplicate: {results[min_ind]}')
        del results[min_ind] 
        return results
    
    #nothing to delete...
    else:
        print(f'No Duplicates found')      
        return results


#Format response result to swagger schema
def schema_results(raw_results):
    
    schema_results = []
    temp_dict = {}
    
    for result in raw_results:
        data_location = "NYU Datamart"
        dataset_id = result.get('id', "None")
        name = result['metadata'].get('name', "None")
        score = result.get('score', "None")

        descr = "None"
        if "description" in result['metadata'].keys():
            descr = result['metadata'].get('description', "None")
    
        temp_dict= {"data_location": data_location,
                    "dataset_id": dataset_id,
                    "name": name,
                    "description": descr,
                    "score": score}

        schema_results.append(temp_dict)

     
    return schema_results


########### METADATA FUNCTIONS ###########

# Make API call for raw metadata results and return swagger schema for output
def nyu_metadata(dataset_id, nyu_meta_url):
    
    response = requests.get(nyu_meta_url + dataset_id)
    response.raise_for_status()
    response.json()  

    json_string = response._content
    raw_meta = json.loads(json_string)
    
    nyu_meta_results = nyu_schema_meta(raw_meta)

    return nyu_meta_results


 #Transform raw result to swagger schema
def nyu_schema_meta(raw_meta):
    
    name = raw_meta['metadata'].get('name', "None")
    descr = raw_meta['metadata'].get('description', "None")
    dataset_id = raw_meta.get('id', "None")
    source = raw_meta['metadata'].get('source', "None")
    spatial_resolution = raw_meta['metadata']['spatial_coverage'][0].get('admin', "None")
    meta = raw_meta.get('metadata', "None")

    temporal_resolution = "None"
    for elem in raw_meta['metadata']['columns']:
        if elem['name'] == "date":
            temporal_resolution = elem.get('temporal_resolution', "None")
    
    nyu_meta_results = {"data_location": "NYU",
                        "name": name,
                        "description": descr,
                        "dataset_id": dataset_id,
                        "source": source,
                        "temporal_resolution": temporal_resolution,
                        "spatial_resolution": spatial_resolution,
                        "z_meta": meta 
                        }
                 
    return nyu_meta_results   
     
############ DOWNLOAD FUNCTION ############# 

# Download NYU dataset with known dataset_ID)
def nyu_download(dataset_ID, nyu_download_url):

    response = requests.get(nyu_download_url + dataset_ID)
    response.raise_for_status()
    downloaded = response.content
    
    return downloaded 
