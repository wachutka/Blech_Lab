/*
  Delivers passive taste deliveries
  *Need to add tone*
  
  Valve outputs should be connected to ports 2-5 of the Arduino board
  
*/
  
int digitalPin1 = 2;    // output pin
int digitalPin2 = 3;    // output pin
int openTime1 = 500;    // time to leave valve 1 open in ms
int openTime2 = 500;    // time to leave valve 2 open in ms
int iti = 5000;         // iti in ms
int trials = 10;        // number of trials

void setup() {
  //start serial connection
  Serial.begin(9600);
  //configure pin2 and pin3 as outputs
   pinMode(digitalPin1, OUTPUT);
   pinMode(digitalPin2, OUTPUT);
 
}

void loop() {
  
  for (int trial = 1; trial < trials + 1; trial ++) {
    digitalWrite(digitalPin1, HIGH);
    delay(openTime1);
    digitalWrite(digitalPin1, LOW);
    delay(iti);
    digitalWrite(digitalPin2, HIGH);
    delay(openTime2);
    digitalWrite(digitalPin2, LOW);
    delay(iti);
  }
  
  while(1) {
  }
  
}
