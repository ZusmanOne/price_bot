import requests
from bs4 import BeautifulSoup
import time
import telegram
from environs import Env
from urllib.parse import urljoin
import logging


logger = logging.getLogger(__file__)


class TelegramLogsHandler(logging.Handler):
    def __init__(self, tg_token, chat_id):
        super().__init__()
        self.tg_bot = telegram.Bot(tg_token)
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def main():
    env = Env()
    env.read_env()
    chat_id = env('TG_CHAT_ID')
    tg_token = env('TG_TOKEN')
    logging.basicConfig(level=logging.ERROR)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(TelegramLogsHandler(tg_token, chat_id))
    logger.info('Парсер запущен')
    bot = telegram.Bot(tg_token)
    current_price = 9350
    while True:
        try:
            url = 'https://sotohit.ru/internet-magazin2/folder/apple-airpods'
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')
            title_airpods = soup.find_all(class_='uk-grid-item shop2-product-item')
            for i in title_airpods:
                title = i.find(class_='product-item-name')
                if 'Apple AirPods 2 ' in title.text:
                    link = title.find('a').get('href')
                    airpods2_url = urljoin('https://sotohit.ru/', link)
                    response_product = requests.get(airpods2_url)
                    response_product.raise_for_status()
                    airpods2_soup = BeautifulSoup(response_product.text, 'lxml')
                    airpods2_title = airpods2_soup.find('h1').text
                    airpods2_price = airpods2_soup.find(class_='price-current').find('strong').text
                    if int(airpods2_price) != current_price:
                        bot.send_message(text=f'цена {airpods2_title} теперь такая {airpods2_price} \n заказать {airpods2_url}',
                                         chat_id=chat_id)
            time.sleep(1800)
        except Exception:
            logger.exception('сломался парсер')


if __name__ == '__main__':
    main()
