#====================================MARSHMALLOWS====================================#
# The following program counts the marshmallows the user takes out or adds to their  #
# bag and is supposed to give the average amount added per round.                    #
#====================================================================================#

# Definition of starting points
huge_bag_of_marshmallows = []
total = 0 
rounds = 0

while True:
    try:
        # The program asks the user for input, if they want to add our take marshmallows
        # out of the bag
        print("=======================================================================================")
        marshmallow_input = int(input(
"""Please enter the amount of marshmallows you want to put into your bag.\n"""))
        
        # This while loop will keep asking the user for input until they enter 0 to stop it
        while marshmallow_input !=0: 

            # If the user tries to take out marshmallows when the bag is empty, an 
            # error message shows and asks them to put more marshmallows into the bag
            if total == 0 and marshmallow_input < 0:
                rounds += 1
                print("You don't have enough marshmallows left to eat.")
                print("Add more marshmallows, before you eat all of them!")
                print("---------------------------------------------------------------------------------------")
                try:
                    marshmallow_input = int(input(
"""Please enter the amount of marshmallows you want to put in or take out of your bag.
Enter negative numbers to take them out. Enter 0 to stop. \n"""))
                    
                # If the user inputs the wrong format, the program informs the user that it's the wrong format
                except ValueError:
                    print("---------------------------------------------------------------------------------------")
                    print("Invalid input. Please enter a number. e.g. '8'.")
                    print("=======================================================================================")

            # If the user has some marshmallows in the bag, but it's not enough for the amount they want to
            # take out, the program informs them that they don't have enough marshmallows in their bag          
            elif total > 0 and marshmallow_input < 0 and abs(marshmallow_input) > total:
                rounds += 1
                total_neg = total * -1
                print(f"You only have {total} marshmallows left.")
                print(f"If you want to eat all of them, take {total_neg} out of your bag.")
                print("---------------------------------------------------------------------------------------")
                try:
                    marshmallow_input = int(input(
"""Please enter the amount of marshmallows you want to put in or take out of your bag.
Enter negative numbers to take them out. Enter 0 to stop. \n"""))
                except ValueError:
                    print("---------------------------------------------------------------------------------------")
                    print("Invalid input. Please enter a number. e.g. '8'.")
                    print("=======================================================================================")

            # Any other times, when the user just adds marshmallows to their bag or takes some out if they have enough
            # to do so, the program makes a mark in the list and considers the entry in the total 
            else:
                rounds += 1
                huge_bag_of_marshmallows.append(marshmallow_input)
                total += marshmallow_input
                try:
                    marshmallow_input = int(input(
"""Please enter the amount of marshmallows you want to put in or take out of your bag.
Enter negative numbers to take them out. Enter 0 to stop. \n"""))
                except ValueError:
                    print("---------------------------------------------------------------------------------------")
                    print("Invalid input. Please enter a number. e.g. '8'.")
                    print("=======================================================================================")

        # When the while loop ends and there are no marshmallows left in the bag
        if total == 0:
            print("---------------------------------------------------------------------------------------")
            print("You have no marshmallows in your bag!")
            print("=======================================================================================")

            # the break below breaks the user finally out of the loop
            break
        
        # When the while loop ends and there are marshmallows in the bag, the program calculates the average
        # and prints the output
        else:
            average_marshmallows = total/rounds

            # Output
            print("---------------------------------------------------------------------------------------")
            if rounds == 1:
                print(f"After {rounds} round, your bag looks like this:{huge_bag_of_marshmallows}")
            else: 
                print(f"After {rounds} rounds, your bag looks like this:{huge_bag_of_marshmallows}")

            if total ==1:
                print(f"You count only {total} marshmallow in your bag.")
            else: 
                print(f"You count {total} marshmallows in your bag.")
            print(f"The average amout of marshmallows you added to your bag per round was {average_marshmallows}.")
            print("=======================================================================================")

            # the break below breaks the user finally out of the loop
            break

    except ValueError: 
        print("---------------------------------------------------------------------------------------")
        print("Invalid input. Please enter a number. e.g. '8'.")
        print("=======================================================================================")
        continue


