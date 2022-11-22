import logging
import requests
from requests.exceptions import HTTPError


def retrieve_one_vendor_recs(vendorurl):
    infologger.debug(f'\n\nStarting retrieve one for vendorurl: {vendorurl}')
    try:
        r = requests.get(vendorurl, headers=myheaders)
        # infologger.debug(f'Text: {r.text}')
        # infologger.debug(f"r.ok: {r.ok}\nr.json[sushi_services]:{r.json()['sushi_services']}\n")
        if not r.ok:
            infologger.error(" Request returned http error: {}".format(r.status_code))
            return None
    except Exception as e:
        infologger.exception("URL request failed: {}".format(e))
        return None
    infologger.debug(f"r.json[sushi_services]:{r.json()['sushi_services']}\n")
    sushi_dict = r.json()['sushi_services'][0]
    infologger.debug(f"sushi_dict[data_host]:{sushi_dict['data_host']}\n")
    infologger.debug(f"sushi_dict[counter_release]:{sushi_dict['counter_release']}\n")
    infologger.debug(f"counter_release: {sushi_dict['counter_release']}\n\n")
    return sushi_dict
