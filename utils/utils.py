import csv

def add_dados_iniciais(session, Ativo):

    with open('seeds/acoes.csv') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        acoes = []
        for row in csv_reader:
            acoes.append(
                {
                    'nome': row['Nome'],
                    'codigo_negociacao': row['Ticker'],
                    'tipo': 'ação'
                }
            )

        session.bulk_insert_mappings(Ativo, acoes)
        session.commit()
        session.close()
