print('Введите delta')
delta = int(input())
print('Введите n')
n = int(input())
a = [0]*n
for i in range(n):
    print('Введите (элементы массива) a[', i, ']', sep='')
    a[i]= int(input()) #вводим элементы массива

xmin=a[0]
i= 1
for i in range(n):
        if a[i]<xmin:
            xmin=a[i] #ищем минимальный элемент в массиве
print('Минимальное значение', xmin) 

j=0 #для подсчета количесва элементов которые удовлетв условию задачи
i=0 
xdelta1 = xmin + delta #искомое число
print('Искомое число', xdelta1)
for i in range(n): #ищем количество
    if a[i]== xdelta1:
        j = j+1

print('Количество элементов большее delta=', delta, ' при минимальном значении массива ', xmin, ' равно ', j)