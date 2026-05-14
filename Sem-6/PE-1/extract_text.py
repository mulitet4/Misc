from pypdf import PdfReader
import os

input_pdf = "pe1_mod4.pdf"
output_txt = "pe1_mod4_transcript_raw.txt"

try:
    reader = PdfReader(input_pdf)
    num_pages = len(reader.pages)
    
    with open(output_txt, "w", encoding="utf-8") as f:
        for i, page in enumerate(reader.pages):
            f.write(f"=== PAGE {i+1} ===\n")
            text = page.extract_text()
            if text:
                f.write(text)
            f.write("\n\n")
            
    print(f"Total pages extracted: {num_pages}")
    print(f"Output file byte size: {os.path.getsize(output_txt)}")
    print("--- First 80 lines ---")
    with open(output_txt, "r", encoding="utf-8") as f:
        for _ in range(80):
            line = f.readline()
            if not line:
                break
            print(line, end="")
except Exception as e:
    print(f"Error: {e}")
