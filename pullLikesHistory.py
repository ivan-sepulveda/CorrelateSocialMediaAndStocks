from random import choice
import json
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from datetime import datetime


_user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
]


class InstagramScraper:

    def __init__(self, user_agents=None, proxy=None):
        self.user_agents = user_agents
        self.proxy = proxy

    def __random_agent(self):
        if self.user_agents and isinstance(self.user_agents, list):
            return choice(self.user_agents)
        return choice(_user_agents)

    def __request_url(self, url):
        try:
            response = requests.get(url, headers={'User-Agent': self.__random_agent()}, proxies={'http': self.proxy,
                                                                                                 'https': self.proxy})
            response.raise_for_status()
        except requests.HTTPError:
            raise requests.HTTPError('Received non 200 status code from Instagram')
        except requests.RequestException:
            raise requests.RequestException
        else:
            return response.text

    @staticmethod
    def extract_json_data(html):
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find('body')
        script_tag = body.find('script')
        raw_string = script_tag.text.strip().replace('window._sharedData =', '').replace(';', '')
        return json.loads(raw_string)

    def profile_page_metrics(self, profile_url):
        results = {}
        try:
            response = self.__request_url(profile_url)
            json_data = self.extract_json_data(response)
            metrics = json_data['entry_data']['ProfilePage'][0]['graphql']['user']
        except Exception as e:
            raise e
        else:
            for key, value in metrics.items():
                if key != 'edge_owner_to_timeline_media':
                    if value and isinstance(value, dict):
                        value = value['count']
                        results[key] = value
                    elif value:
                        results[key] = value
        return results

    def profile_page_recent_posts(self, profile_url):
        results_a = []
        results_b = []
        try:
            response = self.__request_url(profile_url)
            json_data = self.extract_json_data(response)
            metrics = json_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']["edges"]
        except Exception as e:
            raise e
        else:
            count = 1
            for node in metrics:
                print(count)
                node = node.get('node')
                temp_dict = dict()
                if node and isinstance(node, dict):
                    print(node)
                    results_a.append(node)
                    # print("\n{0}________________________________".format(count))
                    like_count = node["edge_liked_by"]['count']
                    temp_dict["like_count"] = node["edge_liked_by"]['count']
                    # print("Likes: ", like_count)
                    comment_count = node["edge_media_to_comment"]['count']
                    temp_dict["comment_count"] = node["edge_media_to_comment"]['count']

                    # print("Comments: ", comment_count)
                    # print(node)
                    timestampUnix = node["taken_at_timestamp"]
                    timestampIso = datetime.fromtimestamp(timestampUnix).isoformat()
                    # print("Uploaded: {0}".format(timestampIso))
                    temp_dict["uploaded"] = datetime.fromtimestamp(timestampUnix).isoformat()
                    results_b.append(temp_dict)
                count += 1

        return results_b

k = InstagramScraper()
results___ = k.profile_page_recent_posts('https://www.instagram.com/nike/?hl=en')
# pprint(results)
