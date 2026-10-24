from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Avtomobil
from .forms import AvtomobilForm
def home(request):
    avtomobiller = Avtomobil.objects.all().order_by("-elave_tarix")

    # Bütün form məlumatlarını tuturuq
    marka = request.GET.get('marka')
    seher = request.GET.get('seher')
    maks_qiymet = request.GET.get('qiymet')
    il = request.GET.get('il')
    
    veziyyet = request.GET.get('veziyyet')
    kredit = request.GET.get('kredit')
    barter = request.GET.get('barter')

    # Standart filterlər
    if marka:
        avtomobiller = avtomobiller.filter(marka=marka)
    if seher:
        avtomobiller = avtomobiller.filter(seher=seher)
    if maks_qiymet:
        avtomobiller = avtomobiller.filter(qiymet__lte=maks_qiymet)
    if il:
        avtomobiller = avtomobiller.filter(il=il)

    # Vəziyyət (Yeni / Sürülmüş) filteri
    if veziyyet == 'yeni':
        avtomobiller = avtomobiller.filter(yeni=True)
    elif veziyyet == 'surulmus':
        avtomobiller = avtomobiller.filter(yeni=False)
        
    # Checkboxlar seçiləndə dəyəri 'on' olaraq gəlir
    if kredit == 'on':
        avtomobiller = avtomobiller.filter(kredit=True)
    if barter == 'on':
        avtomobiller = avtomobiller.filter(barter=True)

    # İstifadəçinin favorilərini sessiyadan oxuyuruq
    favoriler = request.session.get('favoriler', [])

    return render(request, "home.html", {
        "avtomobiller": avtomobiller,
        "favoriler": favoriler,
    })

def haqqimda(request):
    return render(request, "haqqimda.html")

def elan_detay(request, id):
    avto = get_object_or_404(Avtomobil, id=id)
    return render(request, "elan_detay.html", {"avto": avto})

def secilmisler_goster(request):
    favori_ids = request.session.get('favoriler', [])
    avtomobiller = Avtomobil.objects.filter(id__in=favori_ids)
    return render(request, "secilmisler.html", {"avtomobiller": avtomobiller})

def favori_toggle(request, id):
    if 'favoriler' not in request.session:
        request.session['favoriler'] = []
    
    favoriler = request.session['favoriler']
    if id in favoriler:
        favoriler.remove(id)
        durum = "silindi"
    else:
        favoriler.append(id)
        durum = "elave_olundu"
        
    request.session.modified = True
    return JsonResponse({"durum": durum})
def yeni_elan(request):
    if request.method == 'POST':
        form = AvtomobilForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Elan yadda saxlanılnca ana səhifəyə qayıdır
    else:
        form = AvtomobilForm()
    
    return render(request, "elan_yerlesdir.html", {"form": form})