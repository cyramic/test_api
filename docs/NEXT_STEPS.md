# Next Steps
Here are some next steps that could improve this initial prototype:

## Docker files to move to multi-stage
The docker files could use multiple stages to minimise file size and therefore
reduce cost and improve the speed of updating the services.

## Github actions to auto-deploy images to a repository
Once a release happens, the images could be built and sent to a docker
image repository which could then move to staging systems, production, 
and could be used for further testing.  These CI/CD pipelines I felt 
were outside the scope of the task so didn't persue. I also left actions
for testing out as this would use my limited time on actions for the free plan.

## Move Celery to separate container
Celery is currently running (as a POC) on the same container as the API. 
THere's no real benefit to this. It should run on a separate container so
that the file can be processed in a protected environment that couldn't
interfere with the API itself (resources, security, etc).

I didn't have time to implement it in this prototype, so left it as a 
simpler infrastructure for demonstration purposes only.  It is relatively
striaght forward to do by adding it to the docker compose file, but was 
left as a separate task and I felt was outside a "prototype"

## Put files in more sensible structure or libraries
Items like the database connection could be handled in a centralised
way to ensure that it could be maintained in a single instance as opposed to
across several API instances.  This would make this so that it could be 
more centrally maintained

## Increased testing
I have very limited unit testing due to time constraints. Ideally there should 
be more thorough tests and other types of tests here (e.g. integration for how different
functions work together) and end-to-end tests (for how components work from end to end)

## Database Migrations
I realised while making this that I took for granted django's database migration
system and didn't think about it in this instance until the end of my available time.
As such, this system does NOT do this correctly and I didn't have time to remind myself
how to do this adequately.

## Deployment 
Work would need to be done to ensure there is the appropriate development, staging,
and production environments so changes can be quickly tested and rolled out in a
continous manner. This could easily be done in something like Heroku, but could
also be done using IaC to set up an environment on other cloud providers.

