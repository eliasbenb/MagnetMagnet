from pathlib import Path, PureWindowsPath
import os, platform

_platform_ = platform.system()


if _platform_ == 'Windows':
    base_path = PureWindowsPath('%s\\eliasbenb\\MagnetMagnet' %  os.environ['APPDATA'])
else:
    base_path = Path('%s/eliasbenb/MagnetMagnet' % os.environ['HOME'])

images_path = base_path/'images'
icon = str(images_path / "icon.png")
github_icon = str(images_path / "github.png")
website_icon = str(images_path / "website.png")
kat_icon = str(images_path / "kat.png")
nyaa_icon = str(images_path / "nyaa.png")
tpb_icon = str(images_path / "tpb.png")
x1377_icon = str(images_path / "x1377.png")
rarbg_icon = str(images_path / "rarbg.png")