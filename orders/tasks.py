from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def OrderCreated(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Заказ с номером {}'.format(order.id)
    message = 'Дорогой, {}, вы успешно сделали заказ.\
                Номер вашего заказа {}'.format(order.user, order.id)
    mail_send = send_mail(subject, message, 'rysbai.muslim@gmail.com', [order.user.email])
    return mail_send
