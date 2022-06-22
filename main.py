import re
import sys

class ActionOne:
    def __init__(self, name, addition): #constructor
        # self.data_array = data_array
        self.name = name #Имя файла котррый мы откроем в методе adding
        self.addition = addition # новая запись
    #Основная часть где мы добавляем запись введеный  пользователем
    def adding(self):
        f = open(self.name, 'a+')
        f.seek(0)
        # If file is not empty then append '\n'
        data5 = f.read(100)
        if len(data5) > 0:
            f.write("\n")
        # Append text at the end of file
        f.write(self.addition)
        f.close()


class ActionTwo:
    def __init__(self, name, change, data_array): #constructor
        self.data_array = data_array
        self.name = name
        self.change = change

    def changing(self):
        f = open(self.name, "w")
        # f.seek(0)
        temp_data = []
        for i in range(len(self.data_array)):
            s = self.data_array[i]
            #разделяю стринг по " - " чтобы отделить нименование и числа чтоб позже сравнивать наименование с записью который хотим изменить
            temp_name = s.split(" - ")
            if len(s) > 0:
                #если в списке нашелся продукт который мы хотим удалить то мы просто пропускаем его а если не совпало то пишем наименование и число обратно в наш файл
                if temp_name[0].lower() == self.change.lower():
                    nomination = input("Введите новое наименование: ")
                    value = input("Введите новое значение наименования: ")
                    f.write(nomination + " - " + value + "\n")
                else:
                    f.write(temp_name[0] + " - " + temp_name[1] + "\n")
        f.close()


class ActionThree:
    def __init__(self, name, deletion, data_array): #constructor
        self.data_array = data_array
        self.name = name
        self.deletion = deletion

    def deleting(self):
        f = open(self.name, "w")
        # f.seek(0)
        temp_data = []
        for i in range(len(self.data_array)):
            s = self.data_array[i]
            #разделяю стринг по " - " чтобы отделить нименование и числа чтоб позже сравнивать наименование с записью который хотим удалить
            temp_name = s.split(" - ")
            # print(temp_name[0].lower())
            # print(temp_name[1])
            # temp_data.append(temp_name[0])
            if len(s) > 0:
                #если в списке нашелся продукт который мы хотим удалить то мы просто пропускаем его а если не совпало то пишем наименование и число обратно в наш файл
                if temp_name[0].lower() != self.deletion.lower():
                    f.write(temp_name[0] + " - " + temp_name[1] + "\n")


            # print(temp_name)
        # print(temp_data)
        f.close()

class ActionFour:
    def __init__(self, data_array):
        self.data_array = data_array
        # self.init_file = init_file

    def calculate_sum(self):
        #Лист data хрнит в себе и текст и цыфры записей. Тут с помощью модуля regular expression и паттерна который будет искать все числа в тексте и после того как мы извлекли цыфры я добавляю их в новый лист в котором только int
        temp_int = []
        pattern = "[0-9]+.?[0-9]*"
        print(*data, sep="\n")
        for i in range(len(self.data_array)):
            sample = self.data_array[i]
            temp_int.append(int(re.findall(pattern, sample)[0])) #Находим все цифры в тексте из data[0], data[1], data[2].......... После cast to int and append to new list
        #суммирую все цифры в листе и return
        return sum(temp_int)


#A list which will store the data from file
data = []

#Getting filename and the action number from command line arguments
file_name = sys.argv[1]
action = sys.argv[2];

with open(file_name, 'r+') as file:
    data = [line.strip() for line in file] #take all data from opened file


#if user enter 1 in command line argument then we perform action "Добавить в список/Add to list"
if int(action) == 1:
#Ask user to enter what he want yo add to the list
    add = input("1 Добавить в список: ")
    execute = ActionOne(file_name, add)
    execute.adding()
    print(add, " - Добавлен в список.")
    # print(data)
    # data.append(add)





if int(action) == 2:
    print("2 Изменить запись в списке")
    if len(data) == 0:
        print("Список Пуст")

    else:
        to_change = input("Введите Наименование записи которую вы хотите изменить(Например:Огурцы): ")
        execute = ActionTwo(file_name, to_change, data)
        execute.changing()
        print("Запись успешно изменена")







#done
if int(action) == 3:
    print("3 Удалить из списка")
    if len(data) == 0:
        print("Список Пуст")

    else:
        to_delete = input("Введите позицию которую хотите удалить (Например: Огурцы) :")
        execute = ActionThree(file_name, to_delete, data)
        execute.deleting()
        print("Удалено!")

#done
if int(action) == 4:
    print("4 Вычесть общую сумму:")
    #Список пустой
    if len(data) == 0:
        print("Список Пуст")
    # Передаем лист со всеми записями в класс ActionFour
    else:
        execute = ActionFour(data)
        print("Сумма = ", execute.calculate_sum())