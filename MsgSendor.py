import itchat
from getWeather import get_weather_byid
from time import sleep


class MessgSendor(object):
    def __init__(self):
        self.last_time = ''

    def log_in(self):
        itchat.auto_login(enableCmdQR=True)

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
        time = we.get('time')
        print(we)
        if time != self.last_time:
            self.last_time = time
        send_str = cname + time + "天气:" + weather + "温度:" + temp+'°C'
        itchat.send(send_str, toUserName=target)


sender = MessgSendor()


def main():
    sender.log_in()
    while True:
        res = sender.get_time('101010200')
        if res:
            sender.start_send(res, 'filehelper')
        sleep(20)


if __name__ == '__main__':
    main()
