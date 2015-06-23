# BroadGauge

A platform for managing training sessions and workshops to connect trainers and educational institutes interested in conducting training for their students. 

This project is a fork of [Anand Chitipothu](https://github.com/anandology)'s
 [broadgauge](https://github.com/anandology/broadgauge) project.

## Requirements

See [`requirements.txt`](https://github.com/PythonIreland/broadgauge/blob/master/requirements.txt) for the full set of 
requirements.

* Python 2.7
* PostgreSQL
* virtualenv

# How to setup

The short version:

* Install dependencies system-wide
* Clone the GitHub repo
* Create the Python virtualenv
* Install project-specific dependencies in the virtualenv
* Configure the database
** Create an account for use by the BroadGauge server
** Import the database schema as that user
* Start the BroadGauge server

## Install the dependencies

### Linux

There are two stages to installing the dependencies; some you'll install system-wide and some you'll install in the 
project's Python virtual environment. The former set of dependencies guarantee the latter set can be installed
successfully.

Using your package manager, install the following dependencies system-wide:

    python
    python-dev
    postgresql
    postgresql-server-dev-9.3

For example, on Ubuntu or any Debian-derivative:

    sudo apt-get install python python-dev postgresql postgresql-server-dev-9.3

## Clone the broadgauge GitHub repository

Let's say you're going to clone this GitHub repository into `/home/me/src` and run the Broadgauge server as user `me`.

    cd /home/me/src
    git clone git://github.com/PythonIreland/broadgauge.git

## Setup the virtualenv in the project directory
    
    cd broadgauge
    virtualenv -p $(which python2) .
    . bin/activate
    
## Install the project-specific dependencies in the virtualenv

    pip install -r requirements.txt

If `pip install` fails, it'll be because you're missing a system-wide dependency.

## Start the Postgres database server

### Linux

The database is started automatically at installation time, running under the `postgres` user account.

### Mac

To start postgresql at login:

    ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents

Then to load postgresql now:

    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist

Or, if you don't want/need launchctl, you can just run:

    postgres -D /usr/local/var/postgres

### Windows

See http://www.postgresql.org/docs/9.3/static/app-pg-ctl.html

## Configure the database

### Create a database

The database login credentials used by Broadgauge can be found in `broadgauge/default_settings.py`. Make a note of these.

Switch to the `postgres` user account:

    sudo -i -u postgres

Create the database:

    createdb pythonexpress

### Create the database user account

    createuser -P gerry

The database user's default password is `myname1`. You'll be prompted to provide a password as you create the database user.

### Add schema

Switch to the `postgres` user account:

    sudo -i -u postgres

Check that the `postgres` user has at least read-only access to the schema file in the home folder of user `me`:

    cat /home/me/src/broadgauge/broadgauge/schema.sql
    
If you see the contents of the file, you're good to go. Otherwise copy the file to /tmp.

Import the schema as database user `gerry`:

    psql -d pythonexpress -U gerry < /home/me/src/broadgauge/schema.sql

## Start the BroadGauge server

    python run.py

Point your browser at http://localhost:8100/

You're up and running! Keep an eye on the terminal in which you started the Broadgauge server to check for errors.
