"""
openedx_errors Django application initialization.
"""

from django.apps import AppConfig
from openedx.core.djangoapps.plugins.constants import PluginURLs, ProjectType


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
