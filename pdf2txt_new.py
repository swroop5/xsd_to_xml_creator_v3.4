import fitz  # PyMuPDF

def extract_text_with_exclusion(pdf_file, exclusion_rectangles):
    # Open the PDF document
    pdf_document = fitz.open(pdf_file)

    # Initialize the plain text
    plain_text = ''

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        
        # Get the page's bounding box
        page_rect = page.rect

        # Exclude the specified rectangles (headers and footers)
        for exclusion_rect in exclusion_rectangles:
            page_rect -= exclusion_rect

        # # Ensure positive values for the page rectangle
        # if page_rect.width < 0:
        #     page_rect.width = -page_rect.width
        #     page_rect.x1 = page_rect.x0 + page_rect.width
        # if page_rect.height < 0:
        #     page_rect.height = -page_rect.height
        #     page_rect.y1 = page_rect.y0 + page_rect.height

        
        # Extract the text within the modified bounding box
        page_text = page.get_text("text", clip=page_rect)

        # Append the page text to the plain_text variable
        plain_text += page_text

    # Close the PDF document
    pdf_document.close()

    return plain_text

# Define the PDF file path and exclusion rectangles (left, top, right, bottom)
pdf_file = 'Spezifikation_XJustiz_3_4_1.pdf'
exclusion_rectangles = [
    fitz.Rect(0, -50, -595, -750),  # Excludes the top 50 units
    fitz.Rect(0, -50, 595, 842)  # Excludes the bottom 92 units (for A4 size)
]

# Extract text from the PDF while excluding headers and footers
resulting_text = extract_text_with_exclusion(pdf_file, exclusion_rectangles)

# Print or save the resulting plain text
with open('xjustiz_3_4_1_new.txt', 'w+', encoding='utf-8') as f:
    f.write(resulting_text)
