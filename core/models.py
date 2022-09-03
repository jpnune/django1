from django.db import models


class Produto(models.Model):
    """cadastro de produtos"""
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places= 2, max_digits= 8 )
    estoque = models.IntegerField('quantidade em Estoque')

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    """cadastro de clientes"""
    nome = models.CharField('nome', max_length= 100)
    sobrenome = models.CharField('sobrenome', max_length= 100)
    email = models.EmailField('email', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Login(models.Model):
    email = models.CharField('email', max_length=100)
    senha = models.CharField('senha', max_length=100)

    def __str__(self):
        return f'email = {self.email} e senha = {self.senha}'

