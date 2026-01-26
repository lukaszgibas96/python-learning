import requests

def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
            )
        response.raise_for_status()

    except requests.HTTPError:
        print("Couldn't complete requests!")
        return
    
    content = response.json()
    return [artists["title"] for artists in content["data"]]