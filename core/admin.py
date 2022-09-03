from django.contrib import admin

from .models import Produto, Cliente, Login


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email')


class LoginAdmin(admin.ModelAdmin):
    list_display = ('email', 'senha')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Login, LoginAdmin)
