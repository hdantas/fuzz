from sulley import (
    s_initialize, s_string, s_delim,
    s_static, s_get, s_size,
    s_block_start, s_block_end,
    sessions
)

# POST /api/pet HTTP/1.1
# Host: vulnerableapi.herokuapp.com
# Accept: */*
# Content-Type: application/json
# x-access-token: supersecrettoken
# Content-Length: 54
#
# {"id":1,"name":"Whiskers","breed":"Cat","tag":"White"}
