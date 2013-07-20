from random import randrange
from twisted.internet import task, reactor


def auto_announce(config):
    message = ' '.join(config.auto_announce_list[randrange(
        len(config.auto_announce_list))])
    self.connection.send_chat(message)

auto_announce_timer = task.LoopingCall(auto_announce(config))
auto_announce_timer.start(240.0)
reactor.run()
