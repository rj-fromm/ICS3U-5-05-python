#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: November 2019
# This program acts as a postal service


def address_formatted(full_name, address, city, province, postal_code,
                      apt_number=None):
    # return the full formal name

    formatted = full_name
    if apt_number is not None:
        formatted = "{0} \n{1} {2} \n{3} {4} {5}".format(full_name, apt_number,
                                                         address, city,
                                                         province,
                                                         postal_code,)
    else:
        formatted = "{0} \n{1} \n{2} {3} {4}".format(full_name, address, city,
                                                     province, postal_code,)

    return formatted


def main():
    # gets a users name and prints out their formal name
    apt_number = None

    full_name = input("Enter your full name: ")
    question = input("Do you live in an apartement? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_number = input("Enter your apartment number: ")
    address = input("Enter your address (number, street): ")
    city = input("Enter your city: ")
    province = input("Enter your province (short form): ")
    postal_code = input("Enter your postal code: ")

    if apt_number is not None:
        card = address_formatted(full_name, address, city, province,
                                 postal_code, apt_number)
    else:
        card = address_formatted(full_name, address, city, province,
                                 postal_code)

    print(card)


if __name__ == "__main__":
    main()
