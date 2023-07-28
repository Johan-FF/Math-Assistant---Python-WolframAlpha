from gui_manager import GUIManager
from wolfram_alpha_service import WolframAlphaService 

if __name__ == "__main__":
    gui = GUIManager()
    ai = WolframAlphaService(gui)
    
    gui.setup_ui()
    gui.set_buttons_functions(
        ai.get_simple_response,
        ai.get_query_response,
        ai.get_conversation_response
    )
    
    gui.show()