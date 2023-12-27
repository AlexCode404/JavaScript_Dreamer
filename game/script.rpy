# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('[charactername]', color="#36c036")
define a = Character('Прохожий', color="#b0c72e")
define f = Character('Друг', color="#267e23")
define will = Character('Начальник компании', color="#ff0707")
define npc = Character('Сотрудник компании', color="#23297e")

init :
    transform txt_up:
        yalign 1.5
        linear 15.0 yalign -1.5

label creditz:
    scene black with dissolve
    show text " {color=#fdfdfd}{size=+90} КОНЕЦ {/size} {p} {p} {p} {p} {p} {p} {p} {p} {p}  {p} {p} {p} {p} {p} {p} {p} {p} {p} {p}               Материалы взяты из группы: https://vk.com/ayri_attic {p} Music: Magic Escape Room by Kevin MacLeod {p}Free download: https://filmmusic.io/song/10113-magic-escape-room {p}Licensed under CC BY 4.0: https://filmmusic.io/standard-license {p} Music: Space Jazz by Kevin MacLeod {p}Free download: https://filmmusic.io/song/8328-space-jazz {p}Licensed under CC BY 4.0: https://filmmusic.io/standard-license {p}Music: Waltz Primordial (feat. Alexander Nakarada) by Kevin MacLeod {p}Free download: https://filmmusic.io/song/7929-waltz-primordial-feat-alexander-nakarada {p}Licensed under CC BY 4.0: https://filmmusic.io/standard-license {p} Music: Nuh Na Nuh by Kevin MacLeod {p} Free download: https://filmmusic.io/song/6429-nuh-na-nuh {p} Licensed under CC BY 4.0: https://filmmusic.io/standard-license{/color}" at txt_up                                 
    pause 90
    return 


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
define audio.end = "audio/thend.ogg"
define audio.musnight = "audio/night.ogg"

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
    "{cps=30}Однажны главному герою приснился
сон,как он играет в онлайн-игры {/cps}" 
    "{cps=30}Его через приложение поддерживают люди со всего
мира,говорят ему мотивирующие слова,и он всех побеждает,даже оказывается в
топ-игроков мира{/cps}"
    # Анимация закрывания глаз
    scene black with off
    pause 1.0
    scene bg day with onn
    # Анимация закончилась
    show nosleep1:
        xalign -0.1 yalign 1.6
    "{cps=30}Утром главный герой проснулся и поймал себя на мысли,что забыл
свой сон{/cps}"
    e "{cps=30}Что же такое мне снилось?{/cps}"
    "{cps=30}Он долго напрягал
воспоминания и вдруг вспомнил свой сон и снова задумался...{/cps}"

    # Герой встает
    hide nosleep1
    show egor:  
        xpos 300 ypos 200
        linear .3 xpos 700 ypos 230
        

    e "{cps=30}А почему бы не создать такой сайт{/cps}"
    e "{cps=30}Все равно заняться нечем,а так хоть польза будет{/cps}"
    "{cps=30}Главный герой очень
сильно заинтересовался этой темой и много времени думал об этом.{/cps}"
    "{cps=30}В итоге,он
решил,что будет изучать JavaScript и другие языки программирования,чтобы воплотить
свое желание в реальность{/cps}"   

    # Сцена 2
    scene bg night
    with fade
    show frontg:
        xalign 0.9 yalign 1.1
    "{cps=30}Спустя некоторое время,главный герой изучил достаточно
много статей про языки программирования {/cps}"
    "{cps=30}Он решил попробовать создать приложение
на практике,но столкнулся со множеством проблем (одна из них:тяжесть понимания
синтаксиса){/cps}"    
    "{cps=30}Главному герою не хватало практических навыков в разработке
приложения и он решил обратиться в веб-студию «Everest»{/cps}"
    "{cps=30}Это решение он долго
    обдумывал...{/cps}"
    "{cps=30}У него разболелась голова и главный герой решил прогуляться по ночной
    улице{/cps}"
    hide frontg with moveoutright

    #Сцена 2.1
    play music musnight
    scene bg nightstreetl
    show frontg with easeinright:
        xalign 0.9 yalign 1.1
    "{cps=30}Он направился в сторону центра города{/cps}"
    "{cps=30}Вдруг к нему обратился прохожий{/cps}"
    hide frontg
    show egor:
        xalign 0.9 yalign 1.1
    show anonymopen with easeinleft:
        xalign 0.1 yalign 8.6
    a "{cps=30}Молодой человек,а…{/cps}"
    hide anonymopen
    show anonymclose:
        xalign 0.1 yalign 8.6
    e "{cps=30}Вы что-то хотели?{/cps}"
    "{cps=30}Мужчина пристально посмотрел в глаза юного разработчика и сказал{/cps}"
    hide anonymclose
    show anonymopen:
        xalign 0.1 yalign 8.6
    a "{cps=30}Привет, ты выглядишь заблудившимся.
Разберешься с проблемой?{/cps}"
    hide anonymopen
    show anonymclose:
        xalign 0.1 yalign 8.6
    e "«{cps=30}Я пытаюсь создать сайт для своей игры, но не могу освоить JavaScript. Я
рассчитывал обратиться в компанию Эверест для получения помощи{/cps}"
    e "{cps=30}Но моя голова
начала болеть, и я не уверен, что это хорошая идея{/cps}"
    hide anonymclose
    show anonymopen:
        xalign 0.1 yalign 8.6
    a "«{cps=30}Иногда важно действовать так, как велит сердце.{/cps}"
    a "{cps=30}Но помни{/cps}"
    a "{cps=30}Всегда полезно
получить помощь от тех, кто уже прошел этот путь.{/cps}"
    hide anonymopen
    show anonymclose:
        xalign 0.1 yalign 8.6
    "{cps=30}Закончив свою речь,мужчина быстро начал уходить{/cps}"
    hide anonymclose with moveoutleft
    menu:
        "{cps=30}Что делать? Обращаться ли главному герою в компанию Эверест?{/cps}"
        "{cps=30}Обратиться за помощью в компанию Эверест{/cps}":
            jump help_accept
        "{cps=30}Не обращаться за помощью в компанию Эверест{/cps}":
            jump help_refuse
    return
    

# 1 развилка событий с незнакомцем

# Герой соглашается обратиться за помощью
label help_accept:
    "{cps=30}Главный герой решает обратиться в компанию Эверест за помощью{/cps}"
    hide egor with moveoutright
    # Сцена 3
    scene bg night
    play music musnormal
    show frontg with easeinright
    "{cps=30}Главный герой написал письмо на почту о помощи с проблемой в
    компанию{/cps}"
    scene black with off
    pause 1.0
    scene bg day with onn
    show frontg
    "{cps=30}Через день разработчики компании пригласили главного героя к себе,чтобы
показать на практике,как они разрабатывают игры/приложения/сайты{/cps}"
    "{cps=30}Главный герой
согласился и сразу же отправился по адресу,который ему назвали{/cps}"
    hide frontg with moveoutright
    play music musstreet
    scene bg friend
    with fade
    show frontg with easeinright:
        xalign 0.9 yalign 1.1
    "{cps=30}По дороге он
встретил своего друга,у них завязался диалог{/cps}"
    show friend  with easeinleft:
        xalign 0.1 yalign -0.7
    hide friend face
    show friend faces:
        xalign 0.1 yalign -0.7
    f "{cps=30}Эй,привет,ты куда так торопишься?{/cps}"
    hide friend faces 
    show friend face:
        xalign 0.1 yalign -0.7
    menu:
        "{cps=30}Привет, просто гуляю{/cps}":
            f "{cps=30}Ага, конечно, давай говори, что у тебя случилось{/cps}"
        "{cps=30}Привет, у меня важное дело{/cps}":
            f "{cps=30}Рассказывай{/cps}"
    e "{cps=30}Я направился к новым знаниям в разработке{/cps}"
    hide friend face
    show friend faces:
        xalign 0.1 yalign -0.7
    f "{cps=30}«Хорошо,тогда удачи,надеюсь у тебя всё получится{/cps}"
    hide friend faces with moveoutleft
    hide frontg with moveoutright
    play music musstreet
    scene bg office
    with fade
    show frontg with easeinright:
        xalign 0.9 yalign 1.1
    "{cps=30}Юный
разработчик двинулся вперед ко входу и замер на мгновенье,в его голове появились
вопросы{/cps}"
    e "{cps=30}«Точно ли я
хочу заняться разрабатыванием сайта?{/cps}"
    e "{cps=30}Будет ли мне тяжело это даваться?{/cps}"
    e "{cps=30}А вдруг у
меня не получится{/cps}"
    hide frontg
    show staywithnoeye:
        xalign 1.2 yalign -1.5
    "{cps=30}Герой закрыл глаза и представил,как у него все получилось и
огромная аудитория людей восхваляет его{/cps}"
    hide staywithnoeye
    show frontg:
        xalign 0.9 yalign 1.1
    "{cps=30}В эту же секунду все сомнения развеялись
и юный разработчик уверенно зашел в здание{/cps}"
    hide frontg with moveoutright

   
    # Сцена 4
    show bg inoffice
    play music musoffice
    with fade
    show frontg with easeinright:
        xalign 0.9 yalign 1.1
    show npcchara with easeinleft:
        xalign 0.1 yalign 1.1
    npc "{cps=30}День
добрый,вы к кому{/cps}"
    e "{cps=30}Я к лучшим разработчикам{/cps}"
    npc "{cps=30}Тогда вам точно сюда,мне они очень помогли и вам помогут{/cps}"
    npc "{cps=30}Начальник компании просил подняться в
кабинет{/cps}"
    hide frontg with moveoutright
    hide npcchara with moveoutleft
    scene bg mainoffice
    show frontg with easeinright:
        xalign 0.9 yalign 1.1
    show neutral with easeinleft:
        xalign -0.1 yalign 1.1
    will "{cps=30}Ты уже знаешь,к какому наставнику ты пойдешь обучаться?{/cps}"
    e "{cps=30}Да, я кажется выбрал,это будет тот молодой человек в серой футболке, 
        с которым я встретился по пути к вам{/cps}"
    will "{cps=30}Отлично,тогда приступайте{/cps}"
    "{cps=30}Он отправился к нему,чтобы изучить всё с начала и попробовать создать на
практике приложение{/cps}"
    hide frontg with moveoutright
    hide neutral with moveoutleft
    show bg inoffice
    show frontg with easeinright:
        xalign 0.9 yalign 1.1
    show npcchara with easeinleft:
        xalign 0.1 yalign 1.1
    "{cps=30}[charactername] начинает учиться у опытного разработчика компании Эверест{/cps}"
    "{cps=30}Разработчик объясняет ему основной синтаксис и принципы программирования на Javascript{/cps}"
    scene black with off
    pause 1.0
    scene bg day with onn
    "{cps=30}[charactername] в итоге создает свой проект на Javascript{/cps}"
    "{cps=30}Благодаря помощи опытного разработчика, он стал хорошим разработчиком, и
теперь сможет создавать интересные проекты на Javascript{/cps}"
    scene bg night
    show egor
    "{cps=30}Конец{/cps}"
    play music end
    jump creditz
    return


# 2 развилка событий с незнакомцем

# Герой отказывается попросить помощи у компании
label help_refuse:
    play music musnormal
    "{cps=30}Главный герой, взвесив свои возможности, решает продолжить изучение JavaScript
    самостоятельно и не обращаться в компанию Эверест{/cps}"
    hide egor with moveoutright
    scene bg night
    scene black with off
    pause 1.0
    scene bg day with onn
    show frontg
    "{cps=30}Он в течение нескольких дней пытается разобраться в JavaScript самостоятельно{/cps}"
    "{cps=30}Но,
несмотря на упорные попытки его прогресс замедляется, и он теряет веру в свои
способности.{/cps}"
    "{cps=30}Его игровой проект оказывается сложным в реализации, и он чувствует,
что он застрял{/cps}"
    "{cps=30}В итоге [charactername] разочаровался и потерял веру в свои способности разработчика{/cps}"
    "{cps=30}Конец{/cps}"
    play music end
    jump creditz
    return