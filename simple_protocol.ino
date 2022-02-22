#include <CRC8.h>

uint8_t DLE = 0xff;
uint8_t STX = 0x80;
uint8_t ETX = 0x81;
uint8_t DLESTX[2] = {DLE, STX};
uint8_t DLEETX[2] = {DLE, ETX};

uint8_t sample_rate = 2; // Hz

CRC8 crc;

int buf_size = 1000;
uint8_t buf[1000] = {0,};
uint8_t* pbegin = buf;// pointer of data begin
uint8_t* pend = buf;  // pointer of data end
uint8_t* pbufend = buf + buf_size; // pointer of buffer end

int buf_canRead = 0;

uint8_t data = 0x00;
int data_count = 10;  // iteration count for write to buffer
int data_length = 15; // length of data in packet
uint8_t crc_val = 0;
bool crc_ready = false;

int command_length = 4; // length of command packet from host pc. < STX | LENGTH | RATE | CRC >
byte commands[3] = {0, };
byte command_stx = 0x80;

void setup() {
  // put your setup code here, to run once:

  // initialize Serial
  Serial.begin(9600);

  // initialize Timer 1
  timerSettup();
}

void timerSettup(){
  noInterrupts();
  TCCR1A = 0;
  TCCR1B = 0;

  OCR1A = 62500 / sample_rate;  // 16MHz / 256 / sample_rate
  TCCR1B |= (1 << WGM12);       // CTC mode
  TCCR1B |= (1 << CS12);        // 256 prescaler
  TIMSK1 |= (1 << OCIE1A);      // enable timer compare interrupt

  TCNT1 = 0;
  interrupts();
}

ISR(TIMER1_COMPA_vect) {
  // timer compare interrupt service routine:
  if(buf_canRead >= data_length && crc_ready){
    if(pbufend - pbegin < data_length){
      int head = pbufend - pbegin;
      int tail = data_length - head;
      Serial.write(DLESTX, 2);
      Serial.write(pbegin, head);
      Serial.write(buf, tail);
      Serial.write(crc_val);
      Serial.write(DLEETX, 2);

      pbegin = buf + tail;
    }
    else{
      int head = pbufend - pbegin;        // 별 의미 없음. clock 맞추기 용도
      int tail = data_length - head;// clock 맞추기 용도
      Serial.write(DLESTX, 2);
      Serial.write(pbegin, data_length);
      Serial.write(crc_val);
      Serial.write(DLEETX, 2);

      pbegin = pbegin + data_length;
    }
    buf_canRead -= data_length;
    crc_ready = false;
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    command();
  }
  if(buf_size - buf_canRead >= data_count){ // fill buffer
    writeData();
    buf_canRead += data_count;
    data++;
  }
  if(!crc_ready && buf_canRead >= data_length){ // calc crc
    crc_val = calcCRC();
    crc_ready = true;
  }
}

void command(){
  byte incomingByte = Serial.read();
  if(incomingByte == command_stx){
    Serial.readBytes(commands, 3);
    // error check
    crc.reset();
    crc.add(commands, 2);
    if(commands[2] == crc.getCRC()){
      // update length and rate
      if(commands[0] & 0x80){
        data_length = commands[0] & 0x7f;
      }
      if(commands[1] & 0x80){
        sample_rate = commands[1] & 0x7f;
        timerSettup();
      }
    }
  }
}

void writeData() {
  if (pbufend - pend < data_count){
    int head = pbufend - pend;
    int tail = data_count - head;
    for(int i=0; i<head; i++){
      *pend = data;
      pend++;
    }
    pend = buf;
    for(int i=0;i<tail;i++){
      *pend = data;
      pend++;
    }
  }
  else {
    for(int i=0; i<data_count; i++){
      *pend = data;
      pend++;
    }
    if(pend > pbufend){
      pend = buf;
    }
  }
}

uint8_t calcCRC() {
  crc.reset();
  if(pbufend - pbegin < data_length){
    int head = pbufend - pbegin;
    int tail = data_length - head;
    crc.add(pbegin, head);
    crc.add(buf, tail);
  }
  else{
    crc.add(pbegin, data_length);
  }
  return crc.getCRC();
}
