#!/bin/bash
#takes in url, send GET request,send header, display body
curl -sLG -H "X-School-User-ID: 98" $1
