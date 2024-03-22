from django.shortcuts import render
from members.models import memberdetails
def home(request):
        tasks = memberdetails.objects.filter(is_completed=False).order_by('created_at')[:10]
        complete = memberdetails.objects.filter(is_completed=True).order_by('updated_at')
        context = {
                        'dictTask':tasks,
                        'dictcomp':complete,
                }

        return render(request, 'home.html',context) 
