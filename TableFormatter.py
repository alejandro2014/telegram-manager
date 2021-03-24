class TableFormatter:
    def __init__(self):
        pass

    def print_table(self, rows_info):
        fields = list(rows_info[0].keys())
        max_lengths = self.calculate_max_lengths(rows_info)
        border = self.get_border(max_lengths)
        header = self.get_header(fields, max_lengths)

        print(border)
        print(header)
        print(border)

        for i, row_info in enumerate(rows_info):
            fields_mod = []

            for i, field in enumerate(fields):
                spaces_no = self.calculate_spaces(row_info[field], max_lengths[i])
                field_mod = f"{row_info[field]}{' ' * spaces_no}"
                fields_mod.append(field_mod)

            print(f"| {' | '.join(fields_mod)} |")

        print(border)

    def calculate_max_lengths(self, rows_info):
        fields = list(rows_info[0].keys())
        return list(map(lambda f: self.calculate_max_length(f, rows_info), fields))

    def calculate_max_length(self, field, rows_info):
        max_length = 0

        for row_info in rows_info:
            if len(row_info[field]) > max_length:
                max_length = len(row_info[field])

        return max_length

    def calculate_spaces(self, name, max_length):
        return max_length - len(name)

    def get_border(self, max_lengths):
        max_lengths_mod = list(map(lambda ml: f"{'-' * ml}", max_lengths))

        return f"+-{'-+-'.join(max_lengths_mod)}-+"

    def get_header(self, columns, max_lengths):
        columns_mod = []

        for index, v in enumerate(columns):
            columns_mod.append(f"{columns[index]}{' ' * (max_lengths[index] - len(columns[index]))}")

        return f"| {' | '.join(columns_mod)} |"
