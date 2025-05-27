# BStar 3-DOF Booster Protocol Specification

This document defines the message formats and data fields exchanged between sytem components.

## 1️. Sim Harness → Node A (STM32): Sensor Data
Direction: Sim Harness → Node A  
Transport: UDP  
Format: JSON

### Payload Structure:

```json
{
  "timestamp": 1716829384.123,
  "altitude": 100.0,
  "velocity": 50.0,
  "pitch": 5.0,
  "imu": {
    "accel_x": 0.1,
    "accel_y": 0.0,
    "accel_z": -9.8,
    "gyro_x": 0.01,
    "gyro_y": 0.02,
    "gyro_z": 0.00
  }
}

| Field     | Type  | Units           | Description                    |
| --------- | ----- | --------------- | ------------------------------ |
| timestamp | float | seconds (epoch) | Unix timestamp                 |
| altitude  | float | meters          | Altitude                       |
| velocity  | float | m/s             | Vertical velocity              |
| pitch     | float | degrees         | Pitch angle                    |
| imu.\*    | float | m/s², rad/s     | Raw IMU sensor data            |

## 2.Node A → Node B (PC Sim): Control Commands
Direction: Node A → Node B
Transport: UDP (Phase 1), CAN (Phase 2)
Format: JSON

### Payload Structure:
```json
{
  "timestamp": 1716829384.456,
  "throttle": 85.0,
  "gimbal": 2.5,
  "mode": "AUTO"
}

| Field     | Type   | Units   | Description                        |
| --------- | ------ | ------- | ---------------------------------- |
| timestamp | float  | seconds | Unix timestamp                     |
| throttle  | float  | %       | Throttle command (0-100%)          |
| gimbal    | float  | degrees | Gimbal angle (pitch control)       |
| mode      | string | -       | Flight mode (e.g., "AUTO", "SAFE") |


## 3. Node B → Ground UI (WebSocket)
Direction: Node B → Ground UI
Transport: WebSocket
Format: JSON

### Payload Structure:
```json:
{
  "timestamp": 1716829384.789,
  "altitude": 100.0,
  "velocity": 50.0,
  "pitch": 5.0,
  "throttle": 85.0,
  "gimbal": 2.5,
  "health": "OK"
}

| Field     | Type   | Units   | Description                         |
| --------- | ------ | ------- | ----------------------------------- |
| timestamp | float  | seconds | Unix timestamp (optional)           |
| altitude  | float  | meters  | Current altitude (from Node A data) |
| velocity  | float  | m/s     | Vertical velocity                   |
| pitch     | float  | degrees | Pitch angle                         |
| throttle  | float  | %       | Throttle command                    |
| gimbal    | float  | degrees | Gimbal command                      |
| health    | string | -       | FDIR status (OK, WARN, FAIL)        |

## 4. Future Plan (CAN)
When transitioning to CAN:
- The Node A -> Node B JSON packets will be converted to binary frames
- Each field will be assigned a CAN message ID and data length
- Section will be added here for the CAN Frame Map

TLDR:
What data will be sent:
- Sim -> Node A (UDP):
   - JSON: {"altitude": 100.0, "velocity": 50.0, "pitch":5.0}
- Node A -> Node B (UDP):
    - JSON: {"throttle": 80.0, "gimbal": 5.0}
- Node B -> Ground UI (WebSocket):
    - JSON: {"altitude": 100.0, "velocity": 50.0, "pitch": 5.0, "throttle": 80.0, "gimbal": 5.0, "health": "OK"}

