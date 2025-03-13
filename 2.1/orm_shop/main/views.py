from django.http import Http404
from django.shortcuts import render

from main.models import Car


def cars_list_view(request):
    cars = Car.objects.all()
    template_name = 'main/list.html'
    return render(request, template_name, context={"cars": cars})


def car_details_view(request, car_id):
	try:
		car = Car.objects.get(pk=car_id)
		context = {'car': car}
		template_name = 'main/details.html'
		return render(request, template_name, context)
	except Car.DoesNotExist:
		raise Http404('Car not found')


def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
        sales = car.sale_set.all()
        template_name = 'main/sales.html'
        return render(request, template_name, context={'car': car, 'sales': sales})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
