from PIL import Image
import numpy as np
import os

# === FUNCTION: Remove top header ===
def remove_top_header(image_np, crop_ratio):
    height, width, _ = image_np.shape
    split_y = int(height * crop_ratio)

    upper_block = image_np[:split_y, :, :]
    lower_block = image_np[split_y:, :, :]

    return upper_block, lower_block

# === FUNCTION: Split image into left and right blocks ===
def split_left_and_right(image_np, ratio):
    height, width, _ = image_np.shape
    split_x = int(width * ratio)

    left_block = image_np[:, :split_x, :]
    right_block = image_np[:, split_x:, :]

    return left_block, right_block

# === MAIN ===
def process_image_remove_header_and_split(image_path, output_dir):
    print("🌀 Splitting image into link chunks...")

    img = Image.open(image_path).convert("RGB")
    img_np = np.array(img)

    # Step 1: Remove header and Keep Lower
    header_removed, lower_kept = remove_top_header(img_np, crop_ratio=0.058)

    # Step 2: Split left and right
    left_block, right_block = split_left_and_right(lower_kept, ratio=0.65)

    # Prepare output directory
    os.makedirs(output_dir, exist_ok=True)

    # Save chunks
    header_removed_path = os.path.join(output_dir, "header.png")
    lower_kept_path = os.path.join(output_dir, "lower.png")
    left_path = os.path.join(output_dir, "left_links_cleaned.png")
    right_path = os.path.join(output_dir, "right_business_pane_cleaned.png")
    Image.fromarray(header_removed).save(header_removed_path)
    Image.fromarray(lower_kept).save(lower_kept_path)
    Image.fromarray(left_block).save(left_path)
    Image.fromarray(right_block).save(right_path)

    print("✅ Chunks saved at: ", output_dir)

    return [header_removed_path, lower_kept_path, left_path, right_path]



# === CONFIG ===
# IMAGE_PATH = "bing_result.png"
# OUTPUT_DIR = "chunks"

# Execute the function
# chunks = process_image_remove_header_and_split(IMAGE_PATH, OUTPUT_DIR)

