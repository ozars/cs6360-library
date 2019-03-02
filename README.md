# Omer's Library

- Built with Django using Python 3.
- Designed as integrated micro services.
- There are three microservices coordinating with each other: db, web and adminer.
  - db is, well, the database. I used MariaDB, which is an open-source drop-in replacement fork of MySQL.
  - web is python3 container with custom pip installations. Specifically, it installs django mysql client, crispy forms and django-tables2.
  - adminer is the database manager. Similar to phpMyAdmin.
- Frontend is made with good old Bootstrap & jQuery.
- As a C/C++/Python guy, I decided to try Django for the first time. I really enjoyed it, however due to indirect use of database via ORM, the design became more complicated and I had to spend a lot of time with dealing with minute details, resulting in missing some features. I enjoyed it nevertheless. I definitely liked it much more than NodeJS. However, its ecosystem somehow looked immature to me. Perhaps, I couldn't find the right tools.

- How to run project:
```
   docker-compose up --build
```

- It starts publishing the website on `localhost:8000` and adminer interface on `localhost:8080`.
