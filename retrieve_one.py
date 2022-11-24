import logging
import pandas as pd
import requests
from requests.exceptions import HTTPError

logger = logging.getLogger('retrieve_one')


def retrieve_one_vendor_recs(params, vendorid):
    try:
        r = requests.get(params.base_url + vendorid)
        r.raise_for_status()
    except HTTPError as http_err:
        logger.exception("HTTP Error: {}".format(http_err))
    else:
        alldata = r.json()
        df = pd.json_normalize(alldata['sushi_services'])
        df = df[params.sushidata]
        return df
