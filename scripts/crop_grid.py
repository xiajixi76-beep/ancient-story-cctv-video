"""
四宫格关键帧裁图脚本
将 2x2 四宫格图片裁出四个独立格位，用于分段视频生成的首帧参考。

用法：
    python crop_grid.py <输入图片路径> <输出目录>

输出：
    panel1_top_left.png    左上格（开场）
    panel2_top_right.png   右上格（转折）
    panel3_bottom_left.png 左下格（发展）
    panel4_bottom_right.png 右下格（高潮/结尾）
"""

import sys
import os
from PIL import Image


def crop_grid(input_path: str, output_dir: str):
    img = Image.open(input_path)
    w, h = img.size
    print(f"输入图片尺寸: {w}x{h}")

    half_w = w // 2
    half_h = h // 2

    panels = [
        (0, 0, half_w, half_h, "panel1_top_left.png"),
        (half_w, 0, w, half_h, "panel2_top_right.png"),
        (0, half_h, half_w, h, "panel3_bottom_left.png"),
        (half_w, half_h, w, h, "panel4_bottom_right.png"),
    ]

    os.makedirs(output_dir, exist_ok=True)

    for left, top, right, bottom, name in panels:
        panel = img.crop((left, top, right, bottom))
        out_path = os.path.join(output_dir, name)
        panel.save(out_path)
        print(f"  {name}: {panel.size} -> {out_path}")

    print("裁图完成。")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    crop_grid(sys.argv[1], sys.argv[2])
