# Create your views here.

import urllib
import requests
import pdb
import json
import pyrise
import logging

from django import http
from django.conf import settings


client_id = getattr(settings, 'HIGHRISE_CLIENT_ID', None)
redirect_uri = getattr(settings, 'HIGHRISE_REDIRECT_URI', None)
client_secret = getattr(settings, 'HIGHRISE_CLIENT_SECRET', None)
highrise_server = 'https://guideadvisor.highrisehq.com/'

def index(request):
    launchpad_base_url = 'https://launchpad.37signals.com/'
    query_args = {
        'type': 'web_server',
        'client_id': client_id,
        'redirect_uri': redirect_uri
    }
    url = '{0}authorization/new?{1}'.format(
        launchpad_base_url,
        urllib.urlencode(query_args))
    return http.HttpResponseRedirect(url)

def oauth(request):
    code = request.GET.get('code')
    if not code:
        raise http.Http404

    query_args = {
        'type': 'web_server',
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': code
    }
    url = "https://launchpad.37signals.com/authorization/token"
    req = requests.post(url, data=query_args)
    if req.status_code != 200:
        raise http.Http404
    data = json.loads(req.content)
    logging.info(data)
    pyrise.Highrise.set_server(highrise_server)
    pyrise.Highrise.oauth(data['access_token'])
    people = pyrise.Person.all()
    pdb.set_trace()
    return http.HttpResponse(data['access_token'])