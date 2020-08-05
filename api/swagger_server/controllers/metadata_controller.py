import connexion
import six

from swagger_server.models.metadata_result import MetadataResult  # noqa: E501
from swagger_server import util

from requests import get,post,put,delete
import configparser
import requests
import json
import os

import isi_functions as isi
import nyu_functions as nyu


import configparser

wrkDir = os.getcwd()
wrkDir = wrkDir + '/' 

config = configparser.ConfigParser()
configFile = wrkDir + 'config.ini'
config.read(configFile)

isi_user = config['ISI']['user']
isi_pwd = config['ISI']['password']
nyu_user = config['NYU']['user']
nyu_pwd = config['NYU']['password']

def metadata_data_location_id_value_get(data_location, id_value):  # noqa: E501

    #ISI
    isi_base_url = f'https://{isi_user}:{isi_pwd}@dsbox02.isi.edu:8888/datamart-api-wm'

    #NYU
    nyu_meta_url = f'https://{nyu_user}:{nyu_pwd}@wm.auctus.vida-nyu.org/api/v1/metadata/'

    if data_location == "ISI":
       result = isi_metadata(id_value, isi_base_url)

    if data_location == "NYU":

        result = nyu.nyu_metadata(id_value, nyu_meta_url)

    return result

def isi_metadata(id_value, isi_base_url):

    isi_meta_url = f'{isi_base_url}/metadata/datasets/'

    search_url = isi_meta_url + id_value
    response = get(search_url)

    json_string = response._content
    raw_meta = json.loads(json_string)

    isi_meta_results = isi.isi_schema_meta(raw_meta)

    return isi_meta_results       



