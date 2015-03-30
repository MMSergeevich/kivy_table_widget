#!/usr/bin/python3

# Example module
# Copyright (C) 2015 Kato Masaya <masaya@w32.jp>

from kivy.config import Config

Config.set("input", "mouse", "mouse, disable_multitouch")
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from table import Table


class TestScreen(BoxLayout):
    def __init__(self):
        super(TestScreen, self).__init__()

        self.orientation = 'vertical'

        self.table = Table()
        self.table.cols = 2

        self.controls = BoxLayout()
        self.controls.size_hint_y = 0.1
        del_button = Button(text="Remove")
        del_button.bind(on_press=self.del_on_press)
        insert_button = Button(text="Insert")
        insert_button.bind(on_press=self.insert_on_press)
        refresh_button = Button(text="Refresh")
        refresh_button.bind(on_press=self.refresh_on_press)
        self.controls.add_widget(del_button)
        self.controls.add_widget(insert_button)
        self.controls.add_widget(refresh_button)

        self.add_widget(self.table)
        self.add_widget(self.controls)

        self.table_initialize()

    def table_initialize(self):
        self.table.label_panel.labels[1].text = 'X'
        self.table.label_panel.labels[2].text = 'Y'
        for i in range(1, 11):
            self._add_row(str(i), str(i) + 'Y')

    def _rows(self):
        rows = []
        for i in range(self.table.row_count):
            rows.append((self.table.grid.cells[i][0].text, self.table.grid.cells[i][1].text))
        return rows

    def _add_row(self, x, y):
        self.table.add_row(
            [
                TextInput,
                {
                    'text': x,
                },
            ],
            [
                TextInput,
                {
                    'text': y,
                },
            ]
            )

    def _refresh(self, rows):
        for i in range(self.table.row_count):
            self.table.del_row(0)
        for row in rows:
            self._add_row(row[0], row[1])

    def del_on_press(self, instance=None, value=None):
        remove_row = self.table.chosen_row
        self.table.del_row(remove_row)

    def insert_on_press(self, instance=None, value=None):
        print(self.table.chosen_row)
        insert_row = self.table.chosen_row
        rows = self._rows()
        rows.insert(insert_row, ('',''))
        self._refresh(rows)
        self.table.choose_row(insert_row)

    def refresh_on_press(self, instance=None, value=None):
        rows = self._rows()
        self._refresh(rows)



class TestApp(App):
    """ App class """

    def build(self):
        return TestScreen()

    def on_pause(self):
        return True


if __name__ in ('__main__', '__android__'):
    TestApp().run()
