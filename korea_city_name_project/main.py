import turtle
import pandas

screen = turtle
screen.title("도진이를 위한 한국_도시_이름_게임")
image = "city_and_state_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("korea_city_state.scv")
all_state = data.state.to_list()
guess_state = []


while len(guess_state) < 17:
    answer_state = screen.textinput(title=f"{len(guess_state)}/ 17개 맞음", prompt="도진아 대한민국 특별시와 도를 맞춰봐!")
    print(answer_state)

    if answer_state == "Exit":
        missing_state = []
        for state in guess_state:
            if state not in guess_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state_to_learn.csv")
        break

    if answer_state in all_state:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())






# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
