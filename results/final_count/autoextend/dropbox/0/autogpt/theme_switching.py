class ThemeSwitching:
    def __init__(self):
        self.theme = 'light'

    def switch_theme(self):
        if self.theme == 'light':
            self.theme = 'dark'
        else:
            self.theme = 'light'


if __name__ == '__main__':
    theme_switching = ThemeSwitching()
    theme_switching.switch_theme()
    print(f'Theme switched to {theme_switching.theme}.')