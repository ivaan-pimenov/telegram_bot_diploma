import logging
import logging.config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from telebot import TeleBot
from telebot.custom_filters import StateFilter, TextMatchFilter, IsDigitFilter

from config_data.config import load_config
from filters.city_filter import CitiesCallbackFilter
from filters.price_max import PriceMaxFilter
from filters.range_filter import MessageInRangeFilter
from filters.private import IsPrivateChatFilter
from handlers.callback.calendar import register_calendar_callback
from handlers.callback.choice_city import register_city_callback
from handlers.callback.with_photo import register_load_photo_callback
from handlers.callback.without_photo import register_no_photo_callback
from handlers.commands.hello import register_start
from handlers.commands.help import register_helps
from handlers.commands.hi_lo_best import register_commands_price
from handlers.commands.history import register_get_history
from handlers.commands.reset_handler import register_reset_all
from handlers.messages.check_out import register_check_out
from handlers.messages.check_out_wrong import register_check_out_wrong
from handlers.messages.distance import register_get_distance
from handlers.messages.distance_wrong import register_distance_wrong
from handlers.messages.get_city import register_city
from handlers.default_handlers.echo import register_echo
from handlers.messages.price_max import register_get_max_price
from handlers.messages.price_max_wrong import register_get_max_price_wrong
from handlers.messages.price_min import register_get_min_price
from handlers.messages.price_min_wrong import register_get_min_price_wrong
from handlers.messages.quantity_hotels import register_quantity
from handlers.messages.quantity_hotels_wrong import register_quantity_wrong
from handlers.messages.quantity_photo import register_get_quantity_photo
from handlers.messages.quantity_photo_wrong import register_get_quantity_photo_wrong
from middlewares.config import ConfigMiddleware
from middlewares.db import DbSessionMiddleware
from middlewares.logging import LoggingMiddleware
from database.utils import make_connection_string


def register_all_middlewares(bot):
    bot.setup_middleware(LoggingMiddleware())
    bot.setup_middleware(DbSessionMiddleware(session_pool=db_pool))
    bot.setup_middleware(ConfigMiddleware(config=config))
    
    
def register_all_filters(bot):
    bot.add_custom_filter(IsPrivateChatFilter())
    bot.add_custom_filter(StateFilter(bot))
    bot.add_custom_filter(MessageInRangeFilter())
    bot.add_custom_filter(CitiesCallbackFilter())
    bot.add_custom_filter(TextMatchFilter())
    bot.add_custom_filter(IsDigitFilter())
    bot.add_custom_filter(PriceMaxFilter(bot))
    
    
def register_all_handlers(bot):
    register_reset_all(bot)
    register_commands_price(bot)
    register_city(bot)
    register_quantity(bot)
    register_city_callback(bot)
    register_quantity_wrong(bot)
    register_check_out(bot)
    register_check_out_wrong(bot)
    register_get_distance(bot)
    register_distance_wrong(bot)
    register_get_max_price(bot)
    register_get_max_price_wrong(bot)
    register_get_min_price(bot)
    register_get_min_price_wrong(bot)
    register_get_quantity_photo(bot)
    register_get_quantity_photo_wrong(bot)
    register_calendar_callback(bot)
    register_load_photo_callback(bot)
    register_no_photo_callback(bot)
    register_start(bot)
    register_helps(bot)
    register_get_history(bot)
    register_echo(bot)
    
    
if __name__ == "__main__":
    
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('start bot')
    
    # Reading config file
    config = load_config()
    
    # Creating DB engine for PostgreSQL
    engine = create_engine(
        make_connection_string(config.db),
        future=True,
        echo=False
    )
    
    # Creating DB connections pool
    db_pool = sessionmaker(engine, expire_on_commit=False, class_=Session)
    
    bot = TeleBot(token=config.tg_bot.token, use_class_middlewares=True)
    
    register_all_middlewares(bot)
    register_all_filters(bot)
    register_all_handlers(bot)
    
    try:
        logger.info('start polling')
        bot.polling(skip_pending=True, none_stop=True)
    except (KeyboardInterrupt, SystemExit):
        logger.info('Bot stopped, have a nice day')
    finally:
        engine.dispose()
