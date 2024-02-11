Slightly modified [original datalens demo docker-compose](https://github.com/datalens-tech/datalens/blob/main/docker-compose.yml) with [canada service](https://github.com/dmi-feo/canada/tree/main) run instead of us.

Run it:
```
YT_HOST=http://host:port ROOT_COLLECTION_NODE_ID=1-1161-12f-93dbdaa4 docker compose up
```

You can run YT via [this docker-compose file](https://github.com/dmi-feo/yt-local-docker-compose/blob/main/docker-compose.yml).

`ROOT_COLLECTION_NODE_ID` - cypress ID of a directory that `canada` will use as the root collection