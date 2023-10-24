# Phase-3 Project Pokemon CLI

[Vide Walkthrough](https://youtu.be/B2R2hv8nPQM)

## Introduction:
This CLI was created for Pokemon card collectors who are looking for a place to store information about their collection. This CLI is built upon three related tables, Player, Card, and Deck. The Player table is used to store information about the user. Information such as the user's playing level, specific ID to access the user, and the user's username. The Card table stores information about the card's name, who the card belongs to, the HP, and the type of Pokemon on the card. Lastly, the Deck table stores information such as the name of the deck and who the deck belongs to.

## Seeding the File:
After forking and cloning the file, the first thing you need to do is run `pipenv install` inside this project directory, to install the dependencies. Next, run `pipenv shell` to open up a virtual environment. In the virtual environment, run `cd lib/db`. This will get you to the database directory. Type `python seed.py` to seed example data into the database. 

## Setting up:
Back in the lib directory, type `chmod +x cli.py` to give executable permissions to the file. Now you can type `./cli.py` to run the file!

## Login / Signup:
The program will begin asking you to enter a username. Entering a username that is in the Player database, you will be directed to the main menu. If your username is not in the database the program will ask you if you would like to sign-up. Pressing `n` will exit you out of the program. Pressing `y` will give you a series of prompts to create a user.

## Main Menu:
After logging in, you will be asked to choose between quitting the program, looking through your card collection, or looking through your deck collection. 

## Card Collection:
Pressing `c` in the main menu will enter you into your cards database. All of the cards in your database will be shown here if you have any. You will next be prompted to select between heading back to the main menu or, adding, removing, or updating a card. Adding, removing, or updating a card will prompt you to enter the respected information.

## Deck Collection:
Pressing `d` in the main menu will take you to your deck collection database. The prompts are very similar to that of the card collection database, with their respective inputs.
