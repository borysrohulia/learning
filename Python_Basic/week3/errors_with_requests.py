import sys
import requests

url = sys.argv[1]
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print("Error. Time out, url: ", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print("Error url: {0}, code: {1}".format(err, code))
except requests.RequestException:
    print("Base Error, url: ", url)
else:
    print(response.content)