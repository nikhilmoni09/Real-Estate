from django.http import JsonResponse
from .models import Property
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def property(request):
    try:
        if request.method == 'GET':
            all_entries = list(Property.objects.values(
                    'id', 'property_name',
                    'address', 'location', 'features'))
            response = {
            'data': all_entries,
            'message': 'Success',
            'status': True
             }
            return JsonResponse(response)
        print('POSU', request.method)
        if request.method == 'POST':
            property_name = request.POST.get('property_name', None)
            address = request.POST.get('address', None)
            location = request.POST.get('location', None)
            features = request.POST.get('features', None)
            queryset = Property.objects.create(
                    property_name = property_name, 
                    address = address, 
                    location = location,
                    features = features)  
            queryset.save()
        response = {
            'message': 'Success',
            'status': True
        }
        return JsonResponse(response)
    except Exception as error:
        response = {
            'error_message': str(error),
            'status': False
        }
        return JsonResponse(response)