#!/bin/bash
#displays the body of the response with a header variable
curl -s -H "X-School-User-Id: 98" "$1"
