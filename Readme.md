BroadGauge
==========

Platform for managing training/workshops by connecting interested trainers and educational institutes interested in conducting trainings for their students. 

This is going to be used for managing Python workshops going to be conducted across Ireland.



Requirements
------------

* PostgreSQL
* Python 2.7
* virtualenv

How to setup
------------

* Clone the repo

        ## CHANGE TO PYTHON IRELAND git clone git@github.com:PythonIreland/broadgauge.git
        cd broadgauge

* Setup virtualenv and install python packages

        virtualenv .
        . bin/activate
        pip install -r requirements.txt

* Start Postgres server

Linux
        Started automatically. No need to worry.

Mac

        To launch start postgresql at login:
        ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents

        Then to load postgresql now:
        launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
        Or, if you don't want/need launchctl, you can just run:
        postgres -D /usr/local/var/postgres


Windows
        http://www.postgresql.org/docs/9.3/static/app-pg-ctl.html

* Create a database

        createdb pythonexpress

* Add schema
        
        psql pythonexpress < broadgauge/schema.sql

* Become a user in your database

        Create user in database:
                sudo -u postgres psql
                create role [name];
                alter role [name] with login;
                \q
        Edit the default_settings.py file changing the 'user' value to your [name]

* Run the app

        python run.py
