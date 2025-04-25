import asyncio
import aiohttp
from aiohttp import ClientSession
from util.delay_functions import duration

async def fetch_status(session:ClientSession, url:str, delay=0):
    async with session.get(url, timeout=5) as result:
        await asyncio.sleep(delay)
        return result.status
@duration()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        tasks = [asyncio.create_task(fetch_status(session,'https://www.exasfd1ample.com'))]
        for _ in range(100):
            tasks.append(asyncio.create_task(fetch_status(session, url)))
        status_codes = await asyncio.gather(*tasks, return_exceptions=True)
        print(status_codes)