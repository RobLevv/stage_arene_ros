// C++ code
//
#include <Servo.h>

Servo servoBase;

void setup()
{
	pinMode(11,OUTPUT);
	pinMode(10,OUTPUT);
  	pinMode(9,OUTPUT);
  	pinMode(7,INPUT);
  	servoBase.attach(A1);
  	servoBase.write(0);
}

void toRed()
{
    digitalWrite(11,HIGH);
    delay(5000);
    digitalWrite(11,LOW);
}

void upBarrier()
{
  digitalWrite(10,HIGH);
  for(int i=90;i>=0;i--){
    servoBase.write(i);
    delay(20);
  }
  digitalWrite(10,LOW);
}

void downBarrier()
{
  digitalWrite(10,HIGH);
  for(int i=0;i<90;i++){
    servoBase.write(i);
    delay(20);
  }
  digitalWrite(10,LOW);
}

void orangeBlink(int n)
{
  for(int i=0;i<n;i++){
      digitalWrite(10,HIGH);
      delay(500);
      digitalWrite(10,LOW);
      delay(500);
    }
}
  	

void loop()
{
  digitalWrite(9,HIGH);
  if (digitalRead(7)==HIGH){
    digitalWrite(9,LOW);
    orangeBlink(3);
    downBarrier();
    toRed(); 
    upBarrier();
  }
  
}