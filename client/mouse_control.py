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

MouseController().move([200,300])
# # Move mouse to a specific screen position (x=100, y=200)
# pyautogui.moveTo(100, 200, duration=1)  # duration=1s for smooth movement
#
# # Perform a left click
# pyautogui.click()
#
# # Move to another location and double-click
# pyautogui.moveTo(300, 400, duration=1)
# pyautogui.doubleClick()
#
# # Move and right-click
# pyautogui.moveTo(500, 500, duration=1)
# pyautogui.rightClick()
#
# # Scroll down (positive = up, negative = down)
# pyautogui.scroll(-500)
#
# # Optional: Drag the mouse (like selecting)
# pyautogui.moveTo(600, 600, duration=1)
# pyautogui.dragTo(700, 700, duration=2, button='left')
