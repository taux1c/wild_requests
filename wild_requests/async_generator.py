
from httpx import AsyncClient

# Need to add support for additional methods. Only adding get right now.
async def bulk_request(what, method=None, headers=None):
    """This function takes a list or dictionary and returns the responses.
    if you supply a dictionary the key should be a unique id and the value should
    be a url. A dictionary with the key and response will be yielded. For a list
    only a response will be yielded in no specific order."""

    async def make_async(iterable):
        if isinstance(what, dict):
            for k, v in iterable.items():
                if k:
                    if v:
                        yield k,v

        if isinstance(what, list):
            for x in iterable:
                if x:
                    yield x

    if isinstance(what,dict):
        async with AsyncClient() as session:
            if headers:
                session.headers.update(headers)
            async for k,v in make_async(what):
                # Can add logic here for additional methods.
                response = await session.get(v)
                if k:
                    if v:
                        yield k,response

    if isinstance(what,list):
        async with AsyncClient() as session:
            if headers:
                session.headers.update(headers)
            async for x in make_async(what):
                # Can add logic here for additional method support.
                response = await session.get(x)
                yield response