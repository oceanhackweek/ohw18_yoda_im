# ohw18_yoda_im

![logo](logo.png)

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
- `/sites`
- `/regions`

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

## Example URLS
<http://localhost:4567/products>
<http://localhost:4567/products?sal>
<http://localhost:4567/deployments/find/upward_earth_seawater_velocity>

