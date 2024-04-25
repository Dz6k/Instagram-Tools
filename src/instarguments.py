"""Just some arguments of bot"""
from selenium.webdriver.edge.options import Options


class WDArguments:
    """WebDriverArguments
    
    presets of arguments to selenium webdriver
    """
    DisableNotifications = "--disabe-notifications"  # disable notifications
    Headless = "--headless"  # show browser = False
    Anon = "--incognito"  # Incognito mode
    WindowSize = "--window-size=900,900"  # size of window's browser
    OffOutput = "--log-level=3"  # don't show the log output
    EnglishLang = "--lang=en"  # don't change!
    DisableExtensions = "--disable-extensions"  # disable extensions
    DisablePopUp = "--disable-popup-blocking"  # disable pop up
    WindowFScreen = "--start-maximized"  # start full screen
    # start with a guest(without microsoft account vinculation)
    Guest = "--guest"
    # -------------------------------------------- #
    # FOR MASSIVE REPETITIONS, USE "self.options.add_argument(self.Headless" TO CODE RUN IN BACKGROUND

    def __init__(self) -> None:
        self.options = Options()
        self.options.add_argument(self.DisableNotifications)
        self.options.add_argument(self.WindowSize)
        self.options.add_argument(self.Anon)
        # self.options.add_argument(self.Headless)
        self.options.add_argument(self.OffOutput)
        self.options.add_argument(self.DisableExtensions)
        self.options.add_argument(self.DisablePopUp)
        self.options.add_argument(self.EnglishLang)
        self.options.add_argument(self.Guest)
        self.options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        # self.driver = webdriver.Edge(options=self.options)


if __name__ == "__main__":
    print('What are you doing here?')
    # -------------------------------------------- #
