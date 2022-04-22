# from asyncore import loop

define spock = Character("Spock")
define kirk = Character("Kirk")
image spock_talking = Image("images/characters/spock_dialogue.png")

label rescue_crew:

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
    
    show kirk_dialogue at right

    kirk "Stand by transporter room, ready to beam survivors abaord."

    show spock_talking at left:
        zoom 1.90

    spock "Captain, I've lost their signal!!"

    hide kirk_dialogue
    hide spock_talking

    "Computer Voice" "Alert! Sensors indicate three Klingon Cruisers, bearing three one six, mark four, closing fast."

    show kirk_dialogue at right

    kirk "Visual! Battle stations! Activate shields!"

    show spock_talking at left:
        zoom 1.90

    spock "Shields activated!"

    kirk "Inform the Klingons we are on a rescue mission."

    spock "They're jamming the frequencies, Captain."

    hide kirk_dialogue
    hide spock_talking

    "Computer Voice" "Klingons on attack course and closing."

    show kirk_dialogue at right

    kirk "Mister Spock, get us out of here!"

    hide kirk_dialogue

    "Computer Voice" "Alert! Klingon torpedoes activated."

    "(An explosion rocks the bridge!)"

    show kirk_dialogue at right

    kirk "Damage report!"

    show spock_talking at left:
        zoom 1.90

    spock "Main energiser hit, Captain!"

    kirk "Prepare to return fire!"

    kirk "Fire all phasers!"

    spock "No power to the weapons, Captain."

    spock "Captain, it's no use... We're dead in space..."

    hide kirk_dialogue
    hide spock_talking

    jump rescue_outro

label abandon_crew:

    $ times_played += 1

    scene death_by_klingons

    kirk "You die at the hands of the Klingons"
    
    jump menu_choices

label reprogram_simulation:
    return

label menu_choices:

    kirk "What should I do?"

    $ reprogram = renpy.random.random()

    if reprogram > 0.88 and times_played > 2:
        menu:
            "Save the Kobayashi Maru":
                $ times_rescued += 1
                jump rescue_crew
            "Abandon the Kobayashi Maru":
                $ times_abandoned += 1
                jump abandon_crew
            "Reprogram the simulation":
                jump reprogram_simulation

    else:
        menu:
            "Save the Kobayashi Maru":
                $ times_rescued += 1
                jump rescue_crew
            "Abandon the Kobayashi Maru":
                $ times_abandoned += 1
                jump abandon_crew

label rescue_outro:
    return

label abandon_outro:
    return

label start:

    # play music "audio/StarTrek_TOS_Theme.ogg" loop

    $renpy.sound.play("audio/StarTrek_TOS_Theme.ogg", loop=True)

    call variables
    scene start_screen

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

label variables:
    $ times_played = 0
    $ times_abandoned = 0
    $ times_rescued = 0