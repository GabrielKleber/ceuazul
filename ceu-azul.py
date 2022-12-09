from flask import Flask, render_template, request, flash, redirect
import json
import random

'''
---------------------------------------------------------------------------------------------------------------------
NOME DA EQUIPE:
Gabriel Kleber da Silva Batista
Nafanael Pereira Alves
Guilherme Santos de Medeiros

Como o código ficou muito grande, não deu para falar o que cada linha faz, mas da pra interpretar o que elas fazem
----------------------------------------------------------------------------------------------------------------------
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = "chave_secreta123"

@app.route('/')
@app.route('/index')
def index():
    global u
    u = random.randint(111111, 999999)
    senha = []
    with open('confir.json') as confir:
        lista_con = json.load(confir)
        cont = 0
        for h in lista_con:
            cont += 1
            if u == h['senha_conf']:
                pass
            if cont >= len(lista_con):
                senha = [{
                    "senha_conf": u
                }]
                with open('confir.json') as confir:
                    arq = json.load(confir)
                arqui = arq + senha
                with open('confir.json', 'w') as escre:
                    json.dump(arqui, escre, indent=3)

    return render_template('html/index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
@app.route('/home/cadastro', methods=['GET', 'POST'])
def cadastro():
    global nome_cad, senha_cad, email_cad, u
    if request.method == 'GET':
        return render_template('html/cadastro.html')
    else:
        user = []
        nome_cad = request.form.get('usuario_cad')
        senha_cad = request.form.get('senha_cad')
        email_cad = request.form.get('email_cad')
        with open('usuario.json') as usuario:
            lista = json.load(usuario)
            cont = 0
            for c in lista:
                cont += 1
                if email_cad == c['email']:
                    flash('E-mail invalido')
                    return redirect('/cadastro')
                if cont >= len(lista):
                    user=[{
                        "nome": nome_cad,
                        "email": email_cad,
                        "senha": senha_cad,
                    }]
                    with open('usuario.json') as usuarios:
                        arquivo = json.load(usuarios)
                    arquivo_2 = arquivo + user
                    with open('usuario.json', 'w') as arquivo:
                        json.dump(arquivo_2, arquivo, indent=4)
                    return redirect('/home/menu/comidas')

@app.route('/login', methods=['GET', 'POST'])
@app.route('/home/login', methods=['GET', 'POST'])
def login():
    global senha, email
    if request.method == 'GET':
        return render_template('html/login.html')
    else:
        email = request.form.get('email')
        senha = request.form.get('senha')
        with open('usuario.json') as usuario:
            lista = json.load(usuario)
            cont = 0
            for c in lista:
                cont += 1
                if email == c['email']:
                    if senha == c['senha']:
                        return redirect('/home/menu/comidas')
                if cont >= len(lista):
                    flash('E-mail ou Senha invalida')
                    return redirect('/login')

@app.route('/termos')
def termos():
    return render_template('html/termos.html')

@app.route('/erro')
def erro():
    return render_template('html/erro.html')

@app.route("/home/menu/comidas", methods=['GET', 'POST'])
def home_comidas():
    if request.method == 'GET':
        return render_template('html/home.html')
    else:
        pedido = []
        try:
            gmail = email
        except NameError:
            try:
                gmail = email_cad
            except NameError:
                return redirect("/erro")
            else:
                gmail = email_cad
        else:
            gmail = email

        cuscuz = request.form.get('cuscuz') # 63.99
        galinhada = request.form.get('galinhada') # 24.99
        feijoada = request.form.get('feijoada') # 38.90
        tapioca = request.form.get('tapioca') # 4.99
        acaraje = request.form.get('acaraje') # 17.00
        vaca = request.form.get('vaca') # 28.00
        buchada = request.form.get('buchada') # 19.00
        rubacao = request.form.get('rubacao') # 66.00

        if cuscuz == "63.99":
            pedido = [{
                "comida": "cuscuz",
                "preco": 63.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/comidas')
        if cuscuz != "63.99":
            pass

        if galinhada == "24.99":
            pedido = [{
                "comida": "galinhada",
                "preco": 24.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/comidas')
        if galinhada != "24.99":
            pass

        if feijoada == "38.90":
            pedido = [{
                "comida": "feijoada",
                "preco": 38.90,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/comidas')
        if feijoada != "38.90":
            pass

        if tapioca == "4.99":
            pedido = [{
                "comida": "tapioca",
                "preco": 4.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/comidas')
        if tapioca != "4.99":
            pass

        if acaraje == "17.00":
            pedido = [{
                "comida": "acaraje",
                "preco": 17.00,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/comidas')
        if acaraje != "17.00":
            pass

        if vaca == "28.00":
            pedido = [{
                "comida": "vaca atolada",
                "preco": 28.00,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/comidas')
        if vaca != "28.00":
            pass

        if buchada == "19.00":
            pedido = [{
                "comida": "buchada",
                "preco": 19.00,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/comidas')
        if buchada != "19.00":
            pass

        if rubacao == "66.00":
            pedido = [{
                "comida": "rubacao",
                "preco": 66.00,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/comidas')
        if rubacao != "66.00":
            pass

@app.route("/home/menu/bebidas", methods=['GET', 'POST'])
def home_bebidas():
    if request.method == 'GET':
        return render_template('html/home_bebidas.html')
    else:
        pedido = []
        try:
            gmail = email
        except NameError:
            try:
                gmail = email_cad
            except NameError:
                return redirect("/erro")
            else:
                gmail = email_cad
        else:
            gmail = email

        cafe = request.form.get('cafe') # 1.49
        cha = request.form.get('cha') # 1.99
        sucos = request.form.get('sucos') # 0.99
        refri = request.form.get('refrigerantes') # 1.99

        if cafe == "1.49":
            pedido = [{
                "comida": "cafe",
                "preco": 1.49,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/bebidas')
        if cafe != "1.49":
            pass

        if cha == "1.99":
            pedido = [{
                "comida": "cha",
                "preco": 1.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/bebidas')
        if cha != "1.99":
            pass

        if sucos == "limao":
            pedido = [{
                "comida": "suco de limao",
                "preco": 0.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/bebidas')
        if sucos != "limao":
            pass

        if sucos == "laranja":
            pedido = [{
                "comida": "suco de laranja",
                "preco": 0.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/bebidas')
        if sucos != "laranja":
            pass

        if sucos == "tamarindo":
            pedido = [{
                "comida": "suco de tamarindo",
                "preco": 0.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/bebidas')
        if sucos != "tamarindo":
            pass
        
        if sucos == "0":
            return redirect('/home/menu/bebidas')
        if sucos != "0":
            pass

        if refri == "coca":
            pedido = [{
                "comida": "refrigerante de coca",
                "preco": 1.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/bebidas')
        if refri != "coca":
            pass

        if refri == "laranja":
            pedido = [{
                "comida": "refrigerante de laranja",
                "preco": 1.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/bebidas')
        if refri != "laranja":
            pass

        if refri == "guarana":
            pedido = [{
                "comida": "refrigerante de guarana",
                "preco": 1.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/bebidas')
        if refri != "guarana":
            pass

        if refri == "0":
            return redirect('/home/menu/bebidas')
        if refri != "0":
            pass

@app.route("/home/menu/doces", methods=['GET', 'POST'])
def home_doces():
    if request.method == 'GET':
        return render_template('html/home_doces.html')
    else:
        pedido = []
        try:
            gmail = email
        except NameError:
            try:
                gmail = email_cad
            except NameError:
                return redirect("/erro")
            else:
                gmail = email_cad
        else:
            gmail = email

        brigadeiro = request.form.get('brigadeiro') # 2.99
        chocolate = request.form.get('chocolate') # 3.99
        milkshake = request.form.get('milkshake') # 1.99
        mousse = request.form.get('mousse') # 4.99
        pudim = request.form.get('pudim') # 5.99
        raspadinha = request.form.get('raspadinha') # 2.99

        if brigadeiro == "2.99":
            pedido = [{
                "comida": "brigadeiro",
                "preco": 2.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/doces')
        if brigadeiro != "2.99":
            pass

        if chocolate == "3.99":
            pedido = [{
                "comida": "chocolate quente",
                "preco": 3.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/doces')
        if chocolate != "3.99":
            pass

        if milkshake == "1.99":
            pedido = [{
                "comida": "milkshake",
                "preco": 1.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/doces')
        if milkshake != "1.99":
            pass

        if mousse == "4.99":
            pedido = [{
                "comida": "mousse de maracuja",
                "preco": 4.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/doces')
        if mousse != "4.99":
            pass

        if pudim == "5.99":
            pedido = [{
                "comida": "pudim de leite",
                "preco": 5.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/doces')
        if pudim != "5.99":
            pass

        if raspadinha == "2.99":
            pedido = [{
                "comida": "raspadinha",
                "preco": 2.99,
                "email": gmail,
                "senha_conf": u
            }]
            with open('pedido.json') as ped:
                tipo = json.load(ped)
            arquivo = tipo + pedido
            with open('pedido.json', 'w') as pedi:
                json.dump(arquivo, pedi, indent=5)
            return redirect('/home/menu/doces')
        if raspadinha != "2.99":
            pass

@app.route("/home/menu/mesas", methods=['GET', 'POST'])
def home_mesa():
    if request.method == 'GET':
        return render_template('html/home_mesas.html')
    else:
        arq = []
        try:
            gmail = email
        except NameError:
            try:
                gmail = email_cad
            except NameError:
                return redirect("/erro")
            else:
                gmail = email_cad
        else:
            gmail = email
        
        pessoas = request.form.get('quant')
        if pessoas == "2":
            w = random.randint(1, 5)
        if pessoas == "3":
            w = random.randint(6, 10)
        if pessoas == "4":
            w = random.randint(11, 15)
        if pessoas == "5":
            w = random.randint(16, 20)
        if pessoas != "2" and pessoas != "3" and pessoas != "4" and pessoas != "5":
            return "ERRO, POR FAVOR DIGITE A QUANTIDADE DE PESSOAS"
        arq = [{
                "mesa": w,
                "email": gmail,
                "senha_conf": u
            }]
        with open('mesa.json') as pedido:
            ped = json.load(pedido)
        arquivo = ped + arq
        with open('mesa.json', 'w') as esc:
            json.dump(arquivo, esc, indent=4)
        return redirect('/finalizacao')

@app.route('/finalizacao', methods=['GET', 'POST'])
def finalizacao():
    conta_final = 0
    comp = 0
    try:
        gmail = email
    except NameError:
        try:
            gmail = email_cad
        except NameError:
            return redirect("/erro")
        else:
            gmail = email_cad
    else:
        gmail = email
    with open('usuario.json') as usu:
        lista = json.load(usu)
        cont = 0
        for c in lista:
            cont += 1
            if gmail == c['email']:
                nome = c['nome']
            if cont >= len(lista):
                pass
    with open('pedido.json') as ped:
        lista_2 = json.load(ped)
        cont_2 = 0
        for f in lista_2:
            cont_2 += 1
            if gmail == f['email']:
                if u == f['senha_conf']:
                    conta_final += f['preco']
            if cont_2 >= len(lista_2):
                pass
    with open('mesa.json') as mesa:
        lista_3 = json.load(mesa)
        cont_3 = 0
        for j in lista_3:
            cont_3 += 1
            if gmail == j['email']:
                if u == j['senha_conf']:
                    comp += j['mesa']
            if cont_3 >= len(lista_3):
                pass

    if request.method == 'GET':
        return render_template('html/finalizacao.html', nome=nome, preco_final=conta_final, comp=comp, senha_confir=u)
    else:
        pass

@app.route('/suporte', methods=['GET', 'POST'])
@app.route('/home/suporte', methods=['GET', 'POST'])
def suporte():
    if request.method == 'GET':
        return render_template('html/suporte.html')
    else:
        res = int(request.form.get('problema'))
        if res == 1:
            return render_template('html/suporte/pag_1.html')
        elif res == 2:
            return render_template('html/suporte/pag_2.html')
        elif res == 3:
            return render_template('html/suporte/pag_3.html')
        elif res == 4:
            return render_template('html/suporte/pag_4.html')
        elif res == 5:
            return render_template('html/suporte/pag_5.html')
        else:
            return 'Número invalido'

if __name__ == "__main__":
    app.run(debug=True)
