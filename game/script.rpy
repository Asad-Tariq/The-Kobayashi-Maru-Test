# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define spock = Character("Spock")
define kirk = Character("Kirk")
image spock_talking = Image("images/characters/spock_dialogue.png")

label save_crew:

    $ times_played += 1

    kirk "Plot an intercept course Spock."

    show spock_talking at left:
        zoom 1.90

    spock "May I remind the Captain that if a starship enters the Zone..."

    kirk "I am aware of my responsibilities, Spock."

    spock "Okay, Captain. Estimating two minutes to intercept. ...Now entering the Neutral Zone."

    hide kirk_dialogue
    hide spock_talking

    "Computer Voice" "Warning. We have entered the Neutral Zone. ...Warning."
    
    jump outro

label abandon:
    scene death_by_klingons
    kirk "You die at the hands of the Klingons"
    $ times_played += 1
    jump menu_choices

label outro:
    kirk "Your crew gets destroyed"
    return

label menu_choices:

    kirk "What should I do?"

    menu:
        "Save the Kobayashi Maru":
            jump save_crew
        "Abandon the Kobayashi Maru":
            jump abandon
        "End game" if times_played > 0:
            jump outro


label start:

    # Create a variable that records the number of times the Kobayashi Maru
    # Test has been taken.

    $ times_played = 0
    $ times_abandoned = 0
    $ times_rescued = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene start_screen

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Computer Voice" "Captain's log, stardate 8130.3. Starship Enterprise on training mission to Gamma Hydra, Section fourteen, coordinates twenty-two eighty-seven four. Approaching Neutral Zone, all systems normal and functioning."

    show spock_talking at left:
        zoom 1.90

    spock "Captain, ...I'm getting something on the distress channel."

    show kirk_dialogue at right

    kirk "On speakers!"

    hide kirk_dialogue
    hide spock_talking
    
    "Kobayashi Maru Voice" "Imperative! This is the Kobayashi Maru, ...nineteen periods out of Altair Six. We have struck a gravitic mine and have lost all power. ...Our hull is penetrated and we have sustained many casualties."

    show spock_talking at left:
        zoom 1.90

    spock "This is the Starship Enterprise. Your message is breaking up. Can you give your coordinates? Repeat. This is the Starship..."

    hide spock_talking

    "Kobayashi Maru Voice" "Enterprise, our position is Gamma Hydra, Section Ten."

    show kirk_dialogue at right

    kirk "Thats in the Neutral Zone..."

    hide kirk_dialogue

    "Kobayashi Maru Voice" "Hull penetrated, life support systems failing. Can you assist us, Enterprise? Can you assist us?"

    show kirk_dialogue at right

    kirk "Data on the Kobayashi Maru!"

    hide kirk_dialogue

    "Computer Voice" "Subject vessel is third class neutronic fuel carrier, crew of eighty-one, three hundred passengers."

    show kirk_dialogue at right

    jump menu_choices
