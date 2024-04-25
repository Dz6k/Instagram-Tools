
#  Insta Tools


![Python Logo](https://www.python.org/static/community_logos/python-logo.png) <a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="180" alt="Selenium"/></a>
  



This software, called Insta Tools, is an automation tool designed for study purposes and not for mass spamming.

  

---

  

<details>

<summary><strong>How to Use</strong></summary>

  

To start using Insta Tools, follow these steps:

  

1. Clone this repository to your local environment:

  
  

2. Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

  

3. Install the necessary dependencies, including Selenium:

  

4. Open the `instabot.py` file and initiate the classes that are being called at the end of the file.

  

5. First, log in to Instagram to collect your cookies.

  

6. Then, execute the function to collect all the users you follow. This is done through the link `https://www.instagram.com/{your_username}/following`.

  

7. Wait until all followers are pre-loaded in the Instagram DOM.

  

8. Start the main class, which is responsible for opening the link of a post and performing automatic actions, such as making complimentary comments (which are saved in the `jsons/comments.json` file) or tagging other users. The users tagged are those on your profile whom you follow, and these are saved in the `jsons/followers.json` file. According to the settings you define in the class instance, it will make random comments on the post and tag randomly selected users.

  

9. Each comment has a time interval between 100 and 350 seconds to avoid blocks by Instagram (comments with @ too frequently can be considered spam).

  

10. Typing is done in a loop to avoid detection, and each time the class is started, a new user-agent is randomly chosen.

  

Please note that the use of Insta Tools is your responsibility and misuse may violate Instagram's terms of service. Use it only for educational and legitimate purposes.

  

</details>