from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate_queryset(request, queryset, per_page=12, page_kwarg="page", order_by=None):
    if order_by:
        ordered_queryset = queryset.order_by(order_by)
    else:
        ordered_queryset = queryset
    paginator = Paginator(ordered_queryset, per_page)
    page = request.GET.get(page_kwarg)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj