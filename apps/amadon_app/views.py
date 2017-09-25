# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'amadon_app/index.html')

def buy(request):
    print "buy"
    if 'total_items' not in request.session:
        request.session['total_items'] = 0
        request.session['total_charge'] = 0
    if request.POST['product_id'] == '1015':
        request.session['total_items'] += int(request.POST['quantity'])
        updated_charge = 19.99 * int(request.POST['quantity'])
        request.session['total_charge'] += updated_charge
        request.session['charge'] = updated_charge
        request.session['item'] = 'Dojo Tshirt'
    if request.POST['product_id'] == '1016':
        request.session['total_items'] += int(request.POST['quantity'])
        updated_charge = 49.99 * int(request.POST['quantity'])
        request.session['total_charge'] += updated_charge
        request.session['charge'] = updated_charge
        request.session['item'] = 'Algorithm Book'
    if request.POST['product_id'] == '1017':
        request.session['total_items'] += int(request.POST['quantity'])
        updated_charge = 29.99 * int(request.POST['quantity'])
        request.session['total_charge'] += updated_charge
        request.session['charge'] = updated_charge
        request.session['item'] = 'Dojo Sweater'
    if request.POST['product_id'] == '1018':
        request.session['total_items'] += int(request.POST['quantity'])
        updated_charge = 4.99 * int(request.POST['quantity'])
        request.session['total_charge'] += updated_charge
        request.session['charge'] = updated_charge
        request.session['item'] = 'Dojo Cup'
    return redirect('/checkout')

def checkout(request):
    return render(request, 'amadon_app/checkout.html')

def clear(request):
    print "Clear"
    request.session.clear()
    return redirect('/')
