import pandas as pd

from api import models


class ExtractExcelData:
    @staticmethod
    def import_data():
        df = pd.read_excel('api/data.xlsx')

        for index, row in df.iterrows():
                _repr = {
                    'sofifa_id': row['sofifa_id'],
                    'player_url': row['player_url'],
                    'short_name': row['short_name'],
                    'long_name': row['long_name'],
                    'age': row['age'],
                    'nationality': row['nationality'],
                    'club_name': row['club_name'],
                    'league_name': row['league_name'],
                    'overall': row['overall'],
                    'potential': row['potential'],
                }

                models.Player.objects.create(**_repr)


