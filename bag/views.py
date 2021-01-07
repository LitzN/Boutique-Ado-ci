from django.shortcuts import render


def view_bag(request):
    """ A view to show the shopping bag contents"""
    return render(request, 'bag/bag.html')
