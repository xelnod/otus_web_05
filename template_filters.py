import flask
import re

from jinja2 import evalcontextfilter, Markup, escape

blueprint = flask.Blueprint('template_filters', __name__)


@blueprint.app_template_filter()
def display_price(value):
    str_value = str(value)
    return str_value[:-2] + '.' + str_value[-2:]


_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')


@blueprint.app_template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    """
    http://flask.pocoo.org/snippets/28/
    """
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result
