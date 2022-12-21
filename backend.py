import requests
import json
from auth import MyAuth

def headerfxn(head):
    header = json.loads(head)
    return(header)

def request(t, url,auth_token, head,param,json1):
    while len(head)>1:
        jsheader = headerfxn(head)
        break
    else:
        jsheader=head
    if t=="GET":
        r = requests.get(url, auth= MyAuth(auth_token) , headers=jsheader, params =param,json=json1)
        statcode =r.status_code
        txt =r.text
        hed = r.headers
        
    if t=="POST":
         r = requests.post(url, auth= MyAuth(auth_token), headers=jsheader, params= param,json=json1)
         statcode =r.status_code
         txt =r.text
         hed = r.headers

    if t=="PUT":
         r = requests.put(url, auth=MyAuth(auth_token), headers=jsheader, params= param,json=json1)
         statcode =r.status_code
         txt =r.text
         hed = r.headers   

    if t=="PATCH":
         r = requests.patch(url, auth=MyAuth(auth_token), headers=jsheader, params= param,json=json1)
         statcode =r.status_code
         txt =r.text
         hed = r.headers

    if t=="DELETE":
         r = requests.delete(url, auth=MyAuth(auth_token), headers=jsheader, params= param,json=json1)
         statcode =r.status_code
         txt =r.text
         hed = r.headers            
        
    return(statcode,txt,hed)
    

