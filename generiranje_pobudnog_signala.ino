const int dacPin = DAC1;

const int minDacValue = 867; // 1V
const int maxDacValue = 3102; // 3V

int dacValue = minDacValue;
int adder = 1;

void setup() {
  analogWriteResolution(12);
}

void loop() {
  analogWrite(dacPin, dacValue);
  dacValue += adder;

  if ((dacValue == maxDacValue && adder == 1) || (dacValue == minDacValue && adder == -1)) {
    adder *= -1;
  }
}