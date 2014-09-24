/*
  Calibration procedure
  
  Valve outputs should be connected to ports 2-5 of the Arduino board
  
  */
  
int digitalPin = 2;    // pin to calibrate
int openTime = 500;    // time to leave valve open in ms
int iti = 1000;         // iti in ms
int trials = 5;        // number of trials

void setup() {
  //start serial connection
  Serial.begin(9600);
  //configure pin2 and pin3 as outputs
   pinMode(digitalPin, OUTPUT);
 
}

void loop() {
  
     for (int trial = 1; trial < trials + 1; trial ++) {
       digitalWrite(digitalPin, HIGH);
       delay(openTime);
       digitalWrite(digitalPin, LOW);
       delay(iti);
  }
  
  while(1) {
  }

 }
