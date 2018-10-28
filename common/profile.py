import requests

class UserProfile(object):
    def __init__(self, fb_id=None, token=None, **option):
        self.token = token
        self.fb_id = fb_id
        self.api_url = "https://graph.facebook.com/v2.6/" + self.fb_id + "?fields=first_name,last_name,gender,locale,timezone,profile_pic&access_token=" + self.token
        self.results = {}
        self.results = requests.get(url=self.api_url, 
                            params={"access_token": self.token},
                            headers={'Content-type': 'application/json'}).json()
        if self.results is None:
            self.results = {}

    @property
    def first_name(self):
        return self.results.get("first_name", None)

    @property
    def last_name(self):
        return self.results.get("last_name", None)

    @property
    def profile_pic(self):
        return self.results.get("profile_pic", None)

    @property
    def id(self):
        return self.results.get("id", None)

    @property
    def locale(self):
        return self.results.get("locale", None)

    @property
    def gender(self):
        return self.results.get("gender", None)
    
    @property
    def timezone(self):
        return self.results.get("timezone", None)