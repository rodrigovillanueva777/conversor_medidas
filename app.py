import tkinter as tk
import pyperclip  # Para copiar al portapapeles sin messagebox
import re
import math

def convertir():
    try:
        entrada = entry_valor.get().strip()
        matches = re.match(r'(\d+(\.\d+)?)\s*(ft|m)', entrada, re.IGNORECASE)
        if matches:
            valor = float(matches.group(1))
            unidad = matches.group(3).lower()

            if unidad == "ft":
                resultado = valor * 0.3048  # Pies a metros
                resultado_texto.set(f"{round(resultado)} m")
            elif unidad == "m":
                resultado = valor / 0.3048  # Metros a pies
                resultado_texto.set(f"{round(resultado)} ft")
        else:
            resultado_texto.set("Formato incorrecto. Ingresa un número seguido de 'ft' o 'm'.")
    except ValueError:
        resultado_texto.set("Por favor, ingresa un número válido.")

def copiar_resultado():
    resultado_copiado = resultado_texto.get()
    pyperclip.copy(resultado_copiado)

def pegar_medida():
    medida_papeles = pyperclip.paste()
    entry_valor.delete(0, tk.END)
    entry_valor.insert(0, medida_papeles)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Conversor Pies-Metros")

# Configurar para mantener la ventana siempre visible
root.wm_attributes('-topmost', 1)

# Variables
resultado_texto = tk.StringVar()

# Widgets
label_instruccion = tk.Label(root, text="Ingresa la nomenclatura (por ejemplo, 40 ft o 12 m):")
label_instruccion.pack(pady=10)

entry_valor = tk.Entry(root)
entry_valor.pack(pady=10)

# Botón de pegar medida desde el portapapeles
btn_pegar = tk.Button(root, text="Pegar", command=pegar_medida)
btn_pegar.pack(pady=10)

btn_convertir = tk.Button(root, text="Convertir", command=convertir)
btn_convertir.pack(pady=10)

label_resultado = tk.Label(root, textvariable=resultado_texto)
label_resultado.pack(pady=10)

btn_copiar = tk.Button(root, text="Copiar Resultado", command=copiar_resultado)
btn_copiar.pack(pady=10)

root.mainloop()
