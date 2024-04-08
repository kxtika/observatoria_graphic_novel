########################### DEFAULT VARIABLES #################################
default click_times = 0
default count_clicks = True
default countdown_time = 20
default start_timer = False
default flicker_caught = False

default wave_pieces = 6
default full_page_size = (960, 521)
default piece_coordinates = [(128, 267), (254, 267), (131, 353), (131, 730), (130, 459), (657, 540)]
default initial_coordinates = []
default finished_pieces = 0

######################### PYTHON FUNCTIONS #####################################
init python:
    import random

    def click_counter():
        global click_times, start_timer, count_clicks, flicker_caught
        if click_times == 0:
            start_timer = True

        click_times += 1

        if click_times >= 12:
            count_clicks = False
            flicker_caught = True
            renpy.jump("flicker_found")

    def random_position():
        return (random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))

    def time_up():
       global start_timer, count_clicks
       start_timer = False
       count_clicks = False
       if not flicker_caught:
           renpy.jump("flicker_not_found")

    def setup_puzzle():
        for i in range(wave_pieces):
            start_x = 1000
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_coordinates.append(rand_loc)

    def piece_drop(dropped_on, dragged_piece):
        global finished_pieces

        distance_threshold = 20
        distance = ((dropped_on.x - dragged_piece[0].x)**2 + (dropped_on.y - dragged_piece[0].y)**2)**0.5

        if distance <= distance_threshold:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == wave_pieces:
                renpy.jump("connection_established")

################## SCREEN FLICKER COUNTER GAME ########################
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
        timer countdown_time action Function(time_up)

############## SCREEN ESTABLISH CONNECTION GAME ############################
screen establish_connection_game:
    image "connection_bg.png"
    text "Assemble all of the cosmic waves together"  align(0.5, 0.1) size 30 color "#191970"
    frame:
        background "waves_frame.png"
        xysize full_page_size
        anchor(0, 0)
        pos(130, 267)

    draggroup:
        for i in range(wave_pieces):
            drag:
                drag_name i
                pos initial_coordinates[i]
                anchor(0, 0)
                focus_mask True
                drag_raise True
                image "Pieces/piece-%s.png" % (i + 1)

        for i in range(wave_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                anchor(0, 0)
                focus_mask True
                image "Pieces/piece-%s.png" % (i + 1) alpha 0.0



######################## MAIN SCRIPT #######################################
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
    scene spacecraft_bg
    show santos_image at right
    show krystal_image at left
    s "Let's check it out, Krystal."
    "Focus on scanning the area for any incoming signals. Catch as many flickers as you can!"

    call screen flicker_counter_game
    return

label flicker_found:
    scene spacecraft_bg
    show santos_image at right
    show krystal_image at left
    s "Looks like we're onto something!"
    k "Let's see if we can establish a decent connection with the source of the signal."
    "Reassemble the waves together to establish a connection."

    $setup_puzzle()
    call screen establish_connection_game
    return

label flicker_not_found:
    scene spacecraft_bg
    show santos_image at right
    show krystal_image at left
    s "I'm sorry I disturbed you and we haven't found anything."
    k "Don't worry, it was still worth a try."
    k "I'll just get back to work then."

    jump analyze_data

label analyze_data:
    scene spacecraft_bg
    show santos_image at right
    show krystal_image at left
    k "Let's keep our focus on the task at hand."
    s "What do we have here?"
    k "Just a bunch of metrics captured over the last week."

    jump choose_a_tool_quiz

label choose_a_tool_quiz:
    scene computer_bg
    "Krystal needs your help with analyzing metrics. Choose the best tool for each task."

    $score = 0

    "Task 1: Trend Analysis"
    "Which tool is best for identifying trends in the data?"
    menu:
        "A. Line chart":
            "Correct! Line charts are great for showing trends over time."
            $score += 1
            jump task_2
        "B. Pie chart":
            "Incorrect. Pie charts are more suited for showing proportions of a whole."
            jump task_2

    label task_2:
        "Task 2: Outlier Detection"
        "Which tool is best for identifying outliers?"
        menu:
            "A. Box plot":
                "Correct! Box plots are commonly used for detecting outliers."
                $score += 1
                jump task_3
            "B. Scatter plot":
                "Incorrect. Scatter plots are good for visualizing relationships between variables."
                jump task_3

    label task_3:
        "Task 3: Correlation Analysis"
        "Which tool is best for identifying correlations?"
        menu:
            "A. Correlation coefficient":
                "Correct! The correlation coefficient measures the strength and direction of a linear relationship."
                $score += 1
                jump task_4
            "B. Histogram":
                "Incorrect. Histograms display the distribution of a single variable."
                jump task_4

    label task_4:
        "Task 4: Distribution Analysis"
        "Which tool is best for analyzing distribution?"
        menu:
            "A. Histogram":
                "Correct! Histograms show the distribution of a single variable."
                $score += 1
                jump task_5
            "B. Bar chart":
                "Incorrect. Bar charts are used for comparing different categories."
                jump task_5

    label task_5:
        "Task 5: Time Series Forecasting"
        "Which tool is best for time series forecasting?"
        menu:
            "A. Exponential smoothing":
                "Correct! Exponential smoothing is a method for forecasting based on weighted averages."
                $score += 1
                jump task_6
            "B. Box plot":
                "Incorrect. Box plots are used for displaying distribution and detecting outliers."
                jump task_6

    label task_6:
        "Task 6: Cluster Analysis"
        "Which tool is best for cluster analysis?"
        menu:
            "A. K-means clustering":
                "Correct! K-means clustering is a method for partitioning data into clusters."
                $score += 1
                jump quiz_end
            "B. Line chart":
                "Incorrect. Line charts are used for showing trends over time."
                jump quiz_end

    label quiz_end:
        "Quiz complete! Your score is [score]/6."

    jump outro_2

label connection_established:
    scene computer_bg
    k "We got a message! However, I think it's encrypted."
    s "This encryption is quite complex, Krystal. We'll need to combine our skills to crack it."
    k "Agreed. I'll handle the algorithm while you focus on visual patterns."
    s "Got it! Teamwork makes the dream work, right?"
    k "Let's do this, Santos."

    jump encrypted_message


label encrypted_message:
    scene computer_bg

    "Help Santos and Krystal decrypt the signal together."

    "You stare at the alien glyphs flashing on the screen, your heart races with excitement and anticipation."
    "This code could hold the key to the observatory's location, but it's encrypted in an unknown alien language."

    "The alien glyphs swirl and morph, constantly changing their shapes and colors, challenging your comprehension."
    jump decipher_message

label decipher_message:
    scene computer_bg_cipher

    $alien_code = ["ລໄະອຟດດວກໄ"]
    $current_code = ["ລ", "ໄ", "ະ", "ອ", "ຟ", "ດ", "ດ", "ວ", "ກ", "ໄ"]

    $correlation_map = {
        "ໄ": 1, "ຟ": 2, "ກ": 3, "ະ": 4, "ອ": 5, "ັ": 6, "ດ": 7, "ສ": 8, "ລ": 9, "ວ": 0,
    }

    "Decipher the message: [alien_code]"

    label decipher_code:
        $deciphered_message = ""
        $correlation_list = []

        "Enter the corresponding numbers for each symbol in the code:"

        python:
            for symbol in current_code:
                symbol_number = renpy.input("Enter the number for symbol '{}'".format(symbol))
                if symbol_number.isdigit():
                    correlation_list.append((symbol, int(symbol_number)))
                    deciphered_message += str(correlation_map[symbol])
                else:
                    "Please enter a valid number for symbol '{}'".format(symbol)


            if deciphered_message == "9145277031":
                "You've just deciphered the Observatoria's coordinates. Well done!"
                renpy.jump("outro_1")
            else:
                "Sorry, the message is not decrypted correctly. Let's try again."
                renpy.jump("decipher_message")

label outro_1:
    scene observatoria_bg
    show krystal_image at left
    show santos_image at right
    s "We made it, Krystal! The Observatoria."
    k "It's magnificent!"
    s "And with your keen observations and my quick actions, we conquered every challenge."
    k "Together, there's nothing we can't overcome."

    hide krystal_image
    hide santos_image
    "As they entered the Observatoria, Santos and Krystal knew that their journey was just beginning."
    "But with their friendship and skills, they were ready to face whatever mysteries the universe had in store."

    "Images were generated by GenCraft AI. Credit for the flickering light goes to 0melapicks on Freepik."

    return


label outro_2:
    scene spacecraft_bg
    show krystal_image at left
    show santos_image at right
    k "Thank you for helping me out today! Hopefully, we'll reach our destination some day."
    s "I hope so too."
    "Images were generated by GenCraft AI."
    return
