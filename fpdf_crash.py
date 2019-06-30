from fpdf import FPDF      # para crear pdf

titulo='Plane crashes by location and by operator'

class PDF(FPDF):
    def header(self):  # cabecera
        self.set_font('Arial', 'B', 15)  # fuente Arial negrita 15  
        ancho=self.get_string_width(titulo)+6 # calcula el ancho del titulo 
        #y su posicion
        self.set_x((210-ancho)/2)
        self.set_draw_color(0, 80, 180)  # colores del marco, fondo y texto
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1) # ancho del marco (1 mm)
        self.cell(ancho, 9, titulo, 1, 1, 'C', 1)  # titulo
        self.ln(10) # salto de linea


        
