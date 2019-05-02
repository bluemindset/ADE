#!/bin/bash


 kill -9  $(lsof -t -i:8000) ;python -c 'import server; server.serve()'
