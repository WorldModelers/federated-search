import connexion
import six

from swagger_server import util

import configparser
import requests
import os
from requests import get,post,put,delete

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


def download_data_location_id_value_get(data_location, id_value):  # noqa: E501
    # Download datasets

    
    if data_location == "NYU":
        nyu_download_url = f'https://{nyu_user}:{nyu_pwd}@wm.auctus.vida-nyu.org/api/v1/download/'
        nyu_downloaded = nyu_download(id_value, nyu_download_url)
       
    return nyu_downloaded    

    #if data_location == "ISI":
   # 	isi_download_url = 




#/datasets/dataset_id/variables?variable=variable_id