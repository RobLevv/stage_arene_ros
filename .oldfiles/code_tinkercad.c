#include <servo.h>

#define barrier1 A0
#define barrier2 A1

#define green1 5
#define yellow1 6
#define red1 7
#define green2 2
#define yellow2 3
#define red2 4

#define switch 1

Servo servoBarrier1;
Servo servoBarrier2;

int state1 = 0;
int state2 = 0;

void setup(){
    // Attach the servos to their respective pins
    servoBarrier1.attach(barrier1);
    servoBarrier2.attach(barrier2);
    // set the pins to output
    pinMode(green1, OUTPUT);
    pinMode(yellow1, OUTPUT);
    pinMode(red1, OUTPUT);
    pinMode(green2, OUTPUT);
    pinMode(yellow2, OUTPUT);
    pinMode(red2, OUTPUT);
    pinMode(switch, OUTPUT);

    // Default state
    servoBarrier1.write(0);
    servoBarrier2.write(0);
    digitalWrite(green1, HIGH);
    digitalWrite(green2, HIGH);
    digitalWrite(yellow1, HIGH);
    digitalWrite(yellow2, HIGH);
    digitalWrite(red1, LOW);
    digitalWrite(red2, LOW);

}

void blink_change(int id, int n){
    for (int i = 0; i < n; i++) {
        digitalWrite(id, LOW);
        delay(500);
        digitalWrite(id, HIGH);
        delay(500);
    }
}

void change_state(int barrier_id, int state){
    if (barrier_id == 1) {
        if (state == 0) {
            // Open
            blink_change(yellow1, 3);
            digitalWrite(red1, HIGH);
            for (int i = 0; i < 90; i++) {
                servoBarrier1.write(i);
                delay(15);
            }
            digitalWrite(green1, LOW);
        } else {
            // Close
            blink_change(yellow1, 3);
            digitalWrite(green1, HIGH);
            for (int i = 90; i > 0; i--) {
                servoBarrier1.write(i);
                delay(15);
            }
            digitalWrite(red1, LOW);
        }
    } else {
        if (state == 0) {
            // Open
            blink_change(yellow2, 3);
            digitalWrite(red2, HIGH);
            for (int i = 0; i < 90; i++) {
                servoBarrier2.write(i);
                delay(15);
            }
            digitalWrite(green2, LOW);
        } else {
            // Close
            blink_change(yellow2, 3);
            digitalWrite(green2, HIGH);
            for (int i = 90; i > 0; i--) {
                servoBarrier2.write(i);
                delay(15);
            }
            digitalWrite(red2, LOW);
        }
    }
}

void loop(){
    if (state1 == 0) {
        change_state(1, 0);
        state1 = 1;
    } else {
        change_state(1, 1);
        state1 = 0;
    }
    if (state2 == 0) {
        change_state(2, 0);
        state2 = 1;
    } else {
        change_state(2, 1);
        state2 = 0;
    }
}