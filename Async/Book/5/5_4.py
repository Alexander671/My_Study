import asyncpg
import asyncio
from init_query import *
async def main():
    connection:asyncpg.Connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user=    'postgres',
                                       database='products',
                                       password='postgres')

    #task_query_1 = asyncio.create_task(connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')"))
    #task_query_2 = asyncio.create_task(connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')"))

    #await asyncio.gather(task_query_1, task_query_2)

    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results = await connection.fetch(brand_query)
    for brand in results:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')

    await connection.close()

asyncio.run(main())

