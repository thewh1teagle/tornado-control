"""
pip install aiohttp python-dotenv
python main.py
"""

from aux_cloud import AuxCloudAPI
import asyncio
from dotenv import load_dotenv
from os import getenv

load_dotenv()

async def main():
    # Login
    api = AuxCloudAPI(getenv('USER'), getenv('PASSW'), region=getenv('REGION'), session_file=getenv('SESSION_FILE'))
    await api.login()

    # Get specific family
    families = await api.list_families()
    family = families[1]['familyid']

    # Get specific device
    devices = await api.list_devices(family)
    device = devices[1]

    # Turn off
    params = await api.get_device_params(device)
    params['pwr'] = 0
    await api.set_device_params(device, params)
    

asyncio.run(main())