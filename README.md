# Automatic-Smart-Revise
 Automate answering questions on the computer science revision website https://smartrevise.online

## Note
I no longer have access to SmartRevise. If there are issues feel free to create an issue, however, I may not be able to solve most problems. If you are able to fix any issues, feel free to make a pull request

## Usage
1. Download **all** files from this repository
2. Ensure that python 3.7 or higher is installed and working on your machine 
3. Install the selenium web driver by opening the command prompt and typing `python3 -m pip install selenium`
4. Download the correct version of chrome web driver and put **it in the same directory**.
5. Create a file named secrets.py **in the same directory**. Create two python variables with username and password
6. Run the main.py script ensuring that only the topics you want to bot and are fully mapped are checked to revise
7. Ensure that the bot is running correctly and leave it to do its magic 

## Important Note
Any contributors or developers of this project are not responsible for the way it is used. This project was made for fun, not cheating and skipping out on homework or revision. Use this project wisely and at your own discretion.

## Contributors 
* Michael Dormand (Dinoosawruss)
* [Ded-Ex](https://github.com/Ded-Ex)

# Review
## What did this teach me?
This project taught me how to interact with the web and chrome using the selenium web driver and python. It also taught me about interacting with CSV files as databases and how difficult mapping a database can be. 

## Tools Used:
* Python 3.7+
* Selenium Web Driver
* CSV files

# FAQ
*Currently None*

# Updates
## main.py changes:
* Changed some xpath code to target correct elements on updated site
* Added new targeter and click event to remove the cookies button on startup
* Added new targeter and click event to start the quiz properly with new interface
