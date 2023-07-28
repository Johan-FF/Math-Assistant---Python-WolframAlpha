import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class WolframAlphaService:
    def __init__(self, gui_manager):
        self._gui_manager = gui_manager
        self._api_key = os.getenv('API_KEY')
        
        self._simple_api_url = 'http://api.wolframalpha.com/v1/simple'
        self._query_api_url = 'http://api.wolframalpha.com/v2/query'
        self._conversation_api_url = 'http://api.wolframalpha.com/v1/conversation.jsp'
        self._last_conversation_id = ''
        
    def get_simple_response(self, consultation, inf, sup, eje, is_simple_integral):
        self._gui_manager.set_consultation(consultation)
        problem = ''
        if is_simple_integral:
            problem = "Integral of "+consultation
        else: 
            problem = f"spin {consultation}, {eje} = {inf} to {sup}, around the axis {eje}"
        params = {
            "appid": self._api_key,
            "i": problem, # input
            "background": "F1F6F9",
            "fontsize": 16,
            "width": 400
        }
        response = requests.get(self._simple_api_url, params=params)
        if response.status_code == 200:
            data = response.content
            self._gui_manager.set_image_in_solution(data, self.get_simple_response)
        else:
            print("Error: "+str(response.status_code))

    def get_query_response(self, consultation, is_simple_integral, is_question, inf, sup, eje):
        problem = ''
        if not is_question and not is_simple_integral:
            self._gui_manager.set_consultation(consultation)
            problem = f"spin {consultation}, x = {inf} to {sup}, around the axis {eje}"
        elif is_simple_integral:
            problem = "Integral of "+consultation
        else:
            problem = "Resolve "+consultation
        params = {
            "appid": self._api_key,
            "input": problem,
            "podstate": "Result__Step-by-step solution",
            "format": "image",
            "output": "json",
            # "excludepodid": "Result", "BasicInformation:PeopleData", "DecimalApproximation" # se puede repetir varias veces
            # "includepodid": "Result", "BasicInformation:PeopleData", "DecimalApproximation"
        }
        
        response = requests.get(self._query_api_url, params=params)
        # Verificar el código de estado de la respuesta
        if response.status_code == 200:
            data = response.content
            result = self.get_resources(json.loads(data))
            if is_question:
                self._gui_manager.set_procedure_in_problem(result)
            else:
                if is_simple_integral:
                    self._gui_manager.set_procedure_in_solution(result, self.get_simple_response, True)
                else:
                    self._gui_manager.set_procedure_in_solution(result, self.get_simple_response, False)
        else:
            print("Error: "+str(response.status_code))
        
    def get_resources(self, data):
        resources = []
        for pod in data["queryresult"]["pods"]:
            title = pod["title"]
            objeto = {
                "title": title,
                "imgs": []
            }
            for subpod in pod["subpods"]:
                img_src = subpod["img"]["src"]
                objeto['imgs'].append(img_src)
            resources.append(objeto)
        return resources

    def get_conversation_response(self, input_conversation, previus):
        message = ''
        if input_conversation:
            message = input_conversation.text()
        else:
            message = previus
        self._gui_manager.add_user_conversation(message, self.get_conversation_response)
        params = {}
        if(self._conversation_api_url=='http://api.wolframalpha.com/v1/conversation.jsp'):
            params = {
                "appid": self._api_key,
                "i": message
            }
        else:
            params = {
                "appid": self._api_key,
                "conversationid": self._last_conversation_id,
                "i": message,
            }
        response = requests.get(self._conversation_api_url, params=params)
        if response.status_code == 200:
            data = json.loads(response.content)
            self._last_conversation_id = data["conversationID"]
            self._conversation_api_url = 'http://'+data["host"]+'/api/v1/conversation.jsp'
            if input_conversation:
                input_conversation.setText("")
            details_integral = self._gui_manager.get_details_integral()
            self.get_query_response(message, False, True, details_integral[0], details_integral[1], details_integral[2])
            self._gui_manager.add_ai_conversation(data["result"])
        else:
            print("Error: "+str(response.status_code))
