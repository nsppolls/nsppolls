import pandas as pd
from pathlib import Path
import json
import re

resp = Path('presidentielle.json').read_text()

nsp_polls = (pd
    .json_normalize(
        json.loads(resp.text),
        record_path=['tours','hypotheses', 'candidats'],
        meta=[
            'id', 'nom_institut', 'commanditaire', 'debut_enquete', 'fin_enquete', 'echantillon', 'population',
            ['tours', 'tour'],
            ['tours', 'hypotheses', 'hypothese'],
            ['tours', 'hypotheses', 'sous_echantillon'],
        ]
    )
    .rename(columns={
        'tours.tour': 'tour',
        'tours.hypotheses.hypothese': 'hypothese',
        'tours.hypotheses.sous_echantillon': 'sous_echantillon'
    })
    .fillna({
        'parti': '',
        'candidat': 'autre'
    })
    .assign(
        parti = lambda df: df['parti'].apply(lambda p: re.sub('\[|\]|\'', '', str(p))),
        debut_enquete = lambda df: pd.to_datetime(df['debut_enquete']),
        fin_enquete = lambda df: pd.to_datetime(df['fin_enquete']),
        tour = lambda df: df['tour'].replace(['Premier tour', 'Deuxième tour'], [1,2]),
        day = lambda df: (df['fin_enquete'] - pd.to_datetime('2010-01-01')).dt.days
    )
    .to_csv('presidentielle.csv', index=False, sep=',')
)
