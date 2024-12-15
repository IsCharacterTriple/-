import requests
import time

default_uid = "515268644"
print("#不输入则默认为赵泽先生的UID")
UID = input("请输入UID:").strip()
if not UID:
    UID = default_uid
    print(f"将获取赵泽先生的粉丝数")

url = f"https://api.bilibili.com/x/relation/stat?vmid={UID}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
}

while True:
    response = requests.get(url, headers=headers)
    data = response.json()
    following = data.get('data', {}).get('follower')
    
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f'{current_time} UID {UID} 的粉丝数: {following}')
    
    time.sleep(0.2)
