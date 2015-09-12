"""
populationgroupview.py

Contains administrative views for working with population groups.
"""
from admin_helpers import *

from flask import redirect, flash, request, url_for
from flask.ext.admin import BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.actions import action

from remedy.rad.models import Population, PopulationGroup


class PopulationGroupView(AdminAuthMixin, ModelView):
    """
    An administrative view for working with population groups.
    """
    column_list = ('grouporder', 'name', 'description', 'date_created')

    column_default_sort = 'grouporder'

    column_searchable_list = ('name', 'description',)

    column_labels = {
        'grouporder': 'Order', 
        'date_created': 'Date Created'
    }

    form_excluded_columns = ('populations','date_created')

    def __init__(self, session, **kwargs):
        super(PopulationGroupView, self).__init__(PopulationGroup, session, **kwargs)    
