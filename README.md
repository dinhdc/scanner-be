## Features List

### **Manage schools**

- **/api/v1/schools/**:
    - GET: get list schools where user is added to
    - POST: create new school
- **/api/v1/schools/staffs/**:
    - GET: get list staff of school

### **Manage Users**

- **/api/v1/staffs/list/**:
    - GET: get list users in system
- **/api/v1/staffs/add-to-school/**:
    - POST: add one or more users to school

### **Manage Events**

- **/api/v1/school/events/**:
    - GET: get events of school
    - POST: create new event of school

- **/api/v1/school/events/participants/**:
    - GET: get all participants who are invited to event
    - POST: invite participants to event

- **/api/v1/school/events/participants/{code}/**:
    - GET: get participant by code
    - PATCH: update participant checked-in status

## How to run locally

### Remove old container if exists

```commandline
docker rm -f scanner
```

### Run docker image

```docker 
docker run -p 8000:8000 -d --name scanner congdinh2k/scanner:latest
```

### Create new user

```docker 
docker exec -it scanner python manage.py init_superuser <YOUR_USERNAME> <YOUR_PASSWORD>
```

### Create schools fake

```docker
docker exec -it scanner python manage.py init_schools <number_of_schools>
```

### Create users fake

```docker
docker exec -it scanner python manage.py init_user <number_of_user>
```
