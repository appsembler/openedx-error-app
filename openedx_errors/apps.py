"""
openedx_errors Django application initialization.
"""

from django.apps import AppConfig


class OpenedxErrorConfig(AppConfig):
    """
    Configuration for the openedx_errors Django application.
    """

    name = 'openedx_errors'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': u'openedx_errors',
                'regex': u'^',
                'relative_path': u'urls',
            }
        }
    }
