#!/bin/bash
# take URL, send request, display size of response's body
curl -sI $1 | grep 'Content-Length' | cut -d " " -f 2
