#!/bin/bash
# This script sends a request to a URL and displays only the status code of its response
curl -s -o /dev/null -w "%{http_code}" "$1"
