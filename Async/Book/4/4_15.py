# почему стоит все сопрограммы(корутины) оборачивать
# в таски

import asyncio 
import aiohttp
from aiohttp import ClientSession
from util.delay_functions import duration, delay
from fetch import fetch_status
import logging

#@duration()
async def main():
    async with ClientSession() as session:
        check_url_task = asyncio.create_task(fetch_status(session, 'https://example.com', delay=4)) 
        check_url_coro = asyncio.create_task(fetch_status(session, 'https://example.com', delay=4)) 
        
        pending = [asyncio.create_task(fetch_status(session, 'https://example.com', delay=1)),
                    asyncio.create_task(fetch_status(session, 'https://example.com', delay=3)),
                    asyncio.create_task(fetch_status(session, 'https://example.com', delay=3)),
                    check_url_task,
                    ]

        done, pending = await asyncio.wait(pending, return_when='ALL_COMPLETED', timeout=2)
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')
        for done_task in done:
            print(done_task.exception() or await done_task)

        for pending_task in pending:
            if check_url_task is pending_task:
                print('Task is visible')

            if check_url_coro is pending_task:
                print('Coro is visible')


asyncio.run(main())