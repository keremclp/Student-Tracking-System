from django.shortcuts import render




def page1(request):
    breadcrumbs = [
        {
            'name': 'Anasayfa',
            'type': 'href',
            'link': 'panel:home',
        },
        {
            'name': 'Sayfa 1',
            'type': 'text',
            'link': '',
        }
    ]
    context = {'breadcrumbs': breadcrumbs}
    return render(request, 'page1.html', context)