"""Set up for the Tahoe LTI Customizations package."""

from setuptools import setup

setup(
    name='openedx-errors',
    version='0.1.0',
    description='An Open edX app that throws a 500 error in different contexts.',
    packages=[
        'openedx_errors',
    ],
    entry_points={
        'lms.djangoapp': [
            'openedx_errors = openedx_errors.apps:OpenedxErrorsConfig',
        ]
    },
)
