#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -sLH "Origin: You got me!" -d "user_id=98" -X PUT "0.0.0.0:5000/catch_me"
