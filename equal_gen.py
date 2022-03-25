import math
import random

class Equal():

    def Diff(dif):

        dif_array = []

        if dif == "easy":
            a_edge = random.randint(1, 4)
            b_edge = random.randint(2, 10)
            c_edge = random.randint(2, 10)
            dif_array.append(a_edge)
            dif_array.append(b_edge)
            dif_array.append(c_edge)
            return dif_array
        if dif == "medium":
            a_edge = random.randint(2, 6)
            b_edge = random.randint(4, 15)
            c_edge = random.randint(4, 15)
            dif_array.append(a_edge)
            dif_array.append(b_edge)
            dif_array.append(c_edge)
            return dif_array
        if dif == "hard":
            a_edge = random.randint(3, 12)
            b_edge = random.randint(5, 20)
            c_edge = random.randint(6, 20)
            dif_array.append(a_edge)
            dif_array.append(b_edge)
            dif_array.append(c_edge)
            return dif_array
    def Stringing(a, a_p, b, b_p, c, c_p):
        num_ps = [a_p, b_p, c_p]
        nums = [str(a), str(b), str(c)]
        nums2 = [str(a), str(b), str(c)]
        index = 0
        index2 = 0
        ks = ""
        for num_p in num_ps:
            if num_p == False:
                nums[index] = "- " + nums[index]

            if index == 0 and num_p == True:
                nums[index] = "" + nums[index]

            if num_p == True and index != 0:
                nums[index] = "+ " + nums[index]

            index += 1
        for num_p2 in num_ps:
            if num_p2 == False:
                ks += "-" + nums2[index2]
            if num_p2 == True:
                ks += "" + nums2[index2]
            if index2 == 0:
                ks += ";"
            if index2 == 1:
                ks += ","
            index2 += 1


        res = nums[0] + "x² " + nums[1] +  "x " + nums[2] + " = 0"

        return res, ks
    def Solve(string):
        input = string
        edges = []
        for i in input:
            if i == ";":
                edges.append(input.index(";"))
            if i == ",":
                edges.append(input.index(","))
        a = float(input[0: edges[0]])
        b = float(input[edges[0] + 1: edges[1]])
        c = float(input[edges[1] + 1:])


        D = (b * b) - (4 * a * c)
        if D < 0:
            return "Нет корней"
        if D == 0:
            result1 = (-b) / (2 * a)
            return "Дискриминант равен: " + str(D) + "\nЕдинственный корень равен" + str(result1) + "\n" + str(
                (-b)) + " +- " + "√" + str(D) + " \n-------------\n" + str(2 * a)
        first_x = (-b - math.sqrt(D)) / (2 * a)
        second_x = (-b + math.sqrt(D)) / (2 * a)
        result = "Первый корень равен: " + str(first_x) + "\nВторой корень равен: " + str(second_x)
        result2 = str((-b)) + " +- " + "√" + str(D) + " \n-------------\n " + str(2 * a)
        fin_res = "Дискриминант равен: " + str(D) + "\n" + result + "\n" + result2;
        return fin_res;

    def Generate(difficulty):

        egdes = Equal.Diff(difficulty)

        num_a_pointer = bool(random.randint(0, 1))
        num_a = int(random.randint(1, egdes[0]))

        num_b_pointer = bool(random.randint(0, 1))
        num_b = int(random.randint(1, egdes[1]))

        num_c_pointer = bool(random.randint(0, 1))
        num_c = int(random.randint(1, egdes[2]))

        if num_c_pointer == num_a_pointer:
            if ((num_b*num_b) - (4 * num_a * num_c)) < 0:
                Equal.Generate(difficulty)
        res, constructed = Equal.Stringing(num_a, num_a_pointer, num_b, num_b_pointer, num_c, num_c_pointer)

        fin_res = res + "\n.\nСнизу ответы\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n" + Equal.Solve(constructed)
        return fin_res

