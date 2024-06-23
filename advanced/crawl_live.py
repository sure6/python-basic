# -*- coding: UTF-8 -*-
"""
@File: crawl_live.py
@Description: 
@Author: lee sure
@DateTime: 2022/06/10 01:19
@Project_name: python-advanced
@IDE: PyCharm
"""
import requests

huya_headers={
  "Host": "live.huya.com",
  "Connection": "keep-alive",
  "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "sec-ch-ua-mobile": "?0",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
  "sec-ch-ua-platform": "\"Windows\"",
  "Origin": "https://www.huya.com",
  "Sec-Fetch-Site": "same-site",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Dest": "empty",
  "Referer": "https://www.huya.com/",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
  "Cookie": "udb_deviceid=w_589942117006295040; game_did=JNM-QVihB8ydeX2AssI7m1Tn05IhvukUHY6; Hm_lvt_51700b6c722f5bb4cf39906a596ea41f=1655389605; __yamid_new=C9DD608C7DE00001D66C22904E6EA5B0; __yamid_tt1=0.7631724674542615; __yasmid=0.7631724674542615; udb_passdata=3; udb_guiddata=82a70bdfa2894dddacaa3c1bcca3df83; udb_cred=CoAhVMgC4kZ5kmcdURghK1y6Da3W3GnX6dtmMzZEO9Tn35ZfuQgKLNv6vE1zsQji6rFx86IXF3rnwcEWngsRtDYySEFooh67-nPfmgYDyrX-mFyvB-K-J2U8iZTWb0wmiB0; udb_origin=0; udb_passport=1315279127yy; udb_status=1; udb_uid=1211215460; udb_version=1.0; username=1315279127yy; yyuid=1211215460; udb_accdata=undefined; __yaoldyyuid=1211215460; _yasids=__rootsid%3DC9DD60955BD00001D9CA1DE014A1EC50; isInLiveRoom=true; guid=0a43e46f8140ab627501fd3efe3e082b; udb_anouid=1464187792002; SoundValue=0.89; alphaValue=0.30; rep_cnt=60; videoLine=3; videoBitRate=2000; udb_biztoken=AQC6j29jq_MEq5YDlwYXUw1kIVnJQvZMLK4nvifSeLdOx8w-r_9X5DgZNtWm217HHV50v0b6uhEP1TIg-8ld4d6RYOsMX-gSL3H9wccChIFlsCaAyRtVG8DMODNYQmwPlxwutr1euqnB70fiAC7fSoST_cmgiLzyQe662lkB_V48iwaDOfDYhxbpEeF3atEoIWelNsaYc-o922gWgMO8-LvoYjusnvIYHPiASilupBOEMFMyJOTcYdfHGQxvoWAYWt9cpI6FKgzcVOhaW_hn6QeZZ5IeGT-j7zZQIszhGlzLQ5a5xqXoeS7siUMW9U4I8MJ_7BMVjEGU3yoveTPh6-uF; huya_flash_rep_cnt=900; h_unt=1655789155; Hm_lpvt_51700b6c722f5bb4cf39906a596ea41f=1655791982; huya_web_rep_cnt=2186"
}

douyu_headers = {"Host": "www.douyu.com",
           "Connection": "keep-alive",
           "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
           "Accept": "application/json, text/plain, */*",
           "x-dy-traceid": "0fc611a06308c0a6:0fc611a06308c0a6:0:001874",
           "X-Requested-With": "XMLHttpRequest",
           "sec-ch-ua-mobile": "?0",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
           "sec-ch-ua-platform": "\"Windows\"",
           "Sec-Fetch-Site": "same-origin",
           "Sec-Fetch-Mode": "cors",
           "Sec-Fetch-Dest": "empty",
           "Referer": "https://www.douyu.com/directory/myFollow",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
           "Cookie": "Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1655389671; acf_did=95c8acd96c6071465b17a8b700031601; dy_did=95c8acd96c6071465b17a8b700031601; PHPSESSID=7mpo720vpge8ha3rdms1qdhfa5; acf_auth=7a6dTs9LB3O5z1SIlP%2FtCRauscdpbzuDbXzL7%2BaBYC%2B6e6xh4DGjXZgDPnxLxQkxVoPC4czKznY3VrguNvOoDkv3Y3w92WHz730JzhyOKX2LLFZr6E8ZF7c; dy_auth=0c33f7mdu6irnkgsLemJ7eq82xKXe17iA513VX1x%2F1Wq1DH0%2BalLDwcIdHH4zXOO35ZQOAVuX4%2B6a13UE7thC%2FTJLzXzKaQFx5thdcFb5TXBfsodD20P0Yk; wan_auth37wan=4ead08ae5446SA4auML2q47yHOu8RUbJYhoQauZaAmEQyg1adsk6BfOHUyTOjNnCnsBIe%2FqBDMJnHkLqgyG7y55VHQht3mzz%2FpnFWfBPuckheZdHgPo; acf_uid=337231968; acf_username=337231968; acf_nickname=arm58771; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; acf_avatar=https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar_v3%2F201912%2F693d09e4ad754e628bed6e2b0f3b180d_; acf_ct=0; acf_ltkid=34695762; acf_biz=1; acf_stk=8de82fce28faa786; loginrefer=pt_f470hk80i0i; fdata=www.douyu.com%7C%7C%3B%7C%7C%3B%7C%7C%3B%7C%7C%3B%7C%7C%3B%7C%7C%3B; acf_ccn=fe12e4246a2acf970d88e24a10d8fb62; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1655790770"}

r_douyu = requests.get(r"https://www.douyu.com/wgapi/livenc/liveweb/follow/list?sort=0&cid1=0", headers=douyu_headers)
r_huya = requests.get(r"https://live.huya.com/liveHttpUI/getUserSubscribeToInfoList?iPageIndex=0&_=1655791980458", headers=huya_headers)

print(r_huya.json())
