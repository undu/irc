from irc import IRCBot


class GreeterBot(IRCBot):
    def greet(self, nick, message, channel):
        return 'Hi, %s' % nick

    def command_patterns(self):
        return (
            self.ping('^hello', self.greet),
        )


host = 'irc.freenode.net'
port = 6667
nick = 'greeterbot'

greeter = GreeterBot(host, port, nick)
greeter.run(['#botwars'])
