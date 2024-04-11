# From Official Docs
# Client Side

import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            # Printing status and headers from response
            print("Status:", response.status)
            # Content type would be json for rest api, HTML for websites
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

asyncio.run(main())



## Server Side

from aiohttp import web

async def handle(request):
    # Here, if there's a name then it would say "Hello, and the name"
    # Else it would give "Hello, Anonymous"
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])



# the python __name__ variable is main or is it called by import by another program,
if __name__ == '__main__':
    web.run_app(app)