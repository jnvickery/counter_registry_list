"""
COUNTER Registry List
"""

import requests
from pathlib import Path
import os.path
import logging


UA = 'mbelvadi@gmail.com'
SERVICE1 = 'COP'
base_URL = 'https://registry.projectcounter.org/api/v1/platform/'
myheaders = {'User-Agent': UA}


def retrieve_all_vendor_recs():
    v_list = {}
    try:
        r = requests.get(base_URL, headers=myheaders)
        if not r.ok:
            infologger.error(" Request returned http error: {}".format(r.status_code))
            return None
    except Exception as e:
        infologger.exception("URL request failed: {}".format(e))
        return None
    else:
        alldata = r.json()
        infologger.debug(f'Number of platforms in registry: {len(alldata)}')
        for dic in alldata:
            vname = dic['name']
            vid = dic['id']
            if len(dic['sushi_services']) == 0:
                infologger.warning(f'No sushi services listed:\t{vname}\t{base_URL+vid} ')
            else:
                has_5 = False
                for dictx in dic['sushi_services']:
                    if dictx['counter_release'] == '5':
                        has_5 = True
                        break
                if has_5:
                    v_list[vname] = vid
                else:
                    infologger.warning(f'No release 5 sushi services listed:\t{vname}\t{base_URL + vid} ')
        return v_list


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


if __name__ == "__main__":
    try:
        recordsfolder = Path('.')
        os.chdir(recordsfolder)
    except:
        recordsfolder = Path('.')

    outfile = 'registry-entries.tsv'
    loggerfile = 'log-registry-entries.txt'
    infologger = logging.getLogger()
    infologger.setLevel(logging.WARNING)  # DEBUG, WARNING, ERROR -  should be upper-case here but lower case when used
    infohandler = logging.FileHandler(loggerfile, 'w', 'utf-8')  # or whatever
    infoformatter = logging.Formatter('%(message)s')  # or whatever
    infohandler.setFormatter(infoformatter)  # Pass handler as a parameter, not assign
    infologger.addHandler(infohandler)

    print(f'Retrieving all registry data, please wait, this can take a few minutes...')
    vendor_data = retrieve_all_vendor_recs()
    with open(outfile, 'w', encoding='utf-8', errors="ignore") as allreg_out:
        header_line = 'vendor_name\tcounter_release\tsushi_base_url\tcontact\tcustomer_id_info\trequestor_id_required\trequestor_id_info\tapi_key_required\tapi_key_info\tplatform_attr_required\tplatform_specific_info\tcredentials_auto_expire\tcredentials_auto_expire_info\trequest_volume_limits_applied\trequest_volume_limits_info\tip_address_authorization\tip_address_authorization_info\tcustomizations_in_place\tcustomizations_info'
        allreg_out.write(header_line+"\n")
        allreg_out.flush()
        for key in vendor_data:
            one_vendor_URL = 'https://registry.projectcounter.org/api/v1/platform/'+vendor_data[key]+'/'
            infologger.debug(f"URL for {key} is {one_vendor_URL}")
            try:
                infologger.debug(f"Attempting URL for {key} is {one_vendor_URL}")
                one_vendor_data = retrieve_one_vendor_recs(one_vendor_URL)
                infologger.debug(f"Value of one_vendor_data: {one_vendor_data}\t{one_vendor_URL}")
                outline = f"{key}\t{one_vendor_data['counter_release']}\t{one_vendor_data['url']}\t{one_vendor_data['contact']}\t{one_vendor_data['customer_id_info']}\t{one_vendor_data['requestor_id_required']}\t{one_vendor_data['requestor_id_info']}\t{one_vendor_data['api_key_required']}\t{one_vendor_data['api_key_info']}\t{one_vendor_data['platform_attr_required']}\t{one_vendor_data['platform_specific_info']}\t{one_vendor_data['credentials_auto_expire']}\t{one_vendor_data['credentials_auto_expire_info']}\t{one_vendor_data['request_volume_limits_applied']}\t{one_vendor_data['request_volume_limits_info']}\t{one_vendor_data['ip_address_authorization']}\t{one_vendor_data['ip_address_authorization_info']}\t{one_vendor_data['customizations_in_place']}\t{one_vendor_data['customizations_info']}"
                allreg_out.write(outline+"\n")
                allreg_out.flush()
            except:
                infologger.warning(f"Skipping {key}: unable to retrieve vendor record or no sushi services listed\n{key}\t{one_vendor_URL}")

    allreg_out.close()
    print(f"DONE -\nCOUNTER Registry entries as tab delimited\nOutput is in : {outfile}\nCheck loggerfile: {loggerfile} for problems")
