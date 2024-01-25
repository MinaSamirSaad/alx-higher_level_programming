#!/bin/bash
# Script that sends a POST request to a URL and displays the body of the response
curl -sL "$1" -X POST -H "email=test@gmail.com&subject=I will always be here for PLD"
