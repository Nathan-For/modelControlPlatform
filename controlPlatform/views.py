from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
from controlPlatform.models import ThyroidManualMarking


def controlPlatform(request):
    return render(request, 'controlPlatform.html')


#  因为是class，所以访问不到方法
class MarkingDataOperation:
    @staticmethod
    def get_by_id(request):
        data_id = 2782
        marked_data = ThyroidManualMarking.objects.get(pro_data_r=data_id)
        return HttpResponse('查找成功')
