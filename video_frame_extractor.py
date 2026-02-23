import cv2
import os
from typing import List, Optional


def extract_frames(
    video_path: str,
    output_dir: str,
    num_frames: int = 10,
    quality: int = 95,
    indices: Optional[List[int]] = None,
) -> List[str]:
    """Extracts frames from a video file.

    Parameters
    ----------
    video_path : str
        Path to the source video file.
    output_dir : str
        Directory where extracted frames will be saved. It will be
        created if it does not exist.
    num_frames : int, optional
        Number of frames to extract.  Defaults to 10.
    quality : int, optional
        JPEG quality (0-100) used when writing images.  Defaults to 95.
    indices : Optional[List[int]], optional
        Specific frame indices to extract. When provided, ``num_frames`` is
        ignored and the frames at the given positions are saved.  If
        ``indices`` is ``None`` the function selects ``num_frames`` evenly
        spaced frames across the video.

    Returns
    -------
    List[str]
        Paths to the saved image files.
    """

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"无法打开视频: {video_path}")

    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if indices is None:
        if total <= 0:
            indices = []
        else:
            indices = [int(total * i / num_frames) for i in range(num_frames)]

    os.makedirs(output_dir, exist_ok=True)
    saved_paths = []

    for idx, frame_no in enumerate(indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = cap.read()
        if not ret:
            continue
        out_path = os.path.join(output_dir, f"frame_{idx+1:03d}.jpg")
        cv2.imwrite(out_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        saved_paths.append(out_path)

    cap.release()
    return saved_paths


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract evenly spaced frames from a video file."
    )
    parser.add_argument("video", help="Path to input video.")
    parser.add_argument(
        "output", help="Directory where frames will be stored.")
    parser.add_argument(
        "-n", "--num", type=int, default=10, help="Number of frames to extract."
    )
    parser.add_argument(
        "-q", "--quality", type=int, default=95, help="JPEG quality (0-100)."
    )
    args = parser.parse_args()

    paths = extract_frames(
        args.video, args.output, num_frames=args.num, quality=args.quality
    )
    for p in paths:
        print(p)
