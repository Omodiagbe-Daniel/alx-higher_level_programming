#!/bin/bash
# display status code
curl -s -o /dev/null "$1" -w "%{http_code}"
