# Ren'Py script with main storyline, dialogue, and gameplay logic

label start:
    scene black
    show image "images/cats_and_laptop_bg.png" at dissolve
    play music space_theme

    "As the development of technology advanced, so did the space exploration."
    "Most of the work was done by computers, some by humans (yes, they still exist), and some by… cats."
    "Cats."
    "They always loved laptops, didn’t they?"

    "In the vastness of space, where stars shimmered like diamonds and planets danced in a cosmic ballet,"
    "two extraordinary felines, Santos and Krystal, embarked on a mission unlike any other."
    "Their destination: the Observatoria, a mysterious beacon deep in the heart of the galaxy,"
    "rumored to hold the key to unlocking the universe's greatest mysteries."

    "Santos, with his soulful eyes and gentle demeanor, was a dreamer who found beauty in every corner of the cosmos."
    "Krystal, practical and efficient, led the way with a no-nonsense attitude and a laser focus on progress."

    "Together, they journeyed through the cosmos, their trusty laptops and keen senses their only companions."

    "But as they delved deeper into the unknown, they would face challenges that tested their bond and their skills."

    "This is their story. This is Observatoria."

    scene black
    stop music fadeout 2.0
    call dialogue_scene_1
    return

# Define the dialogue scenes including the mini-games
label dialogue_scene_1:
    scene laptop_bg
    show santos normal at left
    show krystal normal at right

    s "Krystal, do you see that?"
    k "See what, Santos? I'm busy analyzing the data from our last scan."
    s "There! A flicker of light in the distance. It could be a signal!"
    k "Hmm, let me take a look."

    "Help Krystal analyze the data to decipher the signal."
    call observation_game.run_observation_game

label dialogue_scene_2:
    scene laptop_bg
    s "This encryption is quite complex, Krystal. We'll need to combine our skills to crack it."
    k "Agreed. I'll handle the algorithm while you focus on visual patterns."
    s "Got it! Teamwork makes the dream work, right?"
    k "Let's do this, Santos."

    "Help Santos and Krystal decrypt the signal together."
    call decryption_game.run_decryption_game

label dialogue_scene_3:
    scene laptop_bg
    s "We made it, Krystal! The Observatoria."
    k "It's magnificent!"
    s "And with your keen observations and my quick actions, we conquered every challenge."
    k "Together, there's nothing we can't overcome."

    "As they entered the Observatoria, Santos and Krystal knew that their journey was just beginning."
    "But with their friendship and skills, they were ready to face whatever mysteries the universe had in store."

    "This is their story. This is Observatoria."

    return
