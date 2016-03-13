# coding=UTF-8
import requests
from bs4 import BeautifulSoup

# Datas
login_url = "https://portalx.yzu.edu.tw/PortalSocialVB/Login.aspx"
user_id = ""
user_password = ""
main_url = "https://portalx.yzu.edu.tw/PortalSocialVB/FMain/DefaultPage.aspx?Menu=Default&LogExcute=Y"

req_ses = requests.Session()
site = req_ses.get(login_url)
dom = BeautifulSoup(site.text, "lxml")

# For Login
__VIEWSTATE = dom.find(id = "__VIEWSTATE")['value']
__VIEWSTATEGENERATOR = dom.find(id = "__VIEWSTATEGENERATOR")['value']
__EVENTVALIDATION = dom.find(id = "__EVENTVALIDATION")['value']

form = {
        '__VIEWSTATE' : __VIEWSTATE,
        '__VIEWSTATEGENERATOR' : __VIEWSTATEGENERATOR,
        '__EVENTVALIDATION' : __EVENTVALIDATION,
        'Txt_UserID' : user_id,
        'Txt_Password' : user_password,
        'ibnSubmit' : '登入'
}

portal = req_ses.post(login_url, data = form)
portal = req_ses.get(main_url)
print(portal.text)
