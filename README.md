# What is this repo?
MagnetMagnet is a scraper that allows you to scrape magnet links from RARBG and The Pirate Bay. I decided to make this app to improve my Python skills.

## Features supported:
- Scraping magnet links from all RARBG mirrors
- Scraping magnet links from **most** The Pirate Bay mirrors (depending on if the mirror supports RSS)
- Ability to choose multiple categories/subcategories to scrape magnet links from
- Copies magnet links to clipboard
- Exports magnet links into .txt file

## How to use:
### Installing:
- To install MagnetMagnet either download the executable file from [here](https://github.com/eliasbenb/MagnetMagnet/releases)
- Or you can download the python file above and run it using python (make sure to install the dependencies in the requirements.txt file)
### Usage:
- There are only three user changeable fields in MagnetMagnet:
![App Screenshot](https://i.imgur.com/iDXRFN2.png)
- Domain: the first field is for the domain, here just input any RARBG/The Pirate Bay domain name. I reccomend https://rarbg.to/ and https://tpb.party/ as of 2020
- Category Number: the second field is for the category number. This must be entered as a number ID. Multiple IDs can be inputed at once when seperated by a semi colon ';'. **All the category IDs can be found below**
- Clipboard: this is the third field and is a yes or no option, this just copies the magnet links to your clipboard
### Category IDs for RARBG:
**You can get any of these IDs from the end of the RARGB link**
- XXX (18+) = 4
- Movies/XVID = 14
- Movies/XVID/720 = 48
- Movies/x264 = 17
- Movies/x264/1080 = 44
- Movies/x264/720 = 45
- Movies/x264/3D = 47
- Movies/x264/4k = 50
- Movies/x265/4k = 51
- Movs/x265/4k/HDR = 52
- Movies/Full BD = 42
- Movies/BD Remux = 46
- TV Episodes = 18
- TV HD Episodes = 41
- TV UHD Episodes = 49
- Music/MP3 = 23
- Music/FLAC = 25
- Games/PC ISO = 27
- Games/PC RIP = 28
- Games/PS3 = 40
- Games/XBOX-360 = 32
- Software/PC ISO = 33
- Games/PS4 = 53
### Category IDs for The Pirate Bay:
**You can get any of these from the end of the The Pirate Bay link here: https://tpb.party/rss**
- Audio = top100/100
- Video = top100/200
- Applications = top100/300
- Games = top100/400
- Porn = top100/500
- Other = top100/600
- All = top100/0
