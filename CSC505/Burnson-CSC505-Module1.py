# John Burnson
# CSC505
# Module 1

class BaseballLeague:
    def __init__(self, sport_level):
        self.sport_level = sport_level
        self.sport_teams = []   # List of class BaseballTeam
        
    def add_team(self, team):
        self.sport_teams.append(team)
        
    def print_league(self):
        for index, value in enumerate(self.sport_teams):
            if (index % 15 == 0):
                print('\n', value.team_conference, sep='')
            if (index % 5 == 0):
                print(' ', value.team_division)
            #print(['', '\n'][index % 5 == 0], value.team_location, value.team_name)
            print('   ',value.team_location, value.team_name)

class BaseballTeam:
    def __init__(self, team_conference, team_division, team_location, team_name):
        self.team_conference = team_conference
        self.team_division = team_division
        self.team_location = team_location
        self.team_name = team_name
    
    def print_team(self):
        print(self.team_conference + ' ' + self.team_division)

data_mlb_teams = [
    BaseballTeam("American League", "East", "Baltimore", "Orioles"),
    BaseballTeam("American League", "East", "Boston", "Red Sox"),
    BaseballTeam("American League", "East", "New York", "Yankees"),
    BaseballTeam("American League", "East", "Tampa Bay", "Rays"),
    BaseballTeam("American League", "East", "Toronto", "Blue Jays"),
    BaseballTeam("American League", "Central", "Chicago", "White Sox"),
    BaseballTeam("American League", "Central", "Cleveland", "Guardians"),
    BaseballTeam("American League", "Central", "Detroit", "Tigers"),
    BaseballTeam("American League", "Central", "Kansas City", "Royals"),
    BaseballTeam("American League", "Central", "Minnesota", "Twins"),
    BaseballTeam("American League", "West", "Oakland", "Athletics"),
    BaseballTeam("American League", "West", "Houston", "Astros"),
    BaseballTeam("American League", "West", "Los Angeles", "Angels"),
    BaseballTeam("American League", "West", "Seattle", "Mariners"),
    BaseballTeam("American League", "West", "Texas", "Rangers"),
    BaseballTeam("National League", "East", "Atlanta", "Braves"),
    BaseballTeam("National League", "East", "Miami", "Marlins"),
    BaseballTeam("National League", "East", "New York", "Mets"),
    BaseballTeam("National League", "East", "Philadelphia", "Phillies"),
    BaseballTeam("National League", "East", "Washington", "Nationals"),
    BaseballTeam("National League", "Central", "Chicago", "Cubs"),
    BaseballTeam("National League", "Central", "Cincinnati", "Reds"),
    BaseballTeam("National League", "Central", "Milwaukee", "Brewers"),
    BaseballTeam("National League", "Central", "Pittsburgh", "Pirates"),
    BaseballTeam("National League", "Central", "St. Louis", "Cardinals"),
    BaseballTeam("National League", "West", "Arizona", "Diamondbacks"),
    BaseballTeam("National League", "West", "Colorado", "Rockies"),
    BaseballTeam("National League", "West", "Los Angeles", "Dodgers"),
    BaseballTeam("National League", "West", "San Diego", "Padres"),
    BaseballTeam("National League", "West", "San Francisco", "Giants")
]

def main():
    print("\n*** Main Start ***")
    
    # Create Level = MLB
    mlb = BaseballLeague("MLB")
    
    # Add teams
    for team in data_mlb_teams:
        mlb.add_team(team)
        
    # Print League
    mlb.print_league()

if __name__ != "__main__":
    print('This program is being imported from another module, so do not run main().')
else:
    print('This program is being executed as __main__')
    main()
    
    