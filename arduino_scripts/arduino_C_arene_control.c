#include <Servo.h>

#define Barrier_1 A1
#define Barrier_2 A2
#define TL1_green 0
#define TL1_yellow 1
#define TL1_red 2
#define TL2_green 3
#define TL2_yellow 4
#define TL2_red 5

Servo servoBarrier_1;
Servo servoBarrier_2;


void reset_arene(){
    servoBarrier_1.write(0);
    servoBarrier_2.write(0);
    digitalWrite(TL1_green, LOW);
    digitalWrite(TL1_yellow, LOW);
    digitalWrite(TL1_red, LOW);
    digitalWrite(TL2_green, LOW);
    digitalWrite(TL2_yellow, LOW);
    digitalWrite(TL2_red, LOW);
    power_on();
    delay(1000);
    power_off();
}

void open_barrier(servo){
    for (int i = 0; i < 90; i++) {
        servo.write(i);
        delay(15);
    }
}

void close_barrier(servo){
    for (int i = 90; i > 0; i--) {
        servo.write(i);
        delay(15);
    }
}

void power_on(){
    digitalWrite(TL1_green, HIGH);
    digitalWrite(TL1_yellow, HIGH);
    digitalWrite(TL1_red, HIGH);
    digitalWrite(TL2_green, HIGH);
    digitalWrite(TL2_yellow, HIGH);
    digitalWrite(TL2_red, HIGH);
}

void power_off(){
    digitalWrite(TL1_green, LOW);
    digitalWrite(TL1_yellow, LOW);
    digitalWrite(TL1_red, LOW);
    digitalWrite(TL2_green, LOW);
    digitalWrite(TL2_yellow, LOW);
    digitalWrite(TL2_red, LOW);
}

void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);
    servoBarrier_1.attach(Barrier_1);
    servoBarrier_2.attach(Barrier_2);
    pinMode(TL1_green, OUTPUT);
    pinMode(TL1_yellow, OUTPUT);
    pinMode(TL1_red, OUTPUT);
    pinMode(TL2_green, OUTPUT);
    pinMode(TL2_yellow, OUTPUT);
    pinMode(TL2_red, OUTPUT);
    reset_arene();
}

void loop() {
    // put your main code here, to run repeatedly:
    if (Serial.available() > 0) {
        int data = Serial.read()-'0';
        switch (data) {
            case 0:
                open_barrier(servoBarrier_1);
                break;
            case 1:
                open_barrier(servoBarrier_2);
                break;
            case 2:
                close_barrier(servoBarrier_1);
                break;
            case 3:
                close_barrier(servoBarrier_2);
                break;
            case 4: // TL1 go to green
                digitalWrite(TL1_green, HIGH);
                digitalWrite(TL1_yellow, LOW);
                digitalWrite(TL1_red, LOW);
                break;
            case 5: // TL1 blink yellow 
                digitalWrite(TL1_green, LOW);
                digitalWrite(TL1_red, LOW);
                for (int i = 0; i < 3; i++) {
                    digitalWrite(TL1_yellow, HIGH);
                    delay(200);
                    digitalWrite(TL1_yellow, LOW);
                    delay(200);
                }
                break;
            case 6: // TL1 go to red
                digitalWrite(TL1_green, LOW);
                digitalWrite(TL1_yellow, LOW);
                digitalWrite(TL1_red, HIGH);
                break;
            case 7: // TL2 go to green
                digitalWrite(TL2_green, HIGH);
                digitalWrite(TL2_yellow, LOW);
                digitalWrite(TL2_red, LOW);
                break;
            case 8: // TL2 blink yellow
                digitalWrite(TL2_green, LOW);
                digitalWrite(TL2_red, LOW);
                for (int i = 0; i < 3; i++) {
                    digitalWrite(TL2_yellow, HIGH);
                    delay(200);
                    digitalWrite(TL2_yellow, LOW);
                    delay(200);
                }
                break;
            case 9: // TL2 go to red
                digitalWrite(TL2_green, LOW);
                digitalWrite(TL2_yellow, LOW);
                digitalWrite(TL2_red, HIGH);
                break;
            default:
                break;
        }
    }
}