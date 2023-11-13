# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('[charactername]', color="#c8ffc8")


#музыка и звуки
define audio.musnormal = "audio/gametheme.ogg"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
init python:
    onn = ImageDissolve("eye.png", 2.0, 50, reverse=False) 
    off = ImageDissolve("eye.png", 2.0, 50, reverse=True) 

label start:

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
    scene black with off
    pause 1.0
    scene bg day with onn
    show nosleep1:
        xalign -0.1 yalign 1.6
    e "А почему бы не создать такое приложение"
    hide nosleep1
    show egor
    e "Буду изучать JavaScript и другие языки программирования,чтобы воплотить свое желание в реальность"
        
    return
