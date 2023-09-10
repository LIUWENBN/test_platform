# coding=utf-8

from django.views.generic import View
from django.shortcuts import redirect, reverse
from django.http import HttpResponse
from lwbtestmune.lib.render_response import render_to_response

class Index(View):
    TEMPLATE = 'base.html'

    def get(self, request):

        return render_to_response(request, self.TEMPLATE)
