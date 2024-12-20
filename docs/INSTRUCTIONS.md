# Instructions
How to run

## Prerequisites
You'll need the following isntalled:
* Docker

If you wish to test outside of docker, this has been developed using:
* FastAPI
* Celery
* Redis
* Poetry (for python development and environment management)

Run the following commands:
1. Copy the `.env.sample` file to `.env` and set your own values if needed
2`docker compose --env-file .env build` to build the docker images
3`docker compose --env-file .env up` to bring up the docker images
4`docker compose --env-file .env down` to bring down the docker images when done

## Sending data to the API
You can test the API endpoint by running the following command (once the 
docker images are running)

```
curl -X POST http://127.0.0.1:8000/upload -F "file=@./data/file_to_test.json" -H "x-api-key:test"
```

## Other Considerations
### FHIR
I've not used FHIR data structures before, and so many of the files fail the validation
check (though not all). Much of my time was spent trying to familiarise myself with this
data structure and so only a few models are implemented (Patient, Observation)
### Database Migrations
Designing this, I came from Django development and accidentally left migrations until
the end. As such, this isn't implemented in the current code base and the correct tables
aren't created using the code itself. This could be done with `alembic` or some other methods,
but that was left for later as this was only supposed to be a prototype.  As such, the database
tables will need to be created manually for now.
More info [here](./NEXT_STEPS.md#database-migrations)