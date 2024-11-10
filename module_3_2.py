def send_email(massage, recipient, *, sender="university.help@gmail.com"):
    if "@" not in (recipient or sender) or not (
            '.com' in recipient[-4:] or '.ru' in recipient[-3:] or '.net' in recipient[-4:]) or not (
            '.com' in sender[-4:] or '.ru' in sender[-3:] or '.net' in sender[-4:]):
        print('Невозможно отправить письмо с адерса', sender, 'на адрес', recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
