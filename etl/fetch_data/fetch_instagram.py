import requests 
import json 

ACCESS_TOKEN=""
INSTAGRAM_BUSINESS_ID=""

def fetch_instagram_metrics():
    url=f"https://graph.facebook.com/v19.0/{INSTAGRAM_BUSINESS_ID}/insights"
    params={
        "metric":"impressions,reach,engament",
        "period":"day",
        "access_token":ACCESS_TOKEN
    }
    response=requests.get(url,params=params)
    data=response.json()
    with open("data/raw_instagram.json","w") as f: 
        json.dump(data, f, indent=4)

if _name_=="__main__":
    fetch_instagram_metrics()