import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title = 'Selecione uma pasta')

listaArquivos = os.listdir(caminho)

locais = {
      'NES Games': ['.nes'],
      'SNES Games': ['.smc', '.sfc', '.swc', '.SMC'],
      'N64 Games': ['.n64', '.N64', '.z64', '.v64'],
      'DS Games': ['.ds', '.dsv'],
      'MegaDrive Games': ['.gen']
}

for arquivo in listaArquivos:
      nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
      for pasta in locais:
            if extensao in locais[pasta]:
                  if not os.path.exists(f'{caminho}/{pasta}'):
                        os.mkdir(f'{caminho}/{pasta}')
                  os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')