#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:13:55 2020

@author: travishartman
"""

from requests import get,post,put,delete
from io import StringIO
import pandas as pd
import configparser
import requests
import json
import copy
import os


############ SEARCH FUNCTIONS ############ 

# Search ISI API
def isi_search(body, base_url):

    # verify that the search has proper (and at least one) parameter(s)
    param_errors = isi_search_validate(body)  

    if param_errors != []:
        return f'{param_errors}', 405, {'x-error': 'method not allowed'}

    else:
        # KEYWORD SEARCH
        # call urlify function to format url search string, searches " OR" keywords (not "and")
        search_url = urlify_search_keywords(body, base_url)
        
        print(search_url)

        #send get call to server
        response = get(search_url)
        json_string = response._content
        raw_results = json.loads(json_string)
        
        # call schema function to get into swagger schema format
        isi_keyword_results = isi_schema_results(raw_results)

        return isi_keyword_results
  

# transform raw return into schema format
def isi_schema_results(raw_results):
    
    isi_schema = []
    temp_dict = {}
    for result in raw_results:
        
        data_location = "ISI Datamart"
        dataset_id = result.get('dataset_id', "None")
        variable_id = result.get('variable_id', "None")
        name = result.get('name', "None")
        descr = "None"
        score = result.get('rank', "None")
    
        temp_dict= {"data_location": data_location,
                    "dataset_id": dataset_id,
                    "variable_id": variable_id,
                    "name": name,
                    "description": descr,
                    "score": score}
        
        isi_schema.append(temp_dict)
    
    # Testing...    
    # schema_results = json.dumps(isi_schema_results, indent = 4)
    
    return isi_schema


# Currently (05AUG2020) ISI does not support temporal of bbox searches
# This function prints an "error" and exits search if filter has unsupported filters
def isi_search_validate(body):

    vlad= []
    get_data ={"keywords": body.get("keywords", {}),
               "geo": body.get('geo', {}).get('type', {}),
               "time": body.get("time", {})
              }       

    #overall check, ensure not null search
    tah = [v for k,v in get_data.items() if v != {}]

    if len(tah) == 0:
        err = "Search requires at least one parameter besides data_location"
        vlad.append(err)

    else:
        #Check for specific keys
        if get_data['geo'] == 'bbox':
            geo_error = 'Error: ISI does not support bounding box searches; remove the bbox filter.'
            vlad.append(geo_error)
        
        if get_data['time'] != {}:           
            time_error = 'Error: ISI does not support temporal searches; remove the time filter'     
            vlad.append(time_error)
 
    return vlad 

# Take user's keywords and format into url string to send to ISI server    
def urlify_search_keywords(body, base_url):
  
    # base_url: ...        /metadata/variables?
    # keywords ONly        /metadata/variables?keyword=
    # Country Only:        /metadata/variables?country=Ethiopia
    # Keyword and Country: /metadata/variables?keyword=road&country=Ethiopia

    amp_keywords=[]

    keywords = body.get('keywords', "None")
    
    if body.get('geo', "None") != "None":
        if body['geo']['type'] == 'place':
            country = body['geo']['value']['place']['area_name']
    else:
        country = "None"

    # Keywords and maybe Country:    
    if keywords != "None":
        for words in body['keywords']:
            new_word = words.replace(" ", "%20")
            amp_keywords.append(new_word)
        
        keyword_string ='&'.join(amp_keywords).strip()
        
        if country != "None":
            keyword_string =  keyword_string.strip() + '&country=' + country

        search_url = base_url + 'keyword=' + keyword_string

    # Country ONLY:    
    if keywords == "None" and country != "None":

        search_url =  base_url + 'country=' + country

    return search_url

############ METADATA FUNCTIONS ############ 

# Query ISI for metadata about a variable
def isi_metadata(dataset_id, variable_id, isi_base_url):
    print(dataset_id, variable_id)
    if variable_id == None:
        isi_meta_url = f'{isi_base_url}/metadata/datasets/'
        search_url = isi_meta_url + dataset_id
        response = get(search_url)

        json_string = response._content
        raw_meta = json.loads(json_string)

        isi_meta_results = isi_schema_meta(raw_meta, variable_id)
        print(isi_meta_results)
        return isi_meta_results 

    if variable_id != None:

        search_url = f'{isi_base_url}/metadata/datasets/{dataset_id}/variables/{variable_id}'
        response = get(search_url)

        json_string = response._content
        raw_meta = json.loads(json_string)

        isi_meta_results = isi_schema_meta(raw_meta, variable_id)

        return isi_meta_results     



 #response = get(f'{isi_base_url}/metadata/datasets/{dataset_id}/variables/{variable_id}')
# format raw results to schema    
def isi_schema_meta(raw_meta, variable_id):

    if variable_id == None:
        #raw_meta is a list with one elem (a dict)
        raw_dict = raw_meta[0]
        name = raw_dict['name']
        descr = raw_dict['description']
        dataset_id = raw_dict['dataset_id']
        url = raw_dict['url']
        source = "None"
        temporal_resolution = "None"
        spatial_resolution = "None"
        z_meta = "None"

        isi_meta_results = {"data_location": "ISI",
                            "name": name,
                            "description": descr,
                            "dataset_id": dataset_id,
                            "source": url,
                            "temporal_resolution": temporal_resolution,
                            "spatial_resolution": spatial_resolution,
                            "z_meta": z_meta 
                            }
        
        return isi_meta_results

    if variable_id != None:
        #unlike above, raw meta is already a dict...
        raw_dict = raw_meta

        name = raw_dict.get('name', "None")
        descr = raw_dict.get('description', "None")
        dataset_id = raw_dict.get('dataset_id', "None")
        variable_id = raw_dict.get('variable_id', "None")
        source = "None"
        temporal_resolution = "None"
        spatial_resolution = "None"
        z_meta = {'corresponds_to_property': raw_dict.get('corresponds_to_property', "None"), 'qualifier':raw_dict.get('qualifier', "None") }

        isi_meta_results = {"data_location": "ISI",
                            "name": name,
                            "description": descr,
                            "dataset_id": dataset_id,
                            "variable_id": variable_id,
                            "source": source,
                            "temporal_resolution": temporal_resolution,
                            "spatial_resolution": spatial_resolution,
                            "z_meta": z_meta 
                            }
        
        return isi_meta_results

############ DOWNLOAD FUNCTION ############# 

# send list of variables to ISI API to download a dataset
def download_isi(body, data_location, dataset_id, datamart_api_url):

    df_all_variables = pd.DataFrame()
    
    variable_ids = body

    if variable_ids == []:
        err = {"Search requires at least one variable"}
        return f'{err}', 405, {'x-error': 'method not allowed'}
    
    else:
        for var in variable_ids:

            response = get(f'{datamart_api_url}/datasets/{dataset_id}/variables/{var}')
            df = pd.read_csv(StringIO(response.text))
            
            #if first variable...
            if df_all_variables.shape[0] == 0:
                df_all_variables = df

            else:
                df_all_variables = df_all_variables.append(df)

        #clean it up and covert to csv
        df_all_variables = df_all_variables.reset_index().drop(columns=['index'])
        df_all_variables = df_all_variables.to_csv()     

        return df_all_variables      
