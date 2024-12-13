## The Task
You are required to build a prototype healthcare API that could be used to provide patients care record to a healthcare application.

You will have approximately 1 week to complete this task and should focus on an MVP but you are free to take this as far as you wish.

## The Solution
Your MVP can use any of the following technologies along with **any frameworks, libraries you feel appropriate**:

- **API** - Python
- **DBs** - MySql / Postgres / SQLServer Express / Filesystem

You should containerise your application using docker / docker-compose. 

## Context
[FHIR](/https://www.hl7.org/fhir/overview.html) is a popular standard within healthcare used by healthcare systems to exchange data and represent details of paitents in a standardised way. Some sample FHIR data has been generated in the data directory using a tool called [synthea](https://www.hl7.org/fhir/overview.html). 

As FHIR is a standard there may be many libraries and UI widgets you can use freely. Google is your friend.

## Evaluation
We take into account 5 areas when evaluating a solution. Each criteria is evaluated from 0 (non-existent) to 5 (excellent) and your final score would be a simple average across all 5 areas. These are:

- Functionality: Is the solution correct? Does it run in a decent amount of time? How well thought and architected is the solution?
- Good Practices: Does the code follow standard practices for the language and framework used? Take into account reusability, names, function length, structure, how crendentials are handled, etc.
- Testing: Test design and coverage.
- Execution environment: Container, Virtual Environment, Dependency Management, Isolation, Ease of transition into a production environment etc.
- Documentation: How to install and run the solution? How to see and use the results? What is the architecture? Any next steps? 

## Submit your solution	
Create a public Github repository and push your solution including any documentation you feel necessary. Commit often - we would rather see a history of trial and error than a single monolithic push. When you're finished, please send us the URL to the repository. 
