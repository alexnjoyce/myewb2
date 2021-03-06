"""myEWB workspace URLs

This file is part of myEWB
Copyright 2009 Engineers Without Borders (Canada) Organisation and/or volunteer contributors

Last modified on 2010-08-20
@author Francis Kung
"""

from django.conf.urls.defaults import *

urlpatterns = patterns('workspace.views',
    url(r'(?P<workspace_id>[\d]+)/browse/$', 'browse', name='workspace_browse'),
    url(r'(?P<workspace_id>[\d]+)/detail/$', 'detail', name='workspace_detail'),
    url(r'(?P<workspace_id>[\d]+)/folderdetail/$', 'folder_detail', name='workspace_folder_detail'),
    url(r'(?P<workspace_id>[\d]+)/upload/$', 'upload', name='workspace_upload'),
    url(r'(?P<workspace_id>[\d]+)/move/$', 'move', name='workspace_move'),
    url(r'(?P<workspace_id>[\d]+)/bulkmove/$', 'bulk_move', name='workspace_bulk_move'),
    url(r'(?P<workspace_id>[\d]+)/rename/$', 'rename', name='workspace_rename'),
    url(r'(?P<workspace_id>[\d]+)/replace/$', 'replace', name='workspace_replace'),
    url(r'(?P<workspace_id>[\d]+)/bulkdelete/$', 'bulk_delete', name='workspace_bulk_delete'),
    url(r'(?P<workspace_id>[\d]+)/delete/$', 'delete', name='workspace_delete'),
    url(r'(?P<workspace_id>[\d]+)/mkdir/$', 'mkdir', name='workspace_mkdir'),
    url(r'(?P<workspace_id>[\d]+)/rmdir/$', 'rmdir', name='workspace_rmdir'),
    url(r'(?P<workspace_id>[\d]+)/preview/$', 'preview', name='workspace_preview'),
    url(r'(?P<workspace_id>[\d]+)/revision/$', 'revision_download', name='workspace_revision_download')
) 
