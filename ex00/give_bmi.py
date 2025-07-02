def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    This program takes as input a list of height in meter
    and a list of weight in kg.
    It returns a list of BMI calculated based on input datas.
    """
    bmi_list = []
    try:
        if len(height) != len(weight):
            raise IndexError("Numbers of input in the two lists are not same")
        else:
            for h, w in zip(height, weight):
                if (
                    not isinstance(h, (int, float))
                    or not isinstance(w, (int, float))
                ):
                    raise TypeError("Must contain only int or float")
                val = w / (h * h)
                bmi_list.append(val)
        return bmi_list

    except IndexError as msg:
        print("IndexError:", msg)

    except TypeError as msg:
        print("TypeError:", msg)

    except Exception as e:
        print("Unhandled error has occured:", e)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Comapare a list of BMI to the second input and return a list True/False
    If a BMI is equal or bigger than the second input,
    it return True, otherwise, it returns False.
    """
    bmi_tf = []
    try:
        if len(bmi) == 0:
            raise IndexError("No data found in BMI list")

        for b in bmi:
            if b >= limit:
                bmi_tf.append(True)
            else:
                bmi_tf.append(False)

        return bmi_tf

    except IndexError as msg:
        print("IndexError:", msg)

    except Exception as e:
        print("Unhandled error has occured:", e)
