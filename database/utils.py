from config_data.config import DB


def make_connection_string(db: DB) -> str:
	"""
	Make connection string to database
	:param db: DB
	:return: str
	"""
	result = f"postgresql+psycopg2://{db.user}:{db.password}@{db.host}:{db.port}/{db.database}"
	return result
