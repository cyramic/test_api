# Assumptions

To streamline development for the task and not bug you with defining
every vagueness in the task, here are a list of assumptions i've 
made for the task:

## There is only one endpoint to this application. It stands alone.
It is assumed that data will be sent to the API via automated means.
No manual uploading or authentication or dashboards will be needed
at this point and would be handled by other services if needed.

There may also need to be other endpoints required:
* Heartbeat - So any monitoring system could determine if the API 
is functioning correctly

## The Healthcare App Operates Using a Database
There are many ways to feed data into an application including 
various ETL pipelines, etc.  I'm assuming that the data merely
needs storing into a database and something could pick up 
from there.

Other types of APIs I've made of this type could just feed the file
into storage (e.g. S3, blob storage on Azure, etc) and then some ETL
program would pick it up and combine with other datasets, etc.

Database storage makes sense for a simple demonstration.

## The System will need to be redundant and scalable
This strikes me as a service that could easily take a constant stream
of information. As such scalability would be key to ensure it could handle
variable loads on it.

## FHIR is the only data structure that will be received.
While the task mentioned this data structure, it didn't
state that it would exclusively receive this structure.  As such
I will assume this will be the case, but it could potentially
be expanded to other data structures or types if needed.

## The things being sent to the API are potentially the same
This API could have the potential to receive the exact same data
as was sent during a previous session. As such, there is the
potential for duplicate records present, and it should be checked
for before storing unnecessarily.

## That pieces of the data should be individually rejected if they don't match a schema
Generally, the idea of least permissability is the right thing to do. I took a middle
ground track here in allowing data that matched the schema, but rejecting anything
that didn't. A more strict way to do this could be to reject the entire file if there
were a single issue found, but I assumed that individual pieces could be handled that 
fit the schema, and anything that didn't match could be independently handled.