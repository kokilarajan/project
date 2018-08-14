# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.shortcuts import render,redirect,HttpResponse,render_to_response

# Create your views here.
from django.views.generic import View
from django.contrib.auth.models import User
from buk.forms import BooksForm
from buk.models import Books


from customer.models import Customer




class AddBuk(View):
	template_name='book.html'
	form_class=BooksForm
	def get(self, request):
		if request.user.is_superuser:
			form = self.form_class()

			context = {
			'form': form
			}
			return render(request,self.template_name,context)
		
	def post(self, request):
		form = self.form_class(request.POST,request.FILES)
		if form.is_valid():
			
			form.save()
			
			context = {
				'form':form,
				'success':"saved successfully"
			}
			return redirect('home')

		else:
			context = {
				'form':form
			}
			return render(request,self.template_name,context)
	



class listbook(View):
	template_name = 'all_buk.html'
	def get(self,request):
		if request.user.is_superuser:
			data = Books.objects.all()
			context={
			'data' :data
			}

			return render(request,self.template_name,context)

class Editbuk(View):
	template_name = 'edit_book.html'
	form_class =BooksForm

	def get(self,request,pk):
		if request.user.is_superuser:
			event_id = pk
			edit_book = Books.objects.get(id=event_id)
			form = BooksForm(
				initial={
				'catg_type':edit_book.catg_type,
				'buk_name':edit_book.buk_name,
				'buk_cover':edit_book.buk_cover,
				'buk_author':edit_book.buk_author,
				'buk_price':edit_book.buk_price,
				'status':edit_book.status,
			
			
				}
			)
			context = {
			'form': form
			}
			return render(request,self.template_name,context)

	def post(self,request,pk):
		event_id = pk
		form = BooksForm(request.POST,request.FILES)
		ed_book =Books.objects.get(id=event_id)
		
		if form.is_valid():
			print "valid"
			# ed_book.catg_type = str(request.POST.get('catg_type'))
			ed_book.catg_type=str(request.POST.get('catg_type'))
			ed_book.buk_cover =request.FILES.get('buk_cover')
			ed_book.buk_name=str(request.POST.get('buk_name'))
			ed_book.buk_author = str(request.POST.get('buk_author'))
			ed_book.buk_price =str(request.POST.get('buk_price'))
			ed_book.status=str(request.POST.get('status'))
			
			
			
			
			ed_book.save()
			
			context = {
			'form': form
			}
			return redirect('/home/')
		else:
			print "not valid",form.errors
			context = {
			'form':form
			}
			return render(request,self.template_name,context)

class ByView(View):
	template_name='buy.html'
	form_class =BooksForm

	def get(self,request,pk):
		 if request.user.is_staff:
			# print("in getTTTTTTTTTTTTTTTTTTTtt",pk)
			stud_id = pk

			stud_obj= Books.objects.get(id=stud_id)
		
			print("%%%%",stud_obj)
		
			form = BooksForm(
				initial={
		
				}
			)
			context = {
				'catg_type':stud_obj.catg_type,
				'buk_name':stud_obj.buk_name,
				'buk_author':stud_obj.buk_author,
				'buk_price':stud_obj.buk_price,
				'buk_cover':stud_obj.buk_cover,
				'status':stud_obj.status,
			
			}
			return render(request,self.template_name,context)

	def post(self,request,pk):
		stud_id=pk
		form=BooksForm(request.POST)
		by_bk=Books.objects.get(id=stud_id)
		
		print(pk)
		if form.is_valid():
			log_user=request.user
			by_bk.buk_name=str(request.POST.get('buk_name'))
			# by_bk.buk_author=str(request.POST.get('buk_cover'))
			# by_bk.buk_price=str(request.POST.get('buk_price'))
			by_bk.status=str("Unavailable")
			by_bk.buk_by=User.objects.get(username=log_user)
			by_bk.save()
			context ={
			'form':form


			}
			return redirect('abt')
		else:
			print("not valid"),form.errors
			by_bk.buk_name=str(request.POST.get('buk_name'))
			by_bk.status=str("Unavailable")
			by_bk.buk_author=str(request.POST.get('buk_cover'))
			by_bk.buk_price=str(request.POST.get('buk_price'))
			
			
			



			context ={
			'form':form

			}
			return render(request,self.template_name)
class Adminhome(View):
	template_name='admin.html'
	def get(self,request):
		return render(request,self.template_name)
         