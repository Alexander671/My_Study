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
    async with connection.transaction():
        query = 'SELECT * FROM product;'
        cursor = await connection.cursor(query)
        await cursor.forward(500)
        products = await cursor.fetch(100)
        for product in products:
            print(product)
    await connection.close()

asyncio.run(main())