from app import db, Beauty

beauty1 = Beauty(id=128, description='中文系\n台大最正Youtuber\n羽球女神\nig: graschne\nYouTube頻道: grace mandarin chinese',
 pictures=['https://scontent.ftpe2-2.fna.fbcdn.net/v/t1.6435-9/cp0/e15/q65/p320x320/213359836_151721957048947_5611045002859929479_n.jpg?_nc_cat=102&ccb=1-3&_nc_sid=110474&efg=eyJpIjoiYiJ9&_nc_ohc=hJGsioV9_ZoAX8FPDc0&_nc_ht=scontent.ftpe2-2.fna&oh=a34149c4bed9896f8d7e50cfa8e3afda&oe=612FC18D',
 'https://scontent.ftpe2-1.fna.fbcdn.net/v/t1.6435-9/cp0/e15/q65/s480x480/201337277_151722000382276_3708835688735640682_n.jpg?_nc_cat=111&ccb=1-3&_nc_sid=110474&efg=eyJpIjoiYiJ9&_nc_ohc=oeOXF79CovkAX8HFTpG&_nc_ht=scontent.ftpe2-1.fna&oh=c440bf7da1b159d1e6eec40cabbc3c40&oe=61308B60'],
 likes=1397,comments=183,number=128,gender='male')
# db.create_all()
# fb=Beauty.query.filter_by(id=128).first()
# db.session.delete(fb)
db.session.add(beauty1)
db.session.commit()
print(Beauty.query.all())
