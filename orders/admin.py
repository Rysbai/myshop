from django.contrib import admin
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils.html import format_html
import csv
import datetime
from .models import Order, OrderItem

def OrderDetail(obj):
    return format_html('<a href="{}">Посмотреть</a>'.format(
        reverse("orders:AdminOrderDetail", args=[obj.id])
        ))

def ExportToCSV(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
            filename=Orders-{}.csv'.format(datetime.datetime.now().strftime("%d/%m/%Y"))
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    #Первая строка - огловления
    writer.writerow(field.verbose_name for field in fields)
    #Заполняем информацией
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

def OrderPDF(obj):
    return format_html('<a href="{}">PDF</a>'.format(
        reverse('orders:AdminOrderPDF', args=[obj.id])
    ))

ExportToCSV.short_description = 'Export CSV'
OrderPDF.short_description = 'В PDF'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated', OrderDetail, OrderPDF,]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [ExportToCSV]

admin.site.register(Order, OrderAdmin)
