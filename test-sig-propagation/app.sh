#!/bin/bash
function finalization() {
    echo "finalizing..."; sleep 1; echo "done!"
    exit 0
}
trap finalization SIGTERM
pstree -Gp
while true; do echo "hello world!"; sleep 1; done
