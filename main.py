# custom switch to calculate all routes
def switch(route):
    if route == "AB":
        return 5
    elif route == "BC":
        return 4
    elif route == "CD":
        return 8
    elif route == "DC":
        return 8
    elif route == "DE":
        return 6
    elif route == "AD":
        return 5
    elif route == "CE":
        return 2
    elif route == "EB":
        return 3
    elif route == "AE":
        return 7
    else:
        return "NO SUCH ROUTE"


def get_routes(name):
    routes = []
    total_distance = 0
    for x in range(len(name)):
        if x + 1 < len(name):
            routes.append(f'{name[x]}{name[x + 1]}')
    for route in routes:
        distance = switch(route)
        if distance == "NO SUCH ROUTE":
            return distance
        else:
            total_distance += distance

    return total_distance


if __name__ == '__main__':
    while input("check Route ?(Y) to continue or any other key to cancel : ").upper() == "Y":

        input_test = input("\nPlease enter route as string example CDC OR CEBC : ")

        if input_test.isalpha():
            input_test.strip()
            print(get_routes(input_test.upper()))
        else:
            print("Invalid string...Avoid special characters or/and numbers")

