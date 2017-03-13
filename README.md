# job-spider
A spider with links extraction for Frontera

## Local Setup w/ Docker

Install Docker Toolbox and run Docker Quickstart Terminal.

Ensure local `default` docker machine is selected:

```bash
eval $(docker-machine env default)
```

Build & Run:

```bash
docker build -t jobspider . && docker run --name jobspider -dit jobspider
```

### Start DB Worker

```bash
# SSH into running container
docker exec -it jobspider /bin/bash
# in the container bash...
cd /home/spider && \
python -m frontera.worker.db --config frontier.workersettings
```

### Start the spiders

```bash
# Open new tab in Terminal
eval $(docker-machine env default)
# SSH into running container
docker exec -it jobspider /bin/bash
# in the container bash...
cd /home/spider && \
scrapy crawl general -L INFO -s FRONTERA_SETTINGS=frontier.spider_settings -s SEEDS_SOURCE=seeds_es_smp.txt -s SPIDER_PARTITION_ID=0
# Open new tab in Terminal
eval $(docker-machine env default)
# SSH into running container
docker exec -it jobspider /bin/bash
# in the container bash...
cd /home/spider && \
scrapy crawl general -L INFO -s FRONTERA_SETTINGS=frontier.spider_settings -s SPIDER_PARTITION_ID=1
```

