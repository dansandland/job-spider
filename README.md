# jobs-spider
A spider with links extraction for Frontera

## Local Setup w/ Docker

Install Docker Toolbox and run Docker Quickstart Terminal.

Ensure default is selected:

```bash
eval $(docker-machine env default)
```

Build & Run:

```bash
cd docker
docker build -t jobspider . && docker run --name jobspider -dit jobspider
```

SSH into running container:

```bash
docker exec -it jobspider /bin/bash
```

Start a spider

```bash

```
