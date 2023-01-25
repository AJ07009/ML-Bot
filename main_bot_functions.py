import cmd2 
import pandas as pd

class DataBot(cmd2.Cmd):
    intro = 'Welcome to the data bot. Type help or ? to list commands.\n'
    prompt = '(data bot) '

    def do_analyze(self, arg):
        # Read in data
        data = pd.read_csv("data.csv")

        # Select rows between 50% and 85%
        data = data[(data["percentage"] > 50) & (data["percentage"] <= 85)]

        # Take lowest position x2 (most profitable)
        data = data.nsmallest(2, "position")
        data["profit"] = data["position"] * 2

        # Find highest frequency change
        data = data.sort_values("change_frequency", ascending=False)
        highest_frequency_change = data.iloc[0]["change_frequency"]
        print(highest_frequency_change)

    def do_quit(self, arg):
        'Quit the data bot'
        print('Thank you for using the data bot')
        return True

if __name__ == '__main__':
    DataBot().cmdloop(intro=None)