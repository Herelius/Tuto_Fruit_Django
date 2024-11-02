from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib import messages

from .models import Produit
from .forms import ProduitForm


def index(request, *args, **kwargs):
    liste_produits = Produit.objects.all()
    context = {
        'produits': liste_produits,
        'nom': 'Produit de la boutique'
    }
    return render(request, 'index.html', context)


# Création du formulaire manuel
# class CreateProduct(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'produits/create_product.html')
    
#     def post(self, request, *args, **kwargs):
#         try:
#             nom = request.POST.get('nom')
#             description = request.POST.get('description')
#             prix = request.POST.get('prix')
#             image = request.FILES.get('image')
            
#             produit = Produit.objects.create(nom=nom, description=description, prix=prix, image=image)
            
#             if produit:
#                 return HttpResponse("Produit enregistré avec succès.")
#         except:
#             return HttpResponse("Erreur d'enregistrement du produit.")

# Création du formulaire avec Django
class CreateProduct(View):
    def get(self, request, *args, **kwargs):
        form = ProduitForm()

        return render(request, 'produits/create_product.html', { 'form': form })
    
    def post(self, request, *args, **kwargs):
        form = ProduitForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit crée avec succès.')
            return redirect('produits:index')
        else:
            messages.error(request, "Erreur lors de l'enregistrement du produit.")
            return render(request, 'produits/create_product.html', { 'form': form })
