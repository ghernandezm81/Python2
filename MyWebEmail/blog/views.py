from django.conf import settings
from django.shortcuts import render

from django.views import View

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from django.shortcuts import render, HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import Post

# Create your views here.
#def index(request):
    #return HttpResponse('Hola Mundo con Django')
    #post = Post.objects.all()
    #print(post)
    #return render(request, 'index.html', {'posts':post})

#def post(request, id):
    #post = Post.objects.get(id=id)
    #print(post)
    #return render(request, 'post.html', {'post':post})
    
    class Send(View):
    def get(self, request):
        return render(request, 'mail/send.html')
    
    def post(self, request):
        email = request.POST.get('email')
        print(email)

        template = get_template('mail/email-order-success.html')

        # Se renderiza el template y se envias parametros
        content = template.render({'email': email})

        # Se crea el correo (titulo, mensaje, emisor, destinatario)
        msg = EmailMultiAlternatives(
            'Gracias por tu compra',
            'Hola, te enviamos un correo con tu factura',
            settings.EMAIL_HOST_USER,
            [email]
        )

        msg.attach_alternative(content, 'text/html')
        msg.send()

        return render(request, 'mail/send.html')
    
    