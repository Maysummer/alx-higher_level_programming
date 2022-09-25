#!/bin/bash
#print only status code
curl -sw '%{http_code}\n' $1
