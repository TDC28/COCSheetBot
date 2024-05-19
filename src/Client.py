import requests


class Client:
    def __init__(self, apikey: str) -> None:
        self.token = apikey if apikey is not None else ""
        self.api_endpoint = "https://api.clashofclans.com/v1"
        self.timeout = 45

    def get(self, uri: str):
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.token,
        }

        url = self.api_endpoint + uri

        response = requests.get(url, headers=headers, timeout=30)
        return response.json()

    def leaguegroup(self, tag: str) -> dict:
        """Returns the league group data associated to a given clan

        Parameters
        ----------
        tag : 'str'
            your clan tag"""
        return self.get(f"/clans/%23{tag[1:]}/currentwar/leaguegroup")

    def war(self, wartag: str) -> dict:
        """Returns the war data associated to a given wartag

        Parameters
        ----------
        wartag : 'str'
            the war tag"""
        return self.get(f"/clanwarleagues/wars/%23{wartag[1:]}")
