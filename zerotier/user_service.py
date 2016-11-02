class UserService:
    def __init__(self, client):
        self.client = client



    def GET_user(self, headers=None, query_params=None):
        """
        List viewable or editable users (including yourself). List viewable or editable users (including yourself)
        It is method for GET /user
        """
        uri = self.client.base_url + "/user"
        return self.client.session.get(uri, headers=headers, params=query_params)


    def GET_user_id(self, id, headers=None, query_params=None):
        """
        Get a user by UUID. Get a user by UUID
        It is method for GET /user/{id}
        """
        uri = self.client.base_url + "/user/"+id
        return self.client.session.get(uri, headers=headers, params=query_params)


    def POST_user_id(self, data, id, headers=None, query_params=None):
        """
        Update user information. Update user information
        It is method for POST /user/{id}
        """
        uri = self.client.base_url + "/user/"+id
        return self.client.session.post(uri, data, headers=headers, params=query_params)
