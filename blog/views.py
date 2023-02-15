# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,reverse,HttpResponse,HttpResponseRedirect,get_object_or_404
#from .models import Blog,Post,Comment,Haber,Duyuru
from .models import Blog
#from .forms import IletisimForm,BlogForm
from .forms import *
from django.contrib import messages

mesajlar = []

# Create your views here.
def iletisim(request):
    #command test
	form = IletisimForm(data=request.GET or None)
	if form.is_valid():
		isim = form.cleaned_data.get('isim')
		soyisim = form.cleaned_data.get('soyisim')
		email = form.cleaned_data.get('email')
		icerik = form.cleaned_data.get('icerik')
		data = {'isim':isim, 'soyisim':soyisim, 'email':email, 'icerik':icerik}
		mesajlar.append(data)
	return render(request, 'iletisim.html',context={'mesajlar':mesajlar, 'form':form})

def posts_list(request):
	postListesi = Blog.objects.all()
	gelenDeger = request.GET.get("id",None)
	if gelenDeger:
		postListesi = postListesi.filter(id=gelenDeger)
	
	context={'postListesi':postListesi}
	return render(request, 'post-list.html',context)

def post_delete(request,slug):
	blog = get_object_or_404(Blog,slug=slug) 
	blog.delete()
	msg = "<strong> %s </strong> isimli postunuz silindi" %(blog.title)
	messages.success(request,msg,extra_tags='danger')
	return HttpResponseRedirect(reverse('post-list'))

def post_create(request):
	form = BlogForm()
	if request.method == "POST":
		form = BlogForm(data=request.POST)
		if form.is_valid():
			blog = form.save()
			msg = "Tebrikler <strong> %s </strong> isimli postunuz başarıyla oluşturuldu" %(blog.title)
			messages.success(request,msg,extra_tags='success')
			url = reverse('post-detail',kwargs={'slug':blog.slug})
			return HttpResponseRedirect(url)
	return render(request,'post-create.html',context={'form':form})

def post_update(request,slug):
	blog = get_object_or_404(Blog,slug=slug) 
	form = BlogForm(instance=blog, data=request.POST or None)
	if form.is_valid():
		form.save()
		msg = "Tebrikler <strong> %s </strong> isimli postunuz başarıyla güncellendi" %(blog.title)
		messages.success(request,msg,extra_tags='info')
		return HttpResponseRedirect(blog.get_absolute_url())
	return render(request,'post-update.html', context={'blog':blog, 'form':form})
	
def sanatcilar(request,sayi):
	sanatcilar_sozluk = {
		'1' : 'Tarkan',
		'2' : ' Ajda Pekkan',
		'3' : 'Duman',
        'eminem' : 'Without Me'
	}
	sanatci = sanatcilar_sozluk.get(sayi,"Aradığınız sanatçı bulunamadı.")
	return HttpResponse(sanatci)

def post_detail(request,slug):
    #post = get_object_or_404(Post,slug=slug)
	try:
		blog = Blog.objects.get(slug=slug)
	except Blog.DoesNotExist:
		return HttpResponse('Böyle bir sayfa bulunamadı')
	
	return render(request,'post-detail.html',context={'blog':blog})
	



#TESTLER    

def test(request):
	test = "Burada Gönderiler Listelenecek"
	test2 = "(Birden fazla parametre göndermek mümkün)"
	uzunluk = "bu cümlenin uzunluğunu hesaplicam" #filter örneği
	buyukHarf = "Cümleyi büyük harfe çevir" #filter örneği
	liste = {1,2,3,4,5,6,7,8,9}
	blogListesi = Blog.objects.all()
	sayi = 10

	#getRequest
	gelenDeger = request.GET.get("id",None)
	postListesi = Post.objects.all()
	if gelenDeger: #gelenDeger None değilse yani boş değilse içeri girecek
		postListesi = postListesi.filter(id=gelenDeger)

	#form
	form = IletisimForm()

	return render(request, 'ornekler.html', context={'value1':test,'value2':test2,'value3':uzunluk,'buyukYap':buyukHarf,'sayiListesi':liste,'blogListesi':blogListesi,'sayi':sayi,'postListesi' : postListesi, 'form':form})

def testBos(request):
	return render(request, 'ornekler.html')


