from django.core.mail import send_mail

from R4C import settings
from orders.models import Order


def send_email_notification(sender, **kwargs):
    robot = kwargs["instance"]
    customers = Order.objects.values("customer__email").\
        filter(robot_serial=robot.serial)
    subject = "Заказ робота"
    message = f"Добрый день!\n" \
              f"Недавно вы интересовались нашим роботом модели {robot.model}" \
              f", версии {robot.version}.\n" \
              f"Этот робот теперь в наличии. Если вам подходит этот вариант" \
              f" - пожалуйста, свяжитесь с нами"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [customer["customer__email"] for customer in customers]
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)
