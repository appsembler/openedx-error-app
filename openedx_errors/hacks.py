import beeline

from django.utils.deprecation import MiddlewareMixin


def add_beeline_instruments_to_middlewares():
    old_call = MiddlewareMixin.__call__

    def patched_middeware_call(self, request):
        trace_name = 'openedx_errors:middleware:{}'.format(self.__class__.__name__)
        with beeline.tracer(trace_name):
            return old_call(self, request)

    MiddlewareMixin.__call__ = patched_middeware_call
