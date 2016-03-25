import requests
uname = ""
passwd = ""

url = "http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://phc.prontonetworks.com/"
load = {'userId':uname,'serviceName':"ProntoAuthentication",'password':passwd,'Submit22':"Login"}
s = requests.Session()
s.get(url)
r = s.post(url,data=load)