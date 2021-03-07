# PosGraduacao

## Features

- **FastAPI** with Python 3.8
- **React 16** with Typescript, Redux, and react-router
- Postgres
- SqlAlchemy with Alembic for migrations
- Pytest for backend tests
- Cypress for frontend tests
- Perttier/Eslint (with Airbnb style guide)
- Docker compose for easier development
- Nginx as a reverse proxy to allow backend and frontend on the same port

## Development

The only dependencies for this project should be docker and docker-compose.

### Quick Start

Starting the project with hot-reloading enabled
(the first time it will take a while):

```bash
docker-compose up -d
```

To run the alembic migrations (for the users table):

```bash
docker-compose run --rm backend alembic upgrade head
```

And navigate to http://localhost:8000

_Note: If you see an Nginx error at first with a `502: Bad Gateway` page, you may have to wait for webpack to build the development server (the nginx container builds much more quickly)._

Auto-generated docs will be at
http://localhost:8000/api/docs

### Rebuilding containers:

```
docker-compose build
```

### Restarting containers:

```
docker-compose restart
```

### Bringing containers down:

```
docker-compose down
```

### Frontend Development

I decided to decouple the frontend from the docker-compose containers so for frontend development you need to 

```
cd frontend
yarn
yarn start
```

This should redirect you to http://localhost:3000

### Frontend E2E Tests

The frontend tests are done mainly with cypress, for this you should probably use a separate database, you can do that using the alternative docker-compose file

```
docker-compose -f docker-compose-e2e.yml up
cd frontend
yarn run cypress open
```

## Migrations

Migrations are run using alembic. To run all migrations:

```
docker-compose run --rm backend alembic upgrade head
```

To create a new migration:

```
alembic revision -m "create users table"
```

And fill in `upgrade` and `downgrade` methods. For more information see
[Alembic's official documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script).

## Testing

There is a helper script for both frontend and backend tests:

```
./buid.sh
```

### Backend Tests

```
docker-compose run backend pytest
```

any arguments to pytest can also be passed after this command

## Logging

```
docker-compose logs
```

Or for a specific service:

```
docker-compose logs -f name_of_service # backend|db
```

## API Sistemas UFRN


```
mv api_fake_keys.json api_keys.json
```

And fill the empty spaces with your own keys, optained in <https://api.ufrn.br/>

## Database Layout

![The Database Layout can be viewed here](https://github.com/luccasmmg/NewPosgrad/blob/master/db.png?raw=true)

## CRUD Backend Todo

* [x] Post Graduation
* [x] User
* [x] Course
* [x] Attendance
* [x] Official Document
* [x] Researcher
* [x] Covenant
* [x] Participation
* [x] Phone
* [x] News
* [x] Event
* [x] Scheduled Report
* [x] Student Advisor
* [x] Staff

## CRUD Frontend Todo

* [x] Post Graduation
* [x] User
* [x] Course
* [x] Researcher
* [x] Attendance
* [x] Student Advisor
* [x] Participation
* [ ] Phone
* [ ] Event
* [ ] Scheduled Report
* [ ] Official Document
* [ ] Covenant
* [ ] News
* [ ] Staff

## Project Layout

```
backend
└── app
    ├── alembic
    │   └── versions        # where migrations are located
    ├── api
    │   └── api_v1
    │       └── endpoints
    ├── core                # config
    │   └── utils           # mainly external api access
    ├── db                  # db models
    │   └── crud            # crud operations
    ├── schemas             # schemas
    ├── tests               # pytest
    └── main.py             # entrypoint to backend

frontend
└── public
└── src
    ├── components
    │   └── Home.tsx
    ├── config
    │   └── index.tsx   # constants
    ├── __tests__
    │   └── test_home.tsx
    ├── index.tsx   # entrypoint
    └── App.tsx     # handles routing
```
