# MongoDB-Python-tutorial

## Running the docker image

```
docker run -d --name mongo_receiver -p 27017:27017  -e MONGO_INITDB_ROOT_USERNAME=<user> -e MONGO_INITDB_ROOT_PASSWORD=<password> mongo:latest 
```

## Installing the Python modules

```
pip install pymongo
```
