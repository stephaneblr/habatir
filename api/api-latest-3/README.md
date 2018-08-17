### setup : 

'''

$ cd chemin/du/projet
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ export FLASK-APP=api.py
'''

### run : 

'''

$ cd chemin/du/projet
$ source env/bin/activate
$ flask run
'''


### jinja2 for web pages : 

Placeholders for dynamic content : 

'''

{{...}}
'''


Conditional statements {% ... %} : 

'''

{% if CONDITION %}
    
{% else %}

{% endif %}



{% for ITEM in LIST %}

{% endfor %}
'''


Framework inheritance : 

'''

{% extends "BASE_TO_INHERIT.html" %}
'''


Render template (rendering) : 

'''

render_template('page.html', [any_python_argument, ...])
'''