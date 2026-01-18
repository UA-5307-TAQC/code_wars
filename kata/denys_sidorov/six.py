import math
import numpy as np

def ex12_cubes(m):
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

def ex13_balance_checking(check_book):
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

def ex14_floating_point(x):
    return x / (math.sqrt(1 + x) + 1)

data = """Rome:Jan 81.2,Feb 63.2,Mar 70.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,Aug 27.5,Sep 60.9,Oct 117.7,Nov 111.0,Dec 97.9
London:Jan 48.0,Feb 38.9,Mar 39.9,Apr 42.2,May 47.3,Jun 52.1,Jul 59.5,Aug 57.2,Sep 55.4,Oct 62.0,Nov 59.0,Dec 52.9
Paris:Jan 182.3,Feb 120.6,Mar 158.1,Apr 204.9,May 323.1,Jun 300.5,Jul 236.8,Aug 192.9,Sep 66.3,Oct 63.3,Nov 83.2,Dec 154.7
NY:Jan 108.7,Feb 101.8,Mar 131.9,Apr 93.5,May 98.8,Jun 93.6,Jul 102.2,Aug 131.8,Sep 92.0,Oct 82.3,Nov 107.8,Dec 94.2
Vancouver:Jan 145.7,Feb 121.4,Mar 102.3,Apr 69.2,May 55.8,Jun 47.1,Jul 31.3,Aug 37.0,Sep 59.6,Oct 116.3,Nov 154.6,Dec 171.5
Sydney:Jan 103.4,Feb 111.0,Mar 131.3,Apr 129.7,May 123.0,Jun 129.2,Jul 102.8,Aug 80.3,Sep 69.3,Oct 82.6,Nov 81.4,Dec 78.2
Bangkok:Jan 10.6,Feb 28.2,Mar 30.7,Apr 71.8,May 189.4,Jun 151.7,Jul 158.2,Aug 187.0,Sep 319.9,Oct 230.8,Nov 57.3,Dec 9.4
Tokyo:Jan 49.9,Feb 71.5,Mar 106.4,Apr 129.2,May 144.0,Jun 176.0,Jul 135.6,Aug 148.5,Sep 216.4,Oct 194.1,Nov 95.6,Dec 54.4
Beijing:Jan 3.9,Feb 4.7,Mar 8.2,Apr 18.4,May 33.0,Jun 78.1,Jul 224.3,Aug 170.0,Sep 58.4,Oct 18.0,Nov 9.3,Dec 2.7
Lima:Jan 1.2,Feb 0.9,Mar 0.7,Apr 0.4,May 0.6,Jun 1.8,Jul 4.4,Aug 3.1,Sep 3.3,Oct 1.7,Nov 0.5,Dec 0.7"""

data1 = """Rome:Jan 90.2,Feb 73.2,Mar 80.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,Aug 27.5,Sep 60.9,Oct 147.7,Nov 121.0,Dec 97.9
London:Jan 58.0,Feb 38.9,Mar 49.9,Apr 42.2,May 67.3,Jun 52.1,Jul 59.5,Aug 77.2,Sep 55.4,Oct 62.0,Nov 69.0,Dec 52.9
Paris:Jan 182.3,Feb 120.6,Mar 188.1,Apr 204.9,May 323.1,Jun 350.5,Jul 336.8,Aug 192.9,Sep 66.3,Oct 63.3,Nov 83.2,Dec 154.7
NY:Jan 128.7,Feb 121.8,Mar 151.9,Apr 93.5,May 98.8,Jun 93.6,Jul 142.2,Aug 131.8,Sep 92.0,Oct 82.3,Nov 107.8,Dec 94.2
Vancouver:Jan 155.7,Feb 121.4,Mar 132.3,Apr 69.2,May 85.8,Jun 47.1,Jul 31.3,Aug 37.0,Sep 69.6,Oct 116.3,Nov 154.6,Dec 171.5
Sydney:Jan 123.4,Feb 111.0,Mar 151.3,Apr 129.7,May 123.0,Jun 159.2,Jul 102.8,Aug 90.3,Sep 69.3,Oct 82.6,Nov 81.4,Dec 78.2
Bangkok:Jan 20.6,Feb 28.2,Mar 40.7,Apr 81.8,May 189.4,Jun 151.7,Jul 198.2,Aug 197.0,Sep 319.9,Oct 230.8,Nov 57.3,Dec 9.4
Tokyo:Jan 59.9,Feb 81.5,Mar 106.4,Apr 139.2,May 144.0,Jun 186.0,Jul 155.6,Aug 148.5,Sep 216.4,Oct 194.1,Nov 95.6,Dec 54.4
Beijing:Jan 13.9,Feb 14.7,Mar 18.2,Apr 18.4,May 43.0,Jun 88.1,Jul 224.3,Aug 170.0,Sep 58.4,Oct 38.0,Nov 19.3,Dec 2.7
Lima:Jan 11.2,Feb 10.9,Mar 10.7,Apr 10.4,May 10.6,Jun 11.8,Jul 14.4,Aug 13.1,Sep 23.3,Oct 1.7,Nov 0.5,Dec 10.7"""

def ex15_rainfall(town, strng):
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
    rain_array = ex15_rainfall(town, strng)
    if isinstance(rain_array, int):
        return -1
    return rain_array.mean()

def variance(town, strng):
    rain_array = ex15_rainfall(town, strng)
    if isinstance(rain_array, int):
        return -1
    return rain_array.var()

r = """Los Angeles Clippers 104 Dallas Mavericks 88,New York Knicks 101 Atlanta Hawks 112,Indiana Pacers 103 Memphis Grizzlies 112,  Los Angeles Clippers 100 Boston Celtics 120"""

def ex16_nba_cup(strng, desired_team):
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

a = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
b = ["A", "B", "C", "W"]

def ex17_bookseller(stocklist, categories):
    count_categories = [0] * len(categories)
    for i in range(len(categories)):
        for j in range(len(stocklist)):
            stocklist_element = stocklist[j].split()
            if stocklist_element[0][0] == categories[i]:
                count_categories[i] += int(stocklist_element[1])
    return " - ".join(f"({category} : {count})" for category, count in zip(categories, count_categories))