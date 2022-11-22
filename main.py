import logging

from params import Params

from retrieve_all import retrieve_all_vendor_recs


def main():
    params = Params()

    logging.basicConfig(
        filename=params.log_name,
        level=logging.INFO,
        format=('%(asctime)s.%(msecs)03d %(levelname)s'
                '%(module)s - %(funcName)s: %(message)s'),
        datefmt='%Y-%m-%d %H:%M:%S')
    retrieve_all_vendor_recs(params)


if __name__ == '__main__':
    main()
