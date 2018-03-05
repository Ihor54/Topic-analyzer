import json
import requests


def vkRequestBuilder(method, **kwargs):
    """
    :param method: method of VK API we want to request
    :param kwargs: arguments of the current method
    :return:
    """
    # form the link of the request
    api_request = 'https://api.vk.com/method/' + method + '?'
    # add parameters
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    return json.loads(requests.get(api_request).text)


def getGroupDescription(ids):
    """
    :param ids: string of the format '1,2,3' containing ids of the group
    :return: dictionary of the format (group, description) if description is not empty
    """
    # send the request
    link = vkRequestBuilder('groups.getById', group_ids=ids, fields='description', v=5.73)
    #receive the response
    link = link['response']
    groupDescr = {}
    for grp in link:
        if 'description' in grp:
            if grp['description']:
                groupDescr[grp['name']] = grp['description']
    return groupDescr


if __name__ == '__main__':
    var = vkRequestBuilder('users.get', user_id=57636259, v=5.73)
    print(var)
    ids = ','.join([str(i) for i in range(1, 10)])
    g = getGroupDescription(ids)
    for k, v in g.items():
        print(k, ':::::::', v)
