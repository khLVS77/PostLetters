#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import easygui
import MarksCourt
import datetime

JFile = "Setup.json"
now_time = datetime.datetime.now()

ReportFile = "Report.txt"

'''
Вартість літерових марок
'''
MarksCost = {
    "F": 13,
    "M": 10.5,
    "X": 10,
    "V": 7,
    "T": 2,
    "H": 0.5,
}


'''
Ініціалізація кільковті марок, що треба наклеїти на лист
'''
MarksOut = {
    "F": 0,
    "M": 0,
    "X": 0,
    "V": 0,
    "T": 0,
    "H": 0,
}


def Cost(cost):
    '''
    Вираховує вартість простого листа, в залежності від його ваги (cost)
    '''
    if cost <= 50:
        n = 7
    if 51 < cost <= 250:
        n = 10.50
    if 251 < cost <= 1000:
        n = 21
    return n


def Letters():
    '''
    Функція обробки листів
    '''
    try:
        with open(JFile) as set_obj:
            Court = json.load(set_obj)
    except:
        MarksCourt.InpMarksKol()

    while True:
        Adresat = easygui.enterbox("Вкажіть адресата:")
        Ves = int(easygui.enterbox("{}\nВведіть вагу [г] \n(для завершення, введіть 0)".format(Adresat)))
        if Ves == 0:
            break
        Vud = easygui.buttonbox("Вкажіть вид листа...", "Вид листа...", ["Простий", "Рекомендоване З повідомленням", "Рекомендоване БЕЗ повідомлення"])
        for key in MarksOut.keys():
            MarksOut[key] = 0
        if Vud == "Рекомендоване БЕЗ повідомлення":
            Num = Cost(Ves) + 6
        elif Vud == "Рекомендоване З повідомленням":
            Num = Cost(Ves) + 16
        else:
            Num = Cost(Ves)
        Num1 = Num
        for key in Court.keys():
            while Court[key] > 0:
                if Num - MarksCost[key] >= 0:
                    Num = Num - MarksCost[key]
                    MarksOut[key] += 1
                    Court[key] -= 1
                else:
                    break
        Rez = ""
        Rez2 = ""
        for key, val in MarksOut.items():
            if val > 0:
                Rez = Rez + u"{} - {} шт.\n".format(key, str(val))
                Rez2 = Rez2 + u"{} - {} шт.; ".format(key, str(val))
        MF = open(ReportFile, "a")
        print("{}\t".format(str(now_time.strftime("%d.%m.%Y")))+"{:35}".format(Adresat[:30])+" ({:3} г.)".format(str(Ves))+"\t"+str(Rez2), file=MF) # python 3.0 друкувати не на екран, а  в файл MF
        MF.close()
        R = MarksOut["X"]*MarksCost["X"]+MarksOut["V"]*MarksCost["V"]+MarksOut["T"]*MarksCost["T"]+MarksOut["M"]*MarksCost["M"]+MarksOut["H"]*MarksCost["H"]+MarksOut["F"]*MarksCost["F"]
        Rez = Rez + "-" * 10 + "\nВартість: {} грн.\nРезультат: {} грн.".format(str(Num1), str(R))
        easygui.msgbox(Rez, "Результат...")
    with open(JFile, 'w') as f_obj:
        json.dump(Court, f_obj)
    return 0
