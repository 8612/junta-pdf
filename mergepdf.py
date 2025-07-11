import os
from tkinter import Tk, Label, Button, filedialog, messagebox
from pypdf import PdfWriter

def selecionar_pdf1():
    global pdf1
    pdf1 = filedialog.askopenfilename(title="Selecione o primeiro arquivo PDF", filetypes=[("PDF Files", "*.pdf")])
    if pdf1:
        label_pdf1.config(text=f"PDF 1: {os.path.basename(pdf1)}")

def selecionar_pdf2():
    global pdf2
    pdf2 = filedialog.askopenfilename(title="Selecione o segundo arquivo PDF", filetypes=[("PDF Files", "*.pdf")])
    if pdf2:
        label_pdf2.config(text=f"PDF 2: {os.path.basename(pdf2)}")

def salvar_pdf():
    global file_path
    file_path = filedialog.asksaveasfilename(title="Salvar como", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        label_salvar.config(text=f"Salvar em: {os.path.basename(file_path)}")

def juntar_pdfs():
    try:
        if not pdf1 or not pdf2 or not file_path:
            messagebox.showerror("Erro", "Certifique-se de selecionar os dois PDFs e o local de salvamento.")
            return

        merger = PdfWriter()
        merger.append(pdf1)
        merger.append(pdf2)
        
        merger.write(file_path)
        merger.close()

        messagebox.showinfo("Sucesso", f"PDFs foram unidos e salvos em:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao juntar os PDFs: {e}")

# Configuração da interface Tkinter
root = Tk()
root.title("Juntar PDFs")
root.geometry("400x400")
root.resizable(False, False)

# Labels
Label(root, text="Selecione os arquivos PDF para juntar", font=("Arial", 14)).pack(pady=10)

label_pdf1 = Label(root, text="PDF 1: Não selecionado", font=("Arial", 12))
label_pdf1.pack(pady=5)

label_pdf2 = Label(root, text="PDF 2: Não selecionado", font=("Arial", 12))
label_pdf2.pack(pady=5)

label_salvar = Label(root, text="Salvar em: Não definido", font=("Arial", 12))
label_salvar.pack(pady=5)

# Botões
Button(root, text="Selecionar PDF 1", command=selecionar_pdf1, font=("Arial", 12)).pack(pady=5)
Button(root, text="Selecionar PDF 2", command=selecionar_pdf2, font=("Arial", 12)).pack(pady=5)
Button(root, text="Escolher local de salvamento", command=salvar_pdf, font=("Arial", 12)).pack(pady=5)
Button(root, text="Juntar PDFs", command=juntar_pdfs, font=("Arial", 12), bg="green", fg="white").pack(pady=15)

root.mainloop()



# from pypdf import PdfWriter
# import os
# from tkinter import filedialog

# merger = PdfWriter()

# #root = tk.Tk()
# #root.withdraw()
# input("Escolha o primeiro PDF - Aperte enter para continuar\n\n")
# pdf1  = filedialog.askopenfilename()
# input("Agora escolha o segundo PDF - Aperte enter para continuar\n\n")
# pdf2 = filedialog.askopenfilename()
# input("Agora escolha onde deseja salvar e o nome do arquivo - Aperte enter para continuar\n\n")
# file_path = filedialog.asksaveasfilename()

# #nomeArquivo = input("Cole o nome do arquivo final aqui: ")

# #pdfList = (sorted(os.listdir()))

# merger.append(pdf1)

# merger.append(pdf2)
# """try:
#     for pdf in [pdfList[1], pdfList[0]]:
#         merger.append(pdf)

# except:
#     print("O arquivo já existe nessa pasta...")
# """
# try:
#     merger.write(f"{file_path}.pdf")
# except:
#     print("Ocorreu um erro ao juntar os PDFs")
# merger.close()