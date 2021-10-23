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
//Pin connected to latch pin (RCLK) of 74HC595
#define latchPin  4
//Pin connected to clock pin (SRCLK) of 74HC595
#define clockPin 3
//Pin connected to data pin (SER) of 74HC595
#define dataPin 2
byte masterOuputs[6] = {
  191, // i == 0
  223, // i == 1
  239, // i == 2
  247, // i == 3
  251, // i == 4
  253, // i == 5
};

byte masterOuputsOff[6] = {
  64, // i == 0
  32, // i == 1
  16, // i == 2
  8, // i == 3
  4, // i == 4
  2, // i == 5
};


int masterLines =10;
int slaveLines = 7; //Change here to the number of lines of your Slave Layer
int matrixMaster[] = {8, 9, 10, 11}; //Put here the pins you connected the lines of your Master Layer 
int matrixSlave[] = {12, 13, A5, A4, A3, A2, A1}; //Put here the pins you connected the lines of your Slave Layer

void setup() {
    Serial.begin(9600);
    for(int i = 0; i < slaveLines; i++){
        pinMode(matrixSlave[i], INPUT_PULLUP);
    }
   for(int i = 0; i < masterLines; i++){
       pinMode(matrixMaster[i], OUTPUT);
       digitalWrite(matrixMaster[i], HIGH);
   }
    
  //Shift Register Pins
  pinMode (latchPin, OUTPUT);
  pinMode (dataPin, OUTPUT);
  pinMode (clockPin, OUTPUT);
}
void loop() {
    for(int i = 0; i < masterLines; i++){
      if(i < 6){
        digitalWrite(latchPin, LOW);
        shiftOut(dataPin, clockPin, LSBFIRST, masterOuputs[i]);
        digitalWrite(latchPin, HIGH); 
      }else{
        digitalWrite(matrixMaster[i-6], LOW);
      }    
        for(int j = 0; j < slaveLines; j++){
            if(digitalRead(matrixSlave[j]) == LOW){
                Serial.print(j);
                Serial.print(",");
                Serial.print(i);
                Serial.print(" ");
                Serial.println(tab2point(j,i));
                delay(500);
                break;
            }
        }
        if(i < 6){
        digitalWrite(latchPin, LOW);
        shiftOut(dataPin, clockPin, MSBFIRST, 255);
        digitalWrite(latchPin, HIGH); 
      }else{
        digitalWrite(matrixMaster[i-6], HIGH);
      }
    } 
}
