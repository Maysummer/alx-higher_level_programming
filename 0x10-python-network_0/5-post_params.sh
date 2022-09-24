#!/bin/bash
#take a URL, send POST request with variables, and display body
curl -sL -d "email=test@gmail.com" -d "I will always be here for PLD" $1
