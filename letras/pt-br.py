# -*- coding: utf-8 -*-
import os
from tkinter import *

def create_html_file():
    # Criando o conteúdo do arquivo HTML
    title_text = title_entry.get()
    h1_text = h1_entry.get()
    h2_text = h2_entry.get()
    p_text = p_entry.get()
    h4_text = h4_entry.get()
    iframe_link = iframe_entry.get()

    html_content = f'''<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
    <title> {h1_text} - {h2_text}</title>
    <link rel="stylesheet" href="../css/nav.css">
    <link rel="stylesheet" href="../css/musicas.css">
    <link rel="shortcut icon" type="image/x-icon" href="../favicon.png">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/3.5.0/css/flag-icon.min.css" />
    <script type="text/javascript" src="../javascript/node.js"></script>
</head>
<body>
    <header>
        <nav>
            <a class="logo" href="/"> Letras Padreco</a>
            <div class="mobile-menu">
                <div class="line1"></div>
                <div class="line2"></div>
                <div class="line3"></div>
            </div>
            <ul class="nav-list">
                <li><a href="/"> Início</a> </li>
                <li><a href="../musicas.html"> Músicas</a> </li>
                <li><a href="../sugestoes.html"> Sugestões</a> </li>
            </ul>
        </nav>
    </header>
    </head>
        <div class="container">
            <div class="letra">
<div id="conteudo"data-novo-conteudo="<h1></h1><h2>{h2_text}</h2>
"><h1>{h1_text}</h1><h2>{h2_text}</h2>
{p_text}</div>
                <h4>Compositor: {h4_text}</h4>
            </div>
            <div class="but" style="display:none;">
                <button class="idioma" onclick="alterarConteudo()" style="display:none;"><span class="flag-icon flag-icon-br"style="display:none;"></span>Tradução</button>
                <button class="idioma" onclick="recuperarConteudo()"style="display:none;"><span class="flag-icon flag-icon-us"style="display:none;"></span>Letra Original</button> 
            </div>
            <div class="video">
                <iframe width="500" height="281" src="https://www.youtube.com/embed/{iframe_link}" frameborder="0"
                    allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
        </div>
        <script src="../javascript/mobile-navbar.js"></script>
        <script src="../javascript/translate-btn.js"></script>
        <div id="disqus_thread"></div>
        <script src="../javascript/disqus.js"></script>
        <script id="dsq-count-scr" src="//letras-padreco.disqus.com/count.js" async></script>
    </body>
</html>'''

    # Escrevendo o conteúdo no novo arquivo HTML
    filename = f"{title_text}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Exibindo mensagem de sucesso
    success_label = Label(window, text=f"Arquivo {h2_text  + h1_text} criado com sucesso!")
    success_label.pack()

# Criando a janela
window = Tk()
window.geometry("500x500")
window.title("Criar novo arquivo HTML")

# Criando campos de entrada para as tags
title_label = Label(window, text="Título:")
title_label.pack()
title_entry = Entry(window)
title_entry.pack()

h1_label = Label(window, text="Nome da música (h1):")
h1_label.pack()
h1_entry = Entry(window)
h1_entry.pack()

h2_label = Label(window, text="Nome do Artista (h2):")
h2_label.pack()
h2_entry = Entry(window)
h2_entry.pack()

p_label = Label(window, text="Letra da música (p):")
p_label.pack()
p_entry = Entry(window)
p_entry.pack()

h4_label = Label(window, text="Compositor (h4):")
h4_label.pack()
h4_entry = Entry(window)
h4_entry.pack()

iframe_label = Label(window, text="Link do iframe:")
iframe_label.pack()
iframe_entry = Entry(window)
iframe_entry.pack()




create_button = Button(window, text="Criar arquivo HTML", command=create_html_file)
create_button.pack()

window.mainloop()