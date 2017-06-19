class SelfService:
    def __init__(self, client):
        self.client = client



    def getAuthenticatedUser(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get currently authenticated user (if any).
        It is method for GET /self
        """
        uri = self.client.base_url + "/self"
        return self.client.get(uri, None, headers, query_params, content_type)
