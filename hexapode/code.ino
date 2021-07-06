#include <VarSpeedServo.h>

 

VarSpeedServo myservo1;

VarSpeedServo myservo2;

VarSpeedServo myservo3;

VarSpeedServo myservo4;

VarSpeedServo myservo5;

VarSpeedServo myservo6;

VarSpeedServo myservo7;

VarSpeedServo myservo8;

VarSpeedServo myservo9;

VarSpeedServo myservo10;

VarSpeedServo myservo11;

VarSpeedServo myservo12;

VarSpeedServo myservo13;

VarSpeedServo myservo14;

VarSpeedServo myservo15;

VarSpeedServo myservo16;

VarSpeedServo myservo17;

VarSpeedServo myservo18;


int i =  100;

int a = 50;

 

const int servoPin14 = 1; // the digital pin used for the first servo

const int servoPin15 = 2; // the digital pin used for the first servo

const int servoPin16 = 3; // the digital pin used for the first servo

const int servoPin17 = 4; // the digital pin used for the first servo

const int servoPin18 = 5; // the digital pin used for the first servo

const int servoPin19 = 6; // the digital pin used for the first servo

const int servoPin20 = 7; // the digital pin used for the first servo

const int servoPin21 = 8; // the digital pin used for the first servo

const int servoPin22 = 9; // the digital pin used for the first servo

const int servoPin23 = 10; // the digital pin used for the first servo

const int servoPin24 = 11; // the digital pin used for the first servo

const int servoPin25 = 12; // the digital pin used for the first servo

const int servoPin26 = 13; // the digital pin used for the first servo

const int servoPin27 = 14; // the digital pin used for the first servo

const int servoPin28 = 15; // the digital pin used for the first servo

const int servoPin29 = 16; // the digital pin used for the first servo

const int servoPin30 = 17; // the digital pin used for the first servo

const int servoPin31 = 18; // the digital pin used for the first servo

void setup() {

  myservo1.attach(servoPin14);  // attaches the servo on pin 9 to the servo object

  myservo2.attach(servoPin15);  // attaches the servo on pin 9 to the servo object

  myservo3.attach(servoPin16);  // attaches the servo on pin 9 to the servo object

  myservo4.attach(servoPin17);  // attaches the servo on pin 9 to the servo object

  myservo5.attach(servoPin18);  // attaches the servo on pin 9 to the servo object

  myservo6.attach(servoPin19);  // attaches the servo on pin 9 to the servo object

  myservo7.attach(servoPin20);  // attaches the servo on pin 9 to the servo object

  myservo8.attach(servoPin21);  // attaches the servo on pin 9 to the servo object

  myservo9.attach(servoPin22);  // attaches the servo on pin 9 to the servo object

  myservo10.attach(servoPin23);  // attaches the servo on pin 9 to the servo object

  myservo11.attach(servoPin24);  // attaches the servo on pin 9 to the servo object

  myservo12.attach(servoPin25);  // attaches the servo on pin 9 to the servo object

  myservo13.attach(servoPin26);  // attaches the servo on pin 9 to the servo object

  myservo14.attach(servoPin27);  // attaches the servo on pin 9 to the servo object

  myservo15.attach(servoPin28);  // attaches the servo on pin 9 to the servo object

  myservo16.attach(servoPin29);  // attaches the servo on pin 9 to the servo object

  myservo17.attach(servoPin30);  // attaches the servo on pin 9 to the servo object

  myservo18.attach(servoPin31);  // attaches the servo on pin 9 to the servo object

}

void loop() {
  // put your main code here, to run repeatedly:
  walkforward();
}

void walkforward() {
  /*-----------STEP-1-----------*/
  //Patte AG
  myservo2.write(90,i, false);
  myservo1.write(90,i, false);
  myservo2.write(45,i, false);
  myservo10.write(45,i, false);
  //Patte MD
  myservo14.write(90,i, false);
  myservo13.write(90,i, false);
  myservo14.write(45,i, false);
  myservo4.write(45,i, false);
  //Patte DG
  myservo8.write(90,i, false);
  myservo7.write(90,i, false);
  myservo8.write(45,i, false);
  myservo16.write(45,i, true);
  /*-----------STEP-2-----------*/
  //Patte AD
  myservo11.write(90,i, false);
  myservo10.write(90,i, false);
  myservo11.write(45,i, false);
  myservo1.write(45,i, false);
  //Patte MG
  myservo5.write(90,i, false);
  myservo4.write(90,i, false);
  myservo5.write(45,i, false);
  myservo13.write(45,i, false);
  //Patte DD
  myservo17.write(90,i, false);
  myservo16.write(90,i, false);
  myservo17.write(45,i, false);
  myservo16.write(45,i, true);
  delay(1000);
}
