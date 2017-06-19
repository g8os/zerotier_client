class NetworkService:
    def __init__(self, client):
        self.client = client



    def deleteMember(self, address, id, headers=None, query_params=None, content_type="application/json"):
        """
        Delete member from network
        It is method for DELETE /network/{id}/member/{address}
        """
        uri = self.client.base_url + "/network/"+id+"/member/"+address
        return self.client.delete(uri, None, headers, query_params, content_type)


    def getMember(self, address, id, headers=None, query_params=None, content_type="application/json"):
        """
        Get network member settings
        It is method for GET /network/{id}/member/{address}
        """
        uri = self.client.base_url + "/network/"+id+"/member/"+address
        return self.client.get(uri, None, headers, query_params, content_type)


    def updateMember(self, data, address, id, headers=None, query_params=None, content_type="application/json"):
        """
        Update member settings
        It is method for POST /network/{id}/member/{address}
        """
        uri = self.client.base_url + "/network/"+id+"/member/"+address
        return self.client.post(uri, data, headers, query_params, content_type)


    def listMembers(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Get a list of network members
        It is method for GET /network/{id}/member
        """
        uri = self.client.base_url + "/network/"+id+"/member"
        return self.client.get(uri, None, headers, query_params, content_type)


    def deleteNetwork(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Delete network
        It is method for DELETE /network/{id}
        """
        uri = self.client.base_url + "/network/"+id
        return self.client.delete(uri, None, headers, query_params, content_type)


    def getNetwork(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Get network configuration and status information
        It is method for GET /network/{id}
        """
        uri = self.client.base_url + "/network/"+id
        return self.client.get(uri, None, headers, query_params, content_type)


    def updateNetwork(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        Update network configuration
        It is method for POST /network/{id}
        """
        uri = self.client.base_url + "/network/"+id
        return self.client.post(uri, data, headers, query_params, content_type)


    def listNetworks(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get a list of networks this user owns or can view/edit
        It is method for GET /network
        """
        uri = self.client.base_url + "/network"
        return self.client.get(uri, None, headers, query_params, content_type)


    def createNetwork(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        Create a new network
        It is method for POST /network
        """
        uri = self.client.base_url + "/network"
        return self.client.post(uri, data, headers, query_params, content_type)
