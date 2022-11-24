from pathlib import Path


class Params:
    """ Centralize anything that can be parametrized in the code.
    """
    # magically load environment variables from any .env files
    # load_dotenv(
    #     os.path.abspath('/Users/jnvicker/code/ill-article-request-etl/.env')
    #     )

    # log file
    log_name = Path('log/registry_log.log')

    # output file
    outdir = Path('data')
    outfile = outdir.joinpath('sushi_entries.csv')

    # base API url
    base_url = 'https://registry.projectcounter.org/api/v1/platform/'

    # sushi service elements to retrieve
    sushidata = ['counter_release', 'url',
                 'customer_id_info', 'requestor_id_info']

    # date params for query
    # get previous month
    # today = pd.Timestamp('today')
    # lastmonth = today - pd.DateOffset(months=1)
    # month = lastmonth.month
    # year = lastmonth.year
