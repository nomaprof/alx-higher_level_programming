#!/bin/bash
# This script sends a request to a server and gets the respons 'You got me!'
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
