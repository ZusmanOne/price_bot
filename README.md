# Бот для доставки уведомлений об изменении цены товара в онлайн магазине



## Как запустить бота
Скачайте код  
```
git clone https://github.com/ZusmanOne/price_bot
```
перейдите в скачанный каталог 
```sh
cd price_bot
```
[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```
**Важно!** Версия Python должна быть не ниже 3.6.

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии.

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

Создайте файл `.env` в корне каталога `price_bot/` со следующими настройками:


- `TG_TOKEN` — для этого вам нужно написать [отцу ботов](https://telegram.me/BotFather).
- `TG_CHAT_ID` — для этого нужно написать [этому боту](https://telegram.me/getmyid_bot)

Бот готов для запуска, запустите файл `main.py` и после проверки проекта вам придет уведомление.