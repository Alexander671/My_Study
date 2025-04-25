import asyncio 
import aiohttp
from aiohttp import ClientSession
from util.delay_functions import duration, delay
from fetch import fetch_status
import logging

#@duration()
async def main():
    async with ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://example.com', 1)),
                    asyncio.create_task(fetch_status(session, 'https://example.com', 3)),
                    asyncio.create_task(fetch_status(session, 'https://exam123aple.com', 3)),]
    
        done, pending = await asyncio.wait(fetchers)

    for done_task in done:
        print(done_task.exception() or await done_task)

asyncio.run(main())