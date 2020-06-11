# rockchip_firmware_crawler

The 'rockchip_firmware_crawlercrawler' crawler intended to download firmware files and collect metadata.

It's designed to run multiple times and update metadata if already exists in DB or add new items to MongoDB.

The crawler is designed to crawler a specific website - 'www.rockchipfirmware.com'. 

## How to run it?

Run "crawler_main.py [website_url]"

Example: "crawler_main.py https://www.rockchipfirmware.com"



## What does it do?

The Crawler:
  
1. Download firmware files found locally to firmware_files directory in the project.
2. collects metadata on each file and store it on MongoDB - Atlas.


In order to run this, you will need to configure mongo_atlas_connect.py =>
change "addres_to_mongo" to your own Atlas address. Make sure it contains your username and password.
