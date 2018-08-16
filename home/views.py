from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def home(request):
    json_data = open('home/static/accounts.json')
    data1 = json.load(json_data)
    data2 = [li['service'] for li in data1]
    json_data.close()
    context = {
        'all_data': data2,
    }
    return render(request, 'home/home.html', context)

def amazon(request):
    json_data = open('home/static/amazon.json')
    data = json.load(json_data)
    data1 = [li['long_title'] for li in data]
    data2 = [li['show_type'] for li in data]
    mylist = zip(data1, data2)
    json_data.close()
    context = {
        'service': 'amazon',
        'all_data1': mylist,

    }
    return render(request, 'home/index2.html', context)

def hulu(request):
    json_data = open('home/static/hulu.json')
    data = json.load(json_data)
    data1 = [li['long_title'] for li in data]
    data2 = [li['show_type'] for li in data]
    mylist = zip(data1, data2)
    json_data.close()
    context = {
        'service': 'hulu',
        'all_data1': mylist,

    }
    return render(request, 'home/index2.html', context)

def netflix_stephen(request):
    json_data = open('home/static/netflix_stephen.json')
    data = json.load(json_data)
    data1 = [li['long_title'] for li in data]
    data2 = [li['show_type'] for li in data]
    mylist = zip(data1, data2)
    json_data.close()
    context = {
        'service': 'stephen',
        'all_data1': mylist,

    }
    return render(request, 'home/index2.html', context)

def netflix_mom(request):
    json_data = open('home/static/netflix_mom.json')
    data = json.load(json_data)
    data1 = [li['long_title'] for li in data]
    data2 = [li['show_type'] for li in data]
    mylist = zip(data1, data2)
    json_data.close()
    context = {
        'service': 'mom',
        'all_data1': mylist,

    }
    return render(request, 'home/index2.html', context)

def netflix_dad(request):
    json_data = open('home/static/netflix_dad.json')
    data = json.load(json_data)
    data1 = [li['long_title'] for li in data]
    data2 = [li['show_type'] for li in data]
    mylist = zip(data1, data2)
    json_data.close()
    context = {
        'service': 'dad',
        'all_data1': mylist,

    }
    return render(request, 'home/index2.html', context)


def netflix(request):
    return render(request, 'home/netflix.html')





