import bs4 #pip install beautifulsoup4
import requests #pip install requests

class Blockscrape:
    def __init__(self):
        forum_html = bs4.BeautifulSoup(requests.get('https://www.blockabl.net/forum/').text, 'html.parser')
        forum_a = forum_html.findAll('a')

        forum = {}
        for topic in forum_a:
            topic = str(topic)
            if topic.startswith('<a href'):
                topic = topic.split('"')[1].split('/')[0]

                topic_html = bs4.BeautifulSoup(requests.get('https://www.blockabl.net/forum/' + topic).text, 'html.parser')
                # print(topic_html)
                posts = []
                posts_html = topic_html.findAll('h5')
                post_num = 0
                for post in posts_html:
                    post_data = {}
                    post_data['title'] = str(post).split('>')[1].split('<')[0]
                    post_data['author'] = str(topic_html.findAll('small')[1]).split('>by ')[1].split(' | ')[0]
                    post_data['rating'] = str(topic_html.findAll('small')[1]).split('>by ')[1].split(' | ')[1].split('</small>')[0]
                    posts.append(post_data)
                    post_num += 1

                forum[topic] = posts

        self.posts = forum

if __name__ == '__main__':
    block = Blockscrape()
    print(block.posts)
