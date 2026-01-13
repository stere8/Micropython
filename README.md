# 📘 Analog Inputs & ESP-to-ESP MQTT  
### MicroPython · Embedded Systems · IoT Communication

A structured **MicroPython lab project** demonstrating how analog sensor data flows from **hardware inputs** to **serial, JSON, Node-RED dashboards**, and finally to **wireless ESP-to-ESP communication using MQTT**.

Designed with **embedded-systems discipline**: each device has a clear responsibility, and code structure mirrors real firmware behavior.

---

## ✨ What This Project Demonstrates

✔ Analog signal acquisition (ADC)  
✔ UART communication  
✔ JSON-based data exchange  
✔ Node-RED visualization  
✔ MQTT messaging (ESP8266 → ESP32)  
✔ Proper MicroPython firmware structure  

---

## 🧱 Project Architecture

```text
MICROPYTHON/
├── ESP32 – MQTT Subscriber + Display/
│   └── main.py
│
├── ESP8266 – MQTT Publisher/
│   └── main.py
│
├── task1_temp.py
├── task2_joystick_raw.py
├── task3_joystick_map.py
├── task4_uart.py
├── task5_json_uart.py
└── task6_temp_units.py
```


### 🔑 Structural Rule (Critical in MicroPython)

> **`main.py` runs automatically on boot**

- ESP boards behave like **real firmware**
- Task scripts are **manual experiments**
- Structure reflects **device responsibility**, not convenience

---

## 🧠 Device Responsibilities

### 🔵 ESP8266 — MQTT Publisher
- Connects to Wi-Fi
- Publishes messages to an MQTT broker
- Acts as a **remote data source / controller**

---

### ⚫ ESP32 — MQTT Subscriber + Display
- Subscribes to MQTT topics
- Receives messages asynchronously
- Displays incoming data on an **SPI LCD**
- Clean separation between **communication** and **UI**

---

### 🟢 Raspberry Pi Pico — Analog & UART Tasks
- Reads internal temperature sensor
- Reads joystick via ADC
- Sends data over UART
- Formats sensor data as JSON
- Integrates with Node-RED dashboards

---

## 🛠️ Toolchain & Technologies

| Category | Tools |
|-------|------|
| Firmware | MicroPython |
| IDE | Thonny |
| Communication | UART · MQTT |
| Visualization | Node-RED |
| Hardware | Pico · ESP8266 · ESP32 |
| Broker | Mosquitto |

---

## ▶️ Running the Project

### Pico Tasks
- Select **MicroPython (Raspberry Pi Pico)** in Thonny
- Run `taskX_*.py` files **manually**

### ESP Firmware
- Flash the correct `main.py` to each board
- Code starts **automatically on boot**

### MQTT Extension
- Start an MQTT broker (e.g. Mosquitto)
- Power ESP32 first, then ESP8266
- Observe live updates on the display

📄 **Detailed wiring, task descriptions, and evaluation steps are provided in the accompanying PDF.**

---

## 🧪 Design Philosophy

> **Observe → Structure → Communicate → Visualize**

This project prioritizes:
- clarity over shortcuts  
- architecture over scripts  
- reproducibility over hacks  

It is built to be **explainable**, **defensible**, and **extendable**.

---

## 📌 Notes

- ESP-to-ESP MQTT is an **optional extension**
- Core requirements are satisfied with **Pico + Node-RED**
- Repository is structured for **labs, exams, and oral defense**

---

### 🚀 Possible Extensions
- Secure MQTT (TLS)
- Web dashboard instead of Node-RED
- Bidirectional ESP control
- Persistent configuration storage

---
