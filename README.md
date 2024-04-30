# SEH500 - Earthquake Detection (Early Warning) System

## Introduction

Earthquakes are natural disasters that can strike without warning, causing significant damage to both lives and infrastructure. With the increasing frequency and severity of earthquakes, there is a critical need for early detection systems to provide timely warnings and minimize the impact of these disasters. The SEH500 project aims to address this need by developing an accelerometer-based earthquake detection system capable of providing real-time data for early warning purposes.

## Background Research

Existing earthquake detection systems include seismometers, GPS and InSAR technology, and research on precursor signals. While these systems have their advantages, they often suffer from limitations such as limited coverage, delayed warnings, or unreliable precursor readings.

## Solution

The SEH500 project proposes the use of accelerometer-based sensors for real-time earthquake detection. This approach offers advantages such as continuous monitoring, portability, accessibility, and high resolution data capture. By integrating accelerometers into various devices and leveraging their real-time data capabilities, the SEH500 system aims to enhance earthquake detection and early warning capabilities.

## Project Work

The project began with brainstorming various ideas, ultimately settling on an earthquake detection system due to the feasibility of utilizing the microcontroller's built-in accelerometer. Initial challenges included setting up the accelerometer and I2C communication, which were overcome with the help of SDK examples and extensive configuration efforts.

Once the sensor data was successfully obtained, efforts focused on visualization using Python libraries. Serial communication was established between the microcontroller and Python script, enabling real-time data plotting. Interrupts were implemented for starting and shutting down the application gracefully, providing user-friendly control over the system.

## Future Work

The SEH500 project serves as a prototype for future endeavors in earthquake detection and early warning systems. Future work could involve integrating accelerometer data with existing systems such as seismic networks or GPS/InSAR technology to enhance coverage and depth assessments. Additionally, integration into smartphones and IoT devices could further expand the system's reach and real-time monitoring capabilities.

## References

- [Atmos: Earthquakes in a Warming World](https://atmos.earth/earthquakes-in-a-warming-world/#:~:text=Today%2C%20earthquakes%20are%20becoming%20more)
- [USGS: Networks of Multiple Seismometers](https://www.usgs.gov/programs/VHP/networks-multiple-seismometers-are-necessary-adequately-monitor-volcanoes#:~:text=A%20seismometer%20is%20an%20instrument)
- Donnellan, Andrea & Lyzenga, Gregory & Peltzer, Gilles & Webb, Frank & Heflin, M. & Zumberge, James. (1999). Use of GPS and InSAR technology and its further development in earthquake modeling.
- Encompass peripheral, Mcu Expresso IDE

