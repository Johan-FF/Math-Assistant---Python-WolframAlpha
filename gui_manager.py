import requests
from PIL import Image
from PIL import ImageQt
from io import BytesIO
from PyQt5 import QtCore, QtGui, QtWidgets

button_style = """
    QPushButton {
        color: #212A3E;
        background-color: #F1F6F9;
        border: none;
        border-radius: 10px;
    }
    
    QPushButton:hover {
        background-color: #212A3E;
        color: #F1F6F9;
    }
"""

panel_style = """
    QWidwet{
        background-color: #394867;
        border-radius: 10px;
    }
"""

class GUIManager:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle("Math Assistant")
        
    # Setup GUI
        
    def setup_ui(self):
        self.window.setStyleSheet("background-color: #212A3E;")
        
        # Create three main panels
        middle_panel = QtWidgets.QWidget()
        left_panel = QtWidgets.QWidget()
        right_panel = QtWidgets.QWidget()
        
        # Set panel sizes
        middle_panel.setMinimumWidth(400)
        left_panel.setMaximumWidth(250)
        right_panel.setMaximumWidth(250)
        
        # Apply styles to panels
        middle_panel.setStyleSheet(panel_style)
        left_panel.setStyleSheet(panel_style)
        right_panel.setStyleSheet(panel_style)
        
        # Create a horizontal layout for the three panels
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(left_panel)
        layout.addWidget(middle_panel)
        layout.addWidget(right_panel)
        
        # Create a main widget to contain the layout
        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(layout)
        
        # Set the main widget as the center content of the window
        self.window.setCentralWidget(main_widget)
        self.setup_left_panel()
        self.setup_right_panel()
        self.setup_middle_panel()
        
    def setup_left_panel(self):
        left_panel = self.window.centralWidget().layout().itemAt(0).widget()
        
        # Create a vertical layout for the left panel
        layout = QtWidgets.QVBoxLayout(left_panel)
        
        # Create a QLabel to display text
        label = QtWidgets.QLabel("Enter a Problem", alignment=QtCore.Qt.AlignCenter)
        font = label.font()
        font.setBold(True)
        font.setFamily("Helvetica [Cronyx]")
        font.setPointSize(16)
        label.setFont(font)
        label.setMaximumHeight(30)
        label.setStyleSheet("color:  #F1F6F9;")
        
        # Create a QLineEdit for the text input
        line_edit = QtWidgets.QLineEdit()
        line_edit.setStyleSheet("color:  #212A3E; background-color: #9BA4B5; border-radius: 10px; padding: 10px; border: 2px solid #F1F6F9;")
        font = line_edit.font()
        font.setPointSize(16)
        line_edit.setFont(font)
        
        # Create a panel for recent posts
        limitis_panel = QtWidgets.QWidget()
        limitis_panel.setStyleSheet("background-color: #9BA4B5; border-radius: 10px; padding: 0px")
        limitis_panel.setMaximumHeight(50)
        
        # Create a vertical layout for the recent posts panel
        layout_limits_panel = QtWidgets.QHBoxLayout(limitis_panel)
        
        # Create a QLineEdit for the text input
        variable_edit = QtWidgets.QLineEdit()
        variable_edit.setStyleSheet("color:  #212A3E; background-color: #F1F6F9; border-radius: 10px; padding: 5px;")
        font = variable_edit.font()
        font.setPointSize(16)
        variable_edit.setFont(font)
        variable_edit.setMaximumWidth(40)
        
        label_limit_inf = QtWidgets.QLabel("Inf: ", alignment=QtCore.Qt.AlignLeft)
        font = label_limit_inf.font()
        font.setBold(True)
        font.setFamily("Helvetica [Cronyx]")
        font.setPointSize(16)
        label_limit_inf.setFont(font)
        label_limit_inf.setMaximumHeight(30)
        label_limit_inf.setMaximumWidth(40)
        label_limit_inf.setStyleSheet("color:  #F1F6F9;")
        
        # Create a QLineEdit for the text input
        inf_limit_edit = QtWidgets.QLineEdit()
        inf_limit_edit.setStyleSheet("color:  #212A3E; background-color: #F1F6F9; border-radius: 10px; padding: 5px;")
        font = inf_limit_edit.font()
        font.setPointSize(16)
        inf_limit_edit.setFont(font)
        inf_limit_edit.setMaximumWidth(40)
        
        label_limit_sup = QtWidgets.QLabel("Sup: ", alignment=QtCore.Qt.AlignLeft)
        font = label_limit_sup.font()
        font.setBold(True)
        font.setFamily("Helvetica [Cronyx]")
        font.setPointSize(16)
        label_limit_sup.setFont(font)
        label_limit_sup.setMaximumHeight(30)
        label_limit_sup.setMaximumWidth(40)
        label_limit_sup.setStyleSheet("color:  #F1F6F9;")
        
        # Create a QLineEdit for the text input
        sup_limit_edit = QtWidgets.QLineEdit()
        sup_limit_edit.setStyleSheet("color:  #212A3E; background-color: #F1F6F9; border-radius: 10px; padding: 5px;")
        font = sup_limit_edit.font()
        font.setPointSize(16)
        sup_limit_edit.setFont(font)
        sup_limit_edit.setMaximumWidth(40)
        
        layout_limits_panel.addWidget(variable_edit)
        layout_limits_panel.addWidget(label_limit_inf)
        layout_limits_panel.addWidget(inf_limit_edit)
        layout_limits_panel.addWidget(label_limit_sup)
        layout_limits_panel.addWidget(sup_limit_edit)
        
        # Create a panel for recent posts
        recent_search_panel = QtWidgets.QWidget()
        recent_search_panel.setStyleSheet("background-color: #9BA4B5; border-radius: 10px;")
        recent_search_panel.setMaximumHeight(400)
        
        # Create a vertical layout for the recent posts panel
        layout_recent_search = QtWidgets.QVBoxLayout(recent_search_panel)
        
        # Create a QLineEdit for the text input
        line_edit_2 = QtWidgets.QLineEdit()
        line_edit_2.setStyleSheet("color:  #212A3E; background-color: #9BA4B5; border-radius: 10px; padding: 10px; border: 2px solid #F1F6F9;")
        font = line_edit_2.font()
        font.setPointSize(16)
        line_edit_2.setFont(font)
        
        # Create two QPushButton
        solution_button_2 = QtWidgets.QPushButton("INTEGRAL")
        font = solution_button_2.font()
        font.setPointSize(16)
        solution_button_2.setFont(font)
        solution_button_2.setStyleSheet(button_style)
        
        # Create two QPushButton
        solution_button = QtWidgets.QPushButton("REVOLUTION")
        font = solution_button.font()
        font.setPointSize(16)
        solution_button.setFont(font)
        solution_button.setStyleSheet(button_style)
        
        procedura_button = QtWidgets.QPushButton("PROCEDURE")
        font = procedura_button.font()
        font.setPointSize(16)
        procedura_button.setFont(font)
        procedura_button.setStyleSheet(button_style)
        
        # Add the widgets to the vertical layout
        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(limitis_panel)
        layout.addWidget(recent_search_panel)
        layout.addWidget(line_edit_2)
        layout.addWidget(solution_button_2)
        layout.addWidget(solution_button)
        layout.addWidget(procedura_button)
        
    def setup_right_panel(self):
        right_panel = self.window.centralWidget().layout().itemAt(2).widget()
        
        # Create a vertical layout for the right panel
        layout = QtWidgets.QVBoxLayout(right_panel)
        
        # Create a QLabel to display text
        label = QtWidgets.QLabel("Enter a Question", alignment=QtCore.Qt.AlignCenter)
        font = label.font()
        font.setBold(True)
        font.setFamily("Helvetica [Cronyx]")
        font.setPointSize(16)
        label.setFont(font)
        label.setMaximumHeight(30)
        label.setStyleSheet("color:  #F1F6F9;")
        
        # Create a QLineEdit for the text input
        line_edit = QtWidgets.QLineEdit()
        line_edit.setStyleSheet("color:  #212A3E; background-color: #9BA4B5; border-radius: 10px; padding: 10px; border: 2px solid #F1F6F9;")
        font = line_edit.font()
        font.setPointSize(16)
        line_edit.setFont(font)
        
        # Create a panel for chat history
        history_panel = QtWidgets.QWidget()
        history_panel.setStyleSheet("background-color: #9BA4B5; border-radius: 10px;")
        history_panel.setMaximumHeight(450)
        
        # Create a vertical layout for the history panel
        layout_history_panel = QtWidgets.QVBoxLayout(history_panel)
        
        # Create a QPushButton
        answer_button = QtWidgets.QPushButton("ANSWER")
        font = answer_button.font()
        font.setPointSize(16)
        answer_button.setFont(font)
        answer_button.setStyleSheet(button_style)
        
        # Add the widgets to the vertical layout
        layout.addWidget(label)
        layout.addWidget(history_panel)
        layout.addWidget(line_edit)
        layout.addWidget(answer_button)
        
    def setup_middle_panel(self):
        middle_panel = self.window.centralWidget().layout().itemAt(1).widget()
        
        # Create a vertical layout for the center panel
        layout = QtWidgets.QVBoxLayout(middle_panel)
        
        # Create a QScrollArea for responses
        scroll_area = QtWidgets.QScrollArea()
        
        # Create the widget contained within the QScrollArea
        top_panel = QtWidgets.QWidget()
        top_panel.setMinimumWidth(500)
        top_panel.setMinimumHeight(2000)
        top_panel.setStyleSheet("background-color: #9BA4B5; border-radius: 10px;")
        layout_panel = QtWidgets.QVBoxLayout(top_panel)
        
        # Add the panel to the QScrollArea
        scroll_area.setWidget(top_panel)
        scroll_area.setWidgetResizable(True)
        scroll_area.setMinimumHeight(300)
        layout_scroll = QtWidgets.QVBoxLayout(scroll_area)
        
        
        # Create a QScrollArea for responses
        scroll_area_2 = QtWidgets.QScrollArea()
        
        # Create the widget contained within the QScrollArea
        panel_below = QtWidgets.QWidget()
        panel_below.setMinimumWidth(500)
        panel_below.setMinimumHeight(1000)
        panel_below.setStyleSheet("background-color: #9BA4B5; border-radius: 10px;")
        layout_panel = QtWidgets.QVBoxLayout(panel_below)
        
        # Add the panel to the QScrollArea
        scroll_area_2.setWidget(panel_below)
        scroll_area_2.setWidgetResizable(True)
        scroll_area_2.setMinimumHeight(300)
        layout_scroll = QtWidgets.QVBoxLayout(scroll_area_2)
        
        # Add the QScrollArea to the main layout
        layout.addWidget(scroll_area)
        layout.addWidget(scroll_area_2)
        
    def set_buttons_functions(self, func_solution, func_procedure, func_conversation):
        # User input - Problem
        problem_input = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(1).widget()
        problem_input_2 = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(4).widget()
        eje = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(2).widget().layout().itemAt(0).widget()
        inf = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(2).widget().layout().itemAt(2).widget()
        sup = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(2).widget().layout().itemAt(4).widget()
        
        # User input - Aks
        conversation_input = self.window.centralWidget().layout().itemAt(2).widget().layout().itemAt(2).widget() 
        
        integral_buton = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(5).widget()
        integral_buton.clicked.connect(lambda: func_procedure(problem_input_2.text(), True, False, inf.text(), sup.text(), eje.text()))
        
        revolution_botton = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(6).widget()
        revolution_botton.clicked.connect(lambda: func_solution(problem_input.text(), inf.text(), sup.text(), eje.text(), False))
        
        procedure_button = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(7).widget()
        procedure_button.clicked.connect(lambda: func_procedure(problem_input.text(), False, False, inf.text(), sup.text(), eje.text()))
        
        answer_button = self.window.centralWidget().layout().itemAt(2).widget().layout().itemAt(3).widget()
        answer_button.clicked.connect(lambda: func_conversation(conversation_input, ''))
        
    # Functionalities Simple Solution
        
    def set_consultation(self, consultation):
        # Update the content of the problem input
        problem_input = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(1).widget()
        problem_input.setText(consultation)
        
    def set_image_in_solution(self, data, func_solution):
        # Search panel
        top_panel = self.window.centralWidget().layout().itemAt(1).widget().layout().itemAt(0).widget().widget()
        layout = top_panel.layout()
        # Delete previous children to create new ones
        self.delete_panel_childs(top_panel)
        # Loads the response from the server as images and creates them as widgets
        imagen = Image.open(BytesIO(data))
        qimage = ImageQt.ImageQt(imagen)
        qpixmap = QtGui.QPixmap.fromImage(qimage)
        label_imagen = QtWidgets.QLabel()
        label_imagen.setPixmap(qpixmap)
        # Udate recent search
        self.add_entry_button(func_solution, False)
        # Add img
        layout.addWidget(label_imagen)
        
    def delete_panel_childs(self, panel):
        # Delete previous children
        children = panel.findChildren(QtWidgets.QWidget)
        if children:
            for child_widget in children:
                child_widget.deleteLater()
        
    def add_entry_button(self, func_solution, is_simple_integral):
        # User input
        problem_input = None
        new_consultation = None
        if not is_simple_integral:
            problem_input = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(1).widget()
            new_consultation = problem_input.text()
        else:
            problem_input = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(4).widget()
            new_consultation = problem_input.text()
        # Panel to inputs
        recent_search_panel = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(3).widget()
        # It is verified that the searched content is not in the history
        exists = False
        for button in recent_search_panel.findChildren(QtWidgets.QPushButton):
            if button.text() == new_consultation:
                exists = True
        if exists:
            return
        details_integral = self.get_details_integral()
        # Layout to add new button
        layout = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(3).widget().layout()
        # Create new consultation button
        new_consultation_button = QtWidgets.QPushButton(new_consultation)
        font = new_consultation_button.font()
        font.setPointSize(14)
        new_consultation_button.setFont(font)
        new_consultation_button.setStyleSheet(button_style)
        new_consultation_button.clicked.connect(lambda: func_solution(new_consultation, details_integral[0], details_integral[1], details_integral[2], is_simple_integral))
        # Add button
        layout.addWidget(new_consultation_button)
        
    # Functionalities Query Solution
        
    def set_procedure_in_solution(self, data, func_solution, is_simple_integral):
        # Find and leave empty the solution panel
        top_panel = self.window.centralWidget().layout().itemAt(1).widget().layout().itemAt(0).widget().widget()
        layout = top_panel.layout()
        self.delete_panel_childs(top_panel)
        # Add query to recent posts
        self.add_entry_button(func_solution, is_simple_integral)
        # Data contains a list of objects with title and image
        for item in data:
            title = item['title']
            image_urls = item['imgs']
            label_title = QtWidgets.QLabel(title)
            font = label_title.font()
            font.setBold(True)
            font.setFamily("Helvetica [Cronyx]")
            font.setPointSize(14)
            label_title.setFont(font)
            label_title.setMaximumHeight(20)
            label_title.setStyleSheet("color:  #212A3E;")
            layout.addWidget(label_title)
            for image_url in image_urls:
                response = requests.get(image_url)
                image_data = response.content
                qimage = QtGui.QImage.fromData(image_data)
                qpixmap = QtGui.QPixmap.fromImage(qimage)
                label_image = QtWidgets.QLabel()
                label_image.setPixmap(qpixmap)
                layout.addWidget(label_image)
        
    def set_procedure_in_problem(self, data):
        # Find and leave empty the solution panel
        panel_below = self.window.centralWidget().layout().itemAt(1).widget().layout().itemAt(1).widget().widget()
        layout = panel_below.layout()
        self.delete_panel_childs(panel_below)
        # Data contains a list of objects with title and image
        for item in data:
            title = item['title']
            image_urls = item['imgs']
            label_title = QtWidgets.QLabel(title)
            font = label_title.font()
            font.setBold(True)
            font.setFamily("Helvetica [Cronyx]")
            font.setPointSize(14)
            label_title.setFont(font)
            label_title.setMaximumHeight(20)
            label_title.setStyleSheet("color:  #212A3E;")
            layout.addWidget(label_title)
            for image_url in image_urls:
                response = requests.get(image_url)
                image_data = response.content
                qimage = QtGui.QImage.fromData(image_data)
                qpixmap = QtGui.QPixmap.fromImage(qimage)
                label_image = QtWidgets.QLabel()
                label_image.setPixmap(qpixmap)
                layout.addWidget(label_image)
        
    def get_details_integral(self):
        eje = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(2).widget().layout().itemAt(0).widget()
        inf = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(2).widget().layout().itemAt(2).widget()
        sup = self.window.centralWidget().layout().itemAt(0).widget().layout().itemAt(2).widget().layout().itemAt(4).widget()
        return [inf.text(), sup.text(), eje.text()]
        
    # Functionalities Conversational Solution
        
    def add_user_conversation(self, message_user, func_conversation):
        layout = self.window.centralWidget().layout().itemAt(2).widget().layout().itemAt(1).widget().layout()
        panel_history = self.window.centralWidget().layout().itemAt(2).widget().layout().itemAt(1).widget()
        
        # It is verified that the searched content is not in the history
        exists = False
        for button in panel_history.findChildren(QtWidgets.QPushButton):
            if button.text() == message_user:
                exists = True
        if exists:
            return
        
        button = QtWidgets.QPushButton(message_user)
        font = button.font()
        font.setPointSize(12)
        button.setFont(font)
        button.setStyleSheet(button_style)
        
        layout.addWidget(button)
        button.clicked.connect(lambda: func_conversation(None, message_user))
        
    def add_ai_conversation(self, message_ai):
        layout = self.window.centralWidget().layout().itemAt(2).widget().layout().itemAt(1).widget().layout()
        panel_history = self.window.centralWidget().layout().itemAt(2).widget().layout().itemAt(1).widget()
        
        # It is verified that the searched content is not in the history
        exists = False
        for label in panel_history.findChildren(QtWidgets.QLabel):
            if label.text() == message_ai:
                exists = True
        if exists:
            return
        
        
        label = QtWidgets.QLabel(message_ai, alignment=QtCore.Qt.AlignLeft)
        font = label.font()
        font.setFamily("Helvetica [Cronyx]")
        font.setPointSize(12)
        label.setFont(font)
        label.setStyleSheet("color:  #212A3E; border-radius: 10px; background-color: #F1F6F9; padding: 5px;")
        label.setWordWrap(True)
        
        layout.addWidget(label)
        
    # Run app
        
    def show(self):
        self.window.resize(900, 600) 
        self.window.show()
        self.app.exec_()
