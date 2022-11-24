import logging
import pandas as pd

from params import Params

from retrieve_all import retrieve_all_vendor_recs
from retrieve_one import retrieve_one_vendor_recs


def main():
    params = Params()

    sushi_df = pd.DataFrame()

    logging.basicConfig(
        filename=params.log_name,
        level=logging.INFO,
        format=('%(asctime)s.%(msecs)03d %(levelname)s '
                '%(module)s - %(funcName)s: %(message)s'),
        datefmt='%Y-%m-%d %H:%M:%S')
    vendids = retrieve_all_vendor_recs(params)
    for vendorid in vendids:
        df = retrieve_one_vendor_recs(params, vendorid)
        sushi_df = pd.concat(sushi_df, df)

    sushi_df.to_csv(params.outfile, index=False)


if __name__ == '__main__':
    main()
