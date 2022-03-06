# Harvest the Project COUNTER Registry

Project COUNTER's Registry of vendors/platforms that are compliant with the Code of Practice Release 5 standard for online resource (ebooks, ejournals, etc.) usage.

The Registry includes information about the platform/provider including contact information, what COP5 (or COP4) reports they support, and all of the specifics regarding how they support COP5 SUSHI API requests for usage reports, basically everything except an institution's own required credentials (customer_id plus optionally requestor_id and api_key) and other constraints on using their SUSHI API server (eg if they also require the request to come from the customer's IP range, if they have volume or speed limits on server requests, etc.) 


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