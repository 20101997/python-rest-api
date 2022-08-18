
import sqlalchemy as db
import pymysql
import cryptography
from sqlalchemy.orm import sessionmaker

from model.job import Job


class DBClient :
    def connectToDb(self):
        # specify database configurations
        config = {
            'host': 'localhost',
            'port': 3307,
            'user': 'newuser',
            'password': 'newpassword',
            'database': 'test_db'
        }
        db_user = config.get('user')
        db_pwd = config.get('password')
        db_host = config.get('host')
        db_port = config.get('port')
        db_name = config.get('database')
        # specify connection string
        connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
        # connect to database
        engine = db.create_engine(connection_str)
        return engine

