# CIS_350_Project
# SNRK Bot
The Multi-Personality AI Chatbot App.

# Abstract
SNRK is a chatbot designed to engage users in dynamic and personalized conversations by embodying multiple distinct personalities. This README file provides a comprehensive introduction to SNRK, outlining its key features, installation and usage instructions, and the underlying technology that powers its multifaceted personas.

# Description
SNRK is a unique chatbot application that stands out for its ability to embody multiple distinct personalities. Users can engage in dynamic and personalized conversations with SNRK, selecting from a variety of pre-defined personas that range from friendly and helpful to witty and sassy. The chatbot's natural language understanding capabilities ensure smooth interactions, and users can switch between personalities during conversations. SNRK is highly customizable, allowing users to define their preferred personalities and traits. SNRK redefines the chatbot experience, offering users a multifaceted and engaging conversational partner.

# Architectural Design
SNRK is based on a client-server-based architecture. The easy-to-use user interface allows you to sign up or login, so the user can access not only new chats but also old conversations across multiple devices. Before being able to use the app the.

## Server - Check!
The server-side processing will be enabled using Firebase. Whenever a new user registers with the app, the record will be stored in the server-side database. Whenever a registered user enters a new chat it sends the message to the server. The server then accesses the Open-Ai Server and the output is sent to the SNRK app. Then the chatbot's answer is outputted to the SNRK app and is received by the user. 

## Diagrams
### Sequence Diagram
![SequenceDiagram](https://github.com/Adkin-s/CIS_350_Project/assets/120053578/07ee623e-a315-4601-b451-2798110873b4)
### Use Case
![SNRK Use Case](https://github.com/Adkin-s/CIS_350_Project/assets/120053578/03a4bfae-4de7-4983-9652-164b311efdbd)
### Class Diagram
![SNRK Class UML](https://github.com/Adkin-s/CIS_350_Project/assets/120053578/35142850-cc3c-457a-aa0e-680af128e412)


### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

James Brands
Elijah Morgan
Drew Adkins

## Version History

* 0.2
    * Various bug fixes and optimizations
* 0.1
    * Initial Release


## Acknowledgments

Inspiration, code snippets, etc.
* [README-Template.md](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
