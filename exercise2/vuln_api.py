from sulley import (
    s_initialize, s_string, s_delim,
    s_static, s_get, s_size,
    s_block_start, s_block_end,
    sessions
)

host = 'vulnerableapi.herokuapp.com'
port = 443

s_initialize('vuln_api')
s_string('POST')
s_delim(' ')
s_string('/api/pet')
s_delim(' ')
s_static(' HTTP/1.1\r\n')
s_static('Host: {}\r\n'.format(host))
s_static('\r\n')
s_static('Connection: keep-alive\r\n')
s_static('Content-Type: application/json')
s_static('\r\n')
s_static('Content-Length: ')
s_size('payload', format='ascii')
s_static('\r\n')
if s_block_start('payload'):
    l = [('breed', 'cat'), ('tag', 'tag'), ('name', 'name'), ('id', 'id')]
    s_delim('{\r\n')
    for i in range(len(l)):
        param, value = l[i]
        s_delim('"')
        s_string(value=param)
        s_delim('" : "')
        s_string(value=value)
        s_delim('"')

        # Add , for all but the last param
        if i < len(l) - 1:
            s_delim(',')

        s_static('\r\n')

    s_delim('}')
    s_static('\r\n')
s_block_end()


sess = sessions.session(proto='ssl')
target = sessions.target(host, port)
sess.add_target(target)
sess.connect(s_get("vuln_api"))
sess.fuzz()
