import requests
import logging
import time
from datetime import datetime

import config


LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=LOG_FORMAT, filename='logfile.log', level=logging.DEBUG)
log = logging.getLogger()


class AbstractCryptoWrapper:
    BASE_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'
    IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{event}/with/key/{IFTTT_key}'

    def __init__(self, crypto, threshold_price):
        self._crypto = crypto
        self._url = AbstractCryptoWrapper.BASE_API_URL + self._crypto
        self._threshold_price = threshold_price

    def get_latest_crypto_price(self):
        try:
            response = requests.get(self._url)
            price = None
            if response.status_code == 200:
                price = float(response.json()[0]['price_usd'])
                if price < self._threshold_price:
                    self._post_ifttt_webhook('bitcoin_price_emergency', price)
            return price
        except ConnectionError as e:
            log.warning('There was a connection error')
            self.get_latest_crypto_price()
        except Exception as e:
            log.error(e)

    def _post_ifttt_webhook(self, event, price):
        # The payload that will be sent to IFTTT service
        data = {'value1': self._crypto.title(), 'value2': price,
                'value3': self._crypto}
        # inserts our desired event
        ifttt_event_url = AbstractCryptoWrapper.IFTTT_WEBHOOKS_URL.format(
            event=event,
            IFTTT_key=getattr(config, 'IFTTT_KEY')
          )
        if data.get('value2') is not None:
            # Sends a HTTP POST request to the webhook URL
            requests.post(ifttt_event_url, json=data)
            log.info('Web hook triggered')


class BitcoinWrapper(AbstractCryptoWrapper):
    def __init__(self):
        super(BitcoinWrapper, self).__init__('bitcoin', 10000)


class EthereumWrapper(AbstractCryptoWrapper):
    def __init__(self):
        super(EthereumWrapper, self).__init__('ethereum', 10000)


if __name__ == '__main__':
    b = BitcoinWrapper()
    while True:
        price = b.get_latest_crypto_price()

        # Sleep for 5 minutes
        time.sleep(5 * 60)




