import  os,requests

base_url = "https://api.vk.com/method/%s"

def get_audios(owner_id, offset, count, token):
	url = base_url % "audio.get"
	params = {"v":"5.37","owner_id":owner_id,"offset":offset,"count":count,"access_token":token}
	resp = requests.get(url, params=params, timeout=3).json()
	return resp["response"]["items"]

def download(url, path):
	with open(path, "wb") as f:
		f.write(requests.get(url, timeout=3).content)

def get_name(owner_id):
	if owner_id < 0:
		return get_community(-owner_id)["screen_name"]
	else:
		return get_user(owner_id)["screen_name"]

def get_community(id):
	url = base_url % "groups.getById"
	params = {"v":"5.37","group_ids":id}
	resp = requests.get(url, params=params, timeout=3).json()
        return resp["response"][0]

def get_user(id):
        url = base_url % "users.get"
        params = {"v":"5.37","user_ids":id,"fields":"screen_name"}
        resp = requests.get(url, params=params, timeout=3).json()
        return resp["response"][0]

