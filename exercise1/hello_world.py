from sulley import (
    s_initialize, s_string, s_delim,
    s_static, s_get, sessions
)

s_initialize('hello_world')

s_string('GET')
s_delim(' ')
s_string('/')
s_delim(' ')
s_static(' HTTP/1.1\r\n')
s_static('Host: 0.0.0.0:5000\r\n')
s_static('\r\n')


# GET / HTTP/1.1
# Host: localhost:5000

sess = sessions.session()
target = sessions.target("localhost", 5000)
sess.add_target(target)
sess.connect(s_get("hello_world"))
sess.fuzz()
