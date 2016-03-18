import  os,requests

base_url = "https://api.vk.com/method/%s"
download_dir = os.environ["HOME"]+"/Music/Mauveton"

def get_audios(owner_id, offset, count, token):
	url = base_url % "audio.get"
	params = {"v":"5.37","owner_id":owner_id,"offset":offset,"count":count,"access_token":token}
	resp = requests.get(url, params=params, timeout=3).json()
	return resp["response"]["items"]

def download(url, owner, name):
	mp3 = requests.get(url, timeout=3).content
	owner_dir = download_dir+os.sep+get_name(owner)
	os.makedirs(owner_dir)
	with open(owner_dir+os.sep+name,"wb") as f:
		f.write(mp3)

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

