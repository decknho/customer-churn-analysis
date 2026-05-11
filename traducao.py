import pandas as pd

pd.options.display.float_format = '{:.2f}'.format

df = pd.read_csv('./data/netflix_customer_churn.csv')

tradução_colunas = {
    "customer_id": "id_cliente",
    "age": "idade",
    "gender": "genero",
    "subscription_type": "tipo_assinatura",
    "watch_hours": "horas_assistidas",
    "last_login_days": "ultimo_dia_logado",
    "region": "regiao",
    "device": "dispositivo",
    "monthly_fee": "pagamento_mensal",
    "churned": "churn",
    "payment_method": "metodo_pagamento",
    "number_of_profiles": "quantidade_perfis",
    "avg_watch_time_per_day": "porcentagem_assistida_por_dia",
    "favorite_genre": "genero_favorito"
}

df.rename(columns=tradução_colunas, inplace=True)

df["tipo_assinatura"] = df["tipo_assinatura"].map({
    "Basic": "Padrão com anúncios",
    "Standard": "Padrão",
    "Premium": "Premium"
})

df["metodo_pagamento"] = df["metodo_pagamento"].map({
    "Credit Card": "Cartão de Crédito",
    "Debit Card": "Cartão de Débito",
    "Crypto": "Criptomoeda",
    "PayPal": "PayPal",
    "Gift Card": "Cartão Presente"
})

df["genero"] = df["genero"].map({
    "Male": "Masculino",
    "Female": "Feminino",
    "Other": "Outro"
})

df["pagamento_mensal"] = df["pagamento_mensal"].map({
    8.99: 20.90,
    13.99: 44.90,
    17.99: 59.90
})

df["genero_favorito"] = df["genero_favorito"].map({
    "Documentary": "Documentário",
    "Action": "Ação",
    "Comedy": "Comédia",
    "Horror": "Terror",
    "Romance": "Romance",
    "Sci-Fi": "Ficção Científica",
    "Drama": "Drama",
})

df["regiao"] = df["regiao"].map({
    "North America": "América do Norte",
    "Europe": "Europa",
    "Asia": "Ásia",
    "South America": "América do Sul",
    "Africa": "África",
    "Oceania": "Oceania"
})

df.head(15)