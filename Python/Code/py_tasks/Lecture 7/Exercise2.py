def losing_team_captain(teams):
    return teams[len(teams)-1][1]

teams = (('Peach', 'Browser', 'Bob'), ('Eve', 'Alice', 'Browser'), ('Eric', 'Mario', 'Toto', 'Eve'))

print(losing_team_captain(teams))


def losing_team_captain_list(teams_list):
    return teams_list[len(teams_list)-1][1]

teams_list = [['Peach', 'Browser', 'Bob'], ['Eve', 'Alice', 'Browser'], ['Eric', 'Mario', 'Toto', 'Eve']]

print(losing_team_captain_list(teams_list))
