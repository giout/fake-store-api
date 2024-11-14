# Fake store API
REST API that provides sample data that can be used to build e-commerce websites or similar projects.

- [API Documentation](#api-documentation)
- [Tech stack](#tech-stack)
- [Required installations](#required-installations)
- [Project initialization](#project-initialization)
- [Commands](#commands)
- [Environment variables](#environment-variables)

## API Documentation
https://documenter.getpostman.com/view/27562812/2sAY55bJGR

## Tech stack
* [Python](https://www.python.org/) 
* [PostgreSQL](https://www.postgresql.org/)
* [Flask](https://flask.palletsprojects.com/en/stable/)

## Required installations
* [Python](https://www.python.org/) - v3.12.1.
* [PostgreSQL](https://www.postgresql.org/) - v12

## Project initialization
1. Install dependencies by executing the dependencies command.
2. Create a postgres database.
3. Create .env file and set variables.
4. Execute "python src/ddl.py" to create the data structure in your postgres database.
5. Run the server.

## Commands 

### Install dependencies
It is mandatory to install dependencies before executing any other step.
```sh
$ pip install -r requirements.txt
```

### Run server
```sh
$ flask --app src/app run
```

### Run server in debug mode
```sh
$ flask --app src/app run --debug
```

## Environment variables
Environment variables should be added to a .env in the root directory, following the structure of .env.example
<table>
<tr>
<th>Variable</th>
<th>Description</th>
</tr>
<tr>
<td>DB_URI</td>
<td>URI to connect to database</td>
</tr>
<tr>
<td>JWT_SECRET</td>
<td>Secret key to sign jwt</td>
</tr>
<tr>
<td>PORT</td>
<td>Server listening port</td>
</tr>
</table>
