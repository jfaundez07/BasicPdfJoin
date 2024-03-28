import PyPDF2

archivos = ["Constancia PAAU Joaquín Faúndez.pdf",
            "Justificacion tutores.pdf"]

nombre_salida = "TutorPAUU.pdf"

pdf_final = PyPDF2.PdfMerger()

for doc in archivos:
    pdf_final.append(doc)

pdf_final.write(nombre_salida)

print("Archiivo creado con exito!")

pdf_final.close()