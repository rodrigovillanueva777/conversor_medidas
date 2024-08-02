import tkinter as tk
import pyperclip  # Para copiar al portapapeles sin messagebox
import re

def convertir():
    try:
        entrada = entry_valor.get().strip()
        matches = re.match(r'(\d+(\.\d+)?)', entrada)
        if matches:
            valor = float(matches.group(1))
            unidad = unidad_var.get().lower()

            if unidad == "ft":
                resultado = valor * 0.3048  # Pies a metros
                resultado_texto.set(f"{round(resultado)} m")
                entry_valor.delete(0, tk.END)
                entry_valor.insert(0, f"{int(valor)} ft")  # Actualizar entrada con unidad
            elif unidad == "m":
                resultado = valor / 0.3048  # Metros a pies
                resultado_texto.set(f"{round(resultado)} ft")
                entry_valor.delete(0, tk.END)
                entry_valor.insert(0, f"{int(valor)} m")  # Actualizar entrada con unidad
        else:
            resultado_texto.set("Formato incorrecto. Ingresa un número válido.")
    except ValueError:
        resultado_texto.set("Por favor, ingresa un número válido.")

def copiar_resultado():
    resultado_copiado = resultado_texto.get()
    pyperclip.copy(resultado_copiado)

def copiar_entrada():
    entrada_copiada = entry_valor.get()
    pyperclip.copy(entrada_copiada)

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
unidad_var = tk.StringVar(value="ft")  # Valor por defecto

# Widgets
label_instruccion = tk.Label(root, text="Ingresa la medida:")
label_instruccion.pack(pady=10)

entry_valor = tk.Entry(root)
entry_valor.pack(pady=5)

# Selector de unidad
label_unidad = tk.Label(root, text="Unidad:")
label_unidad.pack(pady=5)

frame_unidad = tk.Frame(root)
frame_unidad.pack(pady=5)

rb_pies = tk.Radiobutton(frame_unidad, text="Pies (ft)", variable=unidad_var, value="ft")
rb_pies.grid(row=0, column=0)

rb_metros = tk.Radiobutton(frame_unidad, text="Metros (m)", variable=unidad_var, value="m")
rb_metros.grid(row=0, column=1)

# Botones de Pegar y Copiar Entrada en la misma fila
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_pegar = tk.Button(frame_botones, text="Pegar Entrada", command=pegar_medida)
btn_pegar.grid(row=0, column=0, padx=10)

btn_copiar_entrada = tk.Button(frame_botones, text="Copiar Entrada", command=copiar_entrada)
btn_copiar_entrada.grid(row=0, column=2, padx=10)

# Botón Convertir centrado debajo de Pegar y Copiar Entrada
btn_convertir = tk.Button(frame_botones, text="Convertir", command=convertir)
btn_convertir.grid(row=0, column=1, padx=10)

label_resultado = tk.Label(root, textvariable=resultado_texto)
label_resultado.pack(pady=10)

btn_copiar = tk.Button(root, text="Copiar Resultado", command=copiar_resultado)
btn_copiar.pack(pady=5)

root.mainloop()
