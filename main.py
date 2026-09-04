from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyApp(App):

  def build(self):
    layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

    self.label = Label(
        text='Salut! Aceasta este\nprima mea aplicație APK!',
        font_size=20,
        halign='center',
    )
    layout.add_widget(self.label)

    self.text_input = TextInput(
        text='',
        hint_text='Scrie ceva aici...',
        size_hint_y=None,
        height=50,
        font_size=16,
    )
    layout.add_widget(self.text_input)

    btn = Button(
        text='Apasă-mă!',
        size_hint_y=None,
        height=60,
        background_color=(0, 0.8, 0.6, 1),
    )
    btn.bind(on_press=self.la_apasare)
    layout.add_widget(btn)

    return layout

  def la_apasare(self, instance):
    text_introdus = self.text_input.text
    if text_introdus:
      self.label.text = f'Ai scris: {text_introdus}'
      self.text_input.text = ''
    else:
      self.label.text = 'Ai apăsat butonul fără text!'


if __name__ == '__main__':
  MyApp().run()