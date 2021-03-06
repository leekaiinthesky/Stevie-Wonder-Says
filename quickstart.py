#!/usr/bin/python

import httplib2
import os

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
import argparse
from oauth2client import tools

# Path to the client_secret.json file downloaded from the Developer Console
CLIENT_SECRET_FILE = 'client_secret_977858608003-4a8c60lbt40j82rok0samiof5a178uso.apps.googleusercontent.com.json'

if not os.path.isfile(CLIENT_SECRET_FILE):
    with open(CLIENT_SECRET_FILE, 'a') as the_file:
        the_file.write(os.getenv("GMAIL_CLIENT_SECRET"))

# if not os.path.isfile('gmail.storage'):
#     with open('gmail.storage', 'a') as the_file:
#         the_file.write(os.getenv("GMAIL_STORAGE"))

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.modify'

# Location of the credentials storage file
STORAGE = Storage('gmail.storage')

# Start the OAuth flow to retrieve credentials
flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
http = httplib2.Http()

# Try to retrieve credentials from storage or run the flow to generate them
credentials = STORAGE.get()
if credentials is None or credentials.invalid:
  #credentials = run(flow, STORAGE, http=http)

  parser = argparse.ArgumentParser(parents=[tools.argparser])
  flags = parser.parse_args()
  credentials = tools.run_flow(flow, STORAGE, flags)

# Authorize the httplib2.Http object with our credentials
http = credentials.authorize(http)

# Build the Gmail service from discovery
gmail_service = build('gmail', 'v1', http=http)

# # Retrieve a page of threads
# threads = gmail_service.users().threads().list(userId='me').execute()

# # Print ID for each thread
# if threads['threads']:
#   for thread in threads['threads']:
#     print 'Thread ID: %s' % (thread['id'])