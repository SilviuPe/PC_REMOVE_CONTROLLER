# Server-Side Documentation

## Overview
The server starts automatically and begins listening for new client connections. It sends each event to every connected client, except for simple mouse movement events (as Python registers too many of these).

## Features

### Mouse Events
- **mouseDown / mouseUp**
  - When any mouse button is pressed or released, an event is sent.
  - Dragging is detected when the left mouse button is held and moved. However, the event is still sent as a standard click event with position data.

### Display Adjustments
- Display position is sent in **percentage format**.
- On the client side, these percentages are calculated based on the screen's width and height.
- This method avoids display resolution mismatches, provided you use the same OS and programs.

### Keyboard Events
- **keyDown / keyUp**
  - An event is sent when any key is pressed or released.
  - Multiple key events (e.g., key combinations or shortcuts) can be sent in quick succession.

### Scroll Events
- The scroll event is mirrored:
  - When the host scrolls, the client performs the same scroll action.

## Suggestions
- ✅ **Use the same operating system and programs** as the host.
- This ensures better compatibility and avoids UI positioning mismatches.
