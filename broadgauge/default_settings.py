import os

secret_key = "MaXvbXjgqTPRxJrnpZKl"

site_title = "Python Express"

# Notes:
# 1) The application will listen on 0.0.0.0 (i.e. all local IP addresses)
# 2) Port number is 8080 by default and cannot be changed here
# 3) This base url will be passed as part of the redirect URIs to the oauth
#    providers. Make sure this URI is registered correctly. Google allows several,
#    but GitHub only allows one.
base_url = "http://localhost:8080/"

github_client_id = '81679e63a45aee157d62'
github_client_secret = '343c40e95099c9b27b01a49df8daf2f1cedd8f61'

google_client_id = '483978112071-ps7jdal5tdbtjo0utapi5f3lud75spru.apps.googleusercontent.com'
google_client_secret = 'Ld4qdhXnQO-Qzc54tcf51LA6'

db_parameters = dict(dbn='postgres', db='pythonexpress', user='gerry', pw='myname1')

# MAIL SETTINGS

# smtp_server = "smtp.googlemail.com"
# smtp_port = 25
# smtp_username = "you@gmail.com"
# smtp_password = "secret"
# smtp_starttls = True
# from_address = "noreply@yourwebsite.com"

## to enable email on internal errors, uncomment the following line.
# bug_master = "you@example.com"
