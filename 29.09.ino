int led_pin = 13; 
int state = -1;
int led_interval = 400; //400 мс период моргания

// значения сенсоров
int sensor1_val = 0;
int sensor2_val = 0;

bool read_s1 = false;
bool read_s2 = false;

void setup() {
  Serial.begin(9600);
  pinMode(led_pin, OUTPUT);

}


void loop() {
  
  while(Serial.available() > 0) {
    char a = Serial.read();
    if (a == 'u')
      state = 1;
    else if (a == 'd')
      state = 0;
    else if (a == 'b')
      state = 2;

    // передаём в консоль ардуино, что хотим считать датчик 1
    else if (a == '1'){
      read_s1 = true;
    }
    // хотим считать датчик 2
    else if (a == '2'){
      read_s2 = true;
    }
    else
      state = -1; 
     
  }
  
  if (state == 1 or state == 0)
    digitalWrite(led_pin, state);
  else if (state == 2)
    digitalWrite(led_pin, (millis() / led_interval) % 2);  //(millis() / led_interval) % 2) - передаёт 0 или 1

  // считывание данных
  if (read_s1){
    int sensor1_val = analogRead(A0);  // датчик на пине А0
    Serial.println(sensor1_val);
    read_s1 = false;
  }

  if (read_s2){
    int sensor2_val = analogRead(A1);  // датчик на пине А1
    Serial.println(sensor2_val);
    read_s2 = false;
  }

  
}
