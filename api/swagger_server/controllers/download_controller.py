import connexion
import six

from swagger_server import util

from requests import get,post,put,delete
from io import StringIO
import pandas as pd
import configparser
import requests
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


# Download NYU Dataset
def download_data_location_dataset_id_get(data_location, dataset_id):
    
    # Redundant but good check
    if data_location == "NYU":

        nyu_download_url = f'https://{nyu_user}:{nyu_pwd}@wm.auctus.vida-nyu.org/api/v1/download/'
        nyu_downloaded = nyu.nyu_download(dataset_id, nyu_download_url)

    return nyu_downloaded

# Download ISI variables from a dataset to a new single dataset
def download_variables_data_location_dataset_id_post(body, data_location, dataset_id):
    
    # Redundant but good check
    if data_location == "ISI":

        datamart_api_url = f'https://{isi_user}:{isi_pwd}@dsbox02.isi.edu:8888/datamart-api-wm'
        isi_downloaded = isi.download_isi(body, data_location, dataset_id, datamart_api_url)
       
    return isi_downloaded


