from projeto import app, db
from flask import request, jsonify, render_template

from projeto.models import *
from flask import request, redirect, url_for

@app.route('/envia_dados', methods=['GET', 'POST'])
def envia_dados():
    if request.method == 'POST':
        data_venda = request.form['data_venda']
        horario_venda = request.form['horario_venda']
        produto = request.form['produto']
        sku = request.form['sku']
        categoria = request.form['categoria']
        metodo_pagamento = request.form['metodo_pagamento']
        regiao = request.form['regiao']
        cliente = request.form['cliente']
        origem_cliente = request.form['origem_cliente']
        status_pedido = request.form['status_pedido']
        canal_venda = request.form['canal_venda']
        quantidade = request.form['quantidade']
        preco_unitario = request.form['preco_unitario']
        desconto_aplicado = request.form['desconto_aplicado']
        custo_unitario = request.form['custo_unitario']
        total_venda = request.form['total_venda']
        lucro_bruto = request.form['lucro_bruto']
        frete = request.form['frete']
        prazo_entrega_estimado = request.form['prazo_entrega_estimado']
        prazo_entrega_real = request.form['prazo_entrega_real']
        feedback = request.form['feedback']

        novo_dado = Dados(
            data_venda=data_venda,
            horario_venda=horario_venda,
            produto=produto,
            sku=sku,
            categoria=categoria,
            metodo_pagamento=metodo_pagamento,
            regiao=regiao,
            cliente=cliente,
            origem_cliente=origem_cliente,
            status_pedido=status_pedido,
            canal_venda=canal_venda,
            quantidade=quantidade,
            preco_unitario=preco_unitario,
            desconto_aplicado=desconto_aplicado,
            custo_unitario=custo_unitario,
            total_venda=total_venda,
            lucro_bruto=lucro_bruto,
            frete=frete,
            prazo_entrega_estimado=prazo_entrega_estimado,
            prazo_entrega_real=prazo_entrega_real,
            feedback=feedback
        )

        db.session.add(novo_dado)
        db.session.commit()

        return redirect(url_for('envia_dados'))

    return render_template('envia_dados.html')