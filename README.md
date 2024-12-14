<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Encriptação e Desencriptação com AES-GCM</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        h1 {
            text-align: center;
        }
        p, pre {
            background: #fff;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        code {
            background: #eee;
            padding: 2px 4px;
            border-radius: 3px;
        }
        .highlight {
            background: #fffae3;
            border-left: 6px solid #ffe270;
            padding: 10px;
            margin: 20px 0;
        }
        .command {
            background: #272822;
            color: #f8f8f2;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Encriptação e Desencriptação com AES-GCM</h1>
    <h2>Funcionalidades</h2>
    <p>Este projeto implementa uma aplicação gráfica simples para encriptação e desencriptação de arquivos usando o algoritmo AES-GCM. A interface gráfica é feita com Tkinter, e o código de encriptação/desencriptação utiliza a biblioteca <code>cryptography</code>.</p>
    <h3>Funcionalidades</h3>
    <ul>
        <li><strong>Encriptação</strong>: Encripta arquivos usando AES-GCM com uma senha fornecida pelo usuário.</li>
        <li><strong>Desencriptação</strong>: Desencripta arquivos previamente encriptados usando a mesma senha.</li>
    </ul>

    <h2>Requisitos de Instalação</h2>
    <p>Certifique-se de ter as seguintes dependências instaladas:</p>
    <ul>
        <li>Python 3.x</li>
        <li>Bibliotecas Python:
            <ul>
                <li><code>cryptography</code></li>
                <li><code>tkinter</code> (geralmente incluído nas instalações padrão do Python)</li>
            </ul>
        </li>
    </ul>
    <h3>Instalar Dependências no Linux</h3>
    <pre class="command">
        sudo apt update
        sudo apt install python3 python3-pip python3-tk
        pip install cryptography
    </pre>
    <h3>Instalar Dependências no Windows</h3>
    <ol>
        <li>Baixe e Instale Python: <a href="https://www.python.org/downloads/">python.org/downloads</a></li>
        <li>Instale as Bibliotecas:
            <pre class="command">
                pip install cryptography
            </pre>
        </li>
    </ol>
    <h3>Instalar Dependências no macOS</h3>
    <pre class="command">
        brew install python3
        pip3 install cryptography
    </pre>

    <h2>Como Executar</h2>
    <h3>No Linux</h3>
    <pre class="command">
        git clone https://github.com/usuario/repositorio.git
        cd repositorio
        python3 crypt.py
    </pre>
    <h3>No Windows</h3>
    <pre class="command">
        git clone https://github.com/usuario/repositorio.git
        cd repositorio
        python crypt.py
    </pre>
    <h3>No macOS</h3>
    <pre class="command">
        git clone https://github.com/usuario/repositorio.git
        cd repositorio
        python3 crypt.py
    </pre>

    <h2>O Que o Código Faz</h2>
    <p>O código implementa funções para encriptação e desencriptação de arquivos utilizando AES-GCM com uma GUI simples em Tkinter.</p>
    <h3>Funções Principais</h3>
    <ul>
        <li><code>encrypt_AES_GCM</code>: Encripta dados usando AES-GCM.</li>
        <li><code>decrypt_AES_GCM</code>: Desencripta dados previamente encriptados usando AES-GCM.</li>
        <li><code>encrypt_button_clicked</code>: Lida com a encriptação quando o botão "Encrypt" é clicado.</li>
        <li><code>decrypt_button_clicked</code>: Lida com a desencriptação quando o botão "Decrypt" é clicado.</li>
        <li><code>setup_gui</code>: Configura a interface gráfica.</li>
    </ul>
    <h3>Como Funciona</h3>
    <p><strong>Encriptação:</strong></p>
    <div class="highlight">
        <ul>
            <li>Usuário fornece uma senha e escolhe um arquivo.</li>
            <li>O arquivo é encriptado usando AES-GCM com um salt e nonce gerados aleatoriamente.</li>
            <li>O arquivo encriptado é salvo, substituindo o arquivo original.</li>
        </ul>
    </div>
    <p><strong>Desencriptação:</strong></p>
    <div class="highlight">
        <ul>
            <li>Usuário fornece a mesma senha usada para encriptação e escolhe um arquivo encriptado.</li>
            <li>O arquivo é desencriptado usando a senha, salt, nonce, e tag.</li>
            <li>O arquivo desencriptado é salvo, substituindo o arquivo encriptado.</li>
        </ul>
    </div>

    <h3>Interface Gráfica</h3>
    <p>A interface gráfica é feita usando Tkinter com botões para escolher arquivos e realizar a encriptação/desencriptação.</p>
</body>
</html>
