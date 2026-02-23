"""
Video Frame Extractor - 基本用法示例

这个示例展示了如何使用 video_frame_extractor 模块的各种功能。
"""

from video_frame_extractor import extract_frames
import os


def example_1_basic_usage():
    """示例 1: 基本用法 - 提取默认的 10 帧"""
    print("=" * 50)
    print("示例 1: 基本用法")
    print("=" * 50)

    # 替换为你的视频路径
    video_path = "../微信视频2026-02-23_185932_753.mp4"
    output_dir = "example_output/basic"

    # 检查视频文件是否存在
    if not os.path.exists(video_path):
        print(f"⚠️  视频文件不存在: {video_path}")
        print("请修改 video_path 为你自己的视频路径")
        return

    # 提取帧
    paths = extract_frames(video_path, output_dir)

    print(f"✅ 成功提取 {len(paths)} 帧到: {output_dir}/")
    for path in paths:
        print(f"   - {path}")


def example_2_custom_num_frames():
    """示例 2: 自定义提取帧数"""
    print("\n" + "=" * 50)
    print("示例 2: 自定义提取帧数 (20 帧)")
    print("=" * 50)

    video_path = "../微信视频2026-02-23_185932_753.mp4"
    output_dir = "example_output/custom_frames"

    if not os.path.exists(video_path):
        print(f"⚠️  视频文件不存在: {video_path}")
        return

    # 提取 20 帧
    paths = extract_frames(video_path, output_dir, num_frames=20)

    print(f"✅ 成功提取 {len(paths)} 帧到: {output_dir}/")


def example_3_custom_quality():
    """示例 3: 自定义输出质量"""
    print("\n" + "=" * 50)
    print("示例 3: 自定义输出质量")
    print("=" * 50)

    video_path = "../微信视频2026-02-23_185932_753.mp4"

    # 使用不同质量对比
    quality_levels = [60, 80, 95]

    for quality in quality_levels:
        output_dir = f"example_output/quality_{quality}"
        paths = extract_frames(video_path, output_dir, num_frames=3, quality=quality)
        file_size = os.path.getsize(paths[0]) / 1024  # KB
        print(f"质量 {quality}: {paths[0]} ({file_size:.1f} KB)")


def example_4_specific_frames():
    """示例 4: 提取特定位置的帧"""
    print("\n" + "=" * 50)
    print("示例 4: 提取特定位置的帧")
    print("=" * 50)

    video_path = "../微信视频2026-02-23_185932_753.mp4"
    output_dir = "example_output/specific_frames"

    # 提取第 0、50、100 帧
    specific_indices = [0, 50, 100]
    paths = extract_frames(
        video_path,
        output_dir,
        indices=specific_indices
    )

    print(f"✅ 提取了特定帧 {specific_indices}")
    for idx, path in enumerate(paths):
        print(f"   第 {specific_indices[idx]} 帧: {path}")


def example_5_batch_processing():
    """示例 5: 批量处理多个视频"""
    print("\n" + "=" * 50)
    print("示例 5: 批量处理多个视频")
    print("=" * 50)

    # 假设有多个视频文件
    video_files = [
        "../微信视频2026-02-23_185932_753.mp4",
        "../微信视频2026-02-23_185944_862.mp4",
        "../微信视频2026-02-23_185954_720.mp4"
    ]

    for video_path in video_files:
        if not os.path.exists(video_path):
            continue

        # 使用视频文件名（不含扩展名）作为输出目录名
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        output_dir = f"example_output/batch/{video_name}"

        extract_frames(video_path, output_dir, num_frames=5)
        print(f"✅ 处理完成: {video_name}")


def main():
    """运行所有示例"""
    print("\n🎬 Video Frame Extractor - 使用示例\n")

    # 创建输出目录
    os.makedirs("example_output", exist_ok=True)

    # 运行示例（取消注释想要运行的示例）
    example_1_basic_usage()
    # example_2_custom_num_frames()
    # example_3_custom_quality()
    # example_4_specific_frames()
    # example_5_batch_processing()

    print("\n" + "=" * 50)
    print("示例运行完成！")
    print("=" * 50)


if __name__ == "__main__":
    main()
