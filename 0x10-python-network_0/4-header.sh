#!/bin/bash
# send a GET request to a URL, and displays the result
curl -s -H "X-School-User-Id: 98" -X GET "$1"
