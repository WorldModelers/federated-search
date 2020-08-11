import connexion
import six

from swagger_server.models.body import Body
from swagger_server.models.search_result import SearchResult
from swagger_server import util

import configparser
import requests
import os

import nyu_functions as nyu
import isi_functions as isi


# Get Credentials
wrk_dir = os.getcwd()
wrk_dir = wrk_dir + '/' 

config = configparser.ConfigParser()
configFile = wrk_dir + 'config.ini'
config.read(configFile)

isi_user = config['ISI']['user']
isi_pwd = config['ISI']['password']
nyu_user = config['NYU']['user']
nyu_pwd = config['NYU']['password']


# Search for UAZ concept indicators 
def search_concepts_concept_name_get(concept_name):

    tbd = "WORK IN PROGRESS...Your concept is: " + concept_name

    result = [ {"TBD": tbd},
               {"data_location": "TBD",
               "description": "TBD",
               "id_value": "TBD",
               "name": "TBD",
               "score": "TBD"
               }
               ]
    
    return result


# Search over Datamarts to find datasets and variables of interest.
def search_post(body):
    
    # verify correct format
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())

    # NYU Search
    if body['data_location'] == "NYU":
        
        nyu_search_url = f'https://{nyu_user}:{nyu_pwd}@wm.auctus.vida-nyu.org/api/v1/search'
        nyu_search_results = nyu.nyu_search(body, nyu_search_url)
        
        return nyu_search_results

    # ISI Search
    if body['data_location'] == "ISI": 

        isi_search_url= f'https://{isi_user}:{isi_pwd}@dsbox02.isi.edu:8888/datamart-api-wm/metadata/variables?keyword=' 
        isi_search_results = isi.isi_search(body, isi_search_url)

        return isi_search_results







