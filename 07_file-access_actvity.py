file=open("devices.txt","a")
print("ВНИМАНИЕ: Введите 'exit' или 'выход' для выхода" + "\n")
while True:
    newitem=input("Введите новое устройство(-а): ")
    if newitem == 'exit' or newitem == 'выход':
        print("Работа выполнена! До свидания!")
        break
    file.write(newitem + "\n")

file.close()

