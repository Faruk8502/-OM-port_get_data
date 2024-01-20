import serial.tools.list_ports
from tkinter import *
from tkinter import ttk


def update_ports():
    # Обновление списка подключенных COM-портов
    ports = serial.tools.list_ports.comports()
    com_ports = [port.device for port in ports]

    # Обновление элемента "выпадающий список"
    com_port_dropdown['values'] = com_ports


def show_selected_port():
    global ser
    # Отображение выбранного COM-порта в поле вывода
    selected_port = com_port_dropdown.get()
    output_text.configure(state='normal')
    output_text.delete(1.0, END)
    output_text.insert(END, f"Выбран COM-порт: {selected_port}" + '\n')
    # output_text.configure(state='disabled')
    ser = serial.Serial(selected_port, 9600)
    show_data()


def show_data():
    # Прочитать данные с COM-порта
    data = ser.readline().decode().strip()
    print(data)
    # Вывести данные в поле вывода
    output_text.configure(state='normal')
    output_text.insert(END, data + '\n')
    output_text.see(END)  # Прокрутить поле вывода вниз
    if True:
        output_text.after(15000, show_data)

root = Tk()
root.title("COM-порт GUI")

# Создание кнопки для обновления списка COM-портов
update_button = Button(root, text="Обновить", command=update_ports)
update_button.pack()

# Создание выпадающего списка для выбора COM-порта
com_ports = serial.tools.list_ports.comports()
com_port_names = [port.device for port in com_ports]
com_port_dropdown = ttk.Combobox(root, values=com_port_names)
com_port_dropdown.pack()

# Создание поля вывода сообщений
output_text = Text(root, width=40, height=10)
output_text.pack()
# output_text.configure(state='disabled')

# Создание кнопки для отображения выбранного COM-порта
show_button = Button(root, text="Показать COM-порт", command=show_selected_port)
show_button.pack()

root.mainloop()