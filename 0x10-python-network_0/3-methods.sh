#!/bin/bash
# displays all HTTP methods the server will accept
curl -sX "OPTIONS" "$1" -i | grep "Allow" | cut -d " " -f2-4
