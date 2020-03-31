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
	- Kick Ass Torrents
	- The Pirate Bay
	- RARBG
	- 1377x
- Scraping magnet links using specific keywords
- Choosing multiple categories/subcategories to scrape magnet links from
- Exporting magnet links to .txt file in local directory
- Copying magnet links to the clipboard
- Config files to save preferred settings

# Installation
- To install MagnetMagnet either download the executable file from [here](https://github.com/eliasbenb/MagnetMagnet/releases).
- Or you can download the entire repository above and run [app.py](https://github.com/eliasbenb/MagnetMagnet/blob/master/app.py) using python (dependencies must be installed using `pip install -r requirements.txt`)

# Usage:
### Home Screen:
- On launch you get four options of torrent indexers to scrape from: 1377x, KAT, Nyaa, RARBG and TPB,
- There is also a fifth tab named 'Search' which allows you to scrape the aforementioned torrent indexers for specific words

![Home Screen](https://user-images.githubusercontent.com/54410649/78007431-58581680-734f-11ea-80e7-c4432dc607fd.PNG)
### Search:
- In the Search app you have two user editable fields:
- **Checkboxes:** you can select/deselect the torrent indexers you would like to search from
- **Search box:** here you enter the search query you would like to scrape
- **Table:** the table displays all the title names and magnet links for the torrents scraped, here you can copy the magnet link you would like

![Search](https://user-images.githubusercontent.com/54410649/78007442-5aba7080-734f-11ea-97ae-7920e4998c0d.PNG)
### Scrapers:
- There are only two user changeable fields in the scraper apps:
- **Domain:** the first field is for the domain, here just choose the torrent indexer's domain.
- **Category:** the second field is for the category which you can choose from the drop down box

![Scrapers](https://user-images.githubusercontent.com/54410649/78007445-5b530700-734f-11ea-9e5c-575d851a04cd.PNG)
