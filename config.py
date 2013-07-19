# -*- coding: utf-8 -*- 

# Global server name
server_name = 'Herocube'

# Max number of players on the server at once
max_players = 50

# Seed for the server
seed = 11223344

# Time speed modifier, 1.0 is default
time_modifier = 10.0

# List of scripts to run on the server on startup.
# Consider turning on 'pvp', i.e. player versus player
scripts = ['commands', 'welcome', 'ban', 'pvp', 'irc', 'announce']

# Passwords used for rights management. Keys are passwords, and values are
# a list of user types under that password. Right now, only 'admin' is defined,
# but scripts can restrict their usage depending on the user type 
passwords = {
    'PASSWORDREPLACEME' : ['admin']
}

# Used by the welcome.py script. Sends a small welcome message to users,
# replacing %(server_name)s with the server name defined in this file.
welcome = ["Welcome to %(server_name)s!",
           "(server powered by cuwo)"]

# IRC script variables (enable by adding 'irc' to script list)
irc_nickname = 'hcbotz'
irc_server = 'irc.esper.net'
irc_port = 6667
irc_channel = '#herocubechat'
irc_password = 'IRCCHANNELPASS'
irc_commandprefix = '.'
irc_chatprefix = '#'
irc_nickserv_password = 'NICKSERVPASS'

# Randomly announce these messages
auto_announce_list = ["Don't hack - you will be banned!",
    "Hackers will be banned",
    "We do not tolerate hackers",
    "If you cheat, you will be banned"]
    
# Levelcap
max_level = 300
