#include <stdint.h>
#include "config.h"

uint8_t pins_slave[NUM_LINES_SLAVE] = {A5, 12, A4, 13, A3, A1, A2};

int tab2point(int i, int j){
  //single

    if(i == 6 && j == 9) return 1;
    if(i == 4 && j == 5) return 2;
    if(i == 4 && j == 7) return 3;
    if(i == 6 && j == 7) return 4;
    if(i == 6 && j == 2) return 5;
    if(i == 6 && j == 5) return 6;
    if(i == 4 && j == 9) return 7;
    if(i == 4 && j == 2) return 8;
    if(i == 6 && j == 0) return 9;
    if(i == 6 && j == 4) return 10;
    if(i == 4 && j == 1) return 11;
    if(i == 6 && j == 1) return 12;
    if(i == 6 && j == 6) return 13;
    if(i == 4 && j == 0) return 14;
    if(i == 4 && j == 4) return 15;
    if(i == 4 && j == 3) return 16;
    if(i == 4 && j == 6) return 17;
    if(i == 6 && j == 8) return 18;
    if(i == 4 && j == 8) return 19;
    if(i == 6 && j == 3) return 20;
    if(i == 5 && j == 1) return 25;

  //double

    if(i == 1 && j == 9) return 2*1;
    if(i == 3 && j == 5) return 2*2;
    if(i == 3 && j == 7) return 2*3;
    if(i == 1 && j == 7) return 2*4;
    if(i == 1 && j == 2) return 2*5;
    if(i == 1 && j == 5) return 2*6;
    if(i == 3 && j == 9) return 2*7;
    if(i == 3 && j == 2) return 2*8;
    if(i == 1 && j == 0) return 2*9;
    if(i == 1 && j == 4) return 2*10;
    if(i == 3 && j == 1) return 2*11;
    if(i == 1 && j == 1) return 2*12;
    if(i == 1 && j == 6) return 2*13;
    if(i == 3 && j == 0) return 2*14;
    if(i == 3 && j == 4) return 2*15;
    if(i == 3 && j == 3) return 2*16;
    if(i == 3 && j == 6) return 2*17;
    if(i == 1 && j == 8) return 2*18;
    if(i == 3 && j == 8) return 2*19;
    if(i == 1 && j == 3) return 2*20;
    if(i == 5 && j == 0) return 2*25;

  //triple

    if(i == 0 && j == 9) return 3*1;
    if(i == 2 && j == 5) return 3*2;
    if(i == 2 && j == 7) return 3*3;
    if(i == 0 && j == 7) return 3*4;
    if(i == 0 && j == 2) return 3*5;
    if(i == 0 && j == 5) return 3*6;
    if(i == 2 && j == 9) return 3*7;
    if(i == 2 && j == 2) return 3*8;
    if(i == 0 && j == 0) return 3*9;
    if(i == 0 && j == 4) return 3*10;
    if(i == 2 && j == 1) return 3*11;
    if(i == 0 && j == 1) return 3*12;
    if(i == 0 && j == 6) return 3*13;
    if(i == 2 && j == 0) return 3*14;
    if(i == 2 && j == 4) return 3*15;
    if(i == 2 && j == 3) return 3*16;
    if(i == 2 && j == 6) return 3*17;
    if(i == 0 && j == 8) return 3*18;
    if(i == 2 && j == 8) return 3*19;
    if(i == 0 && j == 3) return 3*20;
  return -1;
}
//Shift Register Pins
#define latchPin  4
#define clockPin 3
#define dataPin 2


int masterLines = 10;
int slaveLines = 7; //Change here to the number of lines of your Slave Layer
int matrixSlave[] = {12, 13, A5, A4, A3, A2, A1}; //Put here the pins you connected the lines of your Slave Layer
void pushDataOnRegisters (char reg1, char reg2);

void setup() {
    Serial.begin(9600);
    for(uint8_t i=0; i<NUM_LINES_SLAVE; i++){
        pinMode(matrixSlave[i], INPUT_PULLUP);
    }
    
  //Shift Register Pins
  pinMode (latchPin, OUTPUT);
  pinMode (dataPin, OUTPUT);
  pinMode (clockPin, OUTPUT);

  //Set master pins high 
  pushDataOnRegisters(255, 255); 
}
void loop() {

    for(uint8_t i=0; i<NUM_LINES_MASTER; i++){
      if(i < 6){
        pushDataOnRegisters(masterOuputs[i], 255);    
      }else{
        pushDataOnRegisters(255, masterOuputs[i-6]);  
      }    
        for(uint8_t j=0; j<NUM_LINES_SLAVE; j++){
            if(!digitalRead(matrixSlave[j])){
//                Serial.print(j);
//                Serial.print(",");
//                Serial.print(i);
//                Serial.print(" ");
                Serial.print("if metode:");
                Serial.println(tab2point(j,i));
                Serial.print("Eryk's metode:");
                Serial.println(GET_LOOKUP_VALUE(i, j));
                delay(500);
                break;
            }
        }

        pushDataOnRegisters(255, 255);      
    } 
}

void pushDataOnRegisters (char reg1, char reg2){
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, LSBFIRST, reg2);
  shiftOut(dataPin, clockPin, LSBFIRST, reg1);
  digitalWrite(latchPin, HIGH); 
}
