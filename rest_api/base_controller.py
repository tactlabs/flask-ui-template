'''



'''

from . import api
from flask import request
from custom_flask import render_template
import random


@api.route('/', methods=['GET'])
def index():

    return render_template(
        'index.html'
    )

@api.route('/', methods=['POST'])
def result():

    entry = request.values.get('entry')
    
    result = entry

    print(f'result : {result}')

    return render_template(
        'index.html', 
        result = result
    )
