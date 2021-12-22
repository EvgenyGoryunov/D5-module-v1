from datetime import datetime

from django.core.mail import EmailMultiAlternatives, send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View

from .models import Appointment


# обрабатывает запрос и сохраняет новые объекты в БД (в базе данных), models.py
class AppointmentView(View):
    # получаем шаблон для ввода данных
    def get(self, request, *args, **kwargs):
        return render(request, 'appointment_created.html', {})

    # отправляем на сервер нашу информацию и сохраняем на нем, либо добавляем в БД
    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        # получаем наш html
        html_content = render_to_string(
            'appointment_created.html',
            {
                'appointment': appointment,
            }
        )

        # блок для отправки писем из базы данных любому адресату
        # так как объект уже создан в бд, то достаточно отправить его поля по почте, то есть сформировать из них
        # само письмо, для удобства сделаем так, чтоб имя клиента было темой, выделялось жирным шрифтом и
        # показывалось в письме первым, далее идет само сообщение содержащее краткую суть проблемы и в заключении
        # добавить дату записи. И всё это отправлялось на почту любому адресату
        send_mail(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            # имя клиента и дата записи будут в теме для удобства
            message=appointment.message,  # сообщение с кратким описанием проблемы
            from_email='peterbadson@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
            recipient_list=[]  # здесь список получателей. Например, секретарь, сам врач и т. д.
        )
        # в конструкторе уже знакомые нам параметры, да? Называются правда немного по другому, но суть та же.

        return redirect('appointments:make_appointment')






        # msg = EmailMultiAlternatives(
        #     subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
        #     body=appointment.message,  # это то же, что и message
        #     from_email='peterbadson@yandex.ru',
        #     to=['skavik46111@gmail.com'],  # это то же, что и recipients_list
        # )
        # msg.attach_alternative(html_content, "text/html")  # добавляем html
        #
        # msg.send()  # отсылаем