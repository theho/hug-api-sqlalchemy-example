hug-api-sqlalchemy-example
==========================

A little sandbox project to explore possibility of using hug/falcon for future API development instead of 
Djanog Rest Framework

## Features implemented so far ...
* sqlalchemy extension/middleware (need to tidy up the way it initialise)
* user login/signup with JWT
* alembic integration with sqlalchemy and models used in API
* Unit test base class to create test database and db schema per class

## Installation
If you really want to try this...good luck..

#### Prerequisite
PostgreSQL installed, where

* user: postgres
* password: postgres

and rights to create database

#### install from repo
```
git clone git@github.com:jimmyho/hug-api-sqlalchemy-example.git
pip install -r requirements.txt
gunicorn --reload api.app:__hug_wsgi__

# launch browser to http://127.0.0.1:8000

```


## My Take on Hug/Falcon (vs Django Rest Framework and Flask)
The experience have been pleasant, Hug is great as a micro-framework.

Most of the pain was mainly due to the missing extension/features which DRF and Flask eco-system have.  
But that's the whole point of a micro-framework!


#### What I like
* Python 3 annotation to validate inputs
* CLI support
* simple test client
* I know what's going on underneath

#### What I don't like
* Lacks extensions for common stuff, eg CORS, db, auth.
* Hard to find documentation.  I had to dig into hug's source code


#### Will I use it for serious projects?
* YES!  But only/mostly if...
   - I am using non-relational backends, eg, firebase, cassandra, etc.
   - authentication and authorisation is simple/custom
   - rapid development of micro-services
   - potential pypy'ing
   