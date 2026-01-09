# Smart Campus IoT System
A lightweight IoT-based smart campus system that collects and displays environmental data from campus sensor nodes, with interactive hardware and web-based data management.
<img width="570" height="271" alt="d33a152a60b46831d02182d351159b84" src="https://github.com/user-attachments/assets/96548c08-9000-4640-a764-f5bd570090dc" />


## 📋 Feature Overview
### Core Functionality
- Collect real-time environmental data (temperature, humidity, light, sound) via campus sensor nodes
- Display data and notifications on hardware devices (LED Matrix/M5StickC)
- Web-based data query system (filter by venue/time period)
- MQTT-based data transmission between devices and server

### Hardware Components
| Device               | Key Features                                                                 |
|----------------------|------------------------------------------------------------------------------|
| WEMOS D1 Mini R2 LED Matrix | Display welcome message or IoT data; scroll long text on 8x8 matrix          |
| M5StickC             | Switch display layouts (clock/sensor data/MQTT messages); adjust refresh rate; motion detection (send "Position changed!" via MQTT) |
| Raspberry Pi         | Gather sensor data; handle MQTT communication; control GPIO/LED indicators  |

## 🔧 Technical Implementation
### Programming Languages & Tools
- **Raspberry Pi**: Python (GPIO control, MQTT data handling, threading for LED flashing)
- **ESP8266/M5StickC**: C++ (Arduino IDE) with libraries (MQTT, JSON, DHT11, Neotimer, Button-debounce)
- **Web Application**: Django (backend) + Bootstrap CSS/JavaScript (frontend)

### Key Technical Details
1. **LED Matrix**: Use `scrollTextLeft()` for long text display; `snprintf()` to integrate multiple data types
2. **M5StickC**: `xTaskCreate()` for multi-core task execution; Neotimer for simultaneous task scheduling
3. **Web Interface**:
   - Form-based data filtering (venue/time period) with POST method
   - Django QuerySet for grouped venue data (`values('loc').annotate()`)
   - Bootstrap for animated UI (scroll slides, hover effects, login form)
   - JavaScript for scroll slide control (`document.querySelector()`)

## 🛠️ Skills Involved
### Hardware
- Raspberry Pi (GPIO, LCD, ADC)
- WEMOS D1 Mini R2, M5StickC, DHT11 sensor

### Software
- **Frontend**: Bootstrap CSS (animated search, scroll slides, hover effects), HTML/JavaScript
- **Backend**: Django (QuerySet, HttpRequest/HttpRedirect, form handling)
- **IoT**: MQTT protocol, multi-threading/ multi-tasking
