# python-otrs-restapi
Use OTRS Rest API in Python 3

OTRS is a service management suite. The suite contains an agent portal, admin dashboard and customer portal. In the agent portal, teams process tickets and requests from customers. There are various ways in which this information, as well as customer and related data can be viewed. 

Over last few years I have been using OTRS heavily. Recently i used Python to interact with OTRS web services. This guide will let you utilise OTRS web services as a provider. This code is writtenin Python 3. 

### Set up otrsconfig.py

```
config = {
    'user'  : 'otrsuser', 
    'pw':   'otrspw',
    'url': 'otrs url',
    'sessionroute': '/Session/GetToken?',  # get session, this should match your actual endpoint with route 
    'ticketgetroute': '/Ticket/', # get ticket details, 
    'createticketroute': '/Ticket/TicketCreate', # Ticket Create 
}

```

### example code to use Python warapper for OTRS 5 APIimport otrsapi and otrsconfig module

```
import requests
from otrsconfig import config
from pprint import pprint
import json

# create a otrs session 
session = otrsapi()

# get ticket by TicketID
session.ticketget( { 'TicketID': '6' } ) 

# create Ticket
ticket = {
 'Ticket': { 
     'Queue': 'Raw',
     'State': 'New',
     'Title': 'Python-OTRS',
     'Type': 'Software',
     'CustomerUser': 'pritish.pattanaik',
     'Priority': '3 normal'
  },
  'Article': { 
      'Subject': 'from python request',
      'Body': 'ticket is created by python wrapper',
      'ContentType': 'text/plain; charset=utf8',
  },
  # create with dynamic fields. add one more key 'DynamicField' to ticket dict 
  'DynamicField': [

  { 'Name': 'Category', 'Value': 'Github' },
  { 'Name': 'SubCategory', 'Value': 'Python' },
      
],
}

ticketid = session.createticket(ticket)
```










