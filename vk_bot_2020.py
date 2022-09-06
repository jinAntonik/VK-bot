# -*- coding: utf-8 -*-

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import requests as rq
import emoji

import datetime
from datetime import datetime

token_becurators = "29865031c531b30c70c7784b*************************************************************"

vk = vk_api.VkApi(token=token_becurators)

vk._auth_token()

id_becurators = int(*********)
longpoll = VkBotLongPoll(vk, id_becurators)


while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:

            #! for chat of whole course
            if event.object.peer_id != event.object.from_id:

                if event.object.text.lower() == "бот, спасибо":
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": emoji.emojize(
                                "Всегда пожалуйста! Обращайся:red_heart:"
                            ),
                            "random_id": 0,
                        },
                    )

                if "!кураторы" in event.object.text.lower():
                    student_id = event.object.from_id
                    info = rq.get(
                        f"https://api.vk.com/method/users.get?user_id={student_id}&v=5.92&access_token={token_becurators}"
                    )
                    response = info.json()
                    full_name = (
                        response["response"][0]["first_name"]
                        + " "
                        + response["response"][0]["last_name"]
                    )

                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": "Кураторы узнали о твоем сообщении и скоро помогут тебе!",
                            "random_id": 0,
                        },
                    )

                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 36583****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №1
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 14693****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №2
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 16409****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №3
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 25000****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №4
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 34755****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №5
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 16085****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №6
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 11672****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №7
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 15050****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №8
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 18446****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №9
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 8967****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №10
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 6620****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №11
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 6482****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №12
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 23044****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №13
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 17643****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №14
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 6366****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №15
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 30075****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №16
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 6043****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №17
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": 20682****,
                            "message": f"@id{student_id}({full_name}) задал(а) вопрос\n\n{event.object.text}",
                            "random_id": 0,
                        },
                    )  # Curator №18

                if "!учофис" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": 'Начальник отдела Васильев Филипп Валерьевич fvasilyev@hse.ru\nМетодист Копылова Анастасия Валерьевна avkopylova@hse.ru\nМетодист Скомаровская Евгения Игоревна eskomarovskaya@hse.ru\nСидоренко Виктория Артуровна viktoria.sidorenko@hse.ru\nКостусева Виолетта Александровна vkostuseva@hse.ru\n\nКабинет 4013\n"4 этаж, стеклянный коридор -> В новом корпусе поворачиваете направо и в конце коридора с левой стороны стеклянный кабинет"(Рахманова А.Ф.)\n\nРежим работы учебного офиса: пн-пт 9:30-18:00\nГрафик приема студентов: пн-пт 13:00-16:00\nТелефон: +7 (812) 644-59-11, доб. 61559 (общие вопросы, ИУП, студенческая мобильность), доб. 61560 (вопросы оплаты обучения, справки, вопросы успеваемости)',
                            "random_id": 0,
                        },
                    )

                if "!рейтинг" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": "Здесь вы можете ознакомиться со справкой о том, что такое рейтинг и каким он бывает:\nhttps://www.hse.ru/studyspravka/rate \n\nЗдесь вы можете увидеть ваш рейтинг \nspb.hse.ru/ba/economics/ratings",
                            "random_id": 0,
                        },
                    )

                if "!встреча" in event.object.text.lower():
                    now = datetime.now()
                    vstrecha = datetime(2020, 9, 6)
                    period = vstrecha - now
                    if period.days >= 0:
                        vk.method(
                            "messages.send",
                            {
                                "peer_id": event.object.peer_id,
                                "message": emoji.emojize(
                                    "Встреча назначена на 6 сентября 2020:star-struck: \n\nКураторы будут ждать тебя в 13:00 по адресу: ул.Кантемировская, д.3 (ниже прикреплены маршруты от станции метро Лесная и станции метро Петроградская) \n\nНа входе в университет тебя будут встречать твои кураторы в очень классных свитшотах! \n\nhttps://clck.ru/Pm7jW\nhttps://clck.ru/Pm7nd\n\n"
                                    + "До встречи осталось дней: {}".format(period.days)
                                ),
                                "random_id": 0,
                            },
                        )
                    else:
                        vk.method(
                            "messages.send",
                            {
                                "peer_id": event.object.peer_id,
                                "message": "Встреча прошла. Надеемся, ты ее посетил и тебе всё понравилось!",
                                "random_id": 0,
                            },
                        )

                if "!почта" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": "Коковин Сергей Гелиевич skokovin@hse.ru skokov7@gmail.com \nАлексеева Татьяна Анатольевна talekseeva@hse.ru \n\nПреподаватели по матанализу \nМинабутдинов Алексей Рафаилович aminabutdinov@hse.ru \nРунёв Евгений Валентинович jr_2010@mail.ru \nКсенофонтова Вера Алексеевна vksenofontova@hse.ru \nСейтманбитов Джемиль Акимович dzhem93@gmail.com \nИхсанов Лев Назарович lv.ikhs@gmail.com \n\nПреподаватели по микроэкономике\nКоковин Сергей Гелиевич skokovin@hse.ru skokov7@gmail.com \nКуга Яков Тойвович yakuga@hse.ru ecoman@narod.ru \nТелятников Николай Сергеевич nikolaytelytnikov@gmail.com \n\nПреподаватели по линейной алгебре \nСмирнова Надежда Владимировна nadezhda.v.smirnova@gmail.com \nКумачева Сурия Шакировна skumach@gmail.com \n\nПреподаватели по НИСу \nТерещенко Дмитрий Сергеевич dtereshch@gmail.com \nРуденко Дмитрий Юрьевич drudenko@hse.ru",
                            "random_id": 0,
                        },
                    )

                if "!внеучебка" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": "spb.hse.ru/studlife/",
                            "random_id": 0,
                        },
                    )

                if "!военка" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": "spb.hse.ru/milspb/",
                            "random_id": 0,
                        },
                    )

                if "!справка" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": emoji.emojize(
                                "Чтобы заказать справку, воспользуйся удобной формой заказа справок онлайн\n:down_arrow::down_arrow::down_arrow::down_arrow::down_arrow::down_arrow:\n\nspb.hse.ru/ba/economics/spravki"
                            ),
                            "random_id": 0,
                        },
                    )

                if "!карта" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": emoji.emojize(
                                "Это очень крутая онлайн карта здания на Кантемировской, 3\nА если совсем потерялся, ты всегда можешь написать кураторам, и они помогут тебе\n\nСкопируй это и вставь в адресную строку \n :down_arrow::down_arrow::down_arrow::down_arrow::down_arrow::down_arrow:\n\nhttp://95.161.151.11"
                            ),
                            "random_id": 0,
                        },
                    )
                if "!список кураторов" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": "Вот они сверху вниз:\n\nКураторы 201 группы: Амина Рахманова и Александров Егор \n\nКураторы 202 группы: Даша Тимофеева и Антон Алексеев \n\nКураторы 203 группы: Ася Кукукина, Денис Шумовский и Юля Бухановская \n\nКураторы 204 группы: Настя Милашенко и Дима Жучков \n\nКураторы 205 группы: Лиза Махина, Даша Староватова и Глеб Махнырь \n\nКураторы 206 группы: Алиса Малкина и Тимур Калабаев \n\nКураторы 207 группы: Маша Суслова и Руслан Рощупкин \n\nКураторы 208 группы: Маша Струговец и Милана Выдрина",
                            "random_id": 0,
                        },
                    )

                if "!расписание" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": "spb.hse.ru/ba/economics/timetable",
                            "random_id": 0,
                        },
                    )

                if "!сайт ниу вшэ спб" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": "spb.hse.ru/",
                            "random_id": 0,
                        },
                    )

                if "!пан" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": 'Начиная с 2019 учебного года, на программе «Экономика» создана группа повышенной академической нагрузки (ПАН).\n\nПодробнее можно узнать на сайте https://spb.hse.ru/pan/ \n\nА если хочешь узнать про "внутреннюю кухню" этой группы, можешь задавать вопросы Антону и Диме',
                            "random_id": 0,
                        },
                    )

                if "бот" in event.object.text.lower():
                    if "привет бот" == event.object.text.lower():
                        vk.method(
                            "messages.send",
                            {
                                "peer_id": event.object.peer_id,
                                "message": "Привет!\nКак твои дела?",
                                "random_id": 0,
                            },
                        )
                    if "бот молодец" == event.object.text.lower():
                        vk.method(
                            "messages.send",
                            {
                                "peer_id": event.object.peer_id,
                                "message": "Служить бы рад, прислуживаться тошно",
                                "random_id": 0,
                            },
                        )

                    if "спокойной ночи" in event.object.text.lower():
                        vk.method(
                            "messages.send",
                            {
                                "peer_id": event.object.peer_id,
                                "message": "Сладких снов",
                                "random_id": 0,
                            },
                        )

                if "на бюджет" in event.object.text.lower():
                    if "пере" in event.object.text.lower():
                        vk.method(
                            "messages.send",
                            {
                                "peer_id": event.object.peer_id,
                                "attachment": "photo-196896859_457239039",
                                "random_id": 0,
                            },
                        )

                if "лучшая команда" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "attachment": "photo-196896859_457239040",
                            "message": emoji.emojize("Звали?:smirking_face:"),
                            "random_id": 0,
                        },
                    )

                if "!список команд" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": "Доступные команды: \n>> !сайт ниу вшэ спб\n>> !кураторы(только для беседы)\n>> !учофис\n>> !список кураторов\n>> !почта\n>> !внеучебка\n>> !справка\n>> !военка\n>> !расписание\n>> !карта\n>> !рейтинг\n>> !пан",
                            "random_id": 0,
                        },
                    )

                if "!режим разработчика" == event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "peer_id": event.object.peer_id,
                            "message": "Существующие команды: \n>> !сайт ниу вшэ спб\n>> !учофис\n>> !список кураторов\n>> !встреча(отключена Антоном 29 августа)\n>> !почта(неактивна)\n>> !внеучебка\n>> !справка\n>> !военка\n>> !расписание\n>> !карта\n>> !рейтинг\n>> =красильников пидор для первашей\n>> саныч/красильников пидор для нас\n>> триггер от !кураторы\n>> немножко картинок\n>> немножко милоты\n>> пасхалочка",
                            "random_id": 0,
                        },
                    )

            #! for dialog with bot
            elif event.object.peer_id == event.object.from_id:

                if "!сайт ниу вшэ спб" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": "spb.hse.ru/",
                            "random_id": 0,
                        },
                    )

                if "!почта" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": "Коковин Сергей Гелиевич skokovin@hse.ru skokov7@gmail.com \nАлексеева Татьяна Анатольевна talekseeva@hse.ru \n\nПреподаватели по матанализу \nМинабутдинов Алексей Рафаилович aminabutdinov@hse.ru \nРунёв Евгений Валентинович jr_2010@mail.ru \nКсенофонтова Вера Алексеевна vksenofontova@hse.ru \nСейтманбитов Джемиль Акимович dzhem93@gmail.com \nИхсанов Лев Назарович lv.ikhs@gmail.com \n\nПреподаватели по микроэкономике\nКоковин Сергей Гелиевич skokovin@hse.ru skokov7@gmail.com \nКуга Яков Тойвович yakuga@hse.ru ecoman@narod.ru \nТелятников Николай Сергеевич nikolaytelytnikov@gmail.com \n\nПреподаватели по линейной алгебре \nСмирнова Надежда Владимировна nadezhda.v.smirnova@gmail.com \nКумачева Сурия Шакировна skumach@gmail.com \n\nПреподаватели по НИСу \nТерещенко Дмитрий Сергеевич dtereshch@gmail.com \nРуденко Дмитрий Юрьевич drudenko@hse.ru",
                            "random_id": 0,
                        },
                    )

                if "!расписание" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": "spb.hse.ru/ba/economics/timetable",
                            "random_id": 0,
                        },
                    )

                if "!справка" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": emoji.emojize(
                                "Чтобы заказать справку, воспользуйся удобной формой заказа справок онлайн\n:down_arrow::down_arrow::down_arrow::down_arrow::down_arrow::down_arrow:\n\nspb.hse.ru/ba/economics/spravki"
                            ),
                            "random_id": 0,
                        },
                    )

                if "!рейтинг" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": "Здесь вы можете ознакомиться со справкой о том, что такое рейтинг и каким он бывает:\nhttps://www.hse.ru/studyspravka/rate \n\nЗдесь вы можете увидеть ваш рейтинг \nspb.hse.ru/ba/economics/ratings",
                            "random_id": 0,
                        },
                    )

                if "!внеучебка" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": "spb.hse.ru/studlife/",
                            "random_id": 0,
                        },
                    )

                if "!пан" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": 'Начиная с 2019 учебного года, на программе «Экономика» создана группа повышенной академической нагрузки (ПАН).\n\nПодробнее можно узнать на сайте https://spb.hse.ru/pan/ \n\nА если хочешь узнать про "внутреннюю кухню" этой группы, можешь задавать вопросы Антону и Диме',
                            "random_id": 0,
                        },
                    )

                if "!военка" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": "spb.hse.ru/milspb/",
                            "random_id": 0,
                        },
                    )

                if "!список кураторов" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": "Вот они сверху вниз:\n\nКураторы 201 группы: Амина Рахманова и Александров Егор \n\nКураторы 202 группы: Даша Тимофеева и Антон Алексеев \n\nКураторы 203 группы: Ася Кукукина, Денис Шумовский и Юля Бухановская \n\nКураторы 204 группы: Настя Милашенко и Дима Жучков \n\nКураторы 205 группы: Лиза Махина, Даша Староватова и Глеб Махнырь \n\nКураторы 206 группы: Алиса Малкина и Тимур Калабаев \n\nКураторы 207 группы: Маша Суслова и Руслан Рощупкин \n\nКураторы 208 группы: Маша Струговец и Милана Выдрина",
                            "random_id": 0,
                        },
                    )

                if "!список команд" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": "Доступные команды: \n>> !сайт ниу вшэ спб\n>> !кураторы(только для беседы)\n>> !учофис\n>> !список кураторов\n>> !почта\n>> !внеучебка\n>> !справка\n>> !военка\n>> !расписание\n>> !карта\n>> !рейтинг\n>> !пан",
                            "random_id": 0,
                        },
                    )

                if "!режим разработчика" == event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": "Существующие команды: \n>> !сайт ниу вшэ спб\n>> !учофис\n>> !список кураторов\n>> !встреча(отключена Антоном 29 августа)\n>> !почта(неактивна)\n>> !внеучебка\n>> !справка\n>> !военка\n>> !расписание\n>> !карта\n>> !рейтинг\n>> =красильников пидор для первашей\n>> саныч/красильников пидор для нас\n>> триггер от !кураторы\n>> немножко картинок\n>> немножко милоты\n>> пасхалочка",
                            "random_id": 0,
                        },
                    )

                if "!карта" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": emoji.emojize(
                                "Это очень крутая онлайн карта здания на Кантемировской, 3\nА если совсем потерялся, ты всегда можешь написать кураторам, и они помогут тебе\n\nСкопируй это и вставь в адресную строку \n :down_arrow::down_arrow::down_arrow::down_arrow::down_arrow::down_arrow:\n\nhttp://95.161.151.11"
                            ),
                            "random_id": 0,
                        },
                    )

                if "!учофис" in event.object.text.lower():
                    vk.method(
                        "messages.send",
                        {
                            "user_id": event.object.from_id,
                            "message": 'Начальник отдела Васильев Филипп Валерьевич fvasilyev@hse.ru\nМетодист Копылова Анастасия Валерьевна avkopylova@hse.ru\nМетодист Скомаровская Евгения Игоревна eskomarovskaya@hse.ru\nСидоренко Виктория Артуровна viktoria.sidorenko@hse.ru\nКостусева Виолетта Александровна vkostuseva@hse.ru\n\nКабинет 4013\n"4 этаж, стеклянный коридор -> В новом корпусе поворачиваете направо и в конце коридора с левой стороны стеклянный кабинет"(Рахманова А.Ф.)\n\nРежим работы учебного офиса: пн-пт 9:30-18:00\nГрафик приема студентов: пн-пт 13:00-16:00\nТелефон: +7 (812) 644-59-11, доб. 61559 (общие вопросы, ИУП, студенческая мобильность), доб. 61560 (вопросы оплаты обучения, справки, вопросы успеваемости)',
                            "random_id": 0,
                        },
                    )

                if "бот" in event.object.text.lower():
                    if "привет бот" == event.object.text.lower():
                        vk.method(
                            "messages.send",
                            {
                                "user_id": event.object.from_id,
                                "message": "Привет!\nКак твои дела?",
                                "random_id": 0,
                            },
                        )
                    if "бот молодец" == event.object.text.lower():
                        vk.method(
                            "messages.send",
                            {
                                "user_id": event.object.from_id,
                                "message": "Служить бы рад, прислуживаться тошно",
                                "random_id": 0,
                            },
                        )
                    if "спокойной ночи" in event.object.text.lower():
                        vk.method(
                            "messages.send",
                            {
                                "user_id": event.object.from_id,
                                "message": "Сладких снов",
                                "random_id": 0,
                            },
                        )

