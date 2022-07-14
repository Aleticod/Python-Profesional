
def make_division_by(n: int):

    def division(d: int):
        assert type(d) == int, "Solo se debe usar valores enteros"
        return d // n
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))


if __name__ == '__main__':
    run()