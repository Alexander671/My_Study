import asyncpg
import asyncio
from util.delay_functions import duration

@duration()
async def main():
    connection:asyncpg.Connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='postgres')
    query = 'SELECT * FROM product;'
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)

    await connection.close()

asyncio.run(main())