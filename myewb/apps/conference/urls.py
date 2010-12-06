"""myEWB conference registration URLs

This file is part of myEWB
Copyright 2009 Engineers Without Borders Canada

Created on: 2009-10-18
@author: Francis Kung
"""
from django.conf.urls.defaults import *
from conference.forms import ConferenceRegistrationForm, ConferenceRegistrationFormPreview

urlpatterns = patterns('conference.views',
    url(r'^$', 'view_registration', name='confreg'),    
    url(r'^login/$', 'login', name='conference_login'),    
    url(r'^preview/$', 'registration_preview', name='conference_preview'),
    url(r'^receipt/$', 'receipt', name='conference_receipt'),    
    url(r'^cancel/$', 'cancel', name='conference_cancel'),    
    url(r'^list/$', 'list', name='conference_list'),    
    url(r'^list/(?P<chapter>[\w\._-]+)$', 'list', name='conference_list_chapter'),    
    url(r'^codes/$', 'generate_codes', name='conference_codes'),
    url(r'^codelookup/$', 'lookup_code', name='conference_code_lookup')    ,

    url(r'^download/all/$', 'download', kwargs={'who': 'all'}, name='conference_download_all'),
    url(r'^download/chapter/$', 'download', kwargs={'who': 'chapter'}, name='conference_download_chapter'),
    url(r'^download/open/$', 'download', kwargs={'who': 'open'}, name='conference_download_open'),
    url(r'^download/alumni/$', 'download', kwargs={'who': 'alumni'}, name='conference_download_alumni'),
    url(r'^download/external/$', 'download', kwargs={'who': 'external'}, name='conference_download_external'),
	
    (r'^who/', include('confcomm.urls')),
)
