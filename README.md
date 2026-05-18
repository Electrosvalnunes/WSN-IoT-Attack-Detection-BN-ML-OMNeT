# WSN-IoT Attack Detection using Bayesian Networks and Machine Learning

This repository contains the reproducibility materials of a scientific project focused on the detection of cyberattacks in Wireless Sensor Networks and IoT environments.

The repository includes:

- OMNeT++/INET simulation files for a 36-node WSN topology;
- C++ attack modules for Flooding, Blackhole and Wormhole scenarios;
- Bayesian Network model developed in GeNIe Academic;
- Python implementation of the Bayesian Network;
- Machine Learning scripts used for training and evaluation;
- Dataset and processed metrics;
- Figures and tables used in the scientific analysis.

## Evaluated Scenarios

The following scenarios are considered:

1. Normal operation
2. Flooding attack
3. Manipulated Backoff attack
4. Blackhole attack
5. Wormhole attack

## Detection Approaches

The project combines:

- Bayesian Network inference;
- Random Forest;
- Decision Tree;
- K-Nearest Neighbors;
- Logistic Regression;
- Support Vector Machine with linear kernel;
- Support Vector Machine with RBF kernel.

## Main Metrics

The detection models use network performance metrics extracted from OMNeT++ simulations:

- Packet Delivery Ratio;
- End-to-end Delay;
- Throughput;
- Energy consumption.

## Purpose

This repository supports scientific reproducibility, allowing researchers to verify, adapt and extend the experiments related to attack detection in WSN/IoT environments.
