/*   
import serial

# Enable USB Communication
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5);
while True:
        incoming = ser.readline().strip()
        print 'Received Data : '+ incoming


*/
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#define DHTTYPE           DHT11     // DHT 11 
#define DHTPIN            4         // Pin which is connected to the DHT sensor.
#define ID                0          //ID of current arduino this script will be uploaded
DHT_Unified dht(DHTPIN, DHTTYPE);
void setup() {
  dht.begin();
  sensor_t sensor;
  dht.temperature().getSensor(&sensor);
  Serial.begin(9600);
}

void loop() {
    String srtID = String(ID);
    //Current Sensor
    int RawValue = analogRead(A0);
    double Voltage = (RawValue / 1024.0) * 5000; // Becomes mV
    double Amps = ((Voltage - 2500) / 66);
 
    //Serial.print("Current :");
    Serial.print(Amps,0);
    Serial.println("CID"+srtID);
    //Temperature
    sensors_event_t event;  
    dht.temperature().getEvent(&event);
    //Serial.print("Temp.: "); 
    Serial.print(event.temperature,0); // Prints the temperature value from the sensor
    Serial.println("TID"+srtID);
    dht.humidity().getEvent(&event);
    Serial.print(event.relative_humidity,0);
    Serial.println("HID"+srtID);
    delay(2000); // Delays 2 seconds, as the DHT22 sampling rate is 0.5Hz
}
