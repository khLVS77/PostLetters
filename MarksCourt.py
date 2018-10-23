#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 00:54:55 2018

@author: viktor
"""
import datetime
import json
import webbrowser
import easygui
import t2

JFile = "Setup.json"


def InpMarksKol():
    '''
    Ініціалізація кількості наявних марок
    '''
    Court = {
        "F": 0,
        "M": 0,
        "X": 0,
        "V": 0,
        "T": 0,
        "H": 0,
    }

    for key in Court.keys():
        Kol = int(easygui.enterbox("Введіть наявну кількість марок квтегорії <{}>...".format(key)))
        Court[key] = Kol
    with open(JFile, 'w') as f_obj:
        json.dump(Court, f_obj)
    return 0


def ReportEnd():
    """
    Звіт по залишкам марок
    """
    Rez = ""
    with open(JFile) as set_obj:
        Court = json.load(set_obj)
    now_time = datetime.datetime.now()  # Текущая дата со временем
    for key, val in Court.items():
        Rez = Rez+"[{}] - {} шт.\n".format(key, str(val))
    easygui.msgbox("{}:\n\n{}".format(now_time.strftime("%d.%m.%Y %H:%M"), Rez), "Залишок марок станом на ...")
    return 0


def UkrPost():
    """
    Функція, що обробляє запит на роботу з сайтом Укрпошти
    """

    Variants2 = [
        "4.1. Головна сторіка сайту Укрпошти",
        "4.2. Розрахувати вартість листа",
        "4.3. Тарифи пересилки",
        "4.4. Пошук індексу",
        "4.5. Номінальна вартість літерних поштових марок",
        "4.6. Відстежити лист",
        "Закрити вікно",
        ]
    while True:
        choise1 = easygui.choicebox("-== УКРПОШТА ==-\n\nВаш вибір?", "Послуги Укрпошти Онлайн...", choices = Variants2)
        if choise1 == Variants2[0]:
            webbrowser.open("https://ukrposhta.ua")
        if choise1 == Variants2[1]:
            webbrowser.open("https://a.ukrposhta.ua/calc/s/calc.html")
        if choise1 == Variants2[2]:
            webbrowser.open("https://ukrposhta.ua/dovidka/tarifi/universalni-poslugi/")
        if choise1 == Variants2[3]:
            webbrowser.open("https://ukrposhta.ua/dovidka/indeksi/")
        if choise1 == Variants2[4]:
            webbrowser.open("https://ukrposhta.ua/dovidka/nominalna-vartist-liternix-poshtovix-marok/")
        if choise1 == Variants2[5]:
            webbrowser.open("https://ukrposhta.ua/vidslidkuvati-forma-poshuku")
        if choise1 == Variants2[-1]:
            break
    return 0


if __name__ == "__main__":
    Variants = [
        "1. Ініціалізація кількості марок",
        "2. Клеяти марки на листи",
        "3. Звіт по залишку марок",
        "4. Отримати інформацію з сайту Укрпошти [...]",
        "Вихід з програми",
        ]
    while True:
        choise = easygui.choicebox("*** ГОЛОВНЕ МЕНЮ ПРОГРАМИ ***\n\nВаш вибір?", "Адміністративне меню...", choices = Variants)
        if choise == Variants[0]:
            InpMarksKol()
        if choise == Variants[1]:
            t2.Letters()
        if choise == Variants[2]:
            ReportEnd()
        if choise == Variants[3]:
            UkrPost()
        if choise == Variants[-1]:
            break
