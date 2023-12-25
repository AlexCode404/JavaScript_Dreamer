# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('[charactername]', color="#36c036")
define a = Character('Прохожий', color="#b0c72e")
define f = Character('Друг', color="#267e23")
define will = Character('Начальник компании', color="#ff0707")
define npc = Character('Сотрудник компании', color="#23297e")

#Слои спрайтов
layeredimage friend:
    always:
        "wade5"
    attribute face:
        "wadesmile"
    attribute faces:
        "wadesurprise"

layeredimage npccharacter:
    always:
        "npcchar"
    attribute face:
        "npcneutral"

#музыка и звуки
define audio.musnormal = "audio/gametheme.ogg"
define audio.musstreet = "audio/street.ogg"
define audio.musoffice = "audio/officemusic.ogg"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

      

init python:
    #Анимация закрывания глаз
    onn = ImageDissolve("eye.png", 2.0, 50, reverse=False) 
    off = ImageDissolve("eye.png", 2.0, 50, reverse=True) 

label start:
    # Сцена 1
    scene bg night
    play music musnormal
    $ charactername = renpy.input("Как будут звать главного героя?")
    show sleep:
        xalign -0.1 yalign 1.6
    "Однажны главному герою приснился
сон,как он играет в онлайн-игры" 
    "Его через приложение поддерживают люди со всего
мира,говорят ему мотивирующие слова,и он всех побеждает,даже оказывается в
топ-игроков мира"
    # Анимация закрывания глаз
    scene black with off
    pause 1.0
    scene bg day with onn
    show nosleep1:
        xalign -0.1 yalign 1.6
    "Утром главный герой проснулся и поймал себя на мысли,что забыл
свой сон"
    e "Что же такое мне снилось?"
    "Он долго напрягал
воспоминания и вдруг вспомнил свой сон и снова задумался..."

    # Герой встает
    hide nosleep1
    show egor
    e "А почему бы не создать такой сайт"
    e "Все равно заняться нечем,а так хоть польза будет"
    "Главный герой очень
сильно заинтересовался этой темой и много времени думал об этом."
    "В итоге,он
решил,что будет изучать JavaScript и другие языки программирования,чтобы воплотить
свое желание в реальность"   

    # Сцена 2
    scene bg night
    with fade
    show frontg:
        xalign 0.9 yalign 1.1
    "Спустя некоторое время,главный герой изучил достаточно
много статей про языки программирования "
    "Он решил попробовать создать приложение
на практике,но столкнулся со множеством проблем (одна из них:тяжесть понимания
синтаксиса)"    
    "Главному герою не хватало практических навыков в разработке
приложения и он решил обратиться в веб-студию «Everest»"
    "Это решение он долго
    обдумывал..."
    "У него разболелась голова и главный герой решил прогуляться по ночной
    улице"


    #Сцена 2.1
    scene bg nightstreetl
    show frontg:
        xalign 0.9 yalign 1.1
    "Он направился в сторону центра города"
    "Вдруг к нему обратился прохожий"
    hide frontg
    show egor:
        xalign 0.9 yalign 1.1
    show anonymopen:
        xalign 0.1 yalign 8.6
    a "Молодой человек,а…"
    e "Вы что-то хотели?"
    hide anonymopen
    show anonymclose:
        xalign 0.1 yalign 8.6
    "Мужчина пристально посмотрел в глаза юного разработчика и сказал"
    hide anonymclose
    show anonymopen:
        xalign 0.1 yalign 8.6
    a "Не ходи такой
поникший"
    a "Если тебя мучает что-то,или ты не знаешь как правильно поступить в
какой-либо ситуации,то просто действую"
    a "Любой шаг-движение вперед"
    hide anonymopen
    show anonymclose:
        xalign 0.1 yalign 8.6
    "Закончив свою речь,мужчина быстро начал уходить"
    hide anonymclose
    "Главный герой точно решил,что
будет обращаться в компанию «Everest»"



    # Сцена 3
    scene bg night
    show frontg
    "Главный герой написал письмо на почту о помощи с проблемой в
компанию"
    scene black with off
    pause 1.0
    scene bg day with onn
    show frontg
    "Через день разработчики компании пригласили главного героя к себе,чтобы
показать на практике,как они разрабатывают игры/приложения/сайты"
    "Главный герой
согласился и сразу же отправился по адресу,который ему назвали"
    play music musstreet
    scene bg friend
    with fade
    show frontg:
        xalign 0.9 yalign 1.1
    "По дороге он
встретил своего друга,у них завязался диалог"
    show friend face:
        xalign 0.1 yalign -0.7
    hide friend face
    show friend faces:
        xalign 0.1 yalign -0.7
    f "Эй,привет,ты куда так торопишься?"
    hide friend faces
    show friend face:
        xalign 0.1 yalign -0.7
    e "Привет,у меня очень важное дело,я направился к новым знаниям в разработке"
    hide friend face
    show friend faces:
        xalign 0.1 yalign -0.7
    f "«Хорошо,тогда удачи,надеюсь у тебя всё получится"
    play music musstreet
    scene bg office
    with fade
    show frontg:
        xalign 0.9 yalign 1.1
    "Юный
разработчик двинулся вперед ко входу и замер на мгновенье,в его голове появились
вопросы"
    e "«Точно ли я
хочу заняться разрабатыванием сайта?"
    e "Будет ли мне тяжело это даваться?"
    e "А вдруг у
меня не получится"
    hide frontg
    show staywithnoeye:
        xalign 1.2 yalign -1.5
    "Герой закрыл глаза и представил,как у него все получилось и
огромная аудитория людей восхваляет его"
    hide staywithnoeye
    show frontg:
        xalign 0.9 yalign 1.1
    "В эту же секунду все сомнения развеялись
и юный разработчик уверенно зашел в здание"

   
    # Сцена 4
    show bg inoffice
    play music musoffice
    with fade
    show frontg:
        xalign 0.9 yalign 1.1
    show npcchara:
        xalign 0.1 yalign 1.1
    npc "День
добрый,вы к кому"
    e "Я к лучшим разработчикам"
    npc "Тогда вам точно сюда,мне они очень помогли и вам помогут"
    npc "Начальник компании пригласил подняться в
кабинет"
    scene bg mainoffice
    show frontg:
        xalign 0.9 yalign 1.1
    show neutral:
        xalign -0.1 yalign 1.1
    will "Ты уже знаешь,к какому наставнику ты пойдешь обучаться?"
    e "Нет,но я кажется выбрал,это будет тот молодой человек,которой молчит"
    will "Отлично,тогда приступайте"
    "Они отправились в его кабинет,чтобы изучить всё с начала и попробовать создать на
практике приложение"
    "..."
    return
