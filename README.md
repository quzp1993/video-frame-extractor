# Video Frame Extractor

一个简单易用的 Python 工具，用于从视频文件中提取帧图像。

## 功能特性

- 从视频中均匀提取指定数量的帧
- 支持自定义输出质量（JPEG 格式）
- 支持提取特定位置的帧
- 自动创建输出目录

## 安装

### 依赖项

```bash
pip install opencv-python
```

## 使用方法

### 命令行使用

```bash
# 基本用法：提取 10 帧（默认）
python video_frame_extractor.py input_video.mp4 output_frames/

# 自定义提取帧数
python video_frame_extractor.py input_video.mp4 output_frames/ -n 20

# 自定义输出质量（0-100）
python video_frame_extractor.py input_video.mp4 output_frames/ -q 90
```

### 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `video` | 输入视频文件路径 | 必填 |
| `output` | 输出目录路径 | 必填 |
| `-n, --num` | 提取的帧数 | 10 |
| `-q, --quality` | JPEG 质量 (0-100) | 95 |

### Python 代码调用

```python
from video_frame_extractor import extract_frames

# 基本用法：均匀提取 10 帧
paths = extract_frames(
    video_path="input.mp4",
    output_dir="frames/"
)

# 自定义参数
paths = extract_frames(
    video_path="input.mp4",
    output_dir="frames/",
    num_frames=20,
    quality=90
)

# 提取特定位置的帧
paths = extract_frames(
    video_path="input.mp4",
    output_dir="frames/",
    indices=[0, 100, 200]  # 提取第 0、100、200 帧
)
```

## 函数参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `video_path` | `str` | 输入视频文件路径 |
| `output_dir` | `str` | 输出目录路径（不存在会自动创建） |
| `num_frames` | `int` | 要提取的帧数（默认 10） |
| `quality` | `int` | JPEG 质量 0-100（默认 95） |
| `indices` | `List[int]` | 可选，指定要提取的帧索引列表 |

## 返回值

返回保存的图像文件路径列表 `List[str]`

## 示例

### 示例 1：提取视频缩略图

```bash
python video_frame_extractor.py my_video.mp4 thumbnails/ -n 5 -q 85
```

### 示例 2：Python 批量处理

```python
import os
from video_frame_extractor import extract_frames

videos = ["video1.mp4", "video2.mp4", "video3.mp4"]

for video in videos:
    output_dir = f"frames/{os.path.splitext(video)[0]}"
    extract_frames(video, output_dir, num_frames=10)
    print(f"已提取 {video} 的帧到 {output_dir}")
```

## 许可证

MIT License
