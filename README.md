### Run docker local
```docker 
docker run -p 8000:8000 -d --name scanner congdinh2k/scanner:latest
```

### Create new user
```docker 
docker exec -it scanner python manage.py init_superuser username=<YOUR_USERNAME> password=<YOUR_PASSWORD>
```

### Create schools fake
```docker
docker exec -it scanner python manage.py init_schools <number_of_schools>
```

### Create users fake
```docker
docker exec -it scanner python manage.py init_user <number_of_user>
```

### Stop if rerun
```docker 
docker rm -f scanner
```