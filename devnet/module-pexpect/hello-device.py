import pexpect

ping = pexpect.spawn('ping -c 5 localhost')
# pexpect.spawn and pexpect.run() are not available on Windows
result = ping.expect([pexpect.EOF,pexpect.TIMEOUT])

print(ping.before)
# The parameter 'before' is used to store what came 'before' the EOF or TIMEOUT. In other words, the actual output of
# the ping command, like you would see if you ran the ping at terminal yourself.

