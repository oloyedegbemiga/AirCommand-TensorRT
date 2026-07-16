"""Reusable camera capture utilities for AirCommand Jetson Agent."""

from __future__ import annotations

import logging
import threading
import time
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union

import cv2
import numpy as np

LOGGER = loggin.getLogger(__name__)

class CameraType(str, Enum):
    """Camera backends supported by AirCommand."""
    USB = "usb"
    CSI = "csi"

@dataclass(frozen=True)
class CameraConfig:
    """Configuration for a camera capture source"""
    camera_type: CameraType = CameraType.USB
    device_id: int = 0
    width: int = 1280
    height: int = 720
    fps: int = 30
    flip_method: int = 0

    def __post_init__(self) -> None:
        if self.device_id < 0:
            raise ValueError("Camera width and height must be positive")
        if self.fps <= 0:
            raise ValueError("Camera FPS must be positive")
        if not 0 <= self.flip_method <= 7:
            raise ValueError("flip_method must be between 0 and 7")
class CameraCapture:
    """Threaded camera capture that keeps the most recent frame available."""
    def __init__(self, config: CameraConfig) -> None:
        self.config = config
        self._capture: Optional[cv2.VideoCapture] = None
        self._thread: Optional[threading.Thread] = None

        self._lock = threading.lock()
        self._stop_event = threading.Event()
        self._frame_ready = threading.Event()

        self._latest_frame: Optional[nd.array] = None
        self._latest_timestamp = 0.0
        self._frame_id = 0
        self._capture_fps = 0.0
        self._read_failures = 0

        self._started = False