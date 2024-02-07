import turtle
import pandas as pd
from writer import Writer

def point_on_map(df: pd.DataFrame, name: str):
    row = answers_df[answers_df.state == name]
    return row.iloc[0]

def main():
    # create screen and set it to an image
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    
    # input file with answers
    answers_df = pd.read_csv("50_states.csv")
    answers_df.state = answers_df.state.str.lower
    print(answers_df)
    # creating writing turtle
    writer = Writer()
    
    completed = 0 # no. of states written
    completed_s = str(completed) + "/50 States" # string to write in the window to input
    
    while completed < 50:
        # input the state
        answer_state = screen.textinput(title=completed_s, prompt="Write as much states as You know")
        answer_state_lower = answer_state.lower()
    
        # check if answer is correct
        if answer_state_lower in answers_df.state:
            correct_state, x, y = point_on_map(asnwers_df, answer_state_lower) # find x and y to write
            writer.write_state(correct_state, x, y)
            completed += 1
        


if __name__ == "__main__":
    main()
