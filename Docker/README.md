# Docker compose

### Command
```
docker-compose version
docker-compose build
docker-compose up
docker-compose up -d
docker-compose down
```

### GPU
```
# Update Docker Compose to v1.28.0+ 
# v1.28.0+ allows to define GPU reservations using the device structure defined in the Compose Specification
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```
### Example
```
version: '3'
services:
    my-module:
        image:
        deploy:
            resources:
                reservations:
                    devices:
                        - driver: nvidia
                          count: 1
                          capabilities: [gpu]
```


# Docker command
```
docker ps
docker ps -a

docker-compose build
docker-compose up -d
docker-compose down

docker exec -it [container ID] bash
exit

docker logs [container ID]

docker kill [my_container]  # 先kill
docker rm [my_container]    # 再rm
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

