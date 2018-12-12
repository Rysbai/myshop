from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib import auth
import weasyprint

from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import OrderCreated

@login_required
def orderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.user = auth.get_user(request)
            order.save()
            if cart.cupon:
                order.cupon = cart.cupon
                order.discount = cart.cupon.discount
                order.save()
            for item in cart:
                product = item['product']
                quantity = item['quantity']
                OrderItem.objects.create(order=order, product=product,
                                        price=item['price'],
                                        quantity=quantity)
                product.stock -= quantity
                product.save()

            cart.clear()
            OrderCreated.delay(order.id)
            request.session['order_id'] = order.id
            return render(request, 'orders/order/created.html', {'order': order})

    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                'form': form})

@staff_member_required
def AdminOrderDetail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})


@staff_member_required
def AdminOrderPDF(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['COntent-Desposition'] = 'file_name=order_{}.pdf'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response,
                    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/bootstrap.min.css')])
    return response
