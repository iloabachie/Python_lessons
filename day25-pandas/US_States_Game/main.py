import turtle
import pandas as pd
import time

df = pd.read_csv('D:/documents/Python lessons/AngelaYu/day25/US_States_Game/50_states.csv')

state_list = df.state.to_list()


# state_dict = df.to_dict()
# print(state_dict)
x_list = df.x.to_list()
y_list = df.y.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "D:/documents/Python lessons/AngelaYu/day25/US_States_Game/blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)


# The commented out function below was used to get the coordinates.
# --------------------------------------------------
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)


correct_guesses = []
while len(correct_guesses) < 50:
    time.sleep(0.3)
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Type next state").title()
    if answer_state == "Exit":
        unguessed = [state for state in state_list if state not in correct_guesses]
        # unguessed = []
        # for state in state_list:
        #     if state not in correct_guesses:
        #         unguessed.append(state)
        new_data = pd.DataFrame(unguessed)
        new_data.to_csv('D:/documents/Python lessons/AngelaYu/day25/US_States_Game/unguessed.csv')
        break
    elif answer_state in state_list:
        correct_guesses.append(answer_state)
        # print(correct_guesses)        
        x = x_list[state_list.index(answer_state)]
        y = y_list[state_list.index(answer_state)]
        # print(x, y)
        ans = turtle.Turtle()
        ans.penup()
        ans.hideturtle()
        ans.goto(x, y)
        ans.write(answer_state)
        # alternative to get the x and y coordinates
        # state_data = df[df.state == answer_state]
        # ans.goto(int(state_data.x), int(state_data.y))
        

screen.mainloop()


# screen.exitonclick()