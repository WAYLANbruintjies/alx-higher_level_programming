#/usr/bin/bash
# A Bash script that makes a request to 0.0.0.0:5000/catch_me.
# Server to respond with a message containing You got me!, in the body of the response.

curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:You got me!"
