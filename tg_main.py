# -*- coding: utf8 -*-
import telebot
from telebot import types
import math
from physics import temperature, electricity, weight, s_values

class Discr():
    def GetDis(a, b ,c):
        D = (b * b) - (4 * a * c)
        if D < 0:
            return "Нет корней"
        if D == 0:
            result1 = (-b) / (2*a)
            return "Дискриминант равен: " + str(D) + "\nЕдинственный корень равен" + str(result1) + "\n" + str((-b)) + " +- " + "√" + str(D) + " \n-------------\n" + str(2 * a)
        first_x = (-b - math.sqrt(D)) / (2*a)
        second_x = (-b + math.sqrt(D)) / (2*a)
        result = "Первый корень равен: " + str(first_x) + "\nВторой корень равен: " + str(second_x)
        result2 = str((-b)) + " +- " + "√" + str(D) + " \n-------------\n " + str(2 * a)
        fin_res = "Дискриминант равен: " + str(D) + "\n" +result + "\n" + result2;
        return fin_res;

# put your token in the string
bot = telebot.TeleBot("enter your token here")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет, это бот для физики/алгебры!\n1)Напиши discr и 3 коэфицента уравнения рядом, ставь знаки между числами как в примере: (discr -3;2.0,7), чтобы найти дискриминант\n2)Напиши physics.el для получение формул об электричестве\n3)Напиши physics.temp для получение формул о температуре\n2)Напиши physics.weight для получение формул о весе, силе и давлении\n2)Напиши geom.square для получение формул о площадях фигур")
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.chat.type == 'private':

        if "physics.el" in message.text.lower():
            result = ""
            for i in electricity:
                result += i
            bot.send_message(message.chat.id, result)
        elif "physics.temp" in message.text.lower():
            result = ""
            for i in temperature:
                result += i
            bot.send_message(message.chat.id, result)
        elif "physics.weight" in message.text.lower():
            result = ""
            for i in weight:
                result += i
            bot.send_message(message.chat.id, result)
        elif "geom.square" in message.text.lower():
            result = ""
            for i in s_values:
                result += i
            bot.send_message(message.chat.id, result)
        elif "discr" in message.text.lower():
            statement_error = False
            try:
                input = message.text.lower()[6:]
                edges = []
                for i in input:
                    if i ==";":
                        edges.append(input.index(";"))
                    if i ==",":
                        edges.append(input.index(","))
                a_k = input[0: edges[0]]
                b_k = input[edges[0]+1: edges[1]]
                c_k = input[edges[1]+1:]
            except:
                bot.send_message(message.chat.id, "Что то пошло не так...")
                statement_error = True
            if statement_error == False:
                try:
                    bot.send_message(message.chat.id, Discr.GetDis(float(a_k), float(b_k), float(c_k)))
                except:
                    bot.send_message(message.chat.id, "Что то пошло не так...")
        else:
            bot.send_message(message.chat.id, "/start")
bot.polling(none_stop = True)