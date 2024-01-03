class Utilities:
    @staticmethod
    def correct_pos(position: int, max_value: int) -> int:
        if position < 0:
            position = max_value - 1
        if position >= max_value:
            position = 0

        return position
