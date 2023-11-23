from Hispanist_flask.my_app.models import db, Video
from manage import app

videos = []

title_1 = '¿Por qué las máquinas de movimiento perpetuo nunca funcionan? - Netta Schramm'
link_1 = 'https://www.youtube.com/embed/ajR8dgMwycs'
type_1 = 'видео'

video_1 = Video(title=title_1, link=link_1, type=type_1)
videos.append(video_1)

title_2 = 'La HISTORIA DE ESPAÑA en 15 minutos | El RESUMEN definitivo'
link_2 = 'https://www.youtube.com/embed/90H1JvKT5tI'
description_2 = 'видео на испанском языке по истории и политике разных стран'

video_2 = Video(title=title_2, link=link_2, type=type_1)
videos.append(video_2)

title_3 = 'La GUERRA CIVIL ESPAÑOLA en 13 minutos | Resumen fácil y divertido'
link_3 = 'https://www.youtube.com/embed/5Zwv43MUA7s'
description_3 = 'видео по лексике и грамматике для начинающих'

video_3 = Video(title=title_3, link=link_3, type=type_1)
videos.append(video_3)

title_4 = 'Los alimentos (nivel básico)'
link_4 = 'https://www.youtube.com/embed/OhSjoQofCiw'
description_4 = 'влог на испанском языке'

video_4 = Video(title=title_4, link=link_4, type=type_1)
videos.append(video_4)

title_4 = 'Comunidades autónomas de España (nivel básico)'
link_4 = 'https://www.youtube.com/embed/Md5-ANncZpM'
description_4 = 'влог на испанском языке'

video_5 = Video(title=title_4, link=link_4, type=type_1)
videos.append(video_5)


title_4 = 'Tiempo libre y ocio I (nivel básico)'
link_4 = 'https://www.youtube.com/embed/dMpC1TCDJUI'
description_4 = 'влог на испанском языке'

video_6 = Video(title=title_4, link=link_4, type=type_1)
videos.append(video_6)

with app.app_context():
    for video in videos:
        db.session.add(video)
        db.session.commit()


