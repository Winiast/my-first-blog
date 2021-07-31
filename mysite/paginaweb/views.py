from django.shortcuts import render


def post_list(request):
    return render(request, 'paginaweb/post_list.html', {})

