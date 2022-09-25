#!/bin/bash
#print only status code
curl -w '%{http_code}' -Lso /dev/null $1
