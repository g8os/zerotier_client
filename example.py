from zerotier import client as ztclient
import json


def main():
    token = 'xs9kKSrhHHqcgCqymjAxj9e69tktPDbJ'  # fill it with your zerotier token

    # create client and set the authentication header
    client = ztclient.Client()
    client.set_auth_header("Bearer " + token)

    # print network status
    resp = client.status.getStatus()
    print("NETWORK STATUS \n", resp.text)

    # print name of first network
    networks = client.network.listNetworks().json()
    if len(networks) <= 0:
        return

    net1 = networks[0]

    print("network name = ", net1['config']['name'])

    # modify network name
    net1['config']['name'] = net1['config']['name'][::-1]  # reverse the network name

    print(client.network.updateNetwork(net1, net1['id']))

    # get the modified network
    new_net = client.network.getNetwork(net1['id']).json()
    print("new network name=", new_net['config']['name'])

if __name__ == "__main__":
    main()
