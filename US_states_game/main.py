import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

game_on = True
score = 0
guessd_states =[]


while game_on:
    answer_state = screen.textinput(title=f"{score}/50 Guess the name", prompt="What's another state's name?")
    answer_title = answer_state.title()
    
    if answer_title == "Exit":
        missing_states = [state for state in all_states if state not in guessd_states]

        # for state in all_states:
        #     if state not in guessd_states:
        #         missing_states.append(state)

        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break



    if answer_title in all_states:
        score += 1
        guessd_states.append(answer_title)
        t = turtle.Turtle()
        state_data = data[data.state == answer_title]
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_title, move=True, align="center")
        
