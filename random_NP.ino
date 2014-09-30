void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  randomSeed(analogRead(3));
  
  int digitalPin1 = 2;  // Active Valve 1
  int digitalPin2 = 3;  // Active Valve 2
  int digitalPin3 = 4;  // Tone output
  int digitalPin4 = 5;  // Poke input 1
  int digitalPin5 = 6;  // Poke input 2
  int digitalPin6 = 2;  // Passive Valve 1
  int digitalPin7 = 2;  // Passive Valve 2
  
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
  int iti = 5000;  // iti in ms
  int trials = 10;  // number of trials
  int opentime1 = 100;  // Active valve 1 open time from calibration
  int opentime2 = 100;  // Active valve 2 open time from calibration
  int opentime3 = 100;  // Passive valve 1 open time from calibration
  int opentime4 = 100;  // Passive valve 2 open time from calibration
  
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
  
  for (int a = 0; a < trials; a ++) {
    int r = random(a,trials-1);
    int temp = order[a];
    order[a] = order[r];
    order[r] = temp;
  }
  
   Serial.println();
   Serial.print("Output Array: ");
   
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
       delay(iti);
       i ++;
       Serial.print("Trial ");
       Serial.print(i);
       Serial.print(" of ");
       Serial.print(trials);
       Serial.println(" completed.");
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
   else if (order[i] == 1 && digitalRead(digitalPin5) == LOW) {

      digitalWrite(digitalPin2, HIGH);
      delay(opentime2);
      digitalWrite(digitalPin2, LOW);
      delay(iti);
      i ++;
      Serial.print("Trial ");
      Serial.print(i);
      Serial.print(" of ");
      Serial.print(trials);
      Serial.println(" completed.");
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

void loop() {

}
