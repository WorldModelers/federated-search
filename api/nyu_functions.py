import json
import copy
import requests
from requests import get,post,put,delete


########### SEARCH FUNCTIONS ###########

def nyu_search(body, nyu_url): 

    # Copy dic to maintain original user serach BODY
    new_body = copy.deepcopy(body) 

    #init empty dicts to check if NOT {} --> add to search
    keywords = []
    checked = []

    #add search to relevant dict to be checked if null
    geo = {}
    time = {}

    # Run thru all BODY keys and buld search dict which is sent to NYU server
    for key in new_body.keys():

        if key == "keywords":
            keywords = new_body["keywords"]

        # GEO search is an either/or....bbox OR place
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

        if key == "time":

            time = new_body["time"]  
            time["type"]= "temporal_variable"
              
    #query key "variables" takes a list of dicts
    checker = [geo,time]
    checked = [x for x in checker if x != {}]
  
    query = [{
            "keywords": keywords,
            "variables": checked
             }, "NYU Datamart"]

    response = requests.post(nyu_url, data={'query': json.dumps(query[0])})
    response.raise_for_status()
    raw_results = response.json()['results']   
    
    #call function to format via schema
    nyu_results = schema_results(raw_results)
    
    return nyu_results

#Format response result to swagger schema
def schema_results(raw_results):
    
    schema_results = []
    temp_dict = {}
    
    for result in raw_results:
        data_location = "NYU Datamart"
        dataset_id = result['id']
        name = result['metadata']['name']
        
        descr = "None"
        if "description" in result['metadata'].keys():
            descr = result['metadata']['description']
        
        score = result['score']
    
        temp_dict= {"data_location": data_location,
                    "id_value": dataset_id,
                    "name": name,
                    "description": descr,
                    "score": score}
        schema_results.append(temp_dict)
        
    #schema_results = json.dumps(schema_results, indent = 4) 
     
    return schema_results


########### METADATA FUNCTIONS ###########

# Make API call for raw metadata results and return swagger schema for output
def nyu_metadata(id_value, nyu_meta_url):
    
    response = requests.get(nyu_meta_url + id_value)
    response.raise_for_status()
    response.json()  

    json_string = response._content
    raw_meta = json.loads(json_string)
    
    nyu_meta_results = nyu_schema_meta(raw_meta)

    return nyu_meta_results


 #Transform raw result to swagger schema
def nyu_schema_meta(raw_meta):
    
    name = raw_meta['metadata']['name']
    descr = raw_meta['metadata']['description']
    id_value = raw_meta.get('id', "None")
    source = raw_meta['metadata'].get('source', "None")
    temporal_resolution = "None"
    for elem in raw_meta['metadata']['columns']:
        if elem['name'] == "date":
            temporal_resolution = elem.get('temporal_resolution', "None")
    spatial_resolution = raw_meta['metadata']['spatial_coverage'][0].get('admin', "None")
    meta = raw_meta.get('metadata', "None")
    
    nyu_meta_results = {"data_location": "NYU",
                        "name": name,
                        "description": descr,
                        "id_value": id_value,
                        "source": source,
                        "temporal_resolution": temporal_resolution,
                        "spatial_resolution": spatial_resolution,
                        "z_meta": meta 
                        }
                 
    return nyu_meta_results    

