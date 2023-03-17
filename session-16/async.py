import time
import asyncio
import aiohttp


start_time = time.time()

# SYNC

# for number in range(1, 151):
#     url = f'https://pokeapi.co/api/v2/pokemon/{number}'
#     resp = requests.get(url)
#     pokemon = resp.json()
#     print(f"{pokemon['id']} : {pokemon['name']}")

# print("--- %s seconds ---" % (time.time() - start_time))


# ASYNC
async def main():

    async with aiohttp.ClientSession() as session:

        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print(f"{pokemon['id']} : {pokemon['name']}")

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
