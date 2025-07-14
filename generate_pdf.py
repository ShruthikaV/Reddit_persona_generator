from fpdf import FPDF
import os
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def save_persona_as_pdf(username, persona_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, f"Reddit User Persona: {username}", ln=True, align='C')
    pdf.ln(5)

    pdf.set_font("Arial", size=12)
    for line in persona_text.splitlines():
        line = remove_accents(line)  # Clean line from Unicode special chars

        if line.startswith("##"):
            pdf.set_font("Arial", 'B', 14)
            pdf.multi_cell(0, 10, line.replace("##", "").strip())
        elif line.startswith("**") and line.endswith("**"):
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, line.replace("**", "").strip())
        else:
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 10, line)

    os.makedirs("output", exist_ok=True)
    pdf.output(f"output/{username}_persona.pdf")
