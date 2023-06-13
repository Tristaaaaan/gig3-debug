from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextFieldRect
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout

Builder_string = '''
#:import MDFloatLayout kivymd.uix.floatlayout.MDFloatLayout
#:import MDBoxLayout kivymd.uix.boxlayout.MDBoxLayout
#:import MDRaisedButton kivymd.uix.button.MDRaisedButton
#:import MDRectangleFlatButton kivymd.uix.button.MDRectangleFlatButton
#:import MDDataTable kivymd.uix.datatables.MDDataTable
#:import MDTopAppBar kivymd.uix.toolbar
#:import dp kivy.metrics.dp
#:import SlideTransition kivy.uix.screenmanager.SlideTransition

<RootWidget>:
    ExamScreen:
        name: "assessments"
    AttendanceScreen:
        name: "performance"
    ReportsScreen:
        name: "reports"
    SummaryScreen:
        name: "results"

<ExamScreen>:
    name: "assessments"
    MDScreen:
        ScrollView:
            bar_width:0
            MDBoxLayout:
                orientation:'vertical'
                adaptive_height:True
    MDTopAppBar:
        title: "Exam Results"
        pos_hint: {"top": 1}
        md_bg_color: 'darkgreen'
        elevation: 0

    MDLabel:
        text:'MIDTERM EXAM'
        font_style:"H5"
        bold: True
        halign: 'center'
        pos_hint:{'center_y': 0.83}
    MDLabel:
        text:'FINAL EXAM'
        font_style:"H5"
        bold: True
        halign: 'center'
        pos_hint:{'center_y': 0.47}

    MDRectangleFlatButton:
        text: "Save"
        md_bg_color: 'green'
        text_color: "white"
        font_size: "17sp"
        pos_hint:{'center_x': 0.36, 'center_y': 0.09}
        elevation: 2
        size_hint: (0.145, 0.06)
        on_release: app.show_alert_dialog1()
    MDRectangleFlatButton:
        text: "Next"
        md_bg_color: 'green'
        text_color: "white"
        font_size: "17sp"
        pos_hint:{'center_x': 0.66, 'center_y': 0.09}
        elevation: 2
        size_hint: (0.145, 0.06)
        on_press: app.callback1()

    MDTextField:
        id: midterm_written
        hint_text: "Mid Written"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.3, 'center_y': 0.73}
        size_hint_x:None
        width:141

    MDTextField:
        id: midterm_practical
        hint_text: "Mid Practical"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.3, 'center_y': 0.58}
        size_hint_x:None
        width:141
    MDTextField:
        id: final_written
        hint_text: "Final Written"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.3, 'center_y': 0.37}
        size_hint_x:None
        width:141
    MDTextField:
        id: final_practical
        hint_text: "Final Practical"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.3, 'center_y': 0.22}
        size_hint_x:None
        width:141
    MDTextField:
        id: midterm_written_multiplier
        hint_text: "Multiplier"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'int'
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.74}
        size_hint_x:0.32
        size_hint_y:0.1
        size_hint_x:None
        width:110
    MDTextField:
        id: midterm_practical_multiplier
        hint_text: "Multiplier"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'int'
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.59}
        size_hint_x:0.32
        size_hint_y:0.1
        size_hint_x:None
        width:110
    MDTextField:
        id: final_written_multiplier
        hint_text: "Multiplier"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'int'
        max_text_length: 3
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.38}
        size_hint_x:0.32
        size_hint_y:0.1
        size_hint_x:None
        width:110
    MDTextField:
        id: final_practical_multiplier
        hint_text: "Multiplier"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'int'
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.23}
        size_hint_x:0.32
        size_hint_y:0.1
        size_hint_x:None
        width:110

<AttendanceScreen>
    name: "performance"
    MDScreen:
        ScrollView:
            bar_width:0
            MDBoxLayout:
                orientation:'vertical'
                padding:'20dp'
                adaptive_height:True
    MDTopAppBar:
        title: "Class Performance"
        pos_hint: {"top": 1}
        left_action_items: [["keyboard-return", lambda x: app.callback4()]]
        md_bg_color: 'darkgreen'
        elevation: 0
        on_action_button: app.callback4()


    MDRectangleFlatButton:
        text: "Save"
        md_bg_color: 'green'
        text_color: "white"
        font_size: "17sp"
        pos_hint:{'center_x': 0.36, 'center_y': 0.09}
        elevation: 2
        size_hint: (0.145, 0.06)
        on_release: app.show_alert_dialog2()
    MDRectangleFlatButton:
        text: "Next"
        md_bg_color: 'green'
        text_color: "white"
        font_size: "17sp"
        pos_hint:{'center_x': 0.66, 'center_y': 0.09}
        elevation: 2
        size_hint: (0.145, 0.06)
        on_press: app.callback2()

    MDLabel:
        text:"    ATTENDANCE"
        font_style:"H5"
        bold: True
        pos_hint:{'center_y': 0.82}
    MDTextField:
        id: attendance_multiplier
        hint_text: "Multiplier"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'int'
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.765, 'center_y': 0.83}
        size_hint_x:0.32
        size_hint_y:0.1
        width:110

    MDTextField:
        id: late
        hint_text: "Days Late"
        helper_text_mode: "persistent"
        required: True
        input_filter: 'int'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.275, 'center_y': 0.72}
        size_hint: 0.35, 0.1
        width:141
    MDTextField:
        id: absent
        hint_text: "Days Absent"
        helper_text_mode: "persistent"
        required: True
        input_filter: 'int'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.725, 'center_y': 0.72}
        size_hint_x:None
        size_hint: 0.35, 0.1
        width:141
    MDTextField:
        id: days
        hint_text: "Total Meetings"
        helper_text_mode: "persistent"
        required: True
        input_filter: 'int'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.64}
        size_hint_x:None
        size_hint: 0.40, 0.1
        width:141

    MDLabel:
        text: "    PARTICIPATION"
        font_style:"H5"
        bold: True
        pos_hint:{'center_y': 0.525}
    MDTextField:
        id: participation_multiplier
        hint_text: "Multiplier"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'int'
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.765, 'center_y': 0.53}
        size_hint_x:0.32
        size_hint_y:0.1
        width:110

    MDTextField:
        id: professor
        hint_text: "Student to Professor"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.42}
        size_hint: 0.5, 0.1
        width:141

    MDTextField:
        id: student
        hint_text: "Student to Students"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.32}
        size_hint: 0.5, 0.1
        width:141
    MDTextField:
        id: materials
        hint_text: "Student to Materials"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.22}
        size_hint: 0.5, 0.1
        width:141

<ReportsScreen>
    name: "reports"
    MDScreen:
        ScrollView:
            bar_width:0
            MDBoxLayout:
                orientation:'vertical'
                padding:'20dp'
                adaptive_height:True
    MDTopAppBar:
        title: "Laboratory Reports"
        pos_hint: {"top": 1}
        left_action_items: [["keyboard-return", lambda x: app.callback1()]]
        md_bg_color: 'darkgreen'
        elevation: 0
        on_action_button: app.callback1()
        

    MDLabel:
        text:'       PROJECT'
        font_style:"H5"
        bold: True
        pos_hint:{'center_y': 0.82}
    MDTextField:
        id: project_multiplier
        hint_text: "Multiplier"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'int'
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.7, 'center_y': 0.83}
        size_hint_x:0.32
        size_hint_y:0.1
        width:110

    MDLabel:
        text: "       EXERCISES"
        font_style:"H5"
        bold: True
        pos_hint:{'center_y': 0.61}
    MDTextField:
        id: exercises_multiplier
        hint_text: "Multiplier"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'int'
        mode: "rectangle"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.7, 'center_y': 0.615}
        size_hint_x:0.32
        size_hint_y:0.1
        width:110

    MDRectangleFlatButton:
        text: "Save"
        md_bg_color: 'green'
        text_color: "white"
        font_size: "17sp"
        pos_hint:{'center_x': 0.36, 'center_y': 0.09}
        elevation: 2
        size_hint: (0.145, 0.06)
        on_release: app.show_alert_dialog3()
    MDRectangleFlatButton:
        text: "Compute"
        md_bg_color: 'green'
        text_color: "white"
        font_size: "17sp"
        pos_hint:{'center_x': 0.66, 'center_y': 0.09}
        elevation: 2
        size_hint: (0.145, 0.06)
        on_press: app.callback3()

    MDTextField:
        id: capsule
        hint_text: "Capsule"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.2, 'center_y': 0.72}
        size_hint_x:None
        size_hint: 0.27, 0.1
        width:141
    MDTextField:
        id: proposal
        hint_text: "Proposal"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.72}
        size_hint_x:None
        size_hint: 0.27, 0.1
        width:141
    MDTextField:
        id: final
        hint_text: "Final"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.8, 'center_y': 0.72}
        size_hint_x:None
        size_hint: 0.27, 0.1
        width:141

    MDTextField:
        id: ex1
        hint_text: "Lab ex1 (Lab ex13)"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.265, 'center_y': 0.515}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110

    MDTextField:
        id: ex3
        hint_text: "Lab ex3"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        max_text_length: 3
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.265, 'center_y': 0.45}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110
    MDTextField:
        id: ex5
        hint_text: "Lab ex5"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.265, 'center_y': 0.385}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110

    MDTextField:
        id: ex7
        hint_text: "Lab ex7"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.265, 'center_y': 0.32}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110

    MDTextField:
        id: ex9
        hint_text: "Lab ex9"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        max_text_length: 3
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.265, 'center_y': 0.255}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110
    MDTextField:
        id: ex11
        hint_text: "Lab ex11"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.265, 'center_y': 0.19}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110

    MDTextField:
        id: ex2
        hint_text: "Lab ex2"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.515}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110
    MDTextField:
        id: ex4
        hint_text: "Lab ex4"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        max_text_length: 3
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.45}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110
    MDTextField:
        id: ex6
        hint_text: "Lab ex6"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.385}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110

    MDTextField:
        id: ex8
        hint_text: "Lab ex8 (Lab ex14)"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.32}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110
    MDTextField:
        id: ex10
        hint_text: "Lab ex10"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        max_text_length: 3
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.255}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110
    MDTextField:
        id: ex12
        hint_text: "Lab ex12"
        helper_text_mode: "persistent"
        required: True
        icon_right: "percent"
        input_filter: 'float'
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.75, 'center_y': 0.19}
        size_hint: 0.32, 0.1
        font_size: 13.5
        width:110

<SummaryScreen>
    name: "results"
    MDScreen:
        ScrollView:
            bar_width:0
            MDBoxLayout:
                orientation:'vertical'
                padding:'20dp'
                adaptive_height:True
    MDTopAppBar:
        title: "Results"
        pos_hint: {"top": 1}
        left_action_items: [["keyboard-return", lambda x: app.callback2()]]
        md_bg_color: 'darkgreen'
        elevation: 0
        on_action_button: app.callback2()


    MDLabel:
        text:'Grade'
        font_style:"H5"
        bold: True
        font_size: '20sp'
        pos_hint:{'center_x': 0.785, 'center_y': 0.2725}
    MDLabel:
        text:'Transmutation'
        font_style:"H5"
        bold: True
        font_size: '20sp'
        pos_hint:{'center_x': 0.675, 'center_y': 0.19}
    MDRectangleFlatButton:
        text: "Exit"
        md_bg_color: 'green'
        text_color: "white"
        font_size: "17sp"
        pos_hint:{'center_x': 0.66, 'center_y': 0.09}
        elevation: 2
        size_hint: (0.145, 0.06)
        on_press: app.stop()
    MDRectangleFlatButton:
        text: "Home"
        md_bg_color: 'green'
        text_color: "white"
        font_size: "17sp"
        pos_hint:{'center_x': 0.36, 'center_y': 0.09}
        elevation: 2
        size_hint: (0.145, 0.06)
        on_press: app.callback4()

    MDBoxLayout:
        pos_hint: {"center_x": 0.5}
        adaptive_size: True
        padding: "24dp"
        spacing: "24dp"
'''


class ProjectApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.title = "AGTACalc: CPEN21 Grade Calculator"
        Builder.load_string(Builder_string)
        return RootWidget()

    def show_alert_dialog1(self):
        close_button = MDFlatButton(text="Yes",
                                    on_press=self.confirm1)
        more_button = MDFlatButton(text="Cancel",
                                   on_press=self.close_dialog)
        self.dialog = MDDialog(title="        Confirmation",
                               text="Are the provided data final?",
                               size_hint=(0.7, 0.3), elevation=0,
                               buttons=[close_button, more_button])
        self.dialog.open()

    def confirm1(self, obj):
        global MIDTERM, midterm_mult, FINALS, finals_mult
        mw = float(self.root.get_screen(
            'assessments').ids.midterm_written.text)
        mh = float(self.root.get_screen(
            'assessments').ids.midterm_practical.text)
        fw = float(self.root.get_screen('assessments').ids.final_written.text)
        fh = float(self.root.get_screen(
            'assessments').ids.final_practical.text)
        mwm = int(self.root.get_screen(
            'assessments').ids.midterm_written_multiplier.text)
        mhm = int(self.root.get_screen(
            'assessments').ids.midterm_practical_multiplier.text)
        fwm = int(self.root.get_screen(
            'assessments').ids.final_written_multiplier.text)
        fhm = int(self.root.get_screen(
            'assessments').ids.final_practical_multiplier.text)

        midterm_mult = round((mwm + mhm), 2)
        finals_mult = round((fwm + fhm), 2)

        midterm_written = mw * mwm / 100
        midterm_practical = mh * mhm / 100
        final_written = fw * fwm / 100
        final_practical = fh * fhm / 100

        MIDTERM = round((midterm_written + midterm_practical), 2)
        FINALS = round((final_written + final_practical), 2)

        self.dialog.dismiss()

    def callback1(self):
        self.root.current = 'performance'

    def show_alert_dialog2(self):
        close_button = MDFlatButton(text="Yes",
                                    on_press=self.confirm2)
        more_button = MDFlatButton(text="Cancel",
                                   on_press=self.close_dialog)
        self.dialog = MDDialog(title="        Confirmation",
                               text="Are the provided data final?",
                               size_hint=(0.7, 0.3), elevation=0,
                               buttons=[close_button, more_button])
        self.dialog.open()

    def confirm2(self, obj):
        global performance_mult, PERFORMANCE
        late = int(self.root.get_screen('performance').ids.late.text)
        absent = int(self.root.get_screen('performance').ids.absent.text)
        total = int(self.root.get_screen('performance').ids.days.text)
        am = int(self.root.get_screen(
            'performance').ids.attendance_multiplier.text)

        ATTENDANCE = round(am * (total - absent - late / 2) / total, 2)

        professor = float(self.root.get_screen(
            'performance').ids.professor.text)
        student = float(self.root.get_screen('performance').ids.student.text)
        materials = float(self.root.get_screen(
            'performance').ids.materials.text)
        pm = int(self.root.get_screen(
            'performance').ids.participation_multiplier.text)

        PARTICIPATION = round(pm * (professor + student + materials) / 300, 2)

        performance_mult = am + pm
        PERFORMANCE = ATTENDANCE + PARTICIPATION

        self.dialog.dismiss()

    def callback2(self):
        self.root.current = 'reports'

    def show_alert_dialog3(self):
        close_button = MDFlatButton(text="Yes",
                                    on_press=self.confirm3)
        more_button = MDFlatButton(text="Cancel",
                                   on_press=self.close_dialog)
        self.dialog = MDDialog(title="        Confirmation",
                               text="Are the provided data final?",
                               size_hint=(0.7, 0.3), elevation=0,
                               buttons=[close_button, more_button])
        self.dialog.open()

    def confirm3(self, obj):
        global EXERCISES, exercises_mult, PROJECT, project_mult
        ex1 = float(self.root.get_screen('reports').ids.ex1.text)
        ex2 = float(self.root.get_screen('reports').ids.ex2.text)
        ex3 = float(self.root.get_screen('reports').ids.ex3.text)
        ex4 = float(self.root.get_screen('reports').ids.ex4.text)
        ex5 = float(self.root.get_screen('reports').ids.ex5.text)
        ex6 = float(self.root.get_screen('reports').ids.ex6.text)
        ex7 = float(self.root.get_screen('reports').ids.ex7.text)
        ex8 = float(self.root.get_screen('reports').ids.ex8.text)
        ex9 = float(self.root.get_screen('reports').ids.ex9.text)
        ex10 = float(self.root.get_screen('reports').ids.ex10.text)
        ex11 = float(self.root.get_screen('reports').ids.ex11.text)
        ex12 = float(self.root.get_screen('reports').ids.ex12.text)
        exercises_mult = int(self.root.get_screen(
            'reports').ids.exercises_multiplier.text)

        capsule = float(self.root.get_screen('reports').ids.capsule.text)
        proposal = float(self.root.get_screen('reports').ids.proposal.text)
        final = float(self.root.get_screen('reports').ids.final.text)
        project_mult = int(self.root.get_screen(
            'reports').ids.project_multiplier.text)

        exercises_sum = ex1 + ex2 + ex3 + ex4 + ex5 + \
            ex6 + ex7 + ex8 + ex9 + ex10 + ex11 + ex12
        EXERCISES = round(exercises_mult * exercises_sum / 1200, 2)
        PROJECT = round(project_mult * (capsule + proposal + final) / 300, 2)

        self.dialog.dismiss()

    def callback3(self):
        self.root.current = 'results'

    def callback4(self):
        self.root.current = 'assessments'

    def close_dialog(self, obj):
        self.dialog.dismiss()


class RootWidget(ScreenManager):
    pass


class ExamScreen(Screen):
    pass


class AttendanceScreen(Screen):
    pass


class ReportsScreen(Screen):
    pass


class SummaryScreen(Screen):
    def load_screen(self):
        layout = AnchorLayout()
        self.grade = MDTextFieldRect(size_hint=(0.23, 0.06),
                                     pos_hint={"x": 0.625, "y": 0.2425},
                                     font_size=20,
                                     foreground_color=(0.12, 0.58, 0.95, 1))
        self.transmutation = MDTextFieldRect(size_hint=(0.2, 0.06),
                                             pos_hint={"x": 0.625, "y": 0.16},
                                             font_size=20,
                                             foreground_color=(0.12, 0.58, 0.95, 1))

        final_grade = round(
            (MIDTERM + FINALS + PERFORMANCE + PROJECT + EXERCISES), 3)
        self.grade.text = f"  {final_grade}"
        self.add_widget(self.grade)

        if final_grade >= 290 / 3:
            self.transmutation.text = "  1.00"
        elif 290 / 3 > final_grade >= 280 / 3:
            self.transmutation.text = "  1.25"
        elif 280 / 3 > final_grade >= 90:
            self.transmutation.text = "  1.50"
        elif 90 > final_grade >= 260 / 3:
            self.transmutation.text = "  1.75"
        elif 260 / 3 > final_grade >= 250 / 3:
            self.transmutation.text = "  2.00"
        elif 250 / 3 > final_grade >= 80:
            self.transmutation.text = "  2.25"
        elif 80 > final_grade >= 230 / 3:
            self.transmutation.text = "  2.50"
        elif 230 / 3 > final_grade >= 220 / 3:
            self.transmutation.text = "  2.75"
        elif 220 / 3 > final_grade >= 70:
            self.transmutation.text = "  3.00"
        elif 70 > final_grade:
            self.transmutation.text = "  5.00"
        self.add_widget(self.transmutation)
        return layout

    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.61, "center_x": 0.5},
            size_hint=(0.9, 0.536),
            pagination_menu_height='60dp',
            column_data=[
                ("Criteria", dp(27)),
                ("Max %", dp(15)),
                ("Overall %", dp(15)),
            ],
            row_data=[("Midterm Exams", f"{midterm_mult}", f"{MIDTERM}"),
                      ("Final Exams", f"{finals_mult}", f"{FINALS}"),
                      ("Class Performance",
                       f"{performance_mult}", f"{PERFORMANCE}"),
                      ("Project", f"{project_mult}", f"{PROJECT}"),
                      ("Exercises", f"{exercises_mult}", f"{EXERCISES}")]
        )
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_screen()
        self.load_table()


if __name__ == "__main__":
    ProjectApp().run()
