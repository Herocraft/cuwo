from random import randrange
from twisted.internet import task, reactor


def autoAnnounce(script, config):
    message = ' '.join(config.autoAnnounceList[randrange(
        len(config.autoAnnounceList))])
    script.connection.send_chat(message)

autoAnnounceTimer = task.LoopingCall(autoAnnounce)
autoAnnounceTimer.start(240.0)
reactor.run()