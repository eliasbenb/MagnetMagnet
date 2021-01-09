import requests

headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(
    "https://torrentapi.org/pubapi_v2.php?get_token=get_token&app_id=MagnetMagnet", headers=headers)
print(res.json()["token"])
