# AI-based Traffic Vehicle Detection, Classification & Speed Estimation

> Final Year Project | BS Information Technology

An intelligent traffic monitoring system that detects vehicles, tracks them with unique IDs, and estimates their real-time speed from CCTV footage.

### 🚀 Key Features
- **Vehicle Detection:** YOLOv8 for accurate detection of Car, Bus, Truck, Motorcycle
- **Multi-Object Tracking:** ByteTrack to assign unique ID to each vehicle
- **Speed Estimation:** Calculates speed using virtual line concept -> Speed = Distance / Time * 3.6 (km/h)
- **Data Logging:** Saves vehicle count and speed in CSV file

### 🛠️ Tech Stack
`Python` `OpenCV` `YOLOv8` `ByteTrack` `NumPy` `Pandas`

### 📊 How It Works
1. Video frame -> YOLOv8 detects vehicles
2. ByteTrack tracks vehicles across frames
3. When vehicle crosses Line A and Line B, time is calculated
4. Speed = (Known Distance between lines / Time taken) * 3.6

### 📈 Results
- Tested on highway traffic videos
- Achieved real-time detection
- Demo video will be added soon

### 🔮 Future Work (For MS at KAIST)
- Fog & Night enhancement for all-weather detection
- Edge AI deployment on Jetson Nano
- Integration with pothole detection system

**Author:** Zainab Shafeeq | Aspiring Researcher at KAIST AI# final_year-project
