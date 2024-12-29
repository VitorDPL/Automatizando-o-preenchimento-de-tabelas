import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def abrir_chrome():
    driver = webdriver.Chrome()
    url_desejada = "http://127.0.0.1:5000/envia_dados"
    driver.get(url_desejada)
    return driver

def preencher_formulario(driver, dados):
    driver.find_element(By.ID, 'data_venda').send_keys(dados['Data da Venda'])
    driver.find_element(By.ID, 'horario_venda').send_keys(dados['Horário da Venda'])
    driver.find_element(By.ID, 'produto').send_keys(dados['Produto'])
    driver.find_element(By.ID, 'sku').send_keys(dados['SKU'])
    driver.find_element(By.ID, 'categoria').send_keys(dados['Categoria'])
    driver.find_element(By.ID, 'metodo_pagamento').send_keys(dados['Método de Pagamento'])
    driver.find_element(By.ID, 'regiao').send_keys(dados['Região'])
    driver.find_element(By.ID, 'cliente').send_keys(dados['Cliente'])
    driver.find_element(By.ID, 'origem_cliente').send_keys(dados['Origem do Cliente'])
    driver.find_element(By.ID, 'status_pedido').send_keys(dados['Status do Pedido'])
    driver.find_element(By.ID, 'canal_venda').send_keys(dados['Canal de Venda'])
    driver.find_element(By.ID, 'quantidade').send_keys(dados['Quantidade'])
    driver.find_element(By.ID, 'preco_unitario').send_keys(dados['Preço Unitário'])
    driver.find_element(By.ID, 'desconto_aplicado').send_keys(dados['Desconto Aplicado (%)'])
    driver.find_element(By.ID, 'custo_unitario').send_keys(dados['Custo Unitário'])
    driver.find_element(By.ID, 'total_venda').send_keys(dados['Total da Venda'])
    driver.find_element(By.ID, 'lucro_bruto').send_keys(dados['Lucro Bruto'])
    driver.find_element(By.ID, 'frete').send_keys(dados['Frete'])
    driver.find_element(By.ID, 'prazo_entrega_estimado').send_keys(dados['Prazo de Entrega Estimado (dias)'])
    driver.find_element(By.ID, 'prazo_entrega_real').send_keys(dados['Prazo de Entrega Real (dias)'])
    driver.find_element(By.ID, 'feedback').send_keys(dados['Feedback do Cliente'])
    driver.find_element(By.TAG_NAME, 'button').click()

def iniciar_sistema():
    messagebox.showinfo("Aviso", "O sistema está rodando. Por favor, aguarde.")
    driver = abrir_chrome()
    df = pd.read_excel('relatorio_vendas_robusto.xlsx').head(5)

    for _, dados in df.iterrows():
        preencher_formulario(driver, dados)
        time.sleep(0.5)

    driver.quit()
    messagebox.showinfo("Concluído", "O sistema concluiu a execução.")

def criar_interface():
    root = tk.Tk()
    root.title("Sistema de Automação de Planilhas")
    root.geometry("500x400")
    root.configure(bg="#2C3E50") 

    style = ttk.Style()
    style.theme_use('clam')

    style.configure('TFrame', background='#34495E')

    style.configure('TLabel', background='#34495E', foreground='#ECF0F1', font=('Arial', 12))

    style.configure('TButton', background='#1ABC9C', foreground='#FFFFFF', font=('Arial', 12, 'bold'), padding=10)
    style.map('TButton', background=[('active', '#16A085')])

    frame = ttk.Frame(root, padding="20")
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=450, height=350)

    label_bem_vindo = ttk.Label(frame, text="Bem-vindo ao Sistema de Automação de Planilhas", font=("Arial", 16, "bold"), wraplength=400)
    label_bem_vindo.pack(pady=20)

    label_instrucao = ttk.Label(frame, text="Clique no botão abaixo para iniciar o sistema.", foreground="#BDC3C7")
    label_instrucao.pack(pady=10)

    botao_iniciar = ttk.Button(frame, text="Iniciar Sistema", command=iniciar_sistema)
    botao_iniciar.pack(pady=20)

    label_creditos = ttk.Label(frame, text="Desenvolvido por Vitor Lippi", font=("Arial", 10), foreground="#95A5A6")
    label_creditos.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()
