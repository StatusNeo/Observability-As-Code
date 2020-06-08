* Install Docker Compose

```
$ apt install -y docker-compose
```

* docker-compose.yml

```yml
version: '3'
services:
  statusneo:
    image: shreyasingh18/statusneo
  datadog:
    links:
    - statusneo 
    image: datadog/agent:latest
    environment:
    - DD_API_KEY
    - DD_HOSTNAME=dockerhost
    - DD_APM_ENABLED=true
    - DD_LOGS_ENABLED=true
    volumes:
    - /var/run/docker.sock:/var/run/docker.sock:ro
    - /proc/:/host/proc/:ro
    - /sys/fs/cgroup:/host/sys/fs/cgroup:ro
```

* Export API Key

```
$ export DD_API_KEY=da3d8cde36bdd455f0be8d9b03d516a9
```

* Run Docker Compose

```
$ docker-compose up
```

* Check Agent Status

```
$ docker-compose exec datadog agent status
$ docker-compose exec datadog agent config
```
