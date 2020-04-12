
# Setup

```console
docker build -t checkcheck .
```

# Running

PRODUCT_URL and POSTAL_CODE are required

```console
docker run -it --rm --memory 1024mb --shm-size 2g -e PRODUCT_URL='' -e POSTAL_CODE='' checkcheck:latest bash
```


# Testing
```console
docker run -it --rm --memory 1024mb --shm-size 2g -v $PWD:/home/seluser checkcheck:latest bash
```

make sure to to run `/opt/bin/start-selenium-standalone.sh &` before running the pytest
