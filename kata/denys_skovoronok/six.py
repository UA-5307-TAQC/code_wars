"""File for solving CodeWars 6kyu tasks."""

import re


def find_nb(m):
    """Build a pile of cubes."""
    current_sum = 0
    n = 0
    while current_sum < m:
        n += 1
        current_sum += n**3

    if current_sum > m:
        return -1

    return n


def balance(book):
    """Calculate balance of receipt."""
    book = re.split(pattern=r"[,!?:;\r}{=\n ]", string=book)
    book = [i for i in book if i]
    receipt_balance = float(book[0])
    total_expense = 0
    count = 0

    receipt = f'Original Balance: {format(float(book[0]), ".2f")}\r\n'
    for i in range(1, len(book)):
        if i % 3 == 0:
            receipt += format(float(book[i]), ".2f") + " "
        else:
            receipt += book[i] + " "
        if re.match(r"[\d{1,2}]", book[i]) and i % 3 == 0:
            total_expense += float(book[i])
            count += 1
            receipt_balance -= float(book[i])

            receipt += "Balance " + str(format(receipt_balance, ".2f")) + "\r\n"

    avg_expense = total_expense / count
    receipt += (
        "Total expense  "
        + str(format(total_expense, ".2f"))
        + "\r\n"
        + "Average expense  "
        + str(format(avg_expense, ".2f"))
    )
    return str(receipt)


def f(x):
    """Floating point function."""
    return x / 2 - x**2 / 8 + x**3 / 16 - 5 * x**4 / 128


def mean(town, s):
    """Calculate average rainfall."""
    try:
        s = re.split(pattern=r"[,:\n ]", string=s)
        city_index = s.index(town)
        sum_of_rainfalls = sum(float(i) for i in s[city_index + 2 : city_index + 25 : 2])
        return sum_of_rainfalls / 12
    except ValueError:
        return -1


def variance(town, s):
    """Calculate variance."""
    try:
        s = re.split(pattern=r"[,:\n ]", string=s)
        city_index = s.index(town)
        avg_rainfalls = sum(float(i) for i in s[city_index + 2 : city_index + 25 : 2]) / 12
        deviation = [(float(i) - avg_rainfalls) ** 2 for i in s[city_index + 2 : city_index + 25 : 2]]
        avg_deviation = sum(float(i) for i in deviation) / 12
        return avg_deviation
    except ValueError:
        return -1


def nba_cup(result_sheet, to_find):
    """Calculate match statistic in games."""
    if not to_find:
        return ""

    wins = 0
    draws = 0
    loses = 0
    scored = 0
    conceded = 0
    points = 0
    played = False

    for game in result_sheet.split(","):
        pattern = r"^(.*?) (\d+(?:\.\d+)?) (.*?) (\d+(?:\.\d+)?)$"
        match = re.match(pattern, game)

        if match:
            team_1 = match.group(1)
            score_1 = match.group(2)
            team_2 = match.group(3)
            score_2 = match.group(4)

            if "." in score_1 or "." in score_2:
                return f"Error(float number):{game}"

            score_1, score_2 = int(score_1), int(score_2)

            if team_1 == to_find:
                played = True
                scored += score_1
                conceded += score_2

                if score_1 > score_2:
                    wins += 1
                    points += 3
                elif score_1 == score_2:
                    draws += 1
                    points += 1
                else:
                    loses += 1
            elif team_2 == to_find:
                played = True
                scored += score_2
                conceded += score_1

                if score_2 > score_1:
                    wins += 1
                    points += 3
                elif score_1 == score_2:
                    draws += 1
                    points += 1
                else:
                    loses += 1

    if not played:
        return f"{to_find}:This team didn't play!"

    result = "{}:W={};D={};L={};Scored={};Conceded={};Points={}"
    return result.format(to_find, wins, draws, loses, scored, conceded, points)


def stock_list(stocklist, categories):
    """Count number of books sorted by category."""
    if not stocklist or not categories:
        return ""

    result = ""
    category_dictionary = {item: 0 for item in categories}
    stocklist = [j for i in stocklist for j in i.split()]

    for key in stocklist[::2]:

        if key[0] in category_dictionary:

            category_dictionary[key[0]] += int(stocklist[stocklist.index(key) + 1])

        else:
            pass

    for key in category_dictionary:
        result += f"({key} : {category_dictionary.get(key)}) - "
    return result[:-3]
