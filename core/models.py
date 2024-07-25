from django.db import models
#slug
from django.utils.text import slugify
#format_html pra exibir a imagem em miniatura
from django.utils.html import format_html

# Create your models here.

class Category (models.Model):
    cat_name = models.CharField('Nome da Categoria',unique=True, max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)

#Criação do slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.cat_name)
        super().save(*args, **kwargs)

    '''
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.cat_name)
            text_slug = base_slug
            counter = 1
            while Category.objects.filter(slug=text_slug).exists():
                text_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = text_slug
        super().save(*args, **kwargs)
    '''
    def __str__(self):
        return self.cat_name
    
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Products (models.Model):
    name = models.CharField('Nome', unique=True, max_length=100)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Quantidade em Estoque')
    description = models.TextField('Descrição do Produto', null=True, blank=True)
    pro_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField('Imagem de Capa', upload_to='images/produto', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True,null=True, max_length=255)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
        return self.name
    
    
    #mini_image para retornar a imagem em miniatura no painel admin
    def mini_image(self):
        if self.image:
            return format_html('<img src="{}" style="height: 100px; width: auto;" />', self.image.url)
        return " "
    mini_image.short_description = 'Imagem de Capa'
    
    
class Blog(models.Model):
    blo_title = models.CharField('Título', max_length=100)
    blo_subtitle = models.CharField('Sub-Título', max_length=100, blank=True, null=True)
    blo_description = models.TextField('Texto do Blog')
    #blo_description = HTMLField('Texto do Blog')
    blo_image = models.ImageField('Imagem de Capa', upload_to='images/blog', blank=True, null=True)
    # image = models.ImageField(upload_to='images/', default='images/default.jpg')
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    '''
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blo_title)
        super().save(*args, **kwargs)
    '''
    #Abaixo o slug possui a função de adicionar um sufixo caso já exista com o mesmo nome
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.blo_title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    #mini_image para retornar a imagem em miniatura no painel admin
    def mini_image(self):
        if self.blo_image:
            return format_html('<img src="{}" style="height: 100px; width: auto;" />', self.blo_image.url)
        return " "
    mini_image.short_description = 'Imagem de Capa'

    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
       return self.blo_title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        
