#!/usr/bin/env python3
"""
Resize blog header image for optimal social media sharing.
Target: 1200x630px (OpenGraph/Twitter standard)
"""

from PIL import Image
import sys
from pathlib import Path

def resize_for_social(input_path, output_path="header.png"):
    """
    Resize image to 1200x630px for social media.
    Uses smart cropping to maintain center focus.
    """
    # Target dimensions for social media
    TARGET_WIDTH = 1200
    TARGET_HEIGHT = 630
    TARGET_RATIO = TARGET_WIDTH / TARGET_HEIGHT

    # Open image
    img = Image.open(input_path)
    print(f"Original size: {img.size[0]}x{img.size[1]}")

    # Calculate current ratio
    current_ratio = img.size[0] / img.size[1]

    # Resize while maintaining aspect ratio
    if current_ratio > TARGET_RATIO:
        # Image is wider than target - fit to height
        new_height = TARGET_HEIGHT
        new_width = int(new_height * current_ratio)
    else:
        # Image is taller than target - fit to width
        new_width = TARGET_WIDTH
        new_height = int(new_width / current_ratio)

    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    print(f"Resized to: {img.size[0]}x{img.size[1]}")

    # Crop to exact target size (center crop)
    left = (new_width - TARGET_WIDTH) // 2
    top = (new_height - TARGET_HEIGHT) // 2
    right = left + TARGET_WIDTH
    bottom = top + TARGET_HEIGHT

    img = img.crop((left, top, right, bottom))
    print(f"Cropped to: {img.size[0]}x{img.size[1]}")

    # Convert to RGB if needed (for JPG compatibility)
    if img.mode in ('RGBA', 'LA', 'P'):
        background = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
        img = background

    # Save with optimization
    img.save(output_path, 'PNG', optimize=True, quality=95)

    # Check file size
    file_size = Path(output_path).stat().st_size
    file_size_kb = file_size / 1024
    print(f"Saved as: {output_path}")
    print(f"File size: {file_size_kb:.1f}KB")

    if file_size_kb > 1024:
        print(f"⚠ Warning: File is larger than 1MB ({file_size_kb:.1f}KB)")
        print("Consider saving as JPG for better compression")
    else:
        print("✓ File size is optimal for social media")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python resize_header.py <input_image>")
        print("Example: python resize_header.py downloaded_image.png")
        sys.exit(1)

    input_file = sys.argv[1]

    if not Path(input_file).exists():
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)

    resize_for_social(input_file)
    print("\n✓ Done! Image ready for social media sharing")
