# tornado-control

Control tornado air conditioner

Based on [maeek's](https://github.com/maeek) great RE work!

Tested on [ISKA-INV-12 X WIFI EU](https://www.tornado-top.co.il/catalog/product_page?productid=398)

## Usage

1. Copy `.env.template` to `.env` and fill the credentials from your account in [tornadowifi3](https://play.google.com/store/apps/details?id=com.tornado.tornadowifi3). (You must have a password set. you can change it from their settings.)
2. Install requirements and Run

```console
pip install aiohttp python-dotenv
python main.py
```

## Air conditionars options

| Key                | Description                  | Details                                          |
| ------------------ | ---------------------------- | ------------------------------------------------ |
| **pwr**            | Power status                 | Integer, power on/off status (0 or 1)            |
| **temp**           | Temperature setting          | 3-digit integer                                  |
| **ac_mode**        | Operating mode               | Integer, represents current operating mode       |
| **ac_vdir**        | Vertical airflow direction   | Integer, represents vertical airflow direction   |
| **ac_hdir**        | Horizontal airflow direction | Integer, represents horizontal airflow direction |
| **ac_mark**        | Turbo mode                   | Integer, indicates turbo mode (0 or 1)           |
| **ecomode**        | Eco mode                     | Integer, eco mode status (0 or 1)                |
| **ac_slp**         | Sleep mode                   | Integer, indicates sleep mode (0 or 1)           |
| **childlock**      | Child lock                   | Integer, child lock status (0 or 1)              |
| **tempunit**       | Temperature unit             | Integer, 0 for Celsius, 1 for Fahrenheit         |
| **ac_astheat**     | Auxiliary heating            | Integer, indicates auxiliary heating (0 or 1)    |
| **comfwind**       | Comfort wind                 | Integer, comfort wind setting (0 or 1)           |
| **ac_clean**       | Cleaning mode                | Integer, cleaning mode status (0 or 1)           |
| **ac_health**      | Health mode                  | Integer, health mode status (0 or 1)             |
| **scrdisp**        | Screen display status        | Integer, screen display on/off (0 or 1)          |
| **mldprf**         | Mold-proof function          | Integer, mold-proof status (0 or 1)              |
| **pwrlimitswitch** | Power limit switch           | Integer, power limit switch (0 or 1)             |
| **pwrlimit**       | Power limit setting          | Integer, represents power limit value            |
| **sleepdiy**       | Custom sleep setting         | Integer, indicates custom sleep setting (0 or 1) |
| **ac_tempconvert** | Temperature conversion       | Integer, temperature conversion setting (0 or 1) |
