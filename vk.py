import requests
import operator
from functools import reduce
from time import sleep

base_url = "https://api.vk.com/method/%s"

class VkException(Exception):
    """Exception during VK session"""
    def __init__(self, code, msg):
        super(VkException, self).__init__(msg)
        self.code = code
        
def get_wall_audios(owner_id, offset, count, token):
    MAX_POSTS = 100
    audios = []
    for i in range(offset, offset+count, MAX_POSTS):
        posts = get_posts(owner_id, i, min(count,MAX_POSTS), token)
        sleep(0.3)
        extracted = map(extract_audios_from_post, posts)
        if extracted:
            audios += reduce(operator.add, extracted)
    return audios

def extract_audios_from_post(post):
    audios = []
    if not "attachments" in post: return audios
    attaches = post["attachments"]
    if attaches:
        for a in attaches:
            if a["type"]=="audio":
                audios.append(a["audio"])
    return audios

def get_posts_count(owner_id, token):
    assert type(owner_id) in (str,int)
    assert type(token) in (str,)
    url = base_url % "wall.get"
    params = {"v":"5.37","owner_id":owner_id,"offset":0,"count":1,"access_token":token}
    resp = requests.get(url, params=params, timeout=10).json()
    check_error(resp)
    return resp["response"]["count"]

def get_posts(owner_id, offset, count, token):
    assert type(owner_id) in (str,int)
    assert type(token) in (str,)
    url = base_url % "wall.get"
    params = {"v":"5.37","owner_id":owner_id,"offset":offset,"count":count,"access_token":token}
    resp = requests.get(url, params=params, timeout=10).json()
    check_error(resp)
    return resp["response"]["items"]

def get_audios(owner_id, offset, count, token):
    assert type(owner_id) in (str,int)
    assert type(token) in (str,)
    url = base_url % "audio.get"
    params = {"v":"5.37","owner_id":owner_id,"offset":offset,"count":count,"access_token":token}
    resp = requests.get(url, params=params, timeout=10).json()
    check_error(resp)
    return resp["response"]["items"]

def download(url, path):
    assert type(url) in (str,)
    assert type(path) in (str,)
    with open(path, "wb") as f:
        f.write(requests.get(url, timeout=3).content)

def get_name(owner_id):
    assert type(owner_id) in (str,int)
    if isinstance(owner_id,str): return owner_id
    if owner_id < 0:
        return get_community(-owner_id)["screen_name"]
    else:
        return get_user(owner_id)["screen_name"]

def get_id(owner_id):
    assert type(owner_id) in (str,int)
    if isinstance(owner_id,int): return owner_id
    try:
        return -get_community(owner_id)["id"]
    except VkException:
        return get_user(owner_id)["id"]

def get_community(id):
    assert type(id) in (str,int)
    url = base_url % "groups.getById"
    params = {"v":"5.37","group_ids":id}
    resp = requests.get(url, params=params, timeout=3).json()
    check_error(resp)
    return resp["response"][0]

def get_user(id):
    assert type(id) in (str,int)
    url = base_url % "users.get"
    params = {"v":"5.37","user_ids":id,"fields":"screen_name"}
    resp = requests.get(url, params=params, timeout=3).json()
    check_error(resp)
    return resp["response"][0]

def check_error(resp):
    if "error" in resp:
        err = resp["error"]
        raise VkException(err["error_code"], err["error_msg"])