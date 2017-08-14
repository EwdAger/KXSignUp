# -*- coding: utf-8 -*-
from werobot import WeRoBot

robot = WeRoBot(token='test01')

robot.config["APP_ID"] = "wx898a5c4d88250e4c"
robot.config["APP_SECRET"] = "d4624c36b6795d1d99dcf0547af5443d"

client = robot.client

client.create_menu({
    "button":[{
         "type": "view",
         "name": u"加入科协",
          "url":"http://119.29.25.247/index/"
    }]
})

@robot.handler
def hello(message):
    return 'Hello World!'