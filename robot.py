from werobot import WeRoBot

robot = WeRoBot(token='test01')


@robot.handler
def hello(message):
    return 'Hello World!'