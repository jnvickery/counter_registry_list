import logging
import pandas as pd
import requests
from requests.exceptions import HTTPError

logger = logging.getLogger('retrieve_one')


def get_sushi(params, vendorid):
    """Get sushi service data from
    individual platform instance.
    Returns a DataFrame.
    """
    try:
        r = requests.get(params.base_url + vendorid)
        r.raise_for_status()
    except HTTPError as http_err:
        logger.exception("HTTP Error: {}".format(http_err))
    else:
        alldata = r.json()
        df = pd.json_normalize(alldata['sushi_services'])
        df = df[params.sushidata]
        df.insert(0, 'name', alldata['name'])
        return df
