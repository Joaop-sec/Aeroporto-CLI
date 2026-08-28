import math
from models.mensagem import mensagem
from services.opensky_service import OpenSkyService

def cadastrar_mensagem(id, remetente, destinatario, conteudo, horario):
    mensagem_obj = mensagem(id, remetente, destinatario, conteudo, horario, [])
    return mensagem_obj

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def verificar_ocupacao_pista(lat_pista, lon_pista, raio_km=2.0, altitude_max=500):
    with OpenSkyService() as service:
        resultado = service.buscar_voos()
        if not resultado.success:
            return None, resultado.error
        df = resultado.data
        if df.empty:
            return [], "Nenhum voo ativo no momento."
        df['dist'] = df.apply(
            lambda row: haversine(lat_pista, lon_pista, row['latitude'], row['longitude']),
            axis=1
        )
        ocupantes = df[
            (df['dist'] < raio_km) &
            ((df['baro_altitude'] < altitude_max) | (df['on_ground'] == True))
        ]
        return ocupantes[['callsign', 'dist', 'baro_altitude', 'on_ground']].to_dict('records'), None
