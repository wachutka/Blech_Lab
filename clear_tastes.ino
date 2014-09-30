/* Clear out tastants

*/

int digitalPin1 = 22;     // output pin 1
int digitalPin2 = 23;     // output pin 2
int digitalPin3 = 24;
int openTime = 5000;   // valve open time in ms

void setup() {
  //start serial connection
  Serial.begin(9600);
  //configure pin2 and pin3 as outputs

  pinMode(digitalPin1, OUTPUT);
  pinMode(digitalPin2, OUTPUT);
//  pinMode(digitalPin3, OUTPUT);
  
  digitalWrite(digitalPin1, HIGH);
  digitalWrite(digitalPin2, HIGH);
//  digitalWrite(digitalPin3, HIGH);

  delay(openTime);
  
  digitalWrite(digitalPin1, LOW);
  digitalWrite(digitalPin2, LOW);
//  digitalWrite(digitalPin3, LOW);


}

void loop() {
  // put your main code here, to run repeatedly:

}
