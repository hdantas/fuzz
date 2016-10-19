from sulley import (
    s_initialize, s_string, s_delim,
    s_static, s_get, sessions
)

host = 'localhost'
port = 1337

s_initialize('hello_world')

s_string('GET')
s_delim(' ')
s_string('/')
s_delim(' ')
s_static('HTTP/1.1\r\n')
s_static('Host: {}:{}\r\n'.format(host, port))
s_static('\r\n')


# GET / HTTP/1.1
# Host: localhost:1337

sess = sessions.session()
target = sessions.target(host, port)
sess.add_target(target)
sess.connect(s_get("hello_world"))
sess.fuzz()
