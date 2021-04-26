from django.db import models


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField( max_length=50, null=False)
    descricao = models.CharField(max_length=50, null=False)
    preco = models.FloatField(null=False)
    foto = models.ImageField(null=False)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        # Se a categoria for excluida, todos os produtos que ela contem serão excluidos tbm
    )

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=80, null=False)
    telefone = models.CharField(max_length=80, null=False)
    email = models.EmailField(null=True, upload_to="images")
    # endereco =

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    produto = models.ForeignKey(Produto, null=True, on_delete=models.SET_NULL)
    # entregador =
    # valor_total =
    data = models.DateField(auto_now_add=True)
    STATUS_CHOICES= (
        ('P', 'Pendente'),
        ('SE', 'Saiu Para Entrega'),
        ('E', 'Entregue')
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

# class Entregador(models.Model):