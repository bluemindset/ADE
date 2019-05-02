#!/bin/bash

python -c 'import time;import datetime;import insert; ts = time.time(); timestamp = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S"); insert.insert(10,"c",11,timestamp)'
