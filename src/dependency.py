from src.infrastructure.postgres import session


async def get_db_session():
    db_session = session()
    try:
        yield db_session 
    finally:
        await db_session.close()


    
