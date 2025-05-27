# BStar-3DOF

This project simulates a distributed flight software system inspired by real-world aerospace architectures. 

It consists of Node A running on an STM32 Nucleo board, responsible for real-time flight control and state estimation (EKF + Control), and Node B, currently implemented as a Linux application on a PC, handling fault detection (FDIR) and telemetry. The Sim Harness (Python) generates simulated sensor data (e.g., IMU, altimeter) and sends it over UDP to Node A, while the Ground UI (Flask) visualizes telemetry in real time. Node A and Node B communicate via UDP, with a future transition to a physical CAN bus into a second STM32 board, enabling a fully embedded dual-node system. 

This setup mirrors industry practices for distributed embedded systems, providing a testbed for control algorithms, fault management, and system integration.