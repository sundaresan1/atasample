import httplib2
import json
import assertpy


def getStarWarsPeopleInfo():
    h = httplib2.Http(".cache")
    (resp_headers, content) = h.request("https://swapi.dev/api/people/1/", "GET")

    return content


def getNameFromPeopleInfo():
    people_dict = json.loads(getStarWarsPeopleInfo())
    name = people_dict['name']
    hair_color = people_dict['hair_color']

    return [name, hair_color]


def assertAValue():
    info_list = getNameFromPeopleInfo()
    assertpy.assert_that(info_list[1]).is_equal_to('blond')


def getGoRestPosts():
    h = httplib2.Http(".cache")
    headers = {'Authorization' : 'Bearer 1cd3184440f7fc486992ca46d0ea836ceb06dca2fdcce7bb52e7cf04b58963a5'}
    (resp_headers, content) = h.request("https://gorest.co.in/public-api/users/123/posts", "GET", headers=headers)

    return content


if __name__ == '__main__':
    print(getStarWarsPeopleInfo())
    print(getNameFromPeopleInfo())
    assertAValue()
    print(getGoRestPosts())