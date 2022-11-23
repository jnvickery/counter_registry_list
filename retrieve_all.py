import logging
import requests
from requests.exceptions import HTTPError

logger = logging.getLogger('retrieve_all')


def retrieve_all_vendor_recs(params):
    """Gets all platforms from API.
    Returns a dictionary with platform name and API ID
    to check each individual platform
    """
    v_list = []
    try:
        r = requests.get(params.base_url)
        r.raise_for_status()
    except HTTPError as http_err:
        logger.exception("HTTP Error: {}".format(http_err))
    else:
        alldata = r.json()
        logger.debug(f'Number of platforms in registry: {len(alldata)}')
        for platform_dict in alldata:
            vname = platform_dict['name']
            if len(platform_dict['sushi_services']) == 0:
                logger.warning(f'No sushi services listed: {vname}')
            else:
                vid = platform_dict['id']
                v_list[vname] = vid
        return v_list
