#!/bin/bash

start() {
  python server/server_run.py > /dev/null 2>&1 &
}

stop() {
  pkill -f server/server_run.py
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart)
    stop
    start
    ;;
  *)
    echo "Usage: $0 {start|stop|restart}"
esac

exit 0