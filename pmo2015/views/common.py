# coding=utf-8
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import TemplateView


class CommonView(TemplateView):
    _sub_list = {}
    name = ''
    pmo = 'pmo2015'

    def get(self, request, sub=None, *args, **kwargs):
        if not sub:
            return redirect("pmo2015:%s" % self.name, sub=self._sub_list[0])
        if sub in self._sub_list:
            self.template_name = "pmo2015/%s/%s.html" % (self.name, sub)
            return super().get(request, *args, **kwargs)
        raise Http404


class BaseInfoView(CommonView):
    _sub_list = ["schedule", "place", "ticket", "prize"]
    name = "baseinfo"


class EventView(CommonView):
    _sub_list = ["battle", "stage", "venue", "raffle"]
    name = "event"
