#!/usr/bin/env python3

import requests
from time import sleep
from celery import Celery
from datetime import datetime


broker = Celery('slacker', broker='pyamqp://guest@localhost//')
api_path = "http://127.0.0.1:5000/api/v1/"


class Slacker():
    def __init__(self, threshold=600, interim=60):
        self.threshold = threshold
        self.interim = interim
        self.api_url = api_path + 'heartbeat/1'
        #self.webhook_url = 'https://hooks.slack.com/services/' + slack_id
        self.reset_timer()
        self.loop = True
        self.main()

    def main(self):
        self.calculate_seconds_elapsed()
        while self.loop:
            if (self.seconds_elapsed > self.threshold):
                msg = "timer done. Seconds elapsed = {}".format(
                    self.seconds_elapsed)
                if self.notify_slack(msg):
                    self.reset_timer()
            else:
                sleep(self.interim)

    def reset_timer(self):
        self.notify_slack("timer restarted")
        self.timestamp = datetime.now()

    def calculate_seconds_elapsed(self):
        tdelta = self.timestamp - self.last_checked_in()
        self.seconds_elapsed = tdelta.total_seconds()

    def last_checked_in(self):
        response = requests.get(self.api_url)
        ts_str = response.json()[0]['timestamp']
        return datetime.strptime(ts_str, '%a, %d %b %Y %H:%M:%S -0000')

    def notify_slack(self, text):
        slack_data = {
            "text": text
        }
        #return requests.post(self.webhook_url, json=slack_data)
        return False


@broker.task
def task(threshold=600, interim=60):
    Slacker(threshold, interim)

if __name__ == "__main__":
    task()

