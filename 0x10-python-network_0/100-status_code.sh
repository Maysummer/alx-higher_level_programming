#!/bin/bash
#print only status code
curl -w '%{http_code}' $1 -so /dev/null
