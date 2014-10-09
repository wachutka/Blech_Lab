void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  randomSeed(analogRead(3));
  
  int digitalPin1 = 23;  // Active Valve 1
  int digitalPin2 = 23;  // Active Valve 2
  int digitalPin3 = 27;  // Tone output
  int digitalPin4 = 28;  // Poke input 1
  int digitalPin5 = 29;  // Poke input 2
  int digitalPin6 = 22;  // Passive Valve 1
  int digitalPin7 = 24;  // Passive Valve 2
  
  pinMode(digitalPin1, OUTPUT);
  pinMode(digitalPin2, OUTPUT);
  pinMode(digitalPin3, OUTPUT);
  pinMode(digitalPin4, INPUT_PULLUP);
  pinMode(digitalPin5, INPUT_PULLUP);
  pinMode(digitalPin6, OUTPUT);
  pinMode(digitalPin7, OUTPUT);
  
  digitalWrite(digitalPin1, LOW);
  digitalWrite(digitalPin2, LOW);
  digitalWrite(digitalPin3, LOW);
  digitalWrite(digitalPin6, LOW);
  digitalWrite(digitalPin7, LOW);
  
  int tonedur = 400;  // Tone duration in ms
  int iti = 15000;  // iti in ms
  int iti2 = 25000;    // punishment iti
  int trials = 100;  // number of trials
  int opentime1 = 10;  // Active valve 1 open time from calibration
  int opentime2 = 10;  // Active valve 2 open time from calibration
  int opentime3 = 11;  // Passive valve 1 open time from calibration
  int opentime4 = 9;  // Passive valve 2 open time from calibration
  
  int correct = 0;    // counter for correct pokes
  int wrong = 0;      // counter for incorrect pokes
  int order[trials];
  delay(3000);
 
  for (int i = 0; i < trials; i ++) {
    if (i % 2 == 0) {
      order[i] = 1;
    }
    else {
      order[i] = 0;
    }
  }

  Serial.print("Starting Array: ");
  for (int i = 0; i < trials; i ++) {
    Serial.print(order[i]);
  }
   Serial.println();
   // Play first tone
   digitalWrite(digitalPin3, HIGH);
   delay(tonedur);
   digitalWrite(digitalPin3, LOW);
 
 // Begin trials
 for (int i = 0; i < trials;) {
   
   if (order[i] == 0 && digitalRead(digitalPin4) == LOW) {

       digitalWrite(digitalPin1, HIGH);
       delay(opentime1);
       digitalWrite(digitalPin1, LOW);
       correct++;
       delay(iti);
       i ++;
       Serial.print("Trial ");
       Serial.print(i);
       Serial.print(" of ");
       Serial.print(trials);
       Serial.println(" completed.");
       Serial.print(correct);
       Serial.println(" correct pokes thus far.");
       digitalWrite(digitalPin3, HIGH);
       delay(tonedur);
       digitalWrite(digitalPin3, LOW);
       if (order[i+1] == 0) {
         digitalWrite(digitalPin6, HIGH);
         delay(opentime3);
         digitalWrite(digitalPin6, LOW);
       }
       else if (order[i+1] == 1) {
         digitalWrite(digitalPin7, HIGH);
         delay(opentime4);
         digitalWrite(digitalPin7, LOW);
       } 
   }
   else if (order[i] == 0 && digitalRead(digitalPin5) == LOW) {
     while (1) {
       if (digitalRead(digitalPin5) == HIGH) {
       wrong++;
       break;
       }
       delay(iti2);
       i++;
       Serial.print("Trial ");
       Serial.print(i);
       Serial.print(" of ");
       Serial.print(trials);
       Serial.println(" completed.");
       Serial.print(correct);
       Serial.println(" correct pokes thus far.");
       digitalWrite(digitalPin3, HIGH);
       delay(tonedur);
       digitalWrite(digitalPin3, LOW);
       if (order[i+1] == 0) {
         digitalWrite(digitalPin6, HIGH);
         delay(opentime3);
         digitalWrite(digitalPin6, LOW);
       }
       else if (order[i+1] == 1) {
         digitalWrite(digitalPin7, HIGH);
         delay(opentime4);
         digitalWrite(digitalPin7, LOW);
       }
     }
   }
   else if (order[i] == 1 && digitalRead(digitalPin5) == LOW) {

      digitalWrite(digitalPin2, HIGH);
      delay(opentime2);
      digitalWrite(digitalPin2, LOW);
      correct++;
      delay(iti);
      i ++;
      Serial.print("Trial ");
      Serial.print(i);
      Serial.print(" of ");
      Serial.print(trials);
      Serial.println(" completed.");
      Serial.print(correct);
      Serial.println(" correct pokes thus far.");
      digitalWrite(digitalPin3, HIGH);
      delay(tonedur);
      digitalWrite(digitalPin3, LOW);  
      if (order[i+1] == 0) {
         digitalWrite(digitalPin6, HIGH);
         delay(opentime3);
         digitalWrite(digitalPin6, LOW);
       }
       else if (order[i+1] == 1) {
         digitalWrite(digitalPin7, HIGH);
         delay(opentime4);
         digitalWrite(digitalPin7, LOW);
       }     
   }
      else if (order[i] == 1 && digitalRead(digitalPin4) == LOW) {
        while (1) {
          if (digitalRead(digitalPin4) == HIGH) {   
            wrong++;
            break;
          }
         delay(iti2);
         i++;
         Serial.print("Trial ");
         Serial.print(i);
         Serial.print(" of ");
         Serial.print(trials);
         Serial.println(" completed.");
         Serial.print(correct);
         Serial.println(" correct pokes thus far.");
         digitalWrite(digitalPin3, HIGH);
       delay(tonedur);
       digitalWrite(digitalPin3, LOW);
       if (order[i+1] == 0) {
         digitalWrite(digitalPin6, HIGH);
         delay(opentime3);
         digitalWrite(digitalPin6, LOW);
       }
       else if (order[i+1] == 1) {
         digitalWrite(digitalPin7, HIGH);
         delay(opentime4);
         digitalWrite(digitalPin7, LOW);
       }
        }
      }
   }
}

void loop() {

}
