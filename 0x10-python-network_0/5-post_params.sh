#!/bin/bash
#send a POST request to a URL, and display the body of the response
curl -s -F email=test@gmail.com -F subject="I will always be here for PLD" -X POST "$1"
