#!/usr/bin/env python
from __future__ import print_function
import pickle
import os
import json
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    """
    """
    output = [
            {
                "full_text": "\uf0e0" if not os.environ.get('I3_full_text') else os.environ.get('I3_full_text'),
                "color": "#ffff00",
                },
            ]
    print(json.dumps(output))
    sys.stdout.flush()



    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().messages().list(userId="me", q="in:INBOX is:unread").execute()
    count = results["resultSizeEstimate"]
    output = [
            {
                "full_text": "\uf0e0" + ((" " + str(count)) if (count > 0) else ""),
                "color": ("#ff0000" if (count > 0) else "#ffffff"),
                }
            ]


    print(json.dumps(output))

if __name__ == '__main__':
    main()
