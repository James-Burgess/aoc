
def create(day):

    with open('template.py') as f:
        template = f.read()

    template = template.replace("{day}", day)

    with open(f"day_{day}.py", "w") as f:
        f.write(template)

    with open(f"d{day}.txt", "w") as f:
        f.write("")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog='aoc_maker',
        description='scafolds the aoc for the day',
    )

    parser.add_argument('day')

    args = parser.parse_args()

    create(args.day)
