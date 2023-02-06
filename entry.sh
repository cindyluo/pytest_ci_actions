#!/bin/bash
set -eu
help_and_exit() {
	echo "	   <path-to-script> gin ..."
	echo "	   <path-to-script> shell ..."
	echo "	   <path-to-script> worker ..."
	echo "	   <path-to-script> test"
	exit 1
}
if [ "$#" -lt 1 ]; then
	help_and_exit
fi
# Entries
case "$1" in
shell)
	shift 1
	exec /bin/sh "$@"
	;;
test)
    pytest
	;;
*)
	echo "unknown command: $1"
	exit 1
	;;
esac
exit 0
