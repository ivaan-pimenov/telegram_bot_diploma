# telegram_bot_diploma
Дипломная работа по курсу Python_Basic в Skillbox.

Телеграм-бот, который может получать информацию об отелях со всего мира, используя Rapid API.

## Used technology
* Python (3.11);
* <a link="https://github.com/eternnoir/pyTelegramBotAPI" target="blank">PyTelegramBotApi</a> - Telegram Bot framework
* <a link="https://www.postgresql.org" target="blank">PostgreSQL</a> - database;
* <a link="https://redis.io" target="blank">Redis</a> - persistent storage from some ongoing data;
* <a link="https://www.sqlalchemy.org" target="blank">SQLAlchemy</a> - working with database from Python;

## Installation
- Для начала работы необходимо скопировать все содержимое репозитория в отдельный каталог.
- Установить библиотеки и зависимости из `requirements.txt` (можно использовать команду `pip install -r requirements.txt`)
- Установить и запустить PostgreSQL сервер, создать базу данных для использования бота.
- Открыть файл `.env.template` и переименовать в `.env`, заполнить все данные.
- Сделать миграции с помощью команды к консоли `alembic upgrade head`.
- Установить и запустить Redis-сервер, если планируете его использовать.
- Запустить файл `__main__.py`.