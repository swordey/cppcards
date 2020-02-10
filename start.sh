#!/bin/bash
app="cppcards"
docker build -t ${app} .

docker run -d --name ${app} \
   --expose 80 --net nginx-proxy \
   -e VIRTUAL_HOST=cppcards.swordey.duckdns.org \
   -v $PWD:/app ${app}
