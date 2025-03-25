services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
    depends_on:
      - db
    volumes:
      - ./html:/usr/share/nginx/html

  db:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: examplepassword
      MYSQL_DATABASE: exampledb
      MYSQL_USER: exampleuser
      MYSQL_PASSWORD: examplepass
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
    driver: local
