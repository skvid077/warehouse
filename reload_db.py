import asyncio

from src.database.models import reload_db

if __name__ == '__main__':
    asyncio.run(reload_db())
