
def all_value_equal(lst: list) -> bool:
    """
    This program returns True if all values are same
    """
    first = lst[0]
    return all(x == first for x in lst)


def slice_me(family: list, start: int, end: int) -> list:
    """
    This extracts values in a list using the slicing method in python.
    It includes [start] and stops before [end].
    """
    first_list_len = len(family)
    second_list_len = []
    try:
        if not first_list_len == 0:
            for sub in family:
                second_list_len.append(len(sub))
            if all_value_equal(second_list_len) is not True:
                raise ValueError("All sub-list values must have same length")

            print(f"My shape is : ({first_list_len},{second_list_len[0]})")

            newList = family[start:end]
            print(f"My new shape is : ({len(newList)},{second_list_len[0]})")
            return newList

        else:
            raise AssertionError("No value found in Family list")

    except AssertionError as msg:
        print("AssertionError:", msg)

    except ValueError as msg:
        print("ValueError:", msg)

    except Exception as e:
        print("Unhandled error has occured", e)
