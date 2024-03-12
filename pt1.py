import requests
print("Now login into appleid.apple.com and find value of caw from cookies")
caw=input("Enter value of caw from cookies of browser: ")
burp1_url = "https://familyws.icloud.apple.com:443/api/family-members"
burp1_cookies = {"caw": str(caw)}
burp1_headers = {"User-Agent": ""}
ds=requests.get(burp1_url, headers=burp1_headers, cookies=burp1_cookies)
aa=ds.text
dsid=aa[16:27]
if("currentDsid" in aa):
    print("Found your id")
    print("Value of your dsis is : " + str(dsid))
else:
    print("Do this step again")
print("Note down your dsid, this step is only needed once you can skip this once you got your dsis ")

