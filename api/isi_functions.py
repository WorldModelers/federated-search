#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:13:55 2020

@author: travishartman
"""

############ SEARCH FUNCTIONS ############ 

import json
import copy
import requests
from requests import get,post,put,delete

# Function to send keywords to ISI search endpoint
def isi_search(body, base_url):
    
    # verify that the search has proper filters:
    param_errors = isi_search_validate(body)    
    
    if param_errors['error'] != []:
        return param_errors

    else:       
        
        # call urlify function to format url search string, searches " OR" keywords (not "and")
        search_url = urlify_search(body, base_url)
        #send get call to server
        response = get(search_url)

        json_string = response._content
        raw_results = json.loads(json_string)
        
        # call schema function to get into swagger format
        isi_results = isi_schema_results(raw_results)

        return isi_results


def isi_schema_results(raw_results):
    
    isi_schema = []
    temp_dict = {}
    
    for result in raw_results:
        data_location = "ISI Datamart"
        dataset_id = result['dataset_id']
        name = result['name']
        
        descr = "None"
        score = result['rank']
    
        temp_dict= {"data_location": data_location,
                    "id_value": dataset_id,
                    "name": name,
                    "description": descr,
                    "score": score}
        isi_schema.append(temp_dict)
        
    #schema_results = json.dumps(isi_schema_results, indent = 4)
    
    return isi_schema


# Currently (03AUG2020) ISI does not support temporal of bbox searches
# This function prints an "error" and exits search if filter has unsupported filters
def isi_search_validate(body):
    vlad = [] 

    get_data ={
            "geo": body['geo'].get("type", "None"),
            "keywords":  body.get("keywords", "None"),
            "time": body.get("time", "None")
              }
    
    if get_data['geo'] == "bbox":
        geo_error = 'Error: ISI does not support bounding box search. Enter--> type: place AND value: area_name: <place name>'
        vlad.append(geo_error)
    if get_data['time'] != "None":           
        time_error = 'Error: ISI does not support temporal searches; remove the time filter'        
        vlad.append(time_error)
        
    err = {"error": vlad}
    
    if err["error"] != []:
        for e in err["error"]:
            print(e)

    return err
 
# Take user's keywords and format into url string to send to ISI server    
def urlify_search(body, base_url):
    amp_keywords=[]
    
    for words in body['keywords']:
        new_word = words.replace(" ", "%20")
        amp_keywords.append(new_word)
    
    search_string ='&'.join(amp_keywords)
    
    search_url = base_url + search_string.strip() 
    
    return search_url


############ METADATA FUNCTIONS ############ 

    
def isi_schema_meta(raw_meta):

    #raw_meat is a list with one elem (a dict)
    raw_dict = raw_meta[0]
    name = raw_dict['name']
    descr = raw_dict['description']
    id_value = raw_dict['dataset_id']
    url = raw_dict['url']
    source = "None"
    temporal_resolution = "None"
    spatial_resolution = "None"
    z_meta = "None"

    isi_meta_results = {"data_location": "ISI",
                        "name": name,
                        "description": descr,
                        "id_value": id_value,
                        "source": url,
                        "temporal_resolution": temporal_resolution,
                        "spatial_resolution": spatial_resolution,
                        "z_meta": z_meta 
                        }
    
    return isi_meta_results


############ DOWNLOAD FUNCTION ############# 

      
