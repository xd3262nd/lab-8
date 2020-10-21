import requests
from pprint import pprint
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger('root')

# CONSTANT
COINDESK_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():
    bitcoin_num = get_user_bitcoin_value()
    conversion_value = get_conversion_to_dollars(bitcoin_num)

    display(bitcoin_num, conversion_value)


def display(bitcoin_num, conversion_value):
    if conversion_value is not None:
        print(f'With your {bitcoin_num:.2f} of bitcoin, you will be able to get {conversion_value}USD.')
    else:
        print('Error in converting. Please try again later')


def get_user_bitcoin_value():
    while True:
        try:
            bitcoin_num = float(input('How many bitcoin do you have?\t'))
            if bitcoin_num <= 0:
                raise ValueError('Invalid input. Please enter value that is more than 0')
            return bitcoin_num

        except:
            print('Invalid input. Please enter data in decimal form only.')


def get_conversion_rate():
    data = get_current_exchange_rate()

    if data is not None:
        return data['bpi']['USD']['rate_float']
    else:
        return None


def get_conversion_to_dollars(bitcoin_num):
    conversion_rate = get_conversion_rate()

    if conversion_rate is not None:

        return bitcoin_num * conversion_rate
    else:
        return None


def get_current_exchange_rate():
    try:
        response = requests.get(COINDESK_URL)
        response.raise_for_status()
        data = response.json()
        return data

    except Exception as e:
        log.debug(f'Error occurred while requesting data from \'{COINDESK_URL}\'. More detail: {e}')
        return None


if __name__ == '__main__':
    main()
