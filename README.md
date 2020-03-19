<h3 align="center"><img src="https://i.imgur.com/pX9no9C.png" width="600px"></h3>
<p align="center">
  <a href="https://github.com/eliasbenb/MagnetMagnet/releases"><img src="https://img.shields.io/github/downloads/eliasbenb/MagnetMagnet/total?color=%234197fe&style=for-the-badge"></a>
  <a href="https://github.com/eliasbenb/MagnetMagnet/releases/latest"><img src="https://img.shields.io/github/v/release/eliasbenb/MagnetMagnet?color=%234197fe&style=for-the-badge"></a>
</p>

# What is this repo?
MagnetMagnet is well, a magnet link magnet, it's a scraper that allows you to scrape magnet links from RARBG, The Pirate Bay and Kick Ass Torrents. I decided to make this app to improve my Python skills.

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
- Category Number: the second field is for the category number. This must be entered as a number ID. Multiple IDs can be inputed at once when seperated by a semi colon ';'. ** All the category IDs can be found below **
- Clipboard: this is the third field and is a yes or no option, this just copies the magnet links to your clipboard
- Save Config: this saves whatever is inputed in the text fields to a config file stored in %APPDATA%\eliasbenb
- Load Config: this loads the config that has been saved to make filling the fields easier
## Category IDs:
<h3>KAT:</h3>
<details><summary>Category IDs for KAT</summary><br>
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
    <li> XXX = 2;4</li>
    <details><summary>XXX Subcategories</summary><br>
      <ul>
        <li> XXX (18+) = 4</li>
      </ul>
    </details>
    <li> TV Shows = 2;18;41;49</li>
    <details><summary>TV Shows Subcategories</summary><br>
      <ul>
        <li> TV Episodes = 18</li>
        <li> TV HD Episodes = 41</li>
        <li> TV UHD Episodes = 49</li>
      </ul>
    </details>
    <li> Games = 2;27;28;29;30;31;32;40;53</li>
    <details><summary>Games Subcategories</summary><br>
      <ul>
        <li> Games/PC ISO = 27</li>
        <li> Games/PC RIP = 28</li>
        <li> Games/PS3 = 40</li>
        <li> Games/XBOX-360 = 32</li>
        <li> Games/PS4 = 53</li>
      </ul>
    </details>
    <li> Music = 2;23;24;25;26</li>
    <details><summary>Music Subcategories</summary><br>
      <ul>
        <li> Music/MP3 = 23</li>
        <li> Music/FLAC = 25</li>
      </ul>
    </details>
    <li> Software = 2;33;34;43 </li>
    <details><summary>Software Subcategories</summary><br>
      <ul>
        <li> Software/PC ISO = 33</li>
      </ul>
    </details>       
  </ul>
</details>
<h3>TPB:</h3>
<details><summary>Category IDs for TPB</summary><br>
  <ul>
    <li> Audio = 100</li>
    <details><summary>Audio Subcategories</summary><br>
      <ul>
        <li> Music = 101</li>
        <li> Audio books = 102</li>
        <li> Sound clips = 103</li>
        <li> FLAC = 104</li>
        <li> Other = 199</li>
      </ul>
    </details>
    <li> Video = 200</li>
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
    <li> Applications = 300</li>
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
    <li> Games = 400</li>
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
    <li> Porn = 500</li>
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
    <li> Other = 600</li>
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
    <li> All = 0</li>
  </ul>
</details>
## Working Mirrors:
<h3><details><summary>KAT</summary><br></h3>
  <ul>
    <li> https://kat.rip/</li>
    <li> https://thekat.app/</li>
    <li> https://kickass.ws/</li>
    <li> https://thekat.info/</li>
    <li> https://katcr.co/</li>
  </ul>
</details>
<h3><details><summary>RARBG</summary><br></h3>
  <ul>
    <li> https://rarbgmirror.com/</li>
    <li> https://rarbgaccess.org/</li>
    <li> http://rarbgproxy.org/</li>
    <li> https://rarbgmirror.org/</li>
    <li> https://rarbg.to/</li>
  </ul>
</details>
<h3><details><summary>TPB</summary><br></h3>
  <ul>
    <li> https://piratebay.live/</li>
    <li> https://tpb.party/</li>
    <li> https://piratepiratepirate.net/</li>
    <li> https://lepiratebay.org/</li>
    <li> https://thehiddenbay.com/</li>
  </ul>
</details>
