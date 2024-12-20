# Next Steps
Here are some next steps that could improve this initial prototype:

## Securing API keys
The key as it currently stands is set using environment variables, but this
isn't the best way to store API keys. Really, this should be kept in something
like a parameter store or a database where the keys could be more easily 
secured and rotated by different means. I left it as an environment
variable for ease of configuration on the prototype itself.

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

## Linking data together
I didn't spend much time setting up foreign relationships between the tables and the 
complexity that would exist there. Not only that, but I'm sure there are more complexitites
as the data is parsed. For instance, a patient could have a single id
across different data sets, but may have different recorded names. This may need
to be handled separately in a "patient name" database table or similar.  As such, there
is a lot about the nuance of the FHIR data sets that I potentially don't know that would
need to be considered that is not noted in the prototype as it stands. Not only that,
but there are other issues that would need to be considered:

* How to handle updates to the data (how to determine most recent record)
* How to handle matching between different data sets. Could the same person have different
IDs?
* Can the same person have different recorded names in different records being sent?
* How much validation do we need to do before saving the data?  For instance, if a patient has 
new information come in, but their DOB is different, is this an update or a typo? At what point do
we reject, and when do we bring into the system?

There are many more considerations that I'd want to investigate further that I'm sure would
come with greater familiarity with FHIR datasets.