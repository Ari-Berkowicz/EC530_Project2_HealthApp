from flask import Flask
from json2table import convert
import device_module


# print a nice greeting.
def say_hello(username="World"):
    return '<div class="row"> <div class="col-md-12"><h1>Device Module</h1></div></div>'


json_object = device_module.parse_json('data.json')

build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style": "width:100%; border: 1px solid;"}
html = convert(json_object,
               build_direction=build_direction,
               table_attributes=table_attributes)
print(html)


# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = html
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule(
    '/', 'index',
    (lambda: header_text + say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello',
                         (lambda username: header_text + say_hello(username) +
                          home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host="localhost", port=8000, debug=True)
