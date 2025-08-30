from pypdf import PdfReader

from pypdf import PdfReader

def extract_cv_content(file_obj):
    """
    Extract text from uploaded CV PDF (file-like object).
    """
    pdf = PdfReader(file_obj)
    pages = [page.extract_text() for page in pdf.pages]
    return "\n".join(pages)


# testing 
# if __name__ == "__main__":
#     cv_path = input("Enter path to CV PDF: ")
#     with open(cv_path, "rb") as f:
#         content = extract_cv_content(f)
#         print(content[:500])  # Print first 500 characters of the CV content