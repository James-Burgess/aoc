class InputFile:
    def __init__(self, filename):
        self.filename = filename
        self.lines = None
        self.read()

    def read(self):
        with open(f"2024/d{self.filename}.txt") as f:
            file = f.read()
            self.lines = file.splitlines()

    def to_num(self):
        split_rows = [rows.split() for rows in self.lines]
        ret = []

        # TODO: see what happens if we only have one number in the row
        for row in split_rows:
            ret.append([int(x) for x in row])

        return ret

    def __iter__(self):
        for line in self.lines:
            yield line.split()

    def __getitem__(self, index):
        return self.lines[index]

    def __len__(self):
        return len(self.lines)

    def __repr__(self):
        return f'InputFile({self.filename}) with {len(self)} lines\n{self.lines[:min(10, len(self))]}'
