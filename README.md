# Interactive CS2

Make CS2 harder with a real-life flashbang created by a light bar, and shaking recoil to make the game more real!

Created using Python, a cs2.cfg file, and a bit of hardware. Demo avaliable here: https://www.youtube.com/watch?v=v8uHIMJPxEo

# Light bar flashbang circuitry

![IMG_1678](https://github.com/user-attachments/assets/6803fb5c-b8ff-4513-8f8d-1ca9ab3d0534)

A relay controlled through an arduino is used to toggle the lightbar on and off.

![IMG_1680](https://github.com/user-attachments/assets/fb21ae14-24f6-4afe-9fae-953b6aa5527f)

A USB-C to USB-A cord that is stripped is used to directly power on the lightbar, by soldering the jumpers onto the furthest lines.

# Shaking table circuitry

![PXL_20250316_004412096](https://github.com/user-attachments/assets/2082795e-ca1b-41c1-9f32-14e63461ce81)

A mosfet circuit that is controlled through another pin on the arduino (leftmost gate) and two power cables are used to provide power to the motor. When the script tells it to, the mosfet will let current through, and power the motor.

# Scripting

Counter Strike 2 has a built-in configuration file name that will host the game's data to a local server, in our case: 127.0.0.1:3000. We then setup the Python script to listen to this particular location. Whenever an event happens, a JSON file is outputted, and we parse to look for the important events: Flashbang thrown and Gun fired.

Finally, using arduino's Serial, we write to the plugged-in USB-A through a USB-A COM. This is how we write and control with the motor, and the flashbang, all with python and a bit of C++ to configure the hardware.
