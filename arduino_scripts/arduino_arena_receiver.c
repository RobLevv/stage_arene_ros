//This code is to run on the arduino on the arena. It receives the data from the
//robot and controls the arena accordingly.

//Every LED pin is inverted: HIGH = OFF, LOW = ON (because of the transistor circuit)
//Servos control barriers. 0 degrees = closed, 90 degrees = open

#include <Servo.h>

//Traffic light pins
#define TL1_pin1 0
#define TL1_pin2 1
#define TL1_pin3 2
#define TL2_pin1 3
#define TL2_pin2 4
#define TL2_pin3 5
//Bicolor light pins
#define BiLight_pin1 6
#define BiLight_pin2 7
#define BiLight_pin3 8
//Servo pins
#define Servo1_pin A1
#define Servo2_pin A2

//Servo objects
Servo servo1;
Servo servo2;

void setup(){
    //Traffic light pins
    pinMode(TL1_pin1, OUTPUT);
    pinMode(TL1_pin2, OUTPUT);
    pinMode(TL1_pin3, OUTPUT);
    pinMode(TL2_pin1, OUTPUT);
    pinMode(TL2_pin2, OUTPUT);
    pinMode(TL2_pin3, OUTPUT);
    //Bicolor light pins
    pinMode(BiLight_pin1, OUTPUT);
    pinMode(BiLight_pin2, OUTPUT);
    pinMode(BiLight_pin3, OUTPUT);
    //Servo objects
    servo1.attach(A1);
    servo2.attach(A2);
    //Start serial communication
    Serial.begin(9600);
    //Initialize all lights to off
    reset_arena();
}

void reset_arena(){
    //Turn off all lights
    digitalWrite(TL1_pin1, HIGH);
    digitalWrite(TL1_pin2, HIGH);
    digitalWrite(TL1_pin3, HIGH);
    digitalWrite(TL2_pin1, HIGH);
    digitalWrite(TL2_pin2, HIGH);
    digitalWrite(TL2_pin3, HIGH);
    digitalWrite(BiLight_pin1, HIGH);
    digitalWrite(BiLight_pin2, HIGH);
    digitalWrite(BiLight_pin3, HIGH);
    //Reset servos
    servo1.write(0);
    servo2.write(0);
    Serial.println("Arduino ready to receive data");
    //Test arena
    delay(1000);
    Serial.println("Testing arena");
    delay(1000);
    power_on();
    delay(1000);
    power_off();
    delay(1000);
    Serial.println("Arena ready");
}

void power_on(){
    //Turn on all lights
    digitalWrite(TL1_pin1, LOW);
    digitalWrite(TL1_pin2, LOW);
    digitalWrite(TL1_pin3, LOW);
    digitalWrite(TL2_pin1, LOW);
    digitalWrite(TL2_pin2, LOW);
    digitalWrite(TL2_pin3, LOW);
    digitalWrite(BiLight_pin1, LOW);
    digitalWrite(BiLight_pin2, LOW);
    digitalWrite(BiLight_pin3, LOW);
    //Open servos
    servo1.write(90);
    servo2.write(90);
}

void power_off(){
    //Turn off all lights
    digitalWrite(TL1_pin1, HIGH);
    digitalWrite(TL1_pin2, HIGH);
    digitalWrite(TL1_pin3, HIGH);
    digitalWrite(TL2_pin1, HIGH);
    digitalWrite(TL2_pin2, HIGH);
    digitalWrite(TL2_pin3, HIGH);
    digitalWrite(BiLight_pin1, HIGH);
    digitalWrite(BiLight_pin2, HIGH);
    digitalWrite(BiLight_pin3, HIGH);
    //Close servos
    servo1.write(0);
    servo2.write(0);
}

void open_barrier(Servo Active_servo, int id){
    //Change the traffic light to green
    if (id == 1){
        digitalWrite(TL1_pin1, HIGH);
        digitalWrite(TL1_pin2, LOW);
        digitalWrite(TL1_pin3, HIGH);
    }
    else if (id == 2){
        digitalWrite(TL2_pin1, HIGH);
        digitalWrite(TL2_pin2, LOW);
        digitalWrite(TL2_pin3, HIGH);
    }
    else{
        Serial.println("Invalid barrier id");
        return;
    }
    //Open the barrier with the given id
    Active_servo.write(90);
}

void close_barrier(Servo Active_servo, int id){
    //Close the barrier with the given id
    Active_servo.write(0);
    //Change the traffic light to red
    if (id == 1){
        digitalWrite(TL1_pin1, LOW);
        digitalWrite(TL1_pin2, HIGH);
        digitalWrite(TL1_pin3, HIGH);
    }
    else if (id == 2){
        digitalWrite(TL2_pin1, LOW);
        digitalWrite(TL2_pin2, HIGH);
        digitalWrite(TL2_pin3, HIGH);
    }
    else{
        Serial.println("Invalid barrier id");
        return;
    }
}

void loop(){
    //Read serial data
    if(Serial.available() > 0){
        int data = Serial.read();
        switch (data)
        {
        case 1:
            open_barrier(servo1, 1);
            break;
        case 2:
            open_barrier(servo2, 2);
            break;
        case 3:
            close_barrier(servo1, 1);
            break;
        case 4:
            close_barrier(servo2, 2);
            break;
        default:
            break;
        }
    }
}