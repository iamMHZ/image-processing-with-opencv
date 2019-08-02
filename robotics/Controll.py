import inputs

print(inputs.devices.gamepads)

while True:
    events = inputs.get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)
