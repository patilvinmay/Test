import os, easyocr, chardet
import numpy as np
import pandas as pd
from PIL import Image
from rapidfuzz import fuzz

OCRDataConfidencePath = "C:\\Users\\vinmayp\\PycharmProjects\\ComputerUse\\LogsAndData\\OCRDataConfidence.csv"
OCRDataPath = "C:\\Users\\vinmayp\\PycharmProjects\\ComputerUse\\LogsAndData\\OCRData.txt"
PrimaryFuzzyDataPath = "C:\\Users\\vinmayp\\PycharmProjects\\ComputerUse\\LogsAndData\\PrimaryFuzzyData.csv"

def primary_ocr(image_path):
    print("🖼️➜📝 Performing OCR for checking search echoes...")
    image = Image.open(image_path)
    screenshot_np = np.array(image)
    reader = easyocr.Reader(['en'])  # 'en' for English
    results = reader.readtext(screenshot_np)

    try:
        os.remove(OCRDataConfidencePath)
    except:
        pass
        # print("File 'OCRDataConfidence.txt' doesn't exist")

    try:
        os.remove(OCRDataPath)
    except:
        pass
        # print("File 'OCRData.txt' doesn't exist")

    writelog = open(OCRDataConfidencePath, "a")
    writelog.write(f"Line, Confidence, Top-Left, Bottom-Right\n")
    for (bbox, text, prob) in results:

        top_left = bbox[0]
        bottom_right = bbox[2]
        x1, y1 = int(top_left[0]), int(top_left[1])
        x2, y2 = int(bottom_right[0]), int(bottom_right[1])
        writelog.write(f"\"{text}\", \"{prob:.2f}\", {x1}:{y1}, {x2}:{y2}\n")

        writeocrdata = open(OCRDataPath, "a")
        writeocrdata.write(text + "\n")
        writeocrdata.close()

    writelog.close()

    readocrobj = open(OCRDataPath, 'r')
    ocrdata = readocrobj.readlines()
    readocrobj.close()

    with open(OCRDataConfidencePath, "rb") as f:
        raw_data = f.read()
        detected = chardet.detect(raw_data)

    ocrmetadata = pd.read_csv(OCRDataConfidencePath, header=None, encoding=detected['encoding'])
    ocrmetadata = ocrmetadata.values.tolist()

    return [ocrdata, ocrmetadata]


def has_fuzzy_echo(ocr_lines, ocr_meta_lines, threshold=90):
    print("🧬 Fuzzing for pattern recognition...")
    i = 0
    flag = False
    reference_echoes = [
        "including results for",
        "results for",
        "including results",
        "do you want results only for",
        "do you want",
        "results only for"
        "do you",
        "want results",
        "only for"
    ]

    try:
        os.remove(PrimaryFuzzyDataPath)
    except:
        # print("File 'PrimaryFuzzyData.csv' doesn't exist")
        pass

    writefuzzydata = open(PrimaryFuzzyDataPath, "a")
    writefuzzydata.write("Line Number,Line,Reference Echoes,Score,Flag,Top-Left,Bottom-Right\n")
    for line in ocr_lines:
        line_lower = str(line.lower()).strip()
        if len(line_lower.split(" ")) >= 2:
            for ref in reference_echoes:
                score = fuzz.partial_ratio(ref, line_lower)
                if score >= threshold:
                    writefuzzydata.write(f"{i},\"{line.strip()}\",\"{ref}\",{round(score,2)},True,{ocr_meta_lines[i+1][2]},{ocr_meta_lines[i+1][3]}\n")
                    flag = True
                else:
                    writefuzzydata.write(f"{i},\"{line.strip()}\",\"{ref}\",{round(score,2)},False\n")
        i += 1
    writefuzzydata.close()
    if flag:
        print("❌ Search echoes found")
        return True
    else:
        print("✅ No Search echoes found")
        return False

def identify_trim_coordinates():
    with open(OCRDataConfidencePath, "rb") as f:
        raw_data = f.read()
        detected = chardet.detect(raw_data)

    df = pd.read_csv(PrimaryFuzzyDataPath,encoding=detected['encoding'])
    df = df[df['Flag'] == True]
    df = df.values.tolist()

    topy=0
    bottomy=0
    j=1

    for i in range(len(df)-1):
        diff = df[j][0] - df[i][0]
        if diff >= 20:
            topy = int(str(df[i][6]).split(":")[-1])
            bottomy = int(str(df[j][5]).split(":")[-1])
            break
        i += 1
        j += 1

    return [topy, bottomy]

def split_image_into_echo_and_main(image_path,coordinates):
    # Load image
    image = Image.open(image_path).convert("RGB")
    image_np = np.array(image)
    height = image_np.shape[0]

    # Get Y coordinates from echo logic
    topy = coordinates[0]
    bottomy = coordinates[1]

    # Crop into 3 parts
    top_block = image_np[0:topy, :, :]
    middle_block = image_np[topy:bottomy, :, :]
    bottom_block = image_np[bottomy:, :, :]

    return top_block, middle_block, bottom_block



def ocr_plus_fuzzy(image_path):
    ocr = primary_ocr(image_path)
    search_echo_flag = has_fuzzy_echo(ocr[0], ocr[1])
    if search_echo_flag:
        print("✂️🖼️ Cropping search echoes...")
        coordinates = identify_trim_coordinates()
        top_img, mid_img, bottom_img = split_image_into_echo_and_main(image_path, coordinates)
        Image.fromarray(top_img).save("chunks\\top_echo.png")
        Image.fromarray(mid_img).save("chunks\\search_results_only.png")
        Image.fromarray(bottom_img).save("chunks\\bottom_echo.png")
        print("✅ Search results saved at: chunks\\search_results_only.png")
        return "chunks\\search_results_only.png"
    else:
        print("⏭️ No need to trim image")
        pass
