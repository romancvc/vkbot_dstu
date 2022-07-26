# -*- coding: utf-8 -*-
import vk_api.vk_api
import random
import sqlite3
import re
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


conn = sqlite3.connect('abitvkbot.db')
cursor = conn.cursor()

def get_name(from_id):
    user = vk.method("users.get", {"user_ids": from_id})
    name = user[0]['first_name']
    return name


def check_it_exists(user_id):
    cursor.execute("SELECT * FROM abit WHERE id = %d" % user_id)
    result = cursor.fetchone()
    if result is None:
        return False
    return True


def register_new_user(user_id):
    cursor.execute("INSERT INTO abit(id, name) VALUES (%d, ?)" % user_id, [name])
    conn.commit()


def register_new_mail(user_id):
    cursor.execute("UPDATE abit SET mail = (?) WHERE id = %d" % user_id, [request])
    conn.commit()


def register_new_number(user_id):
    cursor.execute("UPDATE abit SET num = (?) WHERE id = %d" % user_id, [request])
    conn.commit()


def budget_mesta(user_id):
    cursor.execute("UPDATE abit SET b_mesta = (1) WHERE id = %d" % user_id)
    conn.commit()


def update_direct(user_id):
    cursor.execute("UPDATE abit SET direct = (?) WHERE id = %d" % user_id, [direct])
    conn.commit()


# калькулятор!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def calcul_clear(user_id):
    cursor.execute("UPDATE abit SET calcul = (0) WHERE id = %d" % user_id)
    conn.commit()


def check_calculator(user_id):
    cursor.execute("SELECT calcul FROM abit WHERE id = %d" % user_id)
    for result in cursor.fetchone():
        if result == "0":
            return (0)
        else:
            return (1)


def calcul_new(user_id):
    cursor.execute("UPDATE abit SET calcul = (?) WHERE id = %d" % user_id, [num])
    conn.commit()


def calcul_up(user_id):
    cursor.execute("UPDATE abit SET calcul = (calcul || (?)) WHERE id = %d" % user_id, [num])
    conn.commit()


def calcul_check(user_id):
    cursor.execute("SELECT calcul FROM abit WHERE id = %d" % user_id)
    # resultone = cursor.fetchall()
    for resultone in cursor.fetchone():
        # ИСИТ и МАшиностроение
        if resultone == "мат|физ|":
            return (1)
        elif resultone == "мат|хим|":
            return (2)
        elif resultone == "мат|инф|":
            return (3)
        elif resultone == "физ|мат|":
            return (4)
        elif resultone == "хим|мат|":
            return (5)
        elif resultone == "инф|мат|":
            return (6)
        # Экономика и менедж
        elif resultone == "мат|ист|":
            return (7)
        elif resultone == "мат|общ|":
            return (8)
        elif resultone == "ист|мат|":
            return (9)
        elif resultone == "общ|мат|":
            return (10)
        # Соц работа
        elif resultone == "ист|гео|":
            return (11)
        elif resultone == "ист|мат|":
            return (12)
        elif resultone == "ист|инф|":
            return (13)
        elif resultone == "мат|ист|":
            return (14)
        elif resultone == "мат|ист|":
            return (15)
        elif resultone == "физ|ист|":
            return (16)
        # Психология
        elif resultone == "био|мат|":
            return (17)
        elif resultone == "био|общ|":
            return (18)
        elif resultone == "мат|био|":
            return (19)
        elif resultone == "общ|био|":
            return (20)
        # Сервис и туризм
        elif resultone == "общ|ист|":
            return (21)
        elif resultone == "общ|иняз|":
            return (22)
        elif resultone == "общ|мат|":
            return (23)
        elif resultone == "общ|гео|":
            return (24)
        elif resultone == "общ|лит|":
            return (25)
        elif resultone == "ист|общ|":
            return (26)
        elif resultone == "иняз|общ|":
            return (27)
        elif resultone == "мат|общ|":
            return (28)
        elif resultone == "гео|общ|":
            return (29)
        elif resultone == "лит|общ|":
            return (30)
        # Педагогика
        elif resultone == "общ|ист|":
            return (31)
        elif resultone == "общ|био|":
            return (32)
        elif resultone == "общ|физ|":
            return (33)
        elif resultone == "общ|инф|":
            return (34)
        elif resultone == "общ|мат|":
            return (35)
        elif resultone == "ист|общ|":
            return (36)
        elif resultone == "био|общ|":
            return (37)
        elif resultone == "физ|общ|":
            return (38)
        elif resultone == "инф|общ|":
            return (39)
        elif resultone == "мат|общ|":
            return (40)
        else:
            return (0)


# # Конец калькулятора!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def send_message(user_id, message, keyboard=None):
    post = {
        'user_id': user_id,
        'message': message,
        'random_id': get_random_id()
    }

    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post

    vk.method('messages.send', post)


# API-ключ
token = "6ecee66a52385999e76d132f3159a35cf390d40126800a82a8cccb8a908a50c90636c0101d3da489ab454"
vk = vk_api.VkApi(token=token)

# создаем объект для longpoll
longpoll = VkLongPoll(vk)

# основной цикл
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text

            name = get_name(event.user_id)
            if not check_it_exists(event.user_id):
                register_new_user(event.user_id)

            if request == "Начать":
                keyboard = VkKeyboard()
                keyboard.add_button("Хочу поступить!", VkKeyboardColor.PRIMARY)

                send_message(event.user_id, "Если хочешь поступить - нажми кнопку ниже", keyboard)
            if request == "Хочу поступить!" or request == "В начало":
                keyboard = VkKeyboard()
                keyboard.add_button("Узнать о всех направлениях", VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button("Калькулятор вступительных испытаний", VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button("Бюджетные места", VkKeyboardColor.POSITIVE)

                send_message(event.user_id,
                             "Отлично! Теперь вы можете узнать о всех доступных направлениях, воспользоваться калькулятором вступительных испытаний или посмотреть количество бюджетных мест.",
                             keyboard)

            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Ветка 1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if request == "Узнать о всех направлениях":
                keyboard = VkKeyboard()
                keyboard.add_button("Информационные системы и технологии", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Машиностроение", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Менеджмент", VkKeyboardColor.PRIMARY)
                # keyboard.add_line()
                keyboard.add_button("Сервис", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Экономика", VkKeyboardColor.PRIMARY)
                # keyboard.add_line()
                keyboard.add_button("Социальная работа", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Туризм", VkKeyboardColor.PRIMARY)
                # keyboard.add_line()
                keyboard.add_button("Психология", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Педагогическое образование", VkKeyboardColor.PRIMARY)

                send_message(event.user_id, "Вот список доступных направлений", keyboard)

            if request == "Машиностроение":
                direct = '150305'
                update_direct(event.user_id)
                keyboard = VkKeyboard()
                keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                send_message(event.user_id,
                             "Для данного направления необходимы следующие предметы или вступительные испытания:\n-русский язык;\n-математика(профиль);\n-физика/химия/информатика(на выбор).\nХотите узнать о проходных баллах, стоимости обучения и количестве бюджетных мест?",
                             keyboard)

            if request == "Информационные системы и технологии":
                direct = '090302'
                update_direct(event.user_id)
                keyboard = VkKeyboard()
                keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                send_message(event.user_id,
                             "Для данного направления необходимы следующие предметы или вступительные испытания:\n-русский язык;\n-математика(профиль);\n-физика/химия/информатика(на выбор).\nХотите узнать о проходных баллах, стоимости обучения  и количестве бюджетных мест?",
                             keyboard)

            if request == "Менеджмент":
                direct = '380302'
                update_direct(event.user_id)
                keyboard = VkKeyboard()
                keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                send_message(event.user_id,
                             "Для данного направления необходимы следующие предметы или вступительные испытания:\n-русский язык;\n-математика(профиль);\n-обществознание/история(на выбор).\nХотите узнать о проходных баллах, стоимости обучения и количестве бюджетных мест?",
                             keyboard)

            if request == "Экономика":
                direct = '380301'
                update_direct(event.user_id)
                keyboard = VkKeyboard()
                keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                send_message(event.user_id,
                             "Для данного направления необходимы следующие предметы или вступительные испытания:\n-русский язык;\n-математика(профиль);\n-обществознание/история(на выбор).\nХотите узнать о проходных баллах, стоимости обучения и количестве бюджетных мест?",
                             keyboard)

            if request == "Сервис":
                direct = '430301'
                update_direct(event.user_id)
                keyboard = VkKeyboard()
                keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                send_message(event.user_id,
                             "Для данного направления необходимы следующие предметы или вступительные испытания:\n-русский язык;\n-обществознание;\n-история/иностранный язык/математика/география/литература(на выбор).\nХотите узнать о проходных баллах, стоимости обучения и количестве бюджетных мест?",
                             keyboard)

            if request == "Туризм":
                direct = '430302'
                update_direct(event.user_id)
                keyboard = VkKeyboard()
                keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                send_message(event.user_id,
                             "Для данного направления необходимы следующие предметы или вступительные испытания:\n-русский язык;\n-обществознание;\n-история/ин. язык/математика/география/литература(на выбор).\nХотите узнать о проходных баллах, стоимости обучения и количестве бюджетных мест?",
                             keyboard)

            if request == "Психология":
                direct = '370301'
                update_direct(event.user_id)
                keyboard = VkKeyboard()
                keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                send_message(event.user_id,
                             "Для данного направления необходимы следующие предметы или вступительные испытания:\n-русский язык;\n-биология;\n-математика/обществознание(на выбор).\nХотите узнать о проходных баллах, стоимости обучения  и количестве бюджетных мест?",
                             keyboard)

            if request == "Социальная работа":
                direct = '390302'
                update_direct(event.user_id)
                keyboard = VkKeyboard()
                keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                send_message(event.user_id,
                             "Для данного направления необходимы следующие предметы или вступительные испытания:\n-русский язык;\n-история;\n-география/обществознание/литература(на выбор).\nХотите узнать о проходных баллах, стоимости обучения  и количестве бюджетных мест?",
                             keyboard)

            if request == "Педагогическое образование":
                direct = '440301'
                update_direct(event.user_id)
                keyboard = VkKeyboard()
                keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                keyboard.add_line()
                keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                send_message(event.user_id,
                             "Для данного направления необходимы следующие предметы или вступительные испытания:\n-русский язык;\n-обществознание;\n-история/биология/физика/информатика/математика(на выбор)\n.Хотите узнать о проходных баллах, стоимости обучения  и количестве бюджетных мест?",
                             keyboard)
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Конец ветки 1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Ветка 2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if request == "Калькулятор вступительных испытаний":
                calcul_clear(event.user_id)
                keyboard = VkKeyboard()
                keyboard.add_button("Математика (профиль)", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Физика", VkKeyboardColor.PRIMARY)
                # keyboard.add_line()
                keyboard.add_button("Химия", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Информатика", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Биология", VkKeyboardColor.PRIMARY)
                # keyboard.add_line()
                keyboard.add_button("История", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Обществознание", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Литература", VkKeyboardColor.PRIMARY)
                # keyboard.add_line()
                keyboard.add_button("География", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Иностранный язык", VkKeyboardColor.PRIMARY)
                keyboard.add_line()
                keyboard.add_button("Завершить", VkKeyboardColor.POSITIVE)
                send_message(event.user_id,
                             "Русский язык обязателен для всех направлений. Выберете 2 предмета, которые вы хотите сдавать или уже сдали и нажмите 'Завершить'.",
                             keyboard)

            if request == "Математика (профиль)":
                num = 'мат|'
                if check_calculator(event.user_id) == (0):
                    calcul_new(event.user_id)
                else:
                    calcul_up(event.user_id)
            if request == "Физика":
                num = 'физ|'
                if check_calculator(event.user_id) == (0):
                    calcul_new(event.user_id)
                else:
                    calcul_up(event.user_id)
            if request == "Химия":
                num = 'хим|'
                if check_calculator(event.user_id) == (0):
                    calcul_new(event.user_id)
                else:
                    calcul_up(event.user_id)
            if request == "Информатика":
                num = 'инф|'
                if check_calculator(event.user_id) == (0):
                    calcul_new(event.user_id)
                else:
                    calcul_up(event.user_id)
            if request == "Биология":
                num = 'био|'
                if check_calculator(event.user_id) == (0):
                    calcul_new(event.user_id)
                else:
                    calcul_up(event.user_id)
            if request == "История":
                num = 'ист|'
                if check_calculator(event.user_id) == (0):
                    calcul_new(event.user_id)
                else:
                    calcul_up(event.user_id)
            if request == "Обществознание":
                num = 'общ|'
                if check_calculator(event.user_id) == (0):
                    calcul_new(event.user_id)
                else:
                    calcul_up(event.user_id)
            if request == "Литература":
                num = 'лит|'
                if check_calculator(event.user_id) == (0):
                    calcul_new(event.user_id)
                else:
                    calcul_up(event.user_id)
            if request == "География":
                num = 'гео|'
                if check_calculator(event.user_id) == (0):
                    calcul_new(event.user_id)
                else:
                    calcul_up(event.user_id)
            if request == "Иностранный язык":
                num = 'иняз|'
                if check_calculator(event.user_id) == (0):
                    calcul_new(event.user_id)
                else:
                    calcul_up(event.user_id)

            if request == "Завершить":
                keyboard = VkKeyboard()
                # ИСИТ Машиностроение
                if calcul_check(event.user_id) == (1) or calcul_check(event.user_id) == (2) or calcul_check(
                        event.user_id) == (3) or calcul_check(event.user_id) == (4) or calcul_check(event.user_id) == (
                5) or calcul_check(event.user_id) == (6):
                    keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                    send_message(event.user_id,
                                 "По данному набору предметов вы можете поступить на направления подготовки:\n-Информационные системы и технологии\n-Конструкторско-технологическое обеспечение машиностроительных производств.\nХотите узнать больше о проходных баллах, стоимости обучения  и количестве бюджетных мест?",
                                 keyboard)
                # Экономика Менеджмент
                elif calcul_check(event.user_id) == (7) or calcul_check(event.user_id) == (8) or calcul_check(
                        event.user_id) == (9) or calcul_check(event.user_id) == (10):
                    keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                    send_message(event.user_id,
                                 "По данному набору предметов вы можете поступить на направления подготовки:\n-Экономика\n-Менеджмент.\nХотите узнать больше о проходных баллах, стоимости обучения  и количестве бюджетных мест?",
                                 keyboard)
                # Социальная работа
                elif calcul_check(event.user_id) == (11) or calcul_check(event.user_id) == (12) or calcul_check(
                        event.user_id) == (13) or calcul_check(event.user_id) == (14) or calcul_check(
                        event.user_id) == (15) or calcul_check(event.user_id) == (16):
                    keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                    send_message(event.user_id,
                                 "По данному набору предметов вы можете поступить на направления подготовки:\n-Социальная работа.\nХотите узнать больше о проходных баллах, стоимости обучения  и количестве бюджетных мест?",
                                 keyboard)
                # Психология
                elif calcul_check(event.user_id) == (17) or calcul_check(event.user_id) == (18) or calcul_check(
                        event.user_id) == (19) or calcul_check(event.user_id) == (20):
                    keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                    send_message(event.user_id,
                                 "По данному набору предметов вы можете поступить на направления подготовки:\n-Психология.\nХотите узнать больше о проходных баллах, стоимости обучения  и количестве бюджетных мест?",
                                 keyboard)
                # Сервис Туризм
                elif calcul_check(event.user_id) == (21) or calcul_check(event.user_id) == (22) or calcul_check(
                        event.user_id) == (23) or calcul_check(event.user_id) == (24) or calcul_check(
                        event.user_id) == (25) or calcul_check(event.user_id) == (26) or calcul_check(
                        event.user_id) == (27) or calcul_check(event.user_id) == (28) or calcul_check(
                        event.user_id) == (29) or calcul_check(event.user_id) == (30):
                    keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                    send_message(event.user_id,
                                 "По данному набору предметов вы можете поступить на направления подготовки:\n-Сервис\n-Туризм.\nХотите узнать больше о проходных баллах, стоимости обучения  и количестве бюджетных мест?",
                                 keyboard)
                # Педагогика
                elif calcul_check(event.user_id) == (31) or calcul_check(event.user_id) == (32) or calcul_check(
                        event.user_id) == (33) or calcul_check(event.user_id) == (34) or calcul_check(
                        event.user_id) == (35) or calcul_check(event.user_id) == (36) or calcul_check(
                        event.user_id) == (37) or calcul_check(event.user_id) == (38) or calcul_check(
                        event.user_id) == (39) or calcul_check(event.user_id) == (40):
                    keyboard.add_button("Хочу", VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                    send_message(event.user_id,
                                 "По данному набору предметов вы можете поступить на направления подготовки:\n-Педагогическое образование.\nХотите узнать больше о проходных баллах, стоимости обучения  и количестве бюджетных мест?",
                                 keyboard)
                # Ничего
                elif calcul_check(event.user_id) == (0):
                    keyboard.add_button("Оставить", VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_button("Не интересует", VkKeyboardColor.NEGATIVE)
                    send_message(event.user_id,
                                 "Извини, но по данному набору предметов мне нечего вам предложить.\nОставьте свою почту и номер телефона и мы свяжемся с тобой для дополнительной информации",
                                 keyboard)
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Конец 2 ветки!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Ветка 3!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if request == "Бюджетные места":
                budget_mesta(event.user_id)
                send_message(event.user_id,
                             "Для того, чтобы узнать о бюджетных местах - оставь свою почту и я отправлю тебе файл с необходимой информацией на почту.")
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:
                            request = event.text

                            mail = "".join(event.text)
                            mailvalide = re.findall(r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}", mail)
                            if request == mail:
                                register_new_mail(event.user_id)
                                send_message(event.user_id,
                                             "Спасибо. Теперь напиши свой номер телефона, чтобы мы могли с тобой связаться.")
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW:
                                        if event.to_me:
                                            request = event.text
                                            number = "".join(event.text)
                                            numbervalid = re.findall(
                                                r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", number)
                                            if request == number:
                                                keyboard = VkKeyboard()
                                                keyboard.add_button("Номер", VkKeyboardColor.PRIMARY)
                                                keyboard.add_line()
                                                keyboard.add_button("В начало", VkKeyboardColor.SECONDARY)
                                                register_new_number(event.user_id)
                                                send_message(event.user_id,
                                                             "Отлично, в течении нескольких минут тебе придет письмо на почту - не забудь проверить его. Ты всегда можешь вернуться в начало и знать что-то еще. Так же, могу предоставить номер приемной комиссии, если есть дополнительные вопросы. Для этого напиши сообщение - 'Номер'",
                                                             keyboard)
                                            break
                            break
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Конец ветки 3!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if request == "Оставить":
                send_message(event.user_id, "Супер! Напишите мне свою электронную почту.")
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:
                            request = event.text

                            mail = "".join(event.text)
                            mailvalide = re.findall(r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}", mail)
                            if request == mail:
                                register_new_mail(event.user_id)
                                send_message(event.user_id,
                                             "Спасибо. Теперь напиши свой номер телефона, чтобы мы могли с тобой связаться.")
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW:
                                        if event.to_me:
                                            request = event.text
                                            number = "".join(event.text)
                                            numbervalid = re.findall(
                                                r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", number)
                                            if request == number:
                                                keyboard = VkKeyboard()
                                                keyboard.add_button("Номер", VkKeyboardColor.PRIMARY)
                                                keyboard.add_line()
                                                keyboard.add_button("В начало", VkKeyboardColor.SECONDARY)
                                                register_new_number(event.user_id)
                                                send_message(event.user_id,
                                                             "Спасибо, что остался с нами)\n Ты всегда можешь вернуться в начало и знать что-то еще. Так же, могу предоставить номер приемной комиссии, если есть дополнительные вопросы. Для этого напиши сообщение - 'Номер'",
                                                             keyboard)
                                            break
                            break
            if request == "Хочу":
                send_message(event.user_id,
                             "Супер! Напишите мне свою электронную почту и я отправлю тебе всю необходимую информацию.")
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:
                            request = event.text

                            mail = "".join(event.text)
                            mailvalide = re.findall(r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}", mail)
                            if request == mail:
                                register_new_mail(event.user_id)
                                send_message(event.user_id,
                                             "Спасибо. Теперь напиши свой номер телефона, чтобы мы могли с тобой связаться.")
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW:
                                        if event.to_me:
                                            request = event.text
                                            number = "".join(event.text)
                                            numbervalid = re.findall(
                                                r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", number)
                                            if request == number:
                                                keyboard = VkKeyboard()
                                                keyboard.add_button("Номер", VkKeyboardColor.PRIMARY)
                                                keyboard.add_line()
                                                keyboard.add_button("В начало", VkKeyboardColor.SECONDARY)
                                                register_new_number(event.user_id)
                                                send_message(event.user_id,
                                                             "Отлично, в течении нескольких минут тебе придет письмо на почту - не забудь проверить его. Ты всегда можешь вернуться в начало и узнать что-то еще. Также могу предоставить номер телефона приемной комиссии, если есть дополнительные вопросы.",
                                                             keyboard)
                                            break
                            break
            if request == "Не интересует":
                send_message(event.user_id,
                             "Очень жаль, что тебя не заинтересовали наши направления. Оставь свою почту и я буду держать тебя в курсе новинок)")
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:
                            request = event.text

                            mail = "".join(event.text)
                            mailvalide = re.match(r"^[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}", mail)
                            if request == mail:
                                keyboard = VkKeyboard()
                                keyboard.add_button("Номер", VkKeyboardColor.PRIMARY)
                                keyboard.add_line()
                                keyboard.add_button("В начало", VkKeyboardColor.SECONDARY)
                                register_new_mail(event.user_id)
                                send_message(event.user_id,
                                             "Спасибо) Ты всегда сможешь вернуться в начало и узнать что-то еще. Так же, могу предоставить номер приемной комиссии, если есть дополнительные вопросы. Для этого напиши сообщение - 'Номер'",
                                             keyboard)
                            break
            if request == "Номер":
                keyboard = VkKeyboard()
                keyboard.add_button("В начало", VkKeyboardColor.SECONDARY)
                send_message(event.user_id,
                             "Номер приемной комиссии - 8 (8639) 24-01-50.\n Адрес  - г. Волгодонск, пр-кт Мира 16, корпус 1",
                             keyboard)

