import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='postgres')
    async with connection.transaction():  # A
        await connection.execute("INSERT INTO brand "
                                 "VALUES(4206, 'brand_1')")
        await connection.execute("INSERT INTO brand "
                                 "VALUES(4207, 'brand_2')")

    query = """SELECT brand_name, brand_id FROM brand 
                WHERE brand_name LIKE 'brand%'"""
    brands = await connection.fetch(query)  # B
    print(brands)

    await connection.close()


asyncio.run(main())