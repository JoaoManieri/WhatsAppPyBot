"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):

        self.browse("https://web.whatsapp.com/")

        try:
            if not self.find("belatrixNameClick", matching=0.97, waiting_time=25000):
                self.not_found("belatrixNameClick")
            self.click()

        except:
            if not self.find("BelatrixNameWhintMensageClick", matching=0.97, waiting_time=10000):
                self.not_found("BelatrixNameWhintMensageClick")
            self.click()

        if not self.find("MensageBoxClick", matching=0.97, waiting_time=10000):
            self.not_found("MensageBoxClick")
        self.click()

        # if not self.find("newMensageClick", matching=0.97, waiting_time=10000):
        #     self.not_found("newMensageClick")
        # self.click()



    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
