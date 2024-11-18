import flet as ft

# Инициализация карты
maps = [1,2,3,
        4,5,6,
        7,8,9]

# Инициализация победных линий
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],  
             [0,4,8],
             [2,4,6]]

async def main(page: ft.Page):        #характеристики главного окна
    page.title = "APP2"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
#-----------------------------------------------------------------------------------------
    # Сделать ход в ячейку
    def step_maps(step,symbol):
        ind = maps.index(step)
        maps[ind] = symbol
 
    # Получить текущий результат игры
    def get_result():
        win = ""
    
        for i in victories:
            if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
                win = "X"
            if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
                win = "O"   
                
        return win
    
    #Искусственный интеллект: поиск линии с нужным количеством X и O на победных линиях
    def check_line(sum_O,sum_X):
    
        step = ""
        for line in victories:
            o = 0
            x = 0
    
            for j in range(0,3):
                if maps[line[j]] == "O":
                    o = o + 1
                if maps[line[j]] == "X":
                    x = x + 1
    
            if o == sum_O and x == sum_X:
                for j in range(0,3):
                    if maps[line[j]] != "O" and maps[line[j]] != "X":
                        step = maps[line[j]]
                    
        return step
    
    #Искусственный интеллект: выбор хода
    def AI():        
    
        step = ""
    
        # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
        step = check_line(2,0)
    
        # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
        if step == "":
            step = check_line(0,2)        
    
        # 3) если 1 фигура своя и 0 чужих - ставим
        if step == "":
            step = check_line(1,0)           
    
        # 4) центр пуст, то занимаем центр
        if step == "":
            if maps[4] != "X" and maps[4] != "O":
                step = 5           
    
        # 5) если центр занят, то занимаем первую ячейку
        if step == "":
            if maps[0] != "X" and maps[0] != "O":
                step = 1           
    
        return step
#-----------------------------------------------------------------------------------------
    async def img_1(event: ft.ContainerTapEvent):
        image_start1.src = 'cat_hm.png'
        maps[0] = 'X'
        await page.update_async()

    async def img_2(event: ft.ContainerTapEvent):
        image_start2.src = 'cat_hm.png'
        maps[1] = 'X'
        await page.update_async()
    
    async def img_3(event: ft.ContainerTapEvent):
        image_start3.src = 'cat_hm.png'
        maps[2] = 'X'
        await page.update_async()
    
    async def img_4(event: ft.ContainerTapEvent):
        image_start4.src = 'cat_hm.png'
        maps[3] = 'X'
        await page.update_async()
    
    async def img_5(event: ft.ContainerTapEvent):
        image_start5.src = 'cat_hm.png'
        maps[4] = 'X'
        await page.update_async()
    
    async def img_6(event: ft.ContainerTapEvent):
        image_start6.src = 'cat_hm.png'
        maps[5] = 'X'
        await page.update_async()
    
    async def img_7(event: ft.ContainerTapEvent):
        image_start7.src = 'cat_hm.png'
        maps[6] = 'X'
        await page.update_async()
    
    async def img_8(event: ft.ContainerTapEvent):
        image_start8.src = 'cat_hm.png'
        maps[7] = 'X'
        await page.update_async()
    
    async def img_9(event: ft.ContainerTapEvent):
        image_start9.src = 'cat_hm.png'
        maps[8] = 'X'
        await page.update_async()

    image_start1 = ft.Image(src = 'clc.png')
    image_start2 = ft.Image(src = 'clc.png')
    image_start3 = ft.Image(src = 'clc.png')
    image_start4 = ft.Image(src = 'clc.png')
    image_start5 = ft.Image(src = 'clc.png')
    image_start6 = ft.Image(src = 'clc.png')
    image_start7 = ft.Image(src = 'clc.png')
    image_start8 = ft.Image(src = 'clc.png')
    image_start9 = ft.Image(src = 'clc.png')


#---------------------------------------------------------------------------------------------------
    async def field(e):

        start_button.visible = False

        pos1 = ft.Container(content=image_start1, width=50, height=50, bgcolor="#FF00FF", on_click=img_1)
        pos2 = ft.Container(content=image_start2, width=50, height=50, bgcolor="#FF00FF", on_click=img_2)
        pos3 = ft.Container(content=image_start3, width=50, height=50, bgcolor="#FF00FF", on_click=img_3)
        pos4 = ft.Container(content=image_start4, width=50, height=50, bgcolor="#FF00FF", on_click=img_4)
        pos5 = ft.Container(content=image_start5, width=50, height=50, bgcolor="#FF11FF", on_click=img_5)
        pos6 = ft.Container(content=image_start6, width=50, height=50, bgcolor="#FF00FF", on_click=img_6)
        pos7 = ft.Container(content=image_start7, width=50, height=50, bgcolor="#FF00FF", on_click=img_7)
        pos8 = ft.Container(content=image_start8, width=50, height=50, bgcolor="#FF00FF", on_click=img_8)
        pos9 = ft.Container(content=image_start9, width=50, height=50, bgcolor="#FF00FF", on_click=img_9)

        await page.update_async()

        await page.add_async(
            ft.Row(
                [
                     pos1, pos2, pos3               
                ], alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                      pos4, pos5, pos6              
                ], alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                      pos7, pos8, pos9              
                ], alignment=ft.MainAxisAlignment.CENTER
            )
        )

#-----------------------------------------------------------------------------------------
        # Основная программа
        game_over = False
        human = True
        
        while game_over == False:
        
            # 1. Показываем карту
            #print_maps()
        
            # 2. Спросим у играющего куда делать ход
            if human == True:
                symbol = "X"
                #step = int(input("Человек, ваш ход: "))
            else:
                print("Компьютер делает ход: ")
                symbol = "O"
                step = AI()
        
            # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
            if step != "":
                step_maps(step,symbol) # делаем ход в указанную ячейку
                win = get_result() # определим победителя
                if win != "":
                    game_over = True
                else:
                    game_over = False
            else:
                print("Ничья!")
                game_over = True
                win = "дружба"
        
            human = not(human)        
        
        # Игра окончена. Покажем карту. Объявим победителя.        
        #print_maps()
        #print("Победил", win)           

#-----------------------------------------------------------------------------------------


    start_button = ft.TextButton('НАЧАТЬ', on_click=field)

    await page.add_async(
        ft.Row(
            [
                start_button                
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )



#-----------------------------------------------------------------------------------------    
    

if __name__ == "__main__":    
    ft.app(target=main, view=ft.WEB_BROWSER)
    #ft.app(target=main)