import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SimpleApp(App):

    def build(self):
        # Create a layout
        layout = BoxLayout(orientation='vertical')

        # Create a label
        self.label = Label(text="Hello, Kivy!")

        # Create a button
        button = Button(text="Click Me!")
        button.bind(on_press=self.on_button_click)

        # Add the label and button to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        # Change the label text when the button is clicked
        self.label.text = "Button Clicked!"

if __name__ == "__main__":
    SimpleApp().run()