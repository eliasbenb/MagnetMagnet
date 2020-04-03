<a href="#"><h3 align="center"><img src="https://i.ibb.co/w4drV5g/Magnet-Magnet-Header.png" width="600px"></h3></a>
<p align="center">
  <a href="https://github.com/eliasbenb/MagnetMagnet/releases"><img src="https://img.shields.io/github/downloads/eliasbenb/MagnetMagnet/total?color=%234197fe&style=for-the-badge"></a>
  <a href="https://github.com/eliasbenb/MagnetMagnet/releases/latest"><img src="https://img.shields.io/github/v/release/eliasbenb/MagnetMagnet?color=%234197fe&style=for-the-badge"></a>
</p>
<p align="center">
  <a href="https://eliasbenb.github.io"><img src="https://i.ibb.co/6mG3jFz/Produced-by-eliasbenb.png" width="180"></a>
</p>

# What is this repo?
MagnetMagnet is well, a magnet link magnet, it's a scraper that allows you to scrape torrent magnet links from a range of torrent indexers. I decided to make this app to improve my Python skills.


## Features supported:
- Supported torrent indexers:
	- 1377x
	- Kick Ass Torrents
	- Nyaa
	- RARBG
	- The Pirate Bay
- Scraping magnet links using specific keywords
- Choosing the category/subcategory to scrape magnet links from
- Exporting magnet links to .txt file in local directory

# Installation
- To install MagnetMagnet either download the latest executable file from [here](https://github.com/eliasbenb/MagnetMagnet/releases).
- Or you can download the entire repository from [here](https://github.com/eliasbenb/MagnetMagnet/archive/master.zip) and run [main.py](https://github.com/eliasbenb/MagnetMagnet/blob/master/main.py) using python (dependencies must be installed using `pip install -r requirements.txt`)

# Usage:
### Home Screen:
- On launch you get four options of torrent indexers to scrape from: 1377x, KAT, Nyaa, RARBG and TPB,
- There is also a fifth tab named 'Search' which allows you to scrape the aforementioned torrent indexers for specific words

![Home Screen](https://user-images.githubusercontent.com/54410649/78363315-96ae3980-75cc-11ea-9d46-b5ad969a9bbd.PNG)
### Search:
- In the Search app you have two user editable fields:
- **Checkboxes:** you can select/deselect the torrent indexers you would like to search from
- **Search box:** here you enter the search query you would like to scrape
- **Table:** the table displays all the title names and magnet links for the torrents scraped, here you can copy the magnet link you would like by selecting it

![Search](https://user-images.githubusercontent.com/54410649/78363305-94e47600-75cc-11ea-9982-64143e1a1c97.PNG)
### Scrapers:
- There are only two user changeable fields in the scraper apps:
- **Domain:** the first field is for the domain, here just choose the torrent indexer's domain.
- **Category:** the second field is for the category which you can choose from the drop down box

![Scrapers](https://user-images.githubusercontent.com/54410649/78007445-5b530700-734f-11ea-9e5c-575d851a04cd.PNG)
