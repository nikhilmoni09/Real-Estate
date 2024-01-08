from django.http import JsonResponse
from .models import Tenant
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def tenant(request):
    try:
        if request.method == 'GET':
            id = request.GET.get('id', None)            
            filter = {}
            if id :
                filter['id'] = id

            all_entries = list(Tenant.objects.values(
                    'id', 'name',
                    'address', 'document_proofs').filter(**filter))
            response = {
            'data': all_entries,
            'message': 'Success',
            'status': True
             }
            return JsonResponse(response)
        if request.method == 'POST':
            name = request.POST.get('name', None)
            address = request.POST.get('address', None)
            document_proofs = request.POST.get('document_proofs', None)
            queryset = Tenant.objects.create(
                    name = name, 
                    address = address, 
                    document_proofs = document_proofs)  
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