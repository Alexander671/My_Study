import asyncpg
import asyncio
from init_query import *
async def main():
    connection:asyncpg.Connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user=    'postgres',
                                       database='products',
                                       password='postgres')

    statements = [CREATE_BRAND_TABLE,
    CREATE_PRODUCT_TABLE,
    CREATE_PRODUCT_COLOR_TABLE,
    CREATE_PRODUCT_SIZE_TABLE,
    CREATE_SKU_TABLE,
    SIZE_INSERT,
    COLOR_INSERT]


    for statement in statements:
        print(statement)
        status = connection.execute(statement)
        await status
        print(status)
    await connection.close()

asyncio.run(main())