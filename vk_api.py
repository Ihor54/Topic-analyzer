import json
import requests


def vkRequestBuilder(method, **kwargs):
    """
    :param method: method of VK API we want to request
    :param kwargs: arguments of the current method
    :return:
    """
    api_request = 'https://api.vk.com/method/' + method + '?'
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    return json.loads(requests.get(api_request).text)


def getGroupDescription(ids):
    link = vkRequestBuilder('groups.getById', group_ids=ids, fields='description', v=5.73)
    link = link['response']
    print(link)
    groupDescr = {}
    print(len(link))
    for grp in link:
        if 'desription' in grp:
            if grp['description']:
                groupDescr[grp['name']] = grp['description']
    return groupDescr


if __name__ == '__main__':
    var = vkRequestBuilder('users.get', user_id=57636259, v=5.73)
    print(var)
    # var = json.loads(var)
    # print(var)
    # ids = ','.join([str(i) for i in range(1, 3)])
    group = getGroupDescription(1)
    print(group)
    for k, v in group.items():
        print(k, ':::::::', v)
