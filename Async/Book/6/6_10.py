import asyncio 
import aiohttp
from aiohttp import ClientSession
from util.delay_functions import duration, delay
from fetch import fetch_status
import logging

#@duration()
async def main():
    async with ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://example.com')),
                    asyncio.create_task(fetch_status(session, 'https://example.com')),
                    asyncio.create_task(fetch_status(session, 'https://example.com')),]
        task = asyncio.create_task(fetch_status(session, 'https://example.com'))
        task.cancel()
        done, pending = await asyncio.wait(fetchers, return_when='FIRST_COMPLETED')
        
    print(f'Число завершившихся задач: {len(done)}')
    print(f'Число ожидающих задач: {len(pending)}')

    for done_task in done:
        print(done_task.exception() or await done_task)

asyncio.run(main())