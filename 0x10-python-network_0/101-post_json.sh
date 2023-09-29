#!/bin/bash
# This script passes a JSON filetype to a URL using the POST method and gets the body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"i
