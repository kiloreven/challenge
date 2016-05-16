from django.shortcuts import render

from core.models import Config
from levels.models import Level

class ClosedMiddleware(object):
    def process_request(self, request):

        if hasattr(request, 'user') and request.user.is_staff:
            return None

        if Config.objects.all().count() != 1:
            return self.closed(request)

        config = Config.objects.get(pk=1)
        if not config.active:
            return self.closed(request)

        if Level.objects.all().count() == 0:
            return self.closed(request)

        return None

    def closed(self, request):
        c = {'config': Config.objects.get(pk=1)}
        return render(request, 'core/closed.html', c)