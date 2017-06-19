class StatusService:
    def __init__(self, client):
        self.client = client

    def getStatus(self, headers=None, query_params=None):
        """
        Get system version, status, and uptime. This returns the current status of the system. Unlike most of the API it is avilable without authentication, though some fields are omitted in
        this case.
        It is method for GET /status
        """
        uri = self.client.base_url + "/status"
        return self.client.session.get(uri, headers=headers, params=query_params)
