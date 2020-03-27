<h3 align="center"><img src="https://i.imgur.com/pX9no9C.png" width="600px"></h3>
<p align="center">
  <a href="https://github.com/eliasbenb/MagnetMagnet/releases"><img src="https://img.shields.io/github/downloads/eliasbenb/MagnetMagnet/total?color=%234197fe&style=for-the-badge"></a>
  <a href="https://github.com/eliasbenb/MagnetMagnet/releases/latest"><img src="https://img.shields.io/github/v/release/eliasbenb/MagnetMagnet?color=%234197fe&style=for-the-badge"></a>
</p>

# What is this repo?
MagnetMagnet is well, a magnet link magnet, it's a scraper that allows you to scrape magnet links from RARBG, The Pirate Bay and Kick Ass Torrents. It allows allows you to search Kick Ass Torrents and The Pirate Bay for torrents. I decided to make this app to improve my Python skills.

## Features supported:
- Scrape magnet links using specific keywords
- Scraping magnet links from all RARBG mirrors
- Scraping magnet links from **most** The Pirate Bay mirrors
- Scraping magnet links from **most** Kick Ass Torrents mirrors
- Ability to choose multiple categories/subcategories to scrape magnet links from
- Copies magnet links to clipboard
- Exports magnet links into .txt file

## To do list:
- Add support to http://nyaa.si/

## How to use:
### Installing:
**To install MagnetMagnet either download the executable file from [here](https://github.com/eliasbenb/MagnetMagnet/releases).**
**Or you can download the python file above and run it using python (make sure to install the dependencies in the requirements.txt file)**
### Usage:
- On launch you get four options of torrent indexers to scrape from: RARBG, The Pirate Bay, Kick Ass Torrents and 1377x, and an option to make custom search querys for all the aformentioned torrent indexers in the 'Search' menu
![App Screenshot](https://user-images.githubusercontent.com/54410649/77454424-f27d0380-6e11-11ea-95da-9e9b0e6cf4fb.PNG)

- In the MagnetMagnet Search app you have two user editable fields:
![App Screenshot](https://user-images.githubusercontent.com/54410649/77783311-0aeb5900-7072-11ea-8b53-d1a392dbb05e.PNG)
- Checkboxes: you can select/deselect the torrent indexers you would like to search from
- Search box: here you enter what the search query you would like to submit is
To copy any generated magnet links you click on any item in the dropdown

- There are only three user changeable fields in MagnetMagnet's scraper:
![App Screenshot](https://user-images.githubusercontent.com/54410649/77454431-f577f400-6e11-11ea-805e-e21f4e84640e.PNG)
- Domain: the first field is for the domain, here just input the torrent scraper's domain. I reccomend https://rarbg.to/ / https://tpb.party/ / https://kat.rip/ / https://1377x.to/ as of 24th March 2020
- Category Number: the second field is for the category number. This must be entered as string ID. All the category IDs can be found below
- Clipboard: this is the third field and is a yes or no option, this just copies the magnet links to your clipboard
- Save Config: this saves whatever is inputed in the text fields to a config file stored in %APPDATA%\eliasbenb
- Load Config: this loads the config that has been saved to make filling the fields easier
## Category IDs:
<h3>Kick Ass Torrents:</h3>
<details><summary>Category IDs for Kick Ass Torrents</summary><br>
  <ul>
    <li> Movies = movies</li>
    <li> TV = tv</li>
    <li> Anime = anime</li>
    <li> Music = music</li>
    <li> Books = books</li>
    <li> Games = games</li>
    <li> Applications = applications</li>
    <li> XXX = xxx</li>
    <li> All = new</li>
  </ul>
</details>

<h3>RARBG:</h3>
<details><summary>Category IDs for RARBG</summary><br>
    <details><summary>XXX Subcategories</summary><br>
      <ul>
        <li> XXX (18+) = 4</li>
      </ul>
    </details>
    <details><summary>TV Shows Subcategories</summary><br>
      <ul>
        <li> TV Episodes = 18</li>
        <li> TV HD Episodes = 41</li>
        <li> TV UHD Episodes = 49</li>
      </ul>
    </details>
    <details><summary>Games Subcategories</summary><br>
      <ul>
        <li> Games/PC ISO = 27</li>
        <li> Games/PC RIP = 28</li>
        <li> Games/PS3 = 40</li>
        <li> Games/XBOX-360 = 32</li>
        <li> Games/PS4 = 53</li>
      </ul>
    </details>
    <details><summary>Music Subcategories</summary><br>
      <ul>
        <li> Music/MP3 = 23</li>
        <li> Music/FLAC = 25</li>
      </ul>
    </details>
    <details><summary>Software Subcategories</summary><br>
      <ul>
        <li> Software/PC ISO = 33</li>
      </ul>
    </details>
  </ul>
</details>

<h3>The Pirate Bay:</h3>
<details><summary>Category IDs for The Pirate Bay</summary><br>
  <ul>
    <details><summary>Audio Subcategories</summary><br>
      <ul>
        <li> Music = 101</li>
        <li> Audio books = 102</li>
        <li> Sound clips = 103</li>
        <li> FLAC = 104</li>
        <li> Other = 199</li>
      </ul>
    </details>
    <details><summary>Video Subcategories</summary><br>
      <ul>
        <li> Movies = 201</li>
        <li> Movies DVDR = 202</li>
        <li> Music videos = 203</li>
        <li> Movie clips = 204</li>
        <li> TV shows = 205</li>
        <li> Handheld = 206</li>
        <li> HD - Movies = 207</li>
        <li> HD - TV shows = 208</li>
        <li> 3D = 209</li>
        <li> Other = 299</li>
      </ul>
    </details>
    <details><summary>Applications Subcategories</summary><br>
      <ul>
        <li> Windows = 301</li>
        <li> Mac = 302</li>
        <li> Unix clips = 303</li>
        <li> Handheld = 304</li>
        <li> IOS (iPad/iPhone) = 305</li>
        <li> Android = 306</li>
        <li> Other OS = 399</li>
      </ul>
    </details>
    <details><summary>Games Subcategories</summary><br>
      <ul>
        <li> PC = 401</li>
        <li> Mac = 402</li>
        <li> PSx = 403</li>
        <li> XBOX360 = 404</li>
        <li> Wii = 405</li>
        <li> Handheld = 406</li>
        <li> IOS (iPad/iPhone) = 407</li>
        <li> Android = 408</li>
        <li> Other = 499</li>
      </ul>
    </details>
    <details><summary>Porn Subcategories</summary><br>
      <ul>
        <li> Movies = 501</li>
        <li> Movies DVDR = 502</li>
        <li> Pictures = 503</li>
        <li> Games = 504</li>
        <li> HD - Movies = 505</li>
        <li> Movie clips = 506</li>
        <li> Other = 599</li>
      </ul>
    </details>
    <details><summary>Other Subcategories</summary><br>
      <ul>
        <li> E-books = 601</li>
        <li> Comics = 602</li>
        <li> Pictures = 603</li>
        <li> Covers = 604</li>
        <li> Physibles = 605</li>
        <li> Other = 699</li>
      </ul>
    </details>
  </ul>
</details>

<h3>1377x:</h3>
<details><summary>Category IDs for 1377x</summary><br>
  <ul>
    <li> Movies = popular-movies</li>
    <li> TV = popular-tv</li>
    <li> Games = popular-games</li>
    <li> Music = popular-music</li>
    <li> Applications = popular-apps</li>
    <li> Anime = popular-anime</li>
    <li> Documentaries = popular-documentaries</li>
    <li> Other = popular-other</li>
    <li> XXX = popular-xxx</li>
  </ul>
</details>
