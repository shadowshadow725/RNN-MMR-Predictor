import requests
from ratelimit import limits, sleep_and_retry


base_uri = "https://na.whatismymmr.com/api/v1/summoner?name="


@sleep_and_retry
@limits(calls=50, period=60)
def call_api(url) -> requests.models.Response:
    headers = {
        'User-Agent': 'Windows:com.csc413.datacollection:v0.1'
    }
    response = requests.get(url, headers=headers)
    # cloudflare returning 503 for some reason 
    while response.status_code == 503:
        response = requests.get(url, headers=headers)
    return response


# if __name__ == "__main__":
#     res = call_api(base_uri + "Sparysgah").json()
    # print(res['ranked']['avg'])
