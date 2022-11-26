# Harvest the Project COUNTER Registry

Credit and thanks to [Melissa Belvadi](https://github.com/mbelvadi).  
This is forked from 
https://github.com/mbelvadi/counter_registry_list

## Project Organization
├── LICENSE  
├── README.md  
├── data  
│   ├── output csv file  
├── get_sushi_data.py       <- function to get sushi instance data for platform 
├── get_vendorids.py        <- function to get list of vendor/platform ids
├── log  
│   └── registry_log.log  
├── main.py  
├── params.py               <- make changes to default here (output file name, etc.)
├── requirements.txt


The Project COUNTER Registry contains information about  vendors/platforms/providers that are compliant with the Code of Practice Release 5 standard for online resource (ebooks, ejournals, etc.) usage.

The Registry includes information about the platform/provider including contact information, what COP5 (or COP4) reports they support, and all of the specifics regarding how they support COP5 SUSHI API requests for usage reports, basically everything except an institution's own required credentials (customer_id plus optionally requestor_id and api_key) and other constraints on using their SUSHI API server (eg if they also require the request to come from the customer's IP range, if they have volume or speed limits on server requests, etc.) 

March 2022 Note: the Registry is still a work in progress, and only some vendors have finished populating their own entry with
all of the needed data. If you have more direct and relatively recent 
SUSHI information already from a vendor, that may be more accurate than what you get from this.

This simply python program, which runs from the command line and has no user prompts, produces two output files
in the same folder that the code is run from:
* a tab-delimited table of all of the known registry entries that have a COP5 "sushi service" registered called "registry-entries.tsv"
* a log file listing all of the registry entries that exist but don't have a COP5 sushi service registered yet called
'log-registry-entries.txt'

## Interactive home of the registry:
https://registry.projectcounter.org/

## API Root:
https://registry.projectcounter.org/api/v1/

API returns JSON.

## Platform list:
https://registry.projectcounter.org/api/v1/platform/

## Example of platform instance:
https://registry.projectcounter.org/api/v1/platform/60d34416-9666-4b09-8d58-220ffc04901e/


## The SUSHI API for Project COUNTER COP5 is documented at:
https://www.projectcounter.org/counter-sushi/

See also my project providing a COUNTER harvesting tool (also python, with GtK) for a GUI
interface to collect a library's usage data into an sqlite3 database, with friendly search tools.
https://github.com/CS-4820-Library-Project/COUNTER-5-Report-Tool
That project requires the vendor configuration info found in the Registry, 
along with the library's unique credentials (customer_id, requestor_id, api_key).
The Registry provides for each vendor/platform/provider information about who to contact or where to 
look for those credentials.
.


4 directories, 15 files
