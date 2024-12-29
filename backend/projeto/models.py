from projeto import db

class Dados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_venda = db.Column(db.String(100), nullable=False)
    horario_venda = db.Column(db.String(100), nullable=False)
    produto = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    metodo_pagamento = db.Column(db.String(100), nullable=False)
    regiao = db.Column(db.String(100), nullable=False)
    cliente = db.Column(db.String(100), nullable=False)
    origem_cliente = db.Column(db.String(100), nullable=False)
    status_pedido = db.Column(db.String(100), nullable=False)
    canal_venda = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)
    desconto_aplicado = db.Column(db.Float, nullable=False)
    custo_unitario = db.Column(db.Float, nullable=False)
    total_venda = db.Column(db.Float, nullable=False)
    lucro_bruto = db.Column(db.Float, nullable=False)
    frete = db.Column(db.Float, nullable=False)
    prazo_entrega_estimado = db.Column(db.Integer, nullable=False)
    prazo_entrega_real =  db.Column(db.Integer, nullable=False)
    feedback = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Dados %r>' % self.id