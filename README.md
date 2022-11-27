# Harvest the Project COUNTER Registry

Credit and thanks to [Melissa Belvadi](https://github.com/mbelvadi).  
This is forked from 
https://github.com/mbelvadi/counter_registry_list  

## Main changes from upstream
- break script into modules 
- centralize parameters in params.py  
- return csv file with requested sushi data per vendor/platform  

## Project Organization
```
├── LICENSE
├── README.md
├── data
│   ├── sushi_entries.csv  
├── get_sushi_data.py       <- function to get sushi instance data for platform
├── get_vendorids.py        <- function to get list of vendor/platform ids  
├── log
│   └── registry_log.log
├── main.py
├── params.py               <- change defaults (output file name, sushi data requested, etc.)  
├── requirements.txt
```

## About Project COUNTER Registry
The Project COUNTER Registry contains information about  vendors/platforms/providers that are compliant with the Code of Practice Release 5 standard for online resource (ebooks, ejournals, etc.) usage.

The Registry includes information about the platform/provider including contact information, what COP5 (or COP4) reports they support, and all of the specifics regarding how they support COP5 SUSHI API requests for usage reports, basically everything except an institution's own required credentials (customer_id plus optionally requestor_id and api_key) and other constraints on using their SUSHI API server (eg if they also require the request to come from the customer's IP range, if they have volume or speed limits on server requests, etc.)  

### API Root:
https://registry.projectcounter.org/api/v1/

### Platform list:
https://registry.projectcounter.org/api/v1/platform/

### Example of platform instance:
https://registry.projectcounter.org/api/v1/platform/60d34416-9666-4b09-8d58-220ffc04901e/

### The SUSHI API documentation:
https://www.projectcounter.org/counter-sushi/
