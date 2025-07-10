import pyautogui
import time

# Wait 3 seconds so you can switch to the target window



class MouseController(object):

    """
    Object to control the mouse actions
    """

    def __init__(self) -> None:

        pass

    def move(self, position: list) -> None:
        """

        :param position: list [x, y]
        :return: None
        """
        pyautogui.moveTo(position[0], position[1], duration=0.2)

    def click(self) -> None:
        """
        Method used to press left click
        :return: None
        """
        pyautogui.click()

    def double_click(self) -> None:
        """
        Method used to press double click
        :return: None
        """
        pyautogui.doubleClick()

    def right_click(self) -> None:
        """
        Method used to press right click
        :return: None
        """
        pyautogui.rightClick()
