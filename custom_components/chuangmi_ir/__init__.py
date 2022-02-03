"""
Chuang Mi IR remote
Copy custom_components/switch/chuangmi_ir.py to your local HASS configuration folder.
We CAN NOT got chuangmi ir remote token by miio discover command. It will return all zero.
INFO:miio.miio:  IP 192.168.1.191: 174 - token: b'00000000000000000000000000000000'
We can get token adb connect to an ROOT Android phone. Install MiJia app. Login your account and control IR remote by using this app
Connect your phone to PC, and run
adb root
adb shell
cd /data/data/com.xiaomi.smarthome/cache/smrc4-cache
grep -nr token .
You will find there are lots of files contains device token. You can copy one of it and format it do human readable json format.
{
    "did": "123456",
    "token": "asdfghjhjkl",
    "longitude": 111111,
    "latitude": 22222,
    "name": "驴脥脤眉碌脛脥貌脛脺脪拢驴脴脝梅",
    "pid": "0",
    "localip": "192.168.1.191",
    "mac": "xxxxxxxxxxx",
    "ssid": "SchumyOpenWrt",
    "bssid": "20:76:93:3D:3B:24",
    "parent_id": "",
    "parent_model": "",
    "extra": {
	    "isSetPincode": 0,
        "fw_version": "1.2.4_38",
        "needVerifyCode": 0,
        "isPasswordEncrypt": 0
    },
    "show_mode": 1,
    "model": "chuangmi.ir.v2",
    "adminFlag": 1,
    "shareFlag": 0,
    "permitLevel": 16,
	"rssi": -51,
    "isOnline": true,
    "desc": "Added 5 remotes "
}
Config HASS
switch:
  - platform: chuangmi_ir
    name: "livingroomirremote"
    host: !secret chuangmi_ip
    token: !secret chuangmi_key
    switches:
      reciever:
        command_on: ''
        command_off: ''
To learn IR command, you can call service. Service Domain is chuangmi, service is learn_command_YOUR_DEVICE_IP.
After call this service, using the real IR remote send one key to Chuangmi IR remote.
You will get a notification in your HASS States page. Contains learnt IR command. Such as Z6VLAAkCAABpAgAAYgYAAKYIAACJEQAAoSMAAKScAABYeQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABFAQEBAQEBAQEhISEhISEhIQEBISEBAQEBISEBASEhISFhNXE1AQ==
Copy the learnt command to command_on or command_off. This is an example
- platform: chuangmi_ir
  host: !secret chuangmi_ip
  name: "livingroomirremote"
  token: !secret chuangmi_key
  switches:
    reciever:
      command_on: ''
      command_off: ''
    wcfan:
      name: 'wcfan'
      command_on: 'Z6VLAAkCAABpAgAAYgYAAKYIAACJEQAAoSMAAKScAABYeQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABFAQEBAQEBAQEhISEhISEhIQEBISEBAQEBISEBASEhISFhNXE1AQ=='
      command_off: 'Z6VHAPEBAACBAgAASQYAAIYIAABqEQAAySMAAECcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABFAQEBAQEBAQEhISEhISEhIQEBASEhAQEBISEhAQEhISFhNQE='
      
"""
