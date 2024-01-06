#!/bin/bash
#displays the body of the response with a header variable X-School-User-Id must be sent with the value 98.
curl -sH "X-School-User-Id: 98" "$1"
