rockchip_firmware_crawler is a crawler intended to crawler a specific website - 'https://www.rockchipfirmware.com' and get:
   1. download locally firmware files found.
   2.collect metadata on each file and store it on MongoDB - Atlas.

The crawler is intended to run multiple times and update metadata if already exists in DB or add new items to mongo.

in order to run this, you will need to configure mongo_atlas_connect.py => change "addres_to_mongo" to your own Atlas address. make sure it contains your username and password.

