import subprocess
import pickle
import os

def usar_shell_con_riesgo():
    comando = "ls -l"
    subprocess.run(comando, shell=True)  # B602: subprocess call with shell=True

def usar_pickle_inseguro():
    datos = b"cosas"
    obj = pickle.loads(datos)  # B301: pickle es inseguro con input no confiable

def uso_eval():
    codigo = "2 + 2"
    resultado = eval(codigo)  # B307: uso de eval()

def lectura_path_no_validada(user_input):
    os.system(f"cat {user_input}")  # B602: shell injection

usar_shell_con_riesgo()
usar_pickle_inseguro()
uso_eval()
lectura_path_no_validada("archivo.txt")
