#!/home/welkere/env/short/bin/python
# vim:fileencoding=utf-8
"""
Url shortener cgi
"""

import sys, os, cgi
sys.stderr = sys.stdout
print "Content-type: text/xml\n\n"

os.environ['VIRTUAL_ENV'] = '/home/welkere/env/short'
venv = '/home/welkere/env/info/bin/activate_this.py'
execfile(venv, dict(__file__=venv))

_project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, _project_dir)
sys.path.insert(0, '/home/welkere/python/short')
sys.path.insert(0, os.path.dirname(_project_dir))

from short import shorten_url
form = cgi.FieldStorage()
url = form.getvalue('url')
if url is not None:
    short = shorten_url(url)

    print "<url>%s</url>" % short['url']
else:
    print "<error>no url entered</error>"
