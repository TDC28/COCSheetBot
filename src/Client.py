import requests


class Client:
    def __init__(self, apikey: str) -> None:
        self.key = apikey
        self.api_endpoint = "https://api.clashofclans.com/v1"
        self.timeout = 45

    def get(self, uri: str) -> dict:
        """
        get(uri) makes a GET request to the Clash of Clans API.
        get: Client str -> dict
        """
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.key,
        }

        url = self.api_endpoint + uri

        response = requests.get(url, headers=headers, timeout=30)
        return response.json()

    def league_group(self, tag: str) -> dict:
        """
        league_group(tag) retrieves the league group information for a given clan-tag tag.
        league_group: Client str -> dict
        """
        return self.get(f"/clans/%23{tag[1:]}/currentwar/leaguegroup")

    def war(self, wartag: str) -> dict:
        """
        war(wartag) retrives the war information for a given war-tag wartag.
        war: Client str -> dict
        """
        return self.get(f"/clanwarleagues/wars/%23{wartag[1:]}")
