init python:
    import random

    def click_counter():

        global click_times, start_timer, count_clicks, flicker_caught
        if click_times == 0:
            start_timer = True

        click_times += 1
        renpy.restart_interaction()

        if click_times >= 12:
            count_clicks = False
            flicker_caught = True

    def random_position():
        return (random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))

transform button_hover:
    on hover:
        easein 0.2 zoom 1.05
    on idle:
        easein 0.2 zoom 1.0

screen flicker_counter_game:
    image "space_bg_with_signals.png"
    text "Flickers caught: [click_times] Time left: [countdown_time]" align(0.5, 0.65) outlines[(absolute(3.0), "#000000", 0, 0)] size 45

    imagebutton idle "flicker_of_light_big" pos random_position() sensitive count_clicks action Function(click_counter) at button_hover

    if not count_clicks:
        if click_times >= 12:
            text "You received a faint signal from an unrecognised source!" align(0.5, 0.75) outlines[(absolute(3.0), "#000000", 0, 0)] size 45
        else:
            text "The flicker of light is gone, sorry" align(0.5, 0.75) outlines[(absolute(3.0), "#000000", 0, 0)] size 45

    if start_timer:
        timer 1.0 action If(countdown_time > 0, SetVariable("countdown_time", countdown_time - 1), SetVariable("count_clicks", False)) repeat countdown_time > 0

default click_times = 0
default count_clicks = True
default countdown_time = 20
default start_timer = False
default flicker_caught = False

label start:
    scene black
    show image "images/spacecraft_bg.png"
    play music "space_theme.mp3"

    "As the development of technology advanced, so did space exploration."
    "Most of the work was done by computers, some by humans (yes, they still exist), and some by… cats."
    "Cats."
    "In the vastness of space, where stars shimmered like diamonds and planets danced in a cosmic ballet,"
    "two extraordinary felines, Santos and Krystal, embarked on a mission unlike any other."
    "Their destination: the Observatoria, a mysterious beacon deep in the heart of the galaxy,"
    "rumored to hold the key to unlocking the universe's greatest mysteries."

    "Santos, with his soulful eyes and gentle demeanor, was a dreamer who found beauty in every corner of the cosmos."
    "Krystal, practical and efficient, led the way with a no-nonsense attitude and a laser focus on progress."

    "Together, they journeyed through the cosmos, their trusty board computer and keen senses their only companions."

    "But as they delved deeper into the unknown, they would face challenges that tested their bond and their skills."

    "This is their story. This is Observatoria."

    scene black
    stop music fadeout 2.0
    call dialogue_scene_1

    define s = Character("Santos")
    define k = Character("Krystal")

    return

label dialogue_scene_1:
    scene spacecraft_bg
    show santos_image at right
    show krystal_image at left

    s "Krystal, do you see that?"
    k "See what, Santos? I'm busy analyzing the data from our last scan."
    s "There! A flicker of light in the distance. It could be a signal!"
    k "Hmm, let's take a look."

    menu:
        "Investigate the flicker":
            jump investigate_flicker
        "Focus on analyzing the data":
            jump analyze_data

label investigate_flicker:
    s "Let's check it out, Krystal."
    "You focus on scanning the area for any incoming signals. Catch as many flickers as you can!"

    call screen flicker_counter_game

    if flicker_caught:
        jump flicker_found_branch
    else:
        jump flicker_not_found_branch


label flicker_found_branch:
    s "Looks like we're onto something!"
    k "Let's see if we can establish decent connection with the source of the signal."

label flicker_not_found_branch:
    s "I'm sorry I disturbed you and we haven't found anything."
    k "Don't worry, it was still worth a try."
    k "I'll just get back to work then."

label analyze_data:
    k "Alright, let's keep our focus on the task at hand."
    # Continue with the story without additional gameplay
    jump continue_story

label continue_story:
    # Continue with the rest of the dialogue


# label dialogue_scene_2:
#     scene laptop_bg
#     s "This encryption is quite complex, Krystal. We'll need to combine our skills to crack it."
#     k "Agreed. I'll handle the algorithm while you focus on visual patterns."
#     s "Got it! Teamwork makes the dream work, right?"
#     k "Let's do this, Santos."
#
#     "Help Santos and Krystal decrypt the signal together."
#     #call decryption_game.run_decryption_game
#
# label dialogue_scene_3:
#     scene laptop_bg
#     s "We made it, Krystal! The Observatoria."
#     k "It's magnificent!"
#     s "And with your keen observations and my quick actions, we conquered every challenge."
#     k "Together, there's nothing we can't overcome."
#
#     "As they entered the Observatoria, Santos and Krystal knew that their journey was just beginning."
#     "But with their friendship and skills, they were ready to face whatever mysteries the universe had in store."
#
#     "Images were generated by GenCraft AI. Credit for the flickering light goes to 0melapicks on Freepik."
#
#     return
