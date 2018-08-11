import itchat
from getWeather import get_weather_byid
from time import sleep
from base_config import *

class MessgSendor(object):
    def __init__(self):
        self.last_time = ''
        self.weather = ''
        self.temp = ''

    def log_in(self):
        if version == 'release':
            itchat.auto_login(enableCmdQR=True)
        else:
            itchat.auto_login()

    def get_time(self, id):
        data = get_weather_byid(id)
        d_time = data.get('time', '')
        if d_time != self.last_time:
            self.last_time = d_time
            return data
        else:
            return False

    def start_send(self, data, target):
        we = data
        cname = we.get('cityname')
        temp = we.get('temp')
        weather = we.get('weather')
        print(we)
        if temp!=self.temp or weather!=self.weather:
            self.temp = temp
            self.weather = weather
            send_str = cname+"天气变化:"+weather +'=>'+ temp+'°C'
            itchat.send(send_str, toUserName=target)


sender = MessgSendor()


def main():
    sender.log_in()
    while True:
        res = sender.get_time('101010200')
        if res:
            fr = itchat.search_friends(remarkName='2gg')
            tar = fr[0]['UserName']
            sender.start_send(res, tar)
        sleep(20)


if __name__ == '__main__':
    main()
