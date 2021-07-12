"""
openedx_errors Django application initialization.
"""

from django.apps import AppConfig
from openedx.core.djangoapps.plugins.constants import PluginURLs, ProjectType

from .hacks import add_beeline_instruments_to_middlewares


class OpenedxErrorsConfig(AppConfig):
    """
    Configuration for the openedx_errors Django application.
    """

    name = 'openedx_errors'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: '',
                PluginURLs.REGEX: '^',
                PluginURLs.RELATIVE_PATH: 'urls',
            },
            ProjectType.CMS: {
                PluginURLs.NAMESPACE: '',
                PluginURLs.REGEX: '^',
                PluginURLs.RELATIVE_PATH: 'urls',
            },
        },
    }

    def ready(self):
        add_beeline_instruments_to_middlewares()
