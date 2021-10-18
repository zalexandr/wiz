import asyncio

from asyncio.base_events import Server

from pywizlight import PilotBuilder, discovery, wizlight
from pywizlight.bulblibrary import BulbType, KelvinRange, Features

from pywizlight.discovery import discover_lights
import time


async def police_effect():

    bulb = wizlight("192.168.178.108")
    # Set up a standard light
    _bulb = await bulb.get_bulbtype()
    se = await bulb.getSupportedScenes()
    print(se)
    print(_bulb.__dict__)
    for key in [6, 9, 10, 11, 12, 13, 14, 15, 16, 18, 29, 30, 31, 32]:
        pilot = PilotBuilder(brightness=None, colortemp=None, scene=key)
        await bulb.turn_on(pilot)


async def test():
    bulbs = await discover_lights("192.168.178.255")
    for bulb in bulbs:
        print(bulb.ip, bulb.mac)


def main():
    # startup_bulb(module_name="ESP56_SHTW3_01")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())


if __name__ == "__main__":
    main()
