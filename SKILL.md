---
name: video-frame-extractor
description: Extract frames from video files. Use this when users want to extract images from videos, create video thumbnails, or analyze video content frame by frame.
license: MIT
---

## Overview

This skill provides a video frame extraction tool that can:
- Extract evenly spaced frames from a video
- Extract specific frames by index
- Control output image quality
- Batch process multiple videos

## Core Function

The main function is `extract_frames()` with the following parameters:

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `video_path` | `str` | Path to the input video file | Required |
| `output_dir` | `str` | Directory where frames will be saved | Required |
| `num_frames` | `int` | Number of frames to extract (evenly spaced) | 10 |
| `quality` | `int` | JPEG quality (0-100) | 95 |
| `indices` | `List[int]` | Specific frame indices to extract | None |

## Usage Examples

### Command Line

```bash
# Basic: extract 10 frames (default)
python video_frame_extractor.py input.mp4 output/

# Custom number of frames
python video_frame_extractor.py input.mp4 output/ -n 20

# Custom quality
python video_frame_extractor.py input.mp4 output/ -q 90
```

### Python Code

```python
from video_frame_extractor import extract_frames

# Basic usage
paths = extract_frames(
    video_path="input.mp4",
    output_dir="frames/"
)

# Custom parameters
paths = extract_frames(
    video_path="input.mp4",
    output_dir="frames/",
    num_frames=20,
    quality=90
)

# Extract specific frames
paths = extract_frames(
    video_path="input.mp4",
    output_dir="frames/",
    indices=[0, 100, 200]  # Extract frames at indices 0, 100, 200
)
```

## Return Value

Returns a list of saved image file paths (`List[str]`).

## Dependencies

- `opencv-python` (`pip install opencv-python`)

## Notes

- The output directory is created automatically if it doesn't exist
- Frame indexing starts at 0
- Frames are saved as JPEG images
- When `indices` is provided, `num_frames` is ignored
