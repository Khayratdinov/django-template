from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate_queryset(request, queryset, per_page=10, page_kwarg="page"):
    paginator = Paginator(queryset, per_page)
    page = request.GET.get(page_kwarg)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj