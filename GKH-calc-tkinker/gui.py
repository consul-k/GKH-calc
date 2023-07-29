
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("982x493")
window.configure(bg = "#B21F1F")

def calc():
        ''' Заполняет облость данными о расчетах '''
        # получить данные из GUI
        oldhot = int(entry_1.get())
        newhot = int(entry_2.get())
        oldcold = int(entry_3.get())
        newcold = int(entry_4.get())
        oldelectro = int(entry_5.get())
        newelectro = int(entry_6.get())
        day = str(entry_7.get())
        #данные о расходе
        data = {' Расход горячей воды':0,
                ' Расход холодной воды':0,
                ' Расход водоотвода':0,
                ' Расход электроэнергии':0}
        # расход горячей воды
        out_hot_water = newhot - oldhot
        data[' Расход горячей воды'] = out_hot_water
        # расход холодной воды
        out_cold_water = newcold - oldcold
        data[' Расход холодной воды'] = out_cold_water
        # расход электроэнергии
        out_electro = oldelectro - newelectro
        data[' Расход электроэнергии'] = out_electro
        # расход водоотвода
        drinage = out_hot_water + out_cold_water
        data[' Расход водоотвода'] = drinage

        #данные о тарифах
        data_tariffs = {' ГВС':243.16,
                        ' ХВС':50.93,
                        ' Водоотвод':39.97,
                        ' Электроэнергия':6.43}

        #данные о долгах
        data_debt = {' Сумма долга за горячую воду':0,
                     ' Сумма долга за холодную воду':0,
                     ' Сумма долга за воотвод':0,
                     ' Сумма долга за электроэнергию':0,
                     ' Итого задолженность':0}

        #сумма долга за горячую воду
        debt_hot = round(out_hot_water * 243.16)
        data_debt[' Сумма долга за горячую воду'] = debt_hot
        #сумма долга за холодную воду
        debt_cold = round(out_cold_water * 50.93)
        data_debt[' Сумма долга за холодную воду'] = debt_cold
        #сумма долга за электроэнергию
        debt_electro = round(out_electro * 6.43)
        data_debt[' Сумма долга за электроэнергию'] = debt_electro
        #сумма долга за водоотвод 
        debt_drinage = round(drinage * 39.97)
        data_debt[' Сумма долга за воотвод'] = debt_drinage
        #итоговая сумма долга
        debt_all = debt_hot + debt_cold + debt_electro + debt_drinage
        data_debt[' Итого задолженность'] = debt_all

    
        # вывод на экран
        entry_8.delete(0.0, END)
        copy_txt = ''
        show_result = ''
        show_debt = ''
        show_tariffs = ''
        day = ' Дата: ' + day
        line = ' ------------------------------------------'
        for category in data:
            if category != ' Расход электроэнергии':
                show_result += category +': '+str(data[category])+' куб.'+'\n'
            else:
                show_result += category +': '+str(data[category])+' квт.'+'\n'
        for category in data_debt:
            show_debt += category +': '+str(data_debt[category])+' р.'+'\n'
        for category in data_tariffs:
            show_tariffs += category +': '+str(data_tariffs[category])+' р.'+'\n'

        entry_8.insert(END, '\n')
        entry_8.insert(END, show_result)
        entry_8.insert(END, line+'\n')
        entry_8.insert(END, show_debt)
        entry_8.insert(END, line+'\n')
        entry_8.insert(END, ' Расчет выполнен по тарифам: '+'\n')
        entry_8.insert(END, show_tariffs)
        entry_8.insert(END, line+'\n')
        entry_8.insert(END, day)

        #сохранение в буфер обмена
        copy_txt = entry_8.get(0.0, END)
        window.clipboard_clear()
        window.clipboard_append(copy_txt)
        
    

canvas = Canvas(
    window,
    bg = "#B21F1F",
    height = 493,
    width = 982,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    230.0,
    33.0,
    anchor="nw",
    text="ПРОГРАММА ДЛЯ РАСЧЕТА ЖКХ",
    fill="#FFFFFF",
    font=("Inter Bold", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    490.5,
    98.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=475.0,
    y=81.0,
    width=31.0,
    height=32.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    490.5,
    142.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=475.0,
    y=125.0,
    width=31.0,
    height=32.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    490.5,
    190.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=475.0,
    y=173.0,
    width=31.0,
    height=32.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    490.5,
    236.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=475.0,
    y=219.0,
    width=31.0,
    height=32.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    490.5,
    282.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=475.0,
    y=265.0,
    width=31.0,
    height=32.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    490.5,
    328.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=475.0,
    y=311.0,
    width=31.0,
    height=32.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    468.5,
    379.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=431.0,
    y=362.0,
    width=75.0,
    height=32.0
)

canvas.create_text(
    23.0,
    89.0,
    anchor="nw",
    text="Старые показания счетчика по ГОРЯЧЕЙ воде",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    23.0,
    133.0,
    anchor="nw",
    text="Новые показания счетчика по ГОРЯЧЕЙ воде",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    23.0,
    181.0,
    anchor="nw",
    text="Старые показания счетчика по ХОЛОДНОЙ воде",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    23.0,
    227.0,
    anchor="nw",
    text="Новые показания счетчика по ХОЛОДНОЙ воде",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    23.0,
    273.0,
    anchor="nw",
    text="Старые показания ЭЛЕКТРОЭНЕРГИИ",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    23.0,
    319.0,
    anchor="nw",
    text="Новые показания ЭЛЕКТРОЭНЕРГИИ",
    fill="#FFFFFF",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    324.0,
    370.0,
    anchor="nw",
    text="Дата",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)


entry_8 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
)
entry_8.place(
    x=574.0,
    y=81.0,
    width=360.0,
    height=378.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: calc(),
    relief="flat"
)
button_1.place(
    x=146.0,
    y=413.0,
    width=249.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()
