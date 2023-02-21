
API_KEY = '2486d647-45db-4abe-8315-2dcfcf694452'
def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urllib.parse.urlencode  (payload)
    return proxy_url