# API Design
This design is to serve as a prototype. Meaning it is NOT production
ready and shouldn't be used in a production environment.  There are a 
lot of features not implemented and should only serve as a starting point.

## API Structure
The API should function a bit like the following:

```mermaid
flowchart TD;

U[Data Source]-->E[Endpoint]
E-->A{Authorized?}
A-- Yes -->O{Request OK?}
A-- No -->I
A-- No -->R
I[Invalid Key]-->401
R[Rate Limit Exceeded]-->429

O-- Yes -->C{Cached?}
O-- No -->M[Request Malformed]
O-- No -->P[Invalid or Missing Parameter]
O-- No -->S[Server Issue]
M-->400
P-->422
S-->5xx

C-- Yes -->F{Within Freshness Lifetime?}
C-- No -->Store[Store in Cache]

F-- Yes -->2xx
F-- No -->V{Revalidated?}
V-- Yes --> 2xx
V-- No --> Store


Store-->2xx
```

## Infrastructure
A basic understanding of how this could work is as follows:
```mermaid
flowchart TD
    L[Load Balancer]
    L-->S
    subgraph Microservice
        S[API Service]-->D[Database]
        S-->R[Redis]
        R-->C[Celery Workers]
    end
```

If hosting on AWS, the implementation could look something like this:
```mermaid
flowchart TD
    subgraph Cloud Account
        L[Load Balancer]
        L-->S
        ECR["ECR or Docker Hub or Equivalent"]-->S
        subgraph Public Network
            S[Service running on EC2 or ECS]
        end
        subgraph Private network
            S-->D[Database]
            S-->R[Redis]
            R-->C[Celery Workers]
        end
        C-->S3["S3 Bucket"]
    end
```