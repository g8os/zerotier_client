class UserService:
    def __init__(self, client):
        self.client = client



    def getUser(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Get a user by UUID. Get a user by UUID
        It is method for GET /user/{id}
        """
        uri = self.client.base_url + "/user/"+id
        return self.client.get(uri, None, headers, query_params, content_type)


    def updateUser(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        Update user information.
        It is method for POST /user/{id}
        """
        uri = self.client.base_url + "/user/"+id
        return self.client.post(uri, data, headers, query_params, content_type)


    def listUsers(self, headers=None, query_params=None, content_type="application/json"):
        """
        List viewable or editable users (including yourself).
        It is method for GET /user
        """
        uri = self.client.base_url + "/user"
        return self.client.get(uri, None, headers, query_params, content_type)
