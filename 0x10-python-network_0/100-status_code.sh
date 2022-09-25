#!/bin/bash
#print only status code
curl -sw '%{http_code}' $1 -o /dev/null
