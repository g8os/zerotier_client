from zerotier import client
import json


token = 'xs9kKSrhHHqcgCqymjAxj9e69tktPDbJ' # fill it with your zerotier token

# create client and set the authentication header
client = client.Client()
client.set_auth_header("Bearer " + token)

# print network status
resp = client.status.GET_status()
print("NETWORK STATUS \n", resp.text)

# print name of first network
networks = client.network.GET_network().json()
net1 = networks[0]

print("network name = ", net1['config']['name'])

# modify network name
net1['config']['name'] = net1['config']['name'][::-1] # reverse the network name

print(client.network.POST_network_id(net1, net1['id']))

# get the modified network
new_net = client.network.GET_network_id(net1['id']).json()
print("new network name=", new_net['config']['name'])
