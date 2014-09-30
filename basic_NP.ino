/*
  Delivers taste deliveries following pokes
  *Need to add tone*
  
  Valve outputs should be connected to ports 2-5 of the Arduino board
  
*/
  
int digitalPin1 = 22;     // output pin 1
int digitalPin2 = 23;     // output pin 2
int openTime1 = 11;       // time to leave valve 1 open in ms
int openTime2 = 11;       // time to leave valve 2 open in ms
int iti1 = 7000;         // first iti in ms
int iti2 = 10000;         // second iti in ms
int tonedur = 400;      // tone duration in ms
int trials1 = 50;         // number of trials for first iti
int trials2 = 100;         // total number of trials

int digitalPin3 = 28;     // input pin 1
int digitalPin4 = 29;     // input pin 2

int digitalPin5 = 27;    // output pin 3 for tone

void setup() {
  //start serial connection
  Serial.begin(9600);
  //configure pin2 and pin3 as outputs
   pinMode(digitalPin1, OUTPUT);
   pinMode(digitalPin2, OUTPUT);
   pinMode(digitalPin5, OUTPUT);
   digitalWrite(digitalPin1, LOW);
   digitalWrite(digitalPin2, LOW);
   digitalWrite(digitalPin5, LOW);
   pinMode(digitalPin3, INPUT_PULLUP);
   pinMode(digitalPin4, INPUT_PULLUP);

   
   for (int trial = 1; trial <= trials1;) {
       if (digitalRead(digitalPin3) == LOW) {
        digitalWrite(digitalPin1, HIGH);
        delay(openTime1);
        digitalWrite(digitalPin1, LOW);
        Serial.println("Completed trial number"); 
        Serial.println(trial);
        delay(iti1);
        digitalWrite(digitalPin5, HIGH);
        delay(tonedur);
        digitalWrite(digitalPin5, LOW);
        trial ++;
    }
    else if(digitalRead(digitalPin4) == LOW) {
      digitalWrite(digitalPin2, HIGH);
      delay(openTime2);
      digitalWrite(digitalPin2, LOW);
      Serial.println("Completed trial number"); 
      Serial.println(trial); 
      delay(iti1);
      digitalWrite(digitalPin5, HIGH);
      delay(tonedur);
      digitalWrite(digitalPin5, LOW);
      trial ++;
    }
  }
  for (int trial = trials1 +1; trial <= trials2;) {
    if (digitalRead(digitalPin3) == LOW) {
      digitalWrite(digitalPin1, HIGH);
      delay(openTime1);
      digitalWrite(digitalPin1, LOW);
      delay(iti2);
      Serial.println("Completed trial number"); 
      Serial.println(trial); 
      digitalWrite(digitalPin5, HIGH);
      delay(tonedur);
      digitalWrite(digitalPin5, LOW);
      trial ++;
    }
    else if(digitalRead(digitalPin4) == LOW) {
      digitalWrite(digitalPin2, HIGH);
      delay(openTime2);
      digitalWrite(digitalPin2, LOW);
      delay(iti2);
      Serial.println("Completed trial number"); 
      Serial.println(trial); 
      delay(iti2);
      digitalWrite(digitalPin5, HIGH);
      delay(tonedur);
      digitalWrite(digitalPin5, LOW);
      trial ++;
    }
  }
   
 
}

void loop() {
  
}
