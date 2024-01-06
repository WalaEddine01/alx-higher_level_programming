#!/bin/bash
# displays all HTTP methods the server will accept.
curl -sI 0.0.0.0:5000/route_4 | grep Allow | cut -d ":" -f2 | sed "s. .."
