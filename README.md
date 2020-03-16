<h3 align="center"><img src="https://i.imgur.com/pX9no9C.png" width="600px"></h3>
<p align="center">
  <a href="https://github.com/eliasbenb/MagnetMagnet/releases"><img src="https://img.shields.io/github/downloads/eliasbenb/MagnetMagnet/total?color=%234197fe&style=for-the-badge"></a>
  <a href="https://github.com/eliasbenb/MagnetMagnet/releases/latest"><img src="https://img.shields.io/github/v/release/eliasbenb/MagnetMagnet?color=%234197fe&style=for-the-badge"></a>
</p>

<img src="https://user-images.githubusercontent.com/54410649/76709427-0b9dfa00-6718-11ea-9f53-9bc1c848d737.PNG" alt="img" align="right" width="400px">
<img src="https://user-images.githubusercontent.com/54410649/76709428-0d67bd80-6718-11ea-9261-c46a57bf0812.PNG" alt="img" align="right" width="400px">
MagnetMagnet is well, a magnet link magnet, it's a scraper that allows you to scrape magnet links from RARBG, The Pirate Bay and Kick Ass Torrents. I decided to make this app to improve my Python skills.
Supports windows only.

## Features supported:
- Scraping magnet links from all RARBG mirrors
- Scraping magnet links from **most** The Pirate Bay mirrors (depending on if the mirror supports RSS)
- Scraping magnet links from **most** Kick Ass Torrents mirrors (depending on if the mirror contains the magnet link all on one page)
- Ability to choose multiple categories/subcategories to scrape magnet links from
- Copies magnet links to clipboard
- Exports magnet links into .txt file

## How to use:
### Installing:
**To install MagnetMagnet either download the executable file from [here](https://github.com/eliasbenb/MagnetMagnet/releases).**
**Or you can download the python file above and run it using python (make sure to install the dependencies in the requirements.txt file)**
### Usage:
- On launch you get three options of torrent indexers to scrape from: RARBG, The Pirate Bay and Kick Ass Torrents
![App Screenshot](https://user-images.githubusercontent.com/54410649/76709427-0b9dfa00-6718-11ea-9f53-9bc1c848d737.PNG)
- There are only three user changeable fields in MagnetMagnet:
![App Screenshot](https://user-images.githubusercontent.com/54410649/76709428-0d67bd80-6718-11ea-9261-c46a57bf0812.PNG)
- Domain: the first field is for the domain, here just input a RARBG/The Pirate Bay/Kick Ass Torrents domain. I reccomend https://rarbg.to/ / https://tpb.party/ / https://kat.rip/ as of 16th March 2020
- Category Number: the second field is for the category number. This must be entered as a number ID. Multiple IDs can be inputed at once when seperated by a semi colon ';'. **All the category IDs can be found below**
- Clipboard: this is the third field and is a yes or no option, this just copies the magnet links to your clipboard
- Save Config: this saves whatever is inputed in the text fields to a config file stored in %APPDATA%\eliasbenb
- Load Config: this loads the config that has been saved to make filling the fields easier
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
### Category IDs for Kick Ass Torrents:
**You can get any of these from the end of the Kick Ass Torrents link**
- Movies = movies
