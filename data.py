import eikon as ek
import numpy
import pandas
ek.set_app_key('cd027055730e46e08ec6eeeaf0986d86824ec3ff')
ford_news = ek.get_news_headlines('FORD', date_from='2019-03-14T09:00:00', date_to='2019-03-15T18:00:00')
print(ford_news[1:])
print(len(ford_news))
ford_news.to_csv('ford1.csv', sep='\t', encoding='utf-8')

headlines = ek.get_news_headlines('EU AND POL',1)
story_id = headlines.iat[0,2]
print(ek.get_news_story(story_id))
