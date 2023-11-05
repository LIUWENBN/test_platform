#coding=utf-8

from django.views.generic import View
from django.core.paginator import Paginator
from django.shortcuts import redirect, reverse
from django.http import JsonResponse
from lwbtestmune.lib.render_response import render_to_response
from lwbtestmune.model.project_model import BusinessModel, ProjectModel, CaseModel
from lwbtestmune.utils.serial import orderretrun

class TablePull(View):

     TEMPLATE='client/table_pull.html'
     def get(self, request):

         data = {}
         cases = CaseModel.objects.all().order_by('serial_num')
         data['cases']=cases

         return render_to_response(request, self.TEMPLATE, data=data)

     def post(self, request):
         cases = CaseModel.objects.all().order_by('serial_num')
         newindex = request.POST.get('newIndex','')
         oldIndex = request.POST.get('oldIndex', '')
         print('返回序号--->',newindex, type(newindex), oldIndex, type(oldIndex))

         try:
             orderretrun(cases, int(newindex), int(oldIndex))
             return JsonResponse({'code': 0, 'msg': '排序调整成功~', 'cases':cases})
         except:
             return JsonResponse({'code': -1, 'log': 'fail', 'msg': '排序调整出错~'})


