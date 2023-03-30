#include <Servo.h>

#define motorPin 9
#define buttonPin 2

Servo servo;
int servoPosition = 180;
int buttonState = 0;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(motorPin, OUTPUT);
  servo.attach(motorPin);
  servo.write(servoPosition);
}
int angle=0;
void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == LOW) {
    servoPosition = 0;
  } else {
    delay(3000);
    servoPosition = 180;
  }

  servo.write(servoPosition);
  delay(15);
}
