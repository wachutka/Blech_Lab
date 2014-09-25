/* Clear out tastants

*/

int digitalPin1 = 2;     // output pin 1
int digitalPin2 = 3;     // output pin 2
int openTime = 10000;   // valve open time in ms

void setup() {
  //start serial connection
  Serial.begin(9600);
  //configure pin2 and pin3 as outputs

  pinMode(digitalPin1, OUTPUT);
  pinMode(digitalPin2, OUTPUT);

  digitalWrite(digitalPin1, HIGH);
  digitalWrite(digitalPin2, HIGH);

  delay(openTime);
  
  digitalWrite(digitalPin1, LOW);
  digitalWrite(digitalPin1, LOW);

//  digitalWrite(digitalPin1, HIGH);
//  digitalWrite(digitalPin2, HIGH);
//  delay(openTime);
//  digitalWrite(digitalPin1, LOW);
//  digitalWrite(digitalPin2, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:

}
