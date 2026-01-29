import math
import numpy as np

def find_nb(m):
    n = 1
    sum = 0
    while True:
        sum += math.pow(n, 3)
        if sum == m:
            break
        elif sum > m:
            return -1
        n += 1
    return n

def balance(check_book):
    string_into_list = check_book.splitlines()
    list_of_lines = [line for line in string_into_list if line]
    balance = 0
    total_expense = 0
    expense_count = 0
    for i in range(len(list_of_lines)):
        if i == 0:
            balance = float(list_of_lines[i])
            list_of_lines[i] = "Original Balance: " + list_of_lines[i]
        else:
            splitted_line = list_of_lines[i].split(' ')
            price = float(splitted_line[2])
            total_expense += price
            expense_count += 1
            balance -= price
            list_of_lines[i] = list_of_lines[i] + " Balance " + f"{round(balance, 2)}"
        list_of_lines[i] = list_of_lines[i].replace(' ', '_')
    list_of_lines.append("Total_expense__" + f"{round(total_expense, 2)}")
    list_of_lines.append("Average_expense__" + f"{round((total_expense/expense_count), 2)}")
    result_string = '\n'.join(list_of_lines)
    return result_string

def f(x):
    return x / (math.sqrt(1 + x) + 1)

def rainfall(town, strng):
    desired_string = ""
    string_into_list = strng.splitlines()
    for i in range(len(string_into_list)):
        town_in_list = string_into_list[i].split(':')[0]
        if town_in_list == town:
            desired_string = string_into_list[i]
            break
    if not desired_string:
        return -1
    rain = [float(part.split()[1]) for part in desired_string.split(":")[1].split(",")]
    return np.array(rain)

def mean(town, strng):
    rain_array = rainfall(town, strng)
    if isinstance(rain_array, int):
        return -1
    return rain_array.mean()

def variance(town, strng):
    rain_array = rainfall(town, strng)
    if isinstance(rain_array, int):
        return -1
    return rain_array.var()

def nba_cup(strng, desired_team):
    if not desired_team:
        return ""
    team_found = False
    wins = 0
    draws = 0
    loses = 0
    points_scored = 0
    points_conceded = 0
    string_into_list = strng.split(',')
    for i in range(len(string_into_list)):
        match_parts = string_into_list[i].split()
        num_indices = [i for i, x in enumerate(match_parts) if x.isdigit()]
        i1, i2 = num_indices
        team1 = " ".join(match_parts[:i1])
        score1 = int(match_parts[i1])
        team2 = " ".join(match_parts[i1 + 1:i2])
        score2 = int(match_parts[i2])
        if team1 == desired_team:
            team_found = True
            points_scored += score1
            points_conceded += score2
            if score1 > score2:
                wins += 1
            elif score1 < score2:
                loses += 1
            else:
                draws += 1
        elif team2 == desired_team:
            team_found = True
            points_scored += score2
            points_conceded += score1
            if score2 > score1:
                wins += 1
            elif score2 < score1:
                loses += 1
            else:
                draws += 1
    total_points = (wins * 3) + draws
    if not team_found:
        return f"{desired_team}" + ":This team didn't play!"
    return f"{desired_team}" + ":W=" + f"{wins}" + ";D=" + f"{draws}" + ";L=" + f"{wins}" + ";Scored=" + f"{points_scored}" + ";Conceded=" + f"{points_conceded}" + ";Points=" + f"{total_points}"

def stock_list(stocklist, categories):
    if not stocklist:
        return ""
    count_categories = [0] * len(categories)
    for i in range(len(categories)):
        for j in range(len(stocklist)):
            stocklist_element = stocklist[j].split()
            if stocklist_element[0][0] == categories[i]:
                count_categories[i] += int(stocklist_element[1])
    return " - ".join(f"({category} : {count})" for category, count in zip(categories, count_categories))