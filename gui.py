import tkinter as tk
from tkinter import messagebox

def diagnose():
    answers = {
        "demam": var_demam.get(),
        "batuk": var_batuk.get(),
        "pilek": var_pilek.get(),
        "sakit_tenggorokan": var_sakit_tenggorokan.get()
    }

    if all([answers["demam"], answers["batuk"], answers["pilek"]]):
        result = "Anda kemungkinan terkena FLU."
    elif answers["sakit_tenggorokan"] and answers["pilek"]:
        result = "Anda kemungkinan terkena RADANG TENGGOROKAN."
    else:
        result = "Gejala tidak cukup untuk diagnosis tertentu.\nSilakan konsultasikan ke dokter."

    messagebox.showinfo("Hasil Diagnosis", result)

# GUI setup
root = tk.Tk()
root.title("Sistem Pakar Diagnosa Penyakit")

tk.Label(root, text="Jawab gejala berikut:").pack(pady=10)

var_demam = tk.BooleanVar()
var_batuk = tk.BooleanVar()
var_pilek = tk.BooleanVar()
var_sakit_tenggorokan = tk.BooleanVar()

tk.Checkbutton(root, text="Demam", variable=var_demam).pack(anchor="w")
tk.Checkbutton(root, text="Batuk", variable=var_batuk).pack(anchor="w")
tk.Checkbutton(root, text="Pilek", variable=var_pilek).pack(anchor="w")
tk.Checkbutton(root, text="Sakit Tenggorokan", variable=var_sakit_tenggorokan).pack(anchor="w")

tk.Button(root, text="Diagnosa", command=diagnose).pack(pady=10)

root.mainloop()
