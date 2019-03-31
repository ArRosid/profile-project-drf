# profile-project-drf
Django Rest Framework Profile Project Source Code

In this project, we have some functional API.

We can get, add, edit, or delete users
<img src="pictures/pict1.png">

We can login to the application, without login to the application, we can't see or create a feed post
<img src="pictures/pict2.png">

We can get, add, edit, or delete feed post
<img src="pictures/pict3.png">

I write Dockerfile & docker compose in this project, so you can run this project on your own without doing complex things. This is the step by step that you need to do to get this application running on your computer using docker.

<ol>
  <li>Make sure you have docker & docker-compose installed on your computer</li>
  <li>Run <b>docker-compose up --build -d</b></li>
  <li>Run <b>docker ps</b> to see that the container is running</li>
  <li>Run <b>docker-compose run django_api python manage.py createsuperuser</b> to create user on django</li>
  <li>Open your browser and navigate to http://localhost/api/login/, use the username & password that we have created before</li>
  <li>Use the token that we get after logged in, navigate to http://localhost:8000/api/profile/ to see the list of user</li>
  <li>Navigate to http://localhost:8000/api/feed/ to see, add, edit, or delete post</li>
</ol>
