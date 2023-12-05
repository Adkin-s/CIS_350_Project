# CIS_350_Project
# SNRK Bot
The Multi-Personality AI Chatbot App.

### Made By:
James Brands, Elijah Morgan, Drew Adkins

# Abstract
SNRK is a chatbot designed to engage users in dynamic and personalized conversations by embodying multiple distinct personalities. This README file provides a comprehensive introduction to SNRK, outlining its key features, installation and usage instructions, and the underlying technology that powers its multifaceted personas. We want to create a chatbot that is extremely simple to use, and completely safe for users.

# Description
SNRK is a unique chatbot application that stands out for its ability to embody multiple distinct personalities. Users can engage in dynamic and personalized conversations with SNRK, selecting from a variety of pre-defined personas that range from friendly and helpful to witty and sassy. The chatbot's natural language understanding capabilities ensure smooth interactions, and users can switch between personalities during conversations. SNRK is highly customizable, allowing users to define their preferred personalities and traits. SNRK redefines the chatbot experience, offering users a multifaceted and engaging conversational partner.

# Architectural Design
SNRK uses serveless architecture on Firebase. The easy-to-use user interface allows you to sign up or log in, so the user can access not only new chats but also old conversations across multiple devices. Before being able to use the app the user must log in. Then once inside the app, the user can continue the conversation.

## Server
The server-side processing will be enabled using Firebase. Whenever a new user registers with the app, the record will be stored in the server-side database. The client requests the ChatGPT API and displays the returned text in the SNRK App. Each message can be up to 100 API tokens.

## Diagrams
### Sequence Diagram
![SequenceDiagram](https://github.com/Adkin-s/CIS_350_Project/assets/120053578/07ee623e-a315-4601-b451-2798110873b4)
### Use Case
![SNRK Use Case](https://github.com/Adkin-s/CIS_350_Project/assets/120053578/03a4bfae-4de7-4983-9652-164b311efdbd)
### Class Diagram
![SNRK Class UML](https://github.com/Adkin-s/CIS_350_Project/assets/120053578/35142850-cc3c-457a-aa0e-680af128e412)

# User Guide/Implementation
## Starting the application
First, the user needs to install the SNRK bot app from the app store onto their device. After installation, an icon should appear on the home screen. Click on the icon to open the SNRK bot app, and the user will be prompted with a signup or login page.

## Registration
Before using the app, the user will be required to either sign up for the app or to log into an existing account. The user will be asked to enter either an existing password and username to log in or a unique username and password to create a new account. This data will be stored on a server and will be confidentiality stored.

![Screenshot_from_2023-12-02_12-29-14](https://github.com/Adkin-s/CIS_350_Project/assets/120053578/f120a2fe-ad90-4e49-ac0c-ad99bf9fc73f)

## Home Screen - Check!
After logging in or signing up for SNRK, the user will be brought to a home screen where the user will have the ability to access different conversations with different personalities. The user will be able to press on each of the personalities to either begin or continue a conversation with this chatbot.

![Screenshot_from_2023-12-02_12-25-46](https://github.com/Adkin-s/CIS_350_Project/assets/120053578/de17f82c-2bbd-4ebc-8777-4625d8563494)

## Starting a conversation - Check!
If the conversation is accessed for the first time, they will be prompted with a message about that specific personality and what to expect when engaging with it. If not, the user will have the 5 most recently sent messages and chatbot outputs also given so that the user is able to remember their last conversation. To begin a conversation all the user has to do is type to the chatbot using the message box, and then press send and the user will receive a response from the chatbot.

![Screenshot_from_2023-12-02_12-26-36](https://github.com/Adkin-s/CIS_350_Project/assets/120053578/11e3b7bf-e252-43d9-aa0b-42cce2f036c9)


# Future Ideas
We would like to add a user function that allows the user to create their own personality chatbot to suit their specific desires. We would also like to add more themes for the app, as well as animations for when you open a conversation with a specific personality. We believe these ideas will make the app even more exciting for the user. 

# Conclusion
We at SNRK believe that our multi-personality chatbot is a fun, easy-to-use chatbot, that you will be able to use for hours on end in your personal life.

# Walkthrough Video


## Acknowledgments

Inspiration, code snippets, etc.
* [README-Template.md](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [ParkInAndriodReadMe-template](https://github.com/hridoy100/ParkInAndroid#readme)
