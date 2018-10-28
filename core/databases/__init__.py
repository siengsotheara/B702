from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, func
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_ENCODING, \
                    SQLALCHEMY_DATABASE_CONVERT_UNICODE, SQLALCHEMY_DATABASE_ECHO, \
                    SQLALCHEMY_DATABASE_POOL_SIZE, SQLALCHEMY_DATABASE_POOL_TIMEOUT, \
                    SQLALCHEMY_DATABASE_ECHO_POOL, SQLALCHEMY_DATABASE_MAX_OVERFLOW, SQLLACHEMY_DATABASE_POOL_RECYCLE
                    
engine = create_engine(SQLALCHEMY_DATABASE_URI, 
                      convert_unicode=SQLALCHEMY_DATABASE_CONVERT_UNICODE, 
                      encoding=SQLALCHEMY_DATABASE_ENCODING, 
                      echo=SQLALCHEMY_DATABASE_ECHO,
                      echo_pool=SQLALCHEMY_DATABASE_ECHO_POOL, 
                      pool_size=SQLALCHEMY_DATABASE_POOL_SIZE, 
                      pool_timeout=SQLALCHEMY_DATABASE_POOL_TIMEOUT, 
                      max_overflow=SQLALCHEMY_DATABASE_MAX_OVERFLOW)

db = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
