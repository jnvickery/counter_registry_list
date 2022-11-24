from datetime import date
from pathlib import Path


class Params:
    """ Centralize anything that can be
    parametrized in the code.
    """

    # log file
    log_name = Path('log/registry_log.log')

    # output file
    outdir = Path('data')
    outfile = outdir.joinpath(
        'sushi_entries_' + str(date.today()) + '.csv')

    # base API url
    base_url = 'https://registry.projectcounter.org/api/v1/platform/'

    # sushi service elements to retrieve
    sushidata = ['counter_release', 'url',
                 'customer_id_info', 'requestor_id_info']
