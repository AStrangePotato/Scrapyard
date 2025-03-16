#!/usr/bin/env python3.8

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import serial
import time

arduino = serial.Serial('COM3', 9600, timeout=1)
# Store previous ammo counts
previous_ammo = {}

def send_flashbang():
    arduino.write(b'F')  # Send 'F' to trigger the flashbang function
    print("Flashbang triggered!")

def send_fire():
    arduino.write(b'R')  # Send 'R' to trigger the fire function
    print("Fire triggered!")
    
class GSIHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global previous_ammo  # Keep track of ammo count
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data)
            player_state = data.get("player", {}).get("state", {})
            weapons = data.get("player", {}).get("weapons", {})

            # Check flashbang intensity
            flashed = player_state.get("flashed", 0)
            if flashed > 0:
                print(f"🔥 Player is flashbanged! Intensity: {flashed}")
                send_flashbang()

            for weapon_id, weapon_data in weapons.items():
                weapon_name = weapon_data.get("name", "unknown")
                ammo_clip = weapon_data.get("ammo_clip", None)  # Ammo in current mag

                if weapon_name not in previous_ammo:
                    previous_ammo[weapon_name] = ammo_clip  # Initialize tracking

                if ammo_clip is not None and previous_ammo[weapon_name] is not None:
                    if ammo_clip < previous_ammo[weapon_name]:  # Ammo decreased -> shot fired
                        print(f"🔫 {weapon_name}: fired (ammo left: {ammo_clip})")
                        send_fire()
                        
                # Update previous ammo count
                previous_ammo[weapon_name] = ammo_clip

        except json.JSONDecodeError:
            print("Error: Received invalid JSON data.")

        self.send_response(200)
        self.end_headers()

# Start server without unnecessary logging
class SilentHTTPServer(HTTPServer):
    def handle_error(self, request, client_address):
        pass  # Suppresses unwanted error messages

server = SilentHTTPServer(('127.0.0.1', 3000), GSIHandler)
print("🎮 GSI Server listening on port 3000...")
server.serve_forever()
