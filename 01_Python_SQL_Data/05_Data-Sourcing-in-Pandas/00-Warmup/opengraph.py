import requests

def fetch_metadata(url):
    """
    Return a dictionary of OpenGraph metadata found in HTML of given url
    """
    try:
        response = requests.get("https://opengraph.lewagon.com", params={'url': url})
        return response.json()["data"]
    except:
        return {}

# To manually test, please uncomment the following lines and run `python opengraph.py`:
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(fetch_metadata("https://www.github.com"))
