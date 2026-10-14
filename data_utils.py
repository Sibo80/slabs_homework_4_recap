# Author: Siboniile

"""This calculates the average numbers and formates currency."""


def calculate_average(number_list):

    """
    Calculate the average list of numbers.

    :param:(list): A list if numbers 
    :return: The average of numbers 
    """
    return sum(number_list)


def format_currency(amount):
    """
    format an amount as south african rand

    param:(amount): The amount to format.

    return: The amount with R in front.
    """

    return "R" + str(round(amount, 2))


