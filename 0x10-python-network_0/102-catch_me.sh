#!/bin/bash
# Displays the body of the response of a curl POST request
curl -s -X PUT -d "user_id=98" -H "User-Agent: You got me!" -L 0.0.0.0:5000/catch_me
