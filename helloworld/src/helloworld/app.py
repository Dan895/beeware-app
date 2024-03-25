"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import httpx


def gretting(name):
    """
        This is a utility method
    """
    if name:
        return f"Hello, {name}"
    else:
        return f"Hello, stranger"


class HelloWorld(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # This defines the input of the data with
        # a label and a input (both are relashionated)
        name_label = toga.Label(
            "Your name: ",
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        # This defines the box where I put the widgets
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        # This is the form I add a widget to the box created above
        name_box.add(name_label)
        name_box.add(self.name_input)

        # This create a button with an method to invoke
        # when this is pressed (on_press)
        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            style=Pack(padding=5)
        )
        # This adds the widgets that I created above,
        # input and the button, in the main_box element
        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    # This defines the method called when
    # the button is pressed
    def say_hello(self, widget):
        # print(f"Hello, {self.name_input.value}")

        # This add a dialog box to interact
        # with users
        # self.main_window.info_dialog(
        #     f"Hello, {self.name_input.value}",
        #     "Hi there!"
        # )

        # this add the greeting method, this was updated in tutorial 7
        # self.main_window.info_dialog(
        #     gretting(self.name_input.value),
        #     "Hi there!",
        # )

        with httpx.Client() as client:
            response = client.get(
                "https://jsonplaceholder.typicode.com/posts/42")

            payload = response.json()

            self.main_window.info_dialog(
                gretting(self.name_input.value),
                payload["body"],
            )


def main():
    return HelloWorld()
