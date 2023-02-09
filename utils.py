import requests
from pprint import pprint


def get_data(url):
    try:
        response = requests.get(url)  # .json()
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно"
        print(response.status_code)
        return None, f"ERROR: status_code:{response.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "ERROR:  requests.exceptions.ConnectionError"
    except requests.exceptions.JSONDecodeError:
        print(response.url)
        return None, "ERROR:  requests.exceptions.JSONDecodeError"

def get_filtered_data(data, filtered_empty_from=False):
    pprint(data[:5])
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data
    # pprint(response)