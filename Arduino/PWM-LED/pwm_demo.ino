void setup() {
  // put your setup code here, to run once:
  pinMode(9, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(9,0);
  delay(300);
  analogWrite(9,64);
  delay(300);
  analogWrite(9,128);
  delay(300);
  analogWrite(9,192);
  delay(300);
  analogWrite(9,255);
  delay(300);
  analogWrite(9,192);
  delay(300);
  analogWrite(9,128);
  delay(300);
  analogWrite(9,64);
  delay(300);
}
