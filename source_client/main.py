import requests
import time

from db.functions import get_latest_record


""" set interval here """
INTERVAL = 3 # seconds
APIURL = 'http://127.0.0.1:5003/update_record'

""" end of configuration """

def send_request():
    reqdata = get_latest_record()
    print(reqdata)
    sendtime = time.ctime()
    try:
        response = requests.post(APIURL, data=reqdata)
        if response.status_code != 200:
            print(response.status_code, response.data)
        else:
            print(f'sent time: {sendtime}')
    except:
        pass


if __name__ == '__main__':
    while True:
        send_request()
        time.sleep(INTERVAL)
