import requests

def getCards(key, tag='superpage'):

    url = "https://api.supernotes.app/v1/cards/get/select"

    payload = {
        "filter_group": {
            "type": "group",
            "op": "and",
            "filters": [
                {
                    "type": "tag",
                    "op": "contains",
                    "arg": f"{tag}"
                }
            ]
        },
        "sort_type": 0,
        "sort_ascending": True,
    }
    headers = {
        "Api-Key": key,
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers).text
    return response