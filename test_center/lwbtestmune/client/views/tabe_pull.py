#coding=utf-8

from django.views.generic import View
from django.core.paginator import Paginator
from django.shortcuts import redirect, reverse
from django.http import JsonResponse
from lwbtestmune.lib.render_response import render_to_response
from lwbtestmune.model.project_model import BusinessModel, ProjectModel, CaseModel

class TablePull(View):

     TEMPLATE='client/table_pull.html'
     def get(self, request):

         data = {}
         cases = CaseModel.objects.all()
         data['cases']=cases

         return render_to_response(request, self.TEMPLATE, data=data)

     def post(self, request):
         newindex = request.POST.get('newIndex','')
         oldIndex = request.POST.get('oldIndex', '')
         print(newindex, oldIndex)
         return redirect(reverse('table_pull'))


