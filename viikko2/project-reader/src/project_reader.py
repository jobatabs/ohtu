from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = toml.loads(request.urlopen(self._url).read().decode("utf-8"))

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(content['tool']['poetry']['name'], content['tool']['poetry']['description'], content['tool']['poetry']['license'], content['tool']['poetry']['authors'], content['tool']['poetry']['dependencies'].keys(), content['tool']['poetry']['group']['dev']['dependencies'].keys())
