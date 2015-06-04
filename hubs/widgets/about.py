from hubs.widgets.chrome import panel
from hubs.widgets.base import argument

import jinja2

import hubs.validators as validators


template = jinja2.Template("{{text}} decause was here")
chrome = panel("This is a dummy widget")


@argument(name="text", default="Lorem ipsum dolor...",
          validator=validators.text,
          help="Some dummy text to display.")
def data(session, widget, text):
    return dict(text=text)


def should_invalidate(message, session, widget):
    raise NotImplementedError
