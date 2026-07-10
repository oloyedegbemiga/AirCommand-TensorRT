# AirCommand-TensorRT

AirCommand-TensorRT is a real-time edge AI gesture-control system built for the NVIDIA Jetson Orin Nano.

The Jetson captures camera input, detects and classifies hand gestures, identifies swipe motions, and sends high-level gesture events to a desktop companion application called AirCommand Hub.

## Current Status

- [x] Jetson Orin Nano setup
- [x] CUDA and TensorRT verification
- [x] PyTorch GPU verification
- [x] Arducam headless capture test
- [ ] Repository architecture
- [ ] Dataset collection
- [ ] PyTorch gesture classifier
- [ ] Swipe detection
- [ ] ONNX export
- [ ] TensorRT inference
- [ ] AirCommand Hub
- [ ] Benchmarking and portfolio polish

## Development Platform

- NVIDIA Jetson Orin Nano Developer Kit, 8 GB
- JetPack 6.2 / L4T R36.5
- Ubuntu 22.04
- CUDA 12.6
- TensorRT 10.3
- PyTorch 2.8
- TorchVision 0.23
- Arducam USB autofocus camera

## Architecture

```text
Camera
  ↓
Hand localization
  ↓
Static gesture classification
  ↓
TensorRT inference
  ↓
Swipe tracking
  ↓
Gesture smoothing and debounce
  ↓
Gesture event sender
  ↓
AirCommand Hub
  ↓
Desktop action