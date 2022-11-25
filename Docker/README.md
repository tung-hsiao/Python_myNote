
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
image_name="My_image"
docker build -t "$image_name" .
```

# Run Container 
### run as deamon 
```
container_name="My_container"
image_name="My_image"
docker run -d --name ${container_name} \
    -p 5000:5000 \
    ${image_name} \
    tail -f /dev/null
```

