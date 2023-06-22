import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

states_data = pandas.read_csv("50_states.csv")
list_of_states = states_data.state.to_list()
correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 states_correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in list_of_states if state not in correct_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in list_of_states and answer_state not in correct_states:
        correct_states.append(answer_state)
        state = states_data[states_data.state == answer_state]
        tim.goto(int(state.x), int(state.y))
        tim.write(answer_state, align="center", font=("Arial", 10, "normal"))
