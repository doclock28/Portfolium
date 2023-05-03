from argparse import ArgumentParser
import sys

class SelectClub:
    """ A class that takes distance from the pin and returns which club to use
    
    Attributes: 
        Men_clubDict (dict): contains key, value pairs for club and average distance when used for men
        Women_clubDict (dict): contains key, value pairs for club and average distance when used for women
        clubDict (dict): contains key, value pairs for club and average distance when used
        distance (int): the distance the player is from the pin
    """

    def __init__(self, distance):
        """ Initialize
        
        Side effects:
            set attributes Men_clubDict, Women_clubDict, clubDict, and distance
        """
        self.Men_clubDict = {"Driver": 217, "3 Wood": 205, "5 Wood": 195, "7 Wood": 185, "3 Hybrid": 190, "3 Iron": 180, "4 Iron": 170, "5 Iron": 160, "6 Iron": 150, "7 Iron": 140, "8 Iron": 130, "9 Iron": 115, "Pitching Wedge": 105, "Sand Wedge": 80, "Lob Wedge": 70, "Putter": 20}
        self.Women_clubDict = {"Driver": 175, "3 Wood": 150, "5 Wood": 135, "3 Hybrid": 130, "3 Iron": 125, "4 Iron": 120, "5 Iron": 110, "6 Iron": 100, "7 Iron": 90, "8 Iron": 80, "9 Iron": 70, "Pitching Wedge": 60, "Sand Wedge": 50, "Lob Wedge": 45, "Putter": 20}
        self.clubDict = {"Driver": 0, "3 Wood": 0, "5 Wood": 0, "7 Wood": 0, "3 Hybrid": 0, "3 Iron": 0, "4 Iron": 0, "5 Iron": 0, "6 Iron": 0, "7 Iron": 0, "8 Iron": 0, "9 Iron": 0, "Pitching Wedge": 0, "Sand Wedge": 0, "Lob Wedge": 0, "Putter": 20}
        self.distance = int(distance)

    def club_calc(self):
        """ Searches the clubDict for a value that is closest to the distance given
        
        Side effects:
            returns the key for the value closest to the distance given
        """
        new_key, new_val = min(self.clubDict.items(), key=lambda x: abs(self.distance - x[1]))
        return new_key

    
class MenClub(SelectClub):
    """ A class that inherits the SelectClub class and modifies the club_calc method
    for male average distances
    
    Attributes: 
        All attributes from the SelectClub class
    """
    
    def club_calc(self):
        """ Searches the Men_clubDict for a value that is closest to the distance given
        
        Returns:
            the key for the value closest to the distance given
        """
        new_key, new_val = min(self.Men_clubDict.items(), key=lambda x: abs(self.distance - x[1]))
        return new_key



class WomenClub(SelectClub):
    """ A class that inherits the SelectClub class and modifies the club_calc method
    for female average distances
    
    Attributes: 
        All attributes from the SelectClub class
    """

    def club_calc(self):
        """ Searches the Women_clubDict for a value that is closest to the distance given
        
        Returns:
            the key for the value closest to the distance given
        """
        new_key, new_val = min(self.Women_clubDict.items(), key=lambda x: abs(self.distance - x[1]))
        return new_key



def main(player_sex):
    """ Recieve player input for distance and call a class based on sex
    
    Args:
        player_sex (str): the sex of the player
        
    Returns:
        print statement that suggests a club for the distance inputed
        
    """
    while True:
        distance = input("What is the distance to the pin? or 'quit'")
        if distance == "quit":
            break

        if player_sex == "male":
            club = MenClub(distance)
            print(f"You should use the {club.club_calc()} from {distance} yards")

        elif player_sex == "female":
            club = WomenClub(distance)
            print(f"You should use the {club.club_calc()} from {distance} yards")

    print("Thanks for using the Club Selector!")



def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): arguments received from the command line.
    
    Returns:
        players sex to decide which class to call
    """
    parser = ArgumentParser()
    parser.add_argument("player_sex", help="Sex of the player (Male or Female)")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player_sex)