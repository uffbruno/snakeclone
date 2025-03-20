from abc import abstractmethod
from enum import Enum, auto

from pygame import Surface


class GameState(Enum):
    NO_CHANGE = auto()
    INITIAL_SCREEN = auto()
    OPTIONS_SCREEN = auto()
    PLAYING = auto()
    PLAYER_LOST = auto()
    LEVEL_CLEAR = auto()
    GAME_OVER = auto()
    CONGRATS = auto()
    ENDING_SCREEN = auto()
    CREDITS = auto()
    EXIT = auto()


class gamescreen:
    @abstractmethod
    def init(self, display: Surface):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def handle_input(self):
        pass
