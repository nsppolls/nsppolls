import pandas as pd
from pathlib import Path
import json
import re

resp = Path('presidentielle.json').read_text()

nsp_polls = (pd
    .json_normalize(
        json.loads(resp),
        record_path=['tours','hypotheses', 'candidats'],
        meta=[
            'id', 'nom_institut', 'commanditaire', 'debut_enquete', 'fin_enquete', 'echantillon', 'population', 'rolling',
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
        fin_enquete = lambda df: pd.to_datetime(df['fin_enquete'])
    )
    .to_csv('presidentielle.csv', index=False, sep=',')
)
