from django.shortcuts import render
from .models import Schemes
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404
def b_index(request):

    return render(request,'pros/blogindex.html')


def all_sch(request):
    schs = Schemes.objects.all()
    paginator = Paginator(schs,2)
    page = request.GET.get('page')
    paged_sch = paginator.get_page(page)
    context = {'schs': paged_sch}

    return render(request, 'pros/schemes.html', context)


def sig_sch(request, sch_id):
    a = get_object_or_404(Schemes, pk=sch_id)
    context = {'ss':a}
    return render(request, 'pros/sig_sch.html',context)

def search(request):
    schs = Schemes.objects.all()

    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        print('here is the keyword:', keywords)
        if keywords:
            schs: schs.filter(descp__icontains=keywords)

    context = {'schs': schs}
    return render(request,'pros/search.html',context)