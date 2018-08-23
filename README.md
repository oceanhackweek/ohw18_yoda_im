# ohw18_yoda_im
Your ocean data access interface `http://module/methods/<Help you I can>`

## Development setup for command line use

```
conda env create -f environment.yml
source activate yoda_im
```

## Current Endpoints
- `/products`
- `/instruments`
- `/nodes`

## References

- <https://github.com/cormorack/yodapy>
- <http://flask.pocoo.org>

## Docker

To run the server

```
docker-compose -f docker_dev/docker-compose.yml up
```

To tear down server

```
docker-compose -f docker_dev/docker-compose.yml down
```
