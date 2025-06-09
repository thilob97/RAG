from langchain import hub

class HUBRepository:
    def pull(self):
        prompt = hub.pull("article")

        return prompt
