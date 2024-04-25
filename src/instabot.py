from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as exp_conditions
from colorama import init, Fore, Style
from local_path import LocalPath
from time import sleep
from insta_errors import *
from instarguments import WDArguments
import random
import json
import os
import re


# auto reset for colorama
init(autoreset=True)

text = r'''
  ___           _                                                                             _
 |_ _|_ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___     ___ ___  _ __ ___  _ __ ___   ___ _ __ | |_ ___
  | || '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \   / __/ _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \| __/ __|
  | || | | \__ \ || (_| | (_| | | | (_| | | | | | | | (_| (_) | | | | | | | | | | |  __/ | | | |_\__ \
 |___|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|  \___\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__|___/
                         |___/

'''


# webdriver arguments
class TakeCookies(WDArguments):
    """
    Take your sesson cookies and followers
    
    OBS:
    all WebDriver arguments have already been predefined in WDArguments
    """

    def __init__(self):
        super().__init__()
        self.url_login = 'https://www.instagram.com/accounts/login/'
        self.url_profile = 'https://www.instagram.com{}following/'
        # -------------------------------------------- #

    def mycookies(self):
        self.driver = webdriver.Edge(options=self.options)
        # -------------------------------------------- #
        self.driver.get(self.url_login)
        # -------------------------------------------- #
        first_url = self.driver.current_url
        while True:
            new_url = self.driver.current_url
            if new_url != first_url:
                cookiesNew = self.driver.get_cookies()
                with open(LocalPath.cookies_path, 'w') as file:
                    json.dump(cookiesNew, file)

                self.driver.quit()
                os.system('cls')
                print(Fore.LIGHTGREEN_EX+'[Cookies saved]: ' +
                      Fore.LIGHTYELLOW_EX+f'{LocalPath.cookies_path}{os.linesep}')
                break
        # -------------------------------------------- #

    def myfollowers(self):

        self.driver = webdriver.Edge(options=self.options)
        self.wait = WebDriverWait(
            self.driver,
            7,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
            ]
        )
        # -------------------------------------------- #
        self.driver.get(self.url_login)

        with open(LocalPath.cookies_path, 'r') as file:
            cookies_data = json.load(file)
            for cookie in cookies_data:
                try:
                    self.driver.add_cookie(cookie)

                except AssertionError:
                    cookie["sameSite"] = "None"
                    self.driver.add_cookie(cookie)
        # -------------------------------------------- #
        self.driver.refresh()
        self.driver.implicitly_wait(20)

        try:
            cancel_popup = self.wait.until(exp_conditions.visibility_of_all_elements_located(
                (By.XPATH, "//button[text()='Cancel']")))
            cancel_popup[0].click()

        except:
            pass
        # -------------------------------------------- #
        self.driver.implicitly_wait(20)
        try:
            myuserhtml = self.driver.find_element(
                By.XPATH, '//*/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[6]/div/span/div/a').get_attribute('href')[25:]
        except:
            raise ExpiredCookiesError

        self.driver.get(self.url_profile.format(myuserhtml))
        # -------------------------------------------- #
        while True:
            self.driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
            sleep(random.uniform(2.3, 2.5))

            if self.driver.execute_script("return window.innerHeight + window.scrollY") >= self.driver.execute_script("return document.body.scrollHeight"):
                break
        # -------------------------------------------- #
        sleep(2)
        html_content = self.driver.page_source

        matches = re.findall(r'dir="auto">(?!Following)(.*?)<', html_content)
        matches_with_at = ['@' + match for match in matches]

        with open(LocalPath.followers_path, 'w') as f:
            json.dump(matches_with_at, f, ensure_ascii=False, indent=4)
        # -------------------------------------------- #
        with open(LocalPath.followers_path, 'r') as file:
            data = json.load(file)

        os.system('cls')
        print(f'We can find: {len(data)} followers!')
        self.driver.quit()
        # -------------------------------------------- #


class InstaBot(WDArguments):
    """Instagram Bot for auto-comments

        -> Please initialize before the TakeCookies class for take your followers and account cookies 
        
        This is a bot for do automatic comments to any instagram post
    """

    def __init__(self):
        # self.options = webdriver.EdgeOptions()
        super().__init__()

        init(autoreset=True)
        os.system('cls')
        print(Fore.MAGENTA+Style.BRIGHT+text)
        # -------------------------------------------- #
        self.url = input('URL: ')
        if not self.is_valid_url(self.url):
            raise InvalidFormatError
        os.system('cls')
        # -------------------------------------------- #

        # comments: str to comments: int
        try:
            self.comments = int(input('Numbers of comments: '))

        except ValueError:
            os.system('cls')
            print('Just int numbers! (1-9)')
            input('Press any key for continue')
            return InstaBot()

        # and verify if :param:comments > 0
        if self.comments > 0:
            pass
        elif self.comments == 0:
            raise InvalidZeroParamError
        os.system('cls')
        # -------------------------------------------- #
        # tags: str to tags: int
        try:
            self.tags = int(input('Number of tags per comment: '))
        except ValueError:
            os.system('cls')
            print('Just int numbers! (0-9)')
            input('Press any key for continue')
            return InstaBot()

        # verify :param:tags conditions

        if self.tags >= 0:
            pass
        os.system('cls')
        # -------------------------------------------- #

        # confirm inputs

        # -------------------------------------------- #
        while True:
            os.system('cls')
            print(Fore.CYAN+'[URL]   -------------->>   '+Fore.GREEN+f'{self.url}\n'+Fore.CYAN+'[Number of tags]   --->>   ' +
                  Fore.GREEN+f'{self.tags}\n'+Fore.CYAN+'[Numbers of comments] >>   '+Fore.GREEN+f'{self.comments}')
            confirm = input('\t\tit\'s correct? [Y/n]').lower()
            if confirm == 'y':
                break
            elif confirm == 'n':
                print('ok...')
                return InstaBot()
            else:
                print(
                    Fore.LIGHTBLUE_EX+'\t\t  Just ['+Fore.LIGHTGREEN_EX+'Y'+Fore.RESET+'/'+Fore.LIGHTRED_EX+'n'+Fore.LIGHTBLUE_EX+']')
                input('Press any key if you understand ')
                continue
            # -------------------------------------------- #
        # -------------------------------------------- #

    @staticmethod
    def is_valid_url(url) -> bool:
        """
            verify if url input is a instagram post link
        """
        regex = r'^https://www\.instagram\.com/p/'
        return bool(re.match(regex, url))
        # -------------------------------------------- #

    def initialize(self):
        """
            Verify that all JSON files exist, insert cookies into the session, and select a random user-agent
            
            ---> Path: jsons/files.json
        """
        os.system('cls')
        print(Style.BRIGHT+Fore.LIGHTGREEN_EX+'Bot started....')
        # -------------------------------------------- #
        with open(LocalPath.useragents_path, 'r') as f:
            user_agents = json.load(f)

        random_agent = random.choice(user_agents)['useragent']
        self.options.add_argument(f"user-agent={random_agent}")

        self.driver = webdriver.Edge(options=self.options)
        self.driver.get(self.url)
        # -------------------------------------------- #
        with open(LocalPath.cookies_path, 'r') as file:
            cookies_data = json.load(file)
            for cookie in cookies_data:
                try:
                    self.driver.add_cookie(cookie)

                except AssertionError:
                    cookie["sameSite"] = "None"
                    self.driver.add_cookie(cookie)

        self.driver.refresh()
        # -------------------------------------------- #
        if self.tags > 0:
            return self.__instagramers_message(self.comments)
        elif self.tags == 0:
            return self.__automatic_message(self.comments)

        # -------------------------------------------- #

    @staticmethod
    def __random_agent():
        with open(LocalPath.useragents_path, 'r') as f:
            user_agents = json.load(f)
        return random.choice(user_agents)['useragent']

    def __update_useragent(self):
        new_agent = self.__random_agent()
        super().__init__()
        self.options.add_argument(f"user-agent={new_agent}")
        self.driver = webdriver.Edge(options=self.options)
        self.driver.get(self.url)
        # -------------------------------------------- #
        with open(LocalPath.cookies_path, 'r') as file:
            cookies_data = json.load(file)
            for cookie in cookies_data:
                try:
                    self.driver.add_cookie(cookie)

                except AssertionError:
                    cookie["sameSite"] = "None"
                    self.driver.add_cookie(cookie)
        # -------------------------------------------- #
        self.driver.refresh()

    def __instagramers_message(self, comments):
        with open(LocalPath.followers_path, 'r') as f:
            followers = json.load(f)
        self.driver.implicitly_wait(20)
        tags_send = self.comments * self.tags
        # -------------------------------------------- #
        for i in range(comments):
            number_followers = random.choices(followers, k=self.tags)
            number_followers_space = ' '.join(number_followers)
            # -------------------------------------------- #

            for char in number_followers_space:
                try:
                    comment_input = self.driver.find_element(
                        By.XPATH, '//*[@autocomplete="off"]')
                    comment_input.send_keys(char)
                    sleep(random.randint(1, 3)/37)

                except StaleElementReferenceException:
                    comment_input = self.driver.find_element(
                        By.XPATH, '//*[@autocomplete="off"]')
                    comment_input.send_keys(char)
                    sleep(random.randint(1, 4)/33)

                except:
                    raise XPathInstagramError
                    # -------------------------------------------- #
                self.driver.implicitly_wait(30)
                self.driver.find_element(
                    By.XPATH, "//*[text()='Post']").click()
                # -------------------------------------------- #
                sleep(random.uniform(1, 10))
                self.driver.quit()
                sleep(random.uniform(120, 480))
                self.__update_useragent()
                # -------------------------------------------- #
            print(Fore.LIGHTCYAN_EX +
                  f"You send {self.comments} messages to {tags_send}")

    def __automatic_message(self, comments):
        with open(LocalPath.comment_path, 'r') as file:
            auto_message = json.load(file)
        # -------------------------------------------- #
        for i in range(comments):
            message = random.choice(auto_message)
         # -------------------------------------------- #
            for char in message:
                try:
                    comment_input = self.driver.find_element(
                        By.XPATH, '//*[@autocomplete="off"]')
                    comment_input.send_keys(char)
                    sleep(random.randint(1, 4)/33)

                except StaleElementReferenceException:
                    comment_input = self.driver.find_element(
                        By.XPATH, '//*[@autocomplete="off"]')
                    comment_input.send_keys(char)
                    sleep(random.randint(1, 3)/37)

                except:
                    XPathInstagramError
            # -------------------------------------------- #
            self.driver.implicitly_wait(30)
            self.driver.find_element(
                By.XPATH, "//*[text()='Post']").click()
            # -------------------------------------------- #
            sleep(random.uniform(1, 3))
            self.driver.quit()
            sleep(random.uniform(120, 480))
            self.__update_useragent()
        # -------------------------------------------- #
        input(Fore.LIGHTCYAN_EX+f"You send {self.comments} messages!")


if __name__ == "__main__":
    pass
    # TakeCookies().mycookies()
    # TakeCookies().myfollowers()
    # InstaBot().initialize()
