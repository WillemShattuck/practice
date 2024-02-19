"""

"""

from my_list import MyList as mlist


def main():
    """
    Entry point
    """
    lst = mlist()

    lst.append(33)
    lst.append(22)

    print(len(lst))
    print(lst)

    v = lst.at(3)

    print(v)


if __name__ == "__main__":
    main()