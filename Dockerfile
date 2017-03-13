FROM python:2.7-alpine

MAINTAINER Dan Sandland <dansandland@gmail.com>

	# build dependencies
RUN apk --no-cache --virtual=build_dependencies add \
        gcc \
        g++ \
        libffi \
        libffi-dev \
        libxml2-dev \
        libxslt \
        libxslt-dev \
        musl-dev \
        openssl-dev \
        python-dev \
        py-imaging \
        py-pip \

    # ZeroMQ, postgres and others
	&& apk --no-cache add \
		zeromq \
		postgresql \
		postgresql-dev \
        git \
        bash \
        bash-doc \
        bash-completion \

	# pip
    && pip install \
    	Scrapy \
    	frontera[distributed,zeromq,sql] \
    	colorlog \
    	psycopg2 \

    # clean up
    && rm -rf ~/.cache/pip \
    && apk del build_dependencies

# Define working directory.
WORKDIR /home/spider

COPY spider/. /home/spider

CMD ["python", "-m", "frontera.contrib.messagebus.zeromq.broker"]
# CMD ["python", "-m", "frontera.contrib.messagebus.zeromq.broker", "-L", "DEBUG"]