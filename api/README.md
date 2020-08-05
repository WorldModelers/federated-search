# Federated Search

## Contents

1. [Overview](#overview)
2. [Running the API](#running-the-API)
3. [Datamart Functionality](#datamart-functionality)

## Overview
This directory allows you build and test the Federated Search backend API generated with swagger (OpenAPI 3.0). The Federated Search is a single access point to the the ISI and NYU datamart APIs to:

   - search by:
       - keywords
       - temporal filters 
       - geospatial filters
   - search for dataset metadata
   - download datasets of interest
   
Each Datamart has varying functionality, see below for instructions.

## Running the API

### Requirements 
    Python 3.5.2+
    
1. Clone the repository to `your/local/folder`.   
2. Navigate to `your/local/folder/federated-search/api`.  
3. Open the `config.ini` file and update the usernames and passwords for the ISI and NYU datamarts.
4. To run the server, execute the following from the `your/local/folder/federated-search/api` directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```
and open your browser to here:

```
http://localhost:8080/ui/
```

Above are the swaggerized steps: If no sucess try:

Open the requirements file and verify the connexion version => `connexion == 2.6.0` (2.2 is the default version from swagger)

```
pip3 install -r requirements.txt   
pip install swagger_ui_bundle
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/swagger.json
```
## Datamart Functionality

Below is a table of current functionality:

<p align="center">
<img src="https://github.com/WorldModelers/federated-search/blob/master/api/images/datamart_caps.png" alt="drawing" width="550"/>
</p>

### NYU Search

<p align="center">
<img src="https://github.com/WorldModelers/federated-search/blob/master/api/images/search.png" alt="drawing" width="300"/>
</p>

Parameters:

`"data_location": NYU`

`geo['type']`: This can be either `bbox` for bounding box (northwest point :latitude1/longitude1 and southeast point: latitude2/longitude2) OR a wiki place name (see image below).

`keywords`: A list of <i>things</i> you would like to search.

`time`: Enter your start and end time of your search in the ISO 8601 format shown.

### ISI Search

<p align="center">
<img src="https://github.com/WorldModelers/federated-search/blob/master/api/images/isi_search.png" alt="drawing" width="300"/>
</p>

Parameters:

`"data_location": ISI`

`geo['type']`: Enter a wiki place name; be sure to change the dictionary keys (`bbox` to `place` as shown in the image above).

`keywords`: Enter a list of <i>things</i> you would like to search for.

### Metadata Search

For either ISI or NYU:

`"data_location"` = `ISI` or `NYU`

`id_value` = dataset ID from either datamart. 

### Download Dataset

NYU:
`"data_location" = NYU`

`id_value` = dataset ID

ISI:
Work in progress, not yet integrated into Federated Search

