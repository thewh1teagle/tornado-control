"""
pip install -r requirements.txt
python main.py
"""

from aux_cloud import AuxCloudAPI
import asyncio
from dotenv import load_dotenv
from os import getenv

load_dotenv()

async def main():
    # Login
    user = getenv('TUYA_USERNAME')
    password = getenv('TUYA_PASSWORD')
    region = getenv('TUYA_REGION')
    api = AuxCloudAPI(user, password, region=region, session_file=getenv('SESSION_FILE'))
    await api.login()

    # Get specific family
    families = await api.list_families()

    for family in families:
        family_name = family['name']
        print(f'Family: {family_name}')
        family_id = family['familyid']
        try:
            devices = await api.list_devices(family_id)
        except Exception as e:
            print(f'Failed to query family {family_name}', e)
            continue
        for device in devices:
            device_name = device['friendlyName']
            try:
                params = await api.get_device_params(device)
                # Turn off device
                print(f"Turn off device: {device_name}")
                params['pwr'] = 0
                await api.set_device_params(device, params)
            except Exception as e:
                print(f'Failed to turn off device {device_name}')

asyncio.run(main())