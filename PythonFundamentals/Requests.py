import requests

for i in xrange(1,20):
    url = "https://anapioficeandfire.com/api/houses/{}".format(i)
    resp = requests.get(url)
    print resp.json()['name']