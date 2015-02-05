/*
  Delivers passive taste deliveries
  *Need to add tone*
  
  Valve outputs should be connected to ports 2-5 of the Arduino board
  
*/
  
int digitalPin1 = 2;    // output pin
int digitalPin2 = 3;    // output pin
int openTime = 0.2;    // stim duration in ms
int iti = 3;           // iti in ms
int trials = 12;        // number of trials

void setup() {
  //start serial connection
  Serial.begin(9600);
  //configure pin2 and pin3 as outputs
   pinMode(digitalPin1, OUTPUT);
   pinMode(digitalPin2, OUTPUT);
 
}

void loop() {
  for (int repeat = 1; repeat < repeats + 1; repeat ++);
    for (int trial = 1; trial < trials + 1; trial ++) {
      digitalWrite(digitalPin1, HIGH);
      delay(openTime);
      digitalWrite(digitalPin1, LOW);
      delay(iti);
    }
    
    delay(5000);
    
    for (int trial = 1; trial < trials + 1; trial ++) {
      digitalWrite(digitalPin2, HIGH);
      delay(openTime);
      digitalWrite(digitalPin2, LOW);
      delay(iti);
    }
  }
  while(1) {
  }
  
}
