#!/bin/bash
#print only status code
curl -w '%{http_code}' -so /dev/null $1
