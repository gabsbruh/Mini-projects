import turtle
import pandas as pd
from writer import Writer
from time import sleep

def point_on_map(df: pd.DataFrame, name: str):
    row = df[df.state == name]
    return row.iloc[0]

def main():
    # create screen and set it to an image
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    screen.setup(725, 491) # size of the image aligned to size of the image
    turtle.shape(image)
    
    # input file with answers
    answers_df = pd.read_csv("50_states.csv")

    # lower case of state to validate with answer later
    for i in range(len(answers_df.state)):
        answers_df.iloc[i, 0] = answers_df.iloc[i, 0].lower()

    # creating writing turtle
    writer = Writer()
    
    # store states which wasn't written
    written_states = []
    for state in answers_df.state:
        written_states.append(state)
    print(written_states)

    while 50-len(written_states) < 50:
        # input the state
        completed_s = str(50-len(written_states)) + "/50 States" # string to write in the window to input
        answer_state = screen.textinput(title=completed_s, prompt="Write as much states as You know")
        answer_state_lower = answer_state.lower()
    
        # check if answer is correct
        if (answers_df.state.eq(answer_state_lower).any()) and (answer_state_lower in written_states):
            correct_state, x, y = point_on_map(answers_df, answer_state_lower) # find x and y to write
            writer.write_state(correct_state, x, y)
            written_states.remove(answer_state_lower)
        # special state 'exit' to write all states and learn
        elif (answer_state_lower == 'exit'):
            for state in written_states:
                correct_state, x, y = point_on_map(answers_df, state) # find x and y to write
                writer.write_state(correct_state, x, y)
            screen.exitonclick()
            break
            
    # when all states written print 'you win' statement
    if not written_states:
        writer.win()
        sleep(1)
    

if __name__ == "__main__":
    main()
