#!/bin/bash
eval "$(boot2docker shellinit)"
docker exec -i f52d279a7e53 /usr/local/bin/python $@