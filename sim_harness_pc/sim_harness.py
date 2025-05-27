'''
Step-by-Step Process to Build System
Phase 1: Core UDP Communication & Data Flow MVP
Goal: Build a minimal working loop where:
- Sim Harness sends sensor data to STM32 (Node A).
- STM32 (Node A) processes it and sends control commands to Node B (PC Sim).
- Node B (PC Sim) logs/prints the telemetry.
- Ground UI displays telemetry data.

Phase 1 Part 1 - Define the Protocol Format
What data will be sent:
- Sim -> Node A (UDP):
   - JSON: {"altitude": 100.0, "velocity": 50.0, "pitch":5.0}
- Node A -> Node B (UDP):
    - JSON: {"throttle": 80.0, "gimbal": 5.0}
- Node B -> Ground UI (WebSocket):
    - JSON: {"altitude": 100.0, "velocity": 50.0, "pitch": 5.0, "throttle": 80.0,
    "gimbal": 5.0, "health": "OK"}
    
-> This format is documented in shared/protocol_format.md

Phase 2 Part 1 - Write sim_harness.py -> Node A UDP Sender
sim_harness.py:
- Sends fake sensor data every 1 sec
- Receives (optional) status or control packets
STM32:
- Write udp_interface.cpp: listens on UDP port, prints prints received sensor data
- Add a dummy control logic in control.cpp: e.g., throttle always 100%
Milestone: Sim Harness sends data -> STM32 prints it

Phase 3 Part 1 - Node A -> Node B UDP
Node A:
- Add UDP send in udp_interface.cpp: sends control data every loop
Node B (PC Sim, C++):
- Write udp_interface.cpp in node_b_pc/: receives control packets, logs them
Milestone: STM32 sends dummy control data -> PC app prints it

Phase 4 Part 1 - Node B (PC Sim) -> Ground UI (WebSocket)
Node B:
- Send telemetry to Flas app via WebSocket (use Python WebSocket client library in node_b_pc/)
Ground UI (Flask + Plotly):
- Create simple live plot: throttle vs time
Milestone: Telemetry data appears live on the Ground UI

Phase 5 Part 1 - Refine and Expand
Gradually add:
- Noise models in Sim Harness
- Basic EKF in STM32
- FDIR logic in Node B
- Real-time plots in Ground UI

Phase 2: Transition to CAN Bus
Once second STM32 arrives:
- Replace UDP between Node A <-> Node B with CAN
- Update protocol handling to use CAN frameslet
'''

