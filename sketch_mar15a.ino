// Define pin numbers or any hardware you want to control here
int flashbangPin = 7;  // Example pin for flashbang (can change to suit your setup)
int firePin = 9;       // Example pin for fire (can change to suit your setup)

void setup() {
  Serial.begin(9600);        // Initialize serial communication
  pinMode(flashbangPin, OUTPUT); // Set the flashbang pin as output
  pinMode(firePin, OUTPUT);      // Set the fire pin as output
}

void loop() {
  if (Serial.available() > 0) { // Check if data is available to read
    char command = Serial.read(); // Read the incoming byte

    // Call the appropriate function based on the command
    if (command == 'F') { // Flashbang command
      flashbang();
    }
    else if (command == 'R') { // Fire command
      fire();
    }
  }
}

// Flashbang function (currently empty)
void flashbang() {
  // Implement the behavior for flashbang here
  // Example: Turn on the flashbang (e.g., blink an LED)
  digitalWrite(flashbangPin, HIGH);
  delay(2000); // Wait for 1 second
  digitalWrite(flashbangPin, LOW);
}

// Fire function (currently empty)
void fire() {
  digitalWrite(firePin, HIGH);
  delay(250); // Wait for 1 second
  digitalWrite(firePin, LOW);

}
