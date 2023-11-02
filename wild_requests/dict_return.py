import httpx
from httpx import AsyncClient
from asyncio import run
from time import time

# Need to add suppport for all methods but right now I am only adding get.
async def bulk_request(what: dict, headers=None, method=None) -> dict[id:httpx.Response]:
    """This function takes a dictionary that contains a unique id assigned to a string url as the value
    it will then make all of the requests and return a dictionary with all of the response objects.
    You can use the id to get the response."""
    dict_to_return = {}
    async def make_async(iterable: dict):
        """Simple async generator to hand out items from our dictionary."""
        for k,v in iterable.items():
            if k:
                if v:
                    yield k, v
    async with AsyncClient() as session:
        if headers:
            session.headers.update(headers)
        async for k,v in make_async(what):
            # Logic can go here for each method type.
            response = await session.get(v)
            new_dict = {k:response}
            dict_to_return.update(new_dict)

            
    return dict_to_return