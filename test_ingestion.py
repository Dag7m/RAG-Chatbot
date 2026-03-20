import os
from ingestion.pipeline import run_ingestion
from retrieval.chat import ask_question
from PIL import Image

def test():
    print("Testing Image Ingestion...")
    # Create a test image
    img_path = "data/test_image.jpg"
    img = Image.new('RGB', (200, 200), color='salmon')
    img.save(img_path)
    
    # Ingest it
    run_ingestion(file_path=img_path)
    
    # Ask a question
    ans, sources = ask_question("What color is the test_image.jpg that was uploaded?")
    print("\nIMAGE TEST RESULT:")
    print("Answer:", ans)
    print("Sources:", sources)
    
    print("\n-------------------------------\n")
    
    print("Testing PDF Ingestion...")
    pdf_path = "data/AAU secret.pdf"
    if os.path.exists(pdf_path):
        run_ingestion(file_path=pdf_path)
        ans_pdf, sources_pdf = ask_question("What is AAU secret about?")
        print("\nPDF TEST RESULT:")
        print("Answer:", ans_pdf)
        print("Sources:", sources_pdf)
    else:
        print("PDF not found for testing.")

if __name__ == "__main__":
    test()
