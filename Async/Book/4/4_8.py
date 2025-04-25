import asyncio 
import aiohttp
from aiohttp import ClientSession
from util.delay_functions import duration, delay
from fetch import fetch_status

duration()
async def main():
    async with ClientSession() as session:
        fetchers = [fetch_status(session, 'https://example.com', 1),
                    fetch_status(session, 'https://example.com', 10),
                    fetch_status(session, 'https://example.com', 10),]

        for finished_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                print(await finished_task)
            except asyncio.exceptions.TimeoutError as e:
                print(e)
asyncio.run(main())