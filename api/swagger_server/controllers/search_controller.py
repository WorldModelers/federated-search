import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.search_result import SearchResult  # noqa: E501
from swagger_server import util

import configparser
import requests
import os

import nyu_functions as nyu
import isi_functions as isi


# Get Credentials
wrkDir = os.getcwd()
wrkDir = wrkDir + '/' 

config = configparser.ConfigParser()
configFile = wrkDir + 'config.ini'
config.read(configFile)

isi_user = config['ISI']['user']
isi_pwd = config['ISI']['password']
nyu_user = config['NYU']['user']
nyu_pwd = config['NYU']['password']


def search_concepts_concept_name_get(concept_name):  # noqa: E501
    """Concept based search

    Search based on concepts from the [World Modelers Ontology](https://github.com/worldmodelers/ontologies)  # noqa: E501

    :param concept_name: World Modelers ontology concept
    :type concept_name: str

    :rtype: SearchResult
    """

    result = "WORK IN PROGRESS...Your concepts are: " + concept_name

    return result


def search_post(body):  # noqa: E501
    #Search over Datamarts in order to find datasets and variables of interest.
    # Must provide data_location and _should_ provide at least one a [geo, temporal, keyword]

    # Set single source of server/endpoint data:
    # ISI  
    isi_search_url= f'https://{isi_user}:{isi_pwd}@dsbox02.isi.edu:8888/datamart-api-wm/metadata/variables?keyword=' 

 
    # NYU
    nyu_search_url = f'https://{nyu_user}:{nyu_pwd}@wm.auctus.vida-nyu.org/api/v1/search'

    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())

    if body['data_location'] == "NYU":
        
        nyu_search_results = nyu.nyu_search(body, nyu_search_url)
        
        return nyu_search_results

    if body['data_location'] == "ISI": 
        
        isi_search_results = (isi.isi_search(body, isi_search_url))

        return isi_search_results