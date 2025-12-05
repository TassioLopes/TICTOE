import flet as ft
from screenManager import Navegation
from time import sleep
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 1366
    page.window.height = 768
    page.update()

    page.window.maximized = True
    page.update()
    navegation = Navegation(page)

    page.on_route_change = navegation.change_screen

    page.go('bemvindo')
    page.data = {"tipo_processo":''}

    page.update()
    sleep(1/120)
    bemvindo = 'xercícios Anteriores'
    for letra in bemvindo:
        page.views[-1].controls[-1].content.controls[-1].value += letra
        sleep(1/15)
        page.update()
    sleep(1 / 15)
    page.go('/')
    page.update()





if __name__ == '__main__':
    ft.app(main)
    #ft.app(target=main, view=ft.WEB_BROWSER, host="192.168.1.39", port=8000)
    #ft.app(target=main, view=ft.WEB_BROWSER, host="192.168.134.199", port=8000)
