import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")

guess_turtle = turtle.Turtle()
guess_turtle.hideturtle()
guess_turtle.penup()

correct_guesses = 0
all_states = state_data.state.to_list()
past_guesses = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                                    prompt="Name a state:").title()

    # Exit case
    if answer_state == "Exit":
        # List Comprehension
        missing_states = [state for state in all_states if state not in past_guesses]
        
        # For loop
        # for state in all_states:
        #     if state not in past_guesses:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Check answer
    if answer_state in all_states and answer_state not in past_guesses:
        state_x = state_data[state_data.state == answer_state].x
        state_y = state_data[state_data.state == answer_state].y
        guess_turtle.goto(int(state_x), int(state_y))
        guess_turtle.write(answer_state)

        past_guesses.append(answer_state)
        correct_guesses += 1
        if correct_guesses == 50:
            game_is_on = False
