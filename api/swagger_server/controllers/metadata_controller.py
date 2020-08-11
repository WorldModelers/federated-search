import connexion
import six

from swagger_server.models.metadata_result import MetadataResult
from swagger_server import util

from requests import get,post,put,delete
import configparser
import requests
import json
import os

import isi_functions as isi
import nyu_functions as nyu


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


# Either ISI/NYU: get metadata for variable/dataset
def metadata_data_location_id_value_get(data_location, id_value):
    
    #NYU
    if data_location == "NYU":
        
        nyu_meta_url = f'https://{nyu_user}:{nyu_pwd}@wm.auctus.vida-nyu.org/api/v1/metadata/'
        result = nyu.nyu_metadata(id_value, nyu_meta_url)    

    #ISI
    if data_location == "ISI":

       isi_base_url = f'https://{isi_user}:{isi_pwd}@dsbox02.isi.edu:8888/datamart-api-wm'    	
       result = isi.isi_metadata(id_value, isi_base_url)

    return result 
