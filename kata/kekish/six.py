"""6kuy tasks."""

import math
import re


def find_nb(m):
    """Build a pile of Cubes."""
    volume = 0
    n = 0

    while volume < m:
        n += 1
        volume += n**3

    if volume == m:
        return n
    return -1


def balance(book):
    """Easy Balance Checking."""
    num_pattern = r"\d+\.?\d*"
    str_pattern = r"[a-zA-Z]"
    lines_arr = book.split("\n")
    new_balance = float(re.findall(num_pattern, lines_arr[0])[0])
    total_expense = 0
    result = [f"Original Balance: {new_balance:.2f}"]

    for line in lines_arr[1:]:
        line_data = line.split(" ")

        if line_data == [""]:
            continue

        check = int(re.findall(num_pattern, line_data[0])[0])
        check = "0" * (3 - len(str(check))) + str(check)
        operation = "".join(re.findall(str_pattern, line_data[1]))
        price = float(re.findall(num_pattern, line_data[2])[0])
        new_balance -= price
        total_expense += price

        result.append(f"{check} {operation} {price:.2f} Balance {new_balance:.2f}")

    average_expense = total_expense / (len(result) - 1)
    result.append(f"Total expense  {round(total_expense, 2):.2f}")
    result.append(f"Average expense  {round(average_expense, 2):.2f}")

    return "\r\n".join(result)


def f(x):
    """Floating-point Approximation."""
    return x / (math.sqrt(1 + x) + 1)


def get_data(town, s):
    """Parse and serialize data."""
    lines_arr = s.split("\n")
    line = [line for line in lines_arr if re.match(rf"{town}:", line)]

    print(line)
    if len(line) == 0:
        return -1

    data = line[0].split(":")[1].split(",")
    return [float(month.split(" ")[1]) for month in data]


def mean(town, s):
    """Get mean value."""
    numbers = get_data(town, s)

    if numbers == -1:
        return -1

    return sum(numbers) / len(numbers)


def variance(town, s):
    """Get variance."""
    mean_value = mean(town, s)

    if mean_value == -1:
        return -1

    numbers = get_data(town, s)
    return sum((n - mean_value) ** 2 for n in numbers) / len(numbers)


def serialize_match_data(match_str):
    """Parse and serialize match data."""
    try:
        arr = re.split(r"(?<=\d)\s(?=[a-zA-Z])", match_str, 1)
        arr_of_split_data = [re.split(r"\s(?=[a-zA-Z\d]*$)", data) for data in arr]
        return [[data[0], int(data[1])] for data in arr_of_split_data]
    except ValueError as err:
        raise ValueError(f"Error(float number):{match_str}") from err


def nba_cup(result_sheet, to_find):
    """Rank NBA team."""
    if not to_find:
        return ""
    if not re.search(rf"{to_find}\s", result_sheet):
        return f"{to_find}:This team didn't play!"

    arr = result_sheet.split(",")
    try:
        serialized_team_matches = [serialize_match_data(match_str) for match_str in arr if to_find in match_str]
    except ValueError as e:
        return str(e)

    wins, draws, loses, scored, conceded, points = 0, 0, 0, 0, 0, 0

    for data in serialized_team_matches:
        is_draw = data[0][1] == data[1][1]
        first_wins = data[0][1] > data[1][1] and not is_draw
        is_first_in_data = data[0][0] == to_find
        is_win = is_first_in_data and first_wins or not is_first_in_data and not first_wins

        scored += data[0][1] if is_first_in_data else data[1][1]
        conceded += data[1][1] if is_first_in_data else data[0][1]

        if is_win:
            wins += 1
            points += 3
        else:
            loses += 1

        if is_draw:
            draws += 1
            points += 1

    return f"{to_find}:W={wins};D={draws};L={loses};Scored={scored};Conceded={conceded};Points={points}"


def stock_list(stocklist, categories):
    """Help the bookseller."""
    if not stocklist or not categories:
        return ""

    parsed_arr = [[line[0], re.search(r"\d+", line).group()] for line in stocklist]
    return_arr = [[category, 0] for category in categories]

    for category in return_arr:
        arr_of_current_category_stock = list(filter(lambda parsed_data: parsed_data[0] == category[0], parsed_arr))
        return_arr[return_arr.index(category)][1] = sum([int(x[1]) for x in arr_of_current_category_stock])

    return " - ".join([f"({v1} : {v2})" for [v1, v2] in return_arr])
