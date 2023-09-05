from flask import Flask, render_template, request, send_file
from fpdf import FPDF, XPos, YPos

app = Flask(__name__)


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", style="B", size=12)
        self.cell(0, 10, "Información Personal", border=True, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(5)


@app.route("/")
def index():
    return render_template("formulario.html")


@app.route("/generar_pdf", methods=["POST"])
def generar_pdf():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    edad = request.form["edad"]
    dni = request.form["dni"]
    localidad = request.form["localidad"]

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, f"Nombre: {nombre}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, f"Apellido: {apellido}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, f"Edad: {edad}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, f"DNI: {dni}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, f"Localidad: {localidad}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.output("formulario_pdf/informacion_personal.pdf")

    return send_file("informacion_personal.pdf", as_attachment=True, download_name="informacion_personal.pdf",
                     mimetype="application/pdf")


if __name__ == "__main__":
    app.run(debug=True)
