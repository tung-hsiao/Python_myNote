
# Docker command
```
docker ps
docker ps -a

docker-compose build
docker-compose up -d
docker-compose down

docker exec -it [contain ID] bash
exit
```

# How to build image
```
## build docker image
image_name="itri-go/mini-flow-control:21.07"
docker build -t "$image_name" .
```

# Run Container 
### run as deamon 
```
container_name="flow-control-01"
image_name="itri-go/mini-flow-control:21.07"
docker run -d --name ${container_name} \
    -p 5001:5000 \
    ${image_name} \
    tail -f /dev/null
```

