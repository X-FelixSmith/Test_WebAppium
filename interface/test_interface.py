import requests


def test_get_token():
    ID = "wwf9941b46c51c399e"
    SECRET = "WrHORWp_Pw0j9O1_Qdy0av1P7diImwNOmWw9L_QDbi8"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}"
    r = requests.get(url=url)
    print(r.json())
    access_token = r.json()["access_token"]
    print(access_token)
    return access_token

# 创建成员
# 调试工具
# 请求方式：POST（HTTPS）
# 请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
def test_create_member():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_token()}"
    # print(url)
    params = {
        "userid":"0402",
        "name":"张三",
        "mobile":"18000000000",
        "department": [2]
    }
    r = requests.post(url=url,json=params)
    print(r.json())
    errcode = r.json()["errcode"]
    assert errcode == 0

# 请求方式：GET（HTTPS）
# 请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
def test_search_member():
    USERID = "0402"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get_token()}&userid={USERID}"
    r = requests.get(url=url)
    print(r.json())
    errcode = r.json()["errcode"]
    assert errcode == 0

# 请求方式：GET（HTTPS）
# 请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
def test_del_member():
    USERID = "0402"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_get_token()}&userid={USERID}"
    r = requests.get(url=url)
    print(r.json())
    errcode = r.json()["errcode"]
    assert errcode == 0