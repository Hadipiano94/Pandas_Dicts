import pandas

nato_alphabet_data = pandas.read_csv("nato-alphabet.csv")
my_NATO_dict = {row.Letter: row.NATO_word for (index, row) in nato_alphabet_data.iterrows()}


def get_nato():
    name = input("What is your Name?\n").upper()
    try:
        name_nato_list = [my_NATO_dict[n] for n in name]
    except KeyError:
        print("sorry, only alphabets please.")
        get_nato()
    else:
        print(name_nato_list)


get_nato()
