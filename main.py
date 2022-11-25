import logging
import pandas as pd

from params import Params

from get_vendorids import get_ids
from get_sushi_data import get_sushi


def main():
    params = Params()

    sushi_df = pd.DataFrame()

    logging.basicConfig(
        filename=params.log_name,
        level=logging.INFO,
        format=('%(asctime)s.%(msecs)03d %(levelname)s '
                '%(module)s - %(funcName)s: %(message)s'),
        datefmt='%Y-%m-%d %H:%M:%S')
    vendids = get_ids(params)
    for vendorid in vendids:
        df = get_sushi(params, vendorid)
        sushi_df = pd.concat([sushi_df, df], ignore_index=True)

    sushi_df.to_csv(params.outfile, index=False)


if __name__ == '__main__':
    main()
