from models import db, Video
from app import app

videos = []

"""
title_1 = 'TED-Ed Español'
link_1 = 'https://www.youtube.com/@TEDEdEspanol'
type_1 = 'канал'
description_1 = 'короткие видео на испанском языке по разным темам'

video_1 = Video(title=title_1, link=link_1, type=type_1, description=description_1)
videos.append(video_1)


title_2 = 'El mapa de Sebas'
link_2 = 'https://www.youtube.com/@ElMapadeSebas'
description_2 = 'видео на испанском языке по истории и политике разных стран'

video_2 = Video(title=title_2, link=link_2, type=type_1, description=description_2)
videos.append(video_2)


title_3 = 'Tu escuela de español'
link_3 = 'https://www.youtube.com/@TuescueladeespanolEs'
description_3 = 'видео по лексике и грамматике для начинающих'

video_3 = Video(title=title_3, link=link_3, type=type_1, description=description_3)
videos.append(video_3)


title_4 = 'Daniela Bos'
link_4 = 'https://www.youtube.com/@danielabos'
description_4 = 'влог на испанском языке'

video_4 = Video(title=title_4, link=link_4, type=type_1, description=description_4)
videos.append(video_4)
"""

title_4 = 'BBVA Aprendemos juntos'
link_4 = 'https://www.youtube.com/@danielabos'
type_1 = 'видео'
description_4 = 'влог на испанском языке'

video_4 = Video(title=title_4, link=link_4, type=type_1, description=description_4)
videos.append(video_4)

with app.app_context():
    for video in videos:
        db.session.add(video)
        db.session.commit()


