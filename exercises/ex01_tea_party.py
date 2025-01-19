"""Planning a cozy tea party for 334: tea, treats, and cost!"""

__author__: str = "730549114"


def main_planner(guests: int) -> None:
    """Caclulates tea bags, treats, and cost in one go!"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculates how many tea bags needed with parameter people"""
    return people * 2


def treats(people: int) -> float:
    """Calculates how many treats needed with parameter people"""
    return 1.5 * tea_bags(people=people)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates cost based on parameters tea count and treat count"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
