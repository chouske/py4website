"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

from yatl.helpers import A

from py4web import URL, abort, action, redirect, request

from .common import (T, auth, authenticated, cache, db, flash, logger, session,
                     unauthenticated)


@action("index")
@action.uses("index.html", auth, T)
def index():
    user = auth.get_user()
    message = T("Hello {first_name}").format(**user) if user else T("Hello")
    print("Serving index route")
    return dict()
@action("graphics")
@action.uses("graphics.html", auth, T)
def graphics():
    return locals()
@action("graphics/asgn0")
@action.uses("graphics0.html", auth, T)
def graphics():
    return locals()
@action("graphics/asgn1")
@action.uses("graphics1.html", auth, T)
def graphics():
    return locals()
@action("graphics/asgn2")
@action.uses("graphics2.html", auth, T)
def graphics():
    return locals()
@action("graphics/asgn3")
@action.uses("graphics3.html", auth, T)
def graphics():
    return locals()
@action("graphics/asgn4")
@action.uses("graphics4.html", auth, T)
def graphics():
    return locals()
@action("graphics/asgn5")
@action.uses("graphics5.html", auth, T)
def graphics():
    return locals()
@action("memory")
@action.uses("memory.html", auth, T)
def graphics():
    return locals()
@action("memory/multithreaded-http-server")
@action.uses("multithreaded-http-server.html", auth, T)
def graphics():
    return locals()
@action("memory/cached-http-proxy-server")
@action.uses("cached-http-proxy-server.html", auth, T)
def graphics():
    return locals()
@action("aboutme")
@action.uses("aboutme.html", auth, T)
def graphics():
    return locals()
@action("unity")
@action.uses("unity.html", auth, T)
def graphics():
    return locals()
@action("unity/cardgame")
@action.uses("unitycardgame.html", auth, T)
def graphics():
    return locals()