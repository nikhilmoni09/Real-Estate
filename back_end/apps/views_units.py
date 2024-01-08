from django.http import JsonResponse
from .models import Units
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def units(request):
    try:
        if request.method == 'GET':
            id = request.GET.get('id', None)
            tenant_id = request.GET.get('tenant_id', None)
            filter = {}
            if id :
                filter['id'] = id
            if tenant_id :
                filter['tenant_id'] = tenant_id
            all_entries = list(Units.objects.values(
                    'id', 'rent_cost',
                    'type', 'tenant_id', 'property_id',
                    'agree_end_date', 'rent_date', 
                    'tenant_id__name', 
                    'tenant_id__address',
                    'tenant_id__document_proofs',
                    'property_id__property_name',
                    'property_id__address',
                    'property_id__location',
                    'property_id__features'
                    ).filter(**filter))
            response = {
            'data': all_entries,
            'message': 'Success',
            'status': True
             }
            return JsonResponse(response)
        if request.method == 'POST':
            rent_cost = request.POST.get('rent_cost', None)
            type = request.POST.get('type', None)
            tenant_id = request.POST.get('tenant_id', None)
            property_id = request.POST.get('property_id', None)
            agree_end_date = request.POST.get('agree_end_date', None)
            rent_date = request.POST.get('rent_date', None)
            queryset = Units.objects.create(
                    rent_cost = rent_cost, 
                    type = type, 
                    rent_date = rent_date, 
                    agree_end_date = agree_end_date, 
                    property_id_id = property_id, 
                    tenant_id_id = tenant_id)  
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