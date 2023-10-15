
'''
Created on 

@author: Raja CSP Raman

source:
    ?
'''

from constants import *
# from flask import render_template
import flask

def render_template(
    page_name,
    **kwargs
):

    return flask.render_template(
        page_name, 
        APP_TITLE = APP_TITLE,
        **kwargs
    )