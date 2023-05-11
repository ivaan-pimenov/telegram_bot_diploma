import logging
import psycopg2
from config_data.config import DB
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def check_or_create_db(db: DB) -> None:
	"""
	Check connection to db, and create DB if DB_CREATE in .env
	:param db: DB
	:return: None
	"""
	connection = None
	cursor = None
	logger = logging.getLogger(__name__)
	try:
		if not db.autocreate_db:
			connection = psycopg2.connect(user=db.user,
										  dbname=db.database,
										  password=db.password,
										  host=db.host,
										  port=db.port)
		else:
			connection = psycopg2.connect(user=db.user,
										  password=db.password,
										  host=db.host,
										  port=db.port)
			connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
			cursor = connection.cursor()
			cursor.execute('SELECT 1 FROM pg_catalog.pg_roles WHERE rolname = %s',(db.user,))
			user_exists = cursor.fetchone()
			if not user_exists:
				cursor.execute("""create user %s with password %s""", (db.user, db.password))
			cursor.execute('SELECT 1 FROM pg_catalog.pg_database WHERE datname=%s', (db.database,))
			db_exists = cursor.fetchone()
			if not db_exists:
				cursor.execute("""create database %s owner %s""", (db.database, db.user))
			logger.info('BD is ready')
	except (Exception, psycopg2.Error) as error:
		logger.error(error, exc_info=error)
	finally:
		if connection:
			cursor.close()
			connection.close()
			
			
