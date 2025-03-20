from sqlalchemy.ext.asyncio import (
    AsyncSession, 
    create_async_engine, 
    async_sessionmaker

)
from sqlalchemy.orm import declarative_base 

from src.settings import settings


DATABASE_URL = settings.postgres_url

engine = create_async_engine(url=DATABASE_URL)

session = async_sessionmaker(bind=engine, class_=AsyncSession)

Base = declarative_base()
