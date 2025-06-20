const int ANALOG_PIN = A0; 
const int SAMPLE_COUNT = 1024 * 10;
const int SAMPLING_FREQUENCY = 1000; 
const long SAMPLING_PERIOD_MICROS = 1000000L / SAMPLING_FREQUENCY;

void setup() {
  Serial.begin(115200); 
  Serial.println("Arduino is ready. Send any character to start sampling.");
}

void loop() {
  if (Serial.available() > 0) {
    while(Serial.available() > 0) {
      Serial.read();
    }

    Serial.println("Starting data capture...");


    for (int i = 0; i < SAMPLE_COUNT; i++) {
      long startTime = micros();

      int sensorValue = analogRead(ANALOG_PIN);

      Serial.println(sensorValue);

      while (micros() - startTime < SAMPLING_PERIOD_MICROS) {
        // do nothing
      }
    }

    Serial.println("---END---");
    Serial.println("Capture complete. Send any character to sample again.");
  }
}