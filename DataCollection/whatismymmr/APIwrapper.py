import requests
from ratelimit import limits, sleep_and_retry


base_uri = "https://na.whatismymmr.com/api/v1/summoner?name="


@sleep_and_retry
@limits(calls=59, period=60)
def call_api(url) -> requests.models.Response:
    response = requests.get(url)
    print(type(response))
    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))

    return response


if __name__ == "__main__":
    res = call_api(base_uri + "Sparysgah").json()

    for j in res['ranked']:
        print(j, res['ranked'][j])
