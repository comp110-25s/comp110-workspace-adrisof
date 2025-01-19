def fuel_needed(distance: int, mpg: int) -> float:
    return distance / mpg


def total_fuel_cost(distance: int, mpg: int, price_per_gallon: int) -> float:
    return fuel_needed(distance=distance, mpg=mpg) * price_per_gallon


print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))




def main_planner(guests: int) -> None:
    print: "A cozy tea party for "
    print(tea_bags(people=guests))
    print(treats(people=guests))
    print(cost(tea_count=tea_bags, treat_count=treats))

    if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

    """Caclulates tea bags, treats, and cost in one go!"""






