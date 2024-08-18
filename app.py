import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class CGPACalculator(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # List of courses with course code, name, and credits
        self.courses = [
            ('Communicative English', 'ENG101', 3),
            ('Wave, Optics and Thermodynamics', 'PHY1132', 3),
            ('Introduction to Business', 'BUS1123', 3),
            ('Differential and Integral Calculus', 'MAT1134', 3),
            ('Electricity, Magnetism and Electrical Circuit', 'EEE1135', 3),
            ('Electricity, Magnetism and Electrical Circuit Lab', 'EEE11P6', 0.75),
            ('Computer Fundamentals', 'CSE1127', 2),
            ('Computer Fundamentals Lab', 'CSE11P8', 0.75)
        ]

        # Dictionary to hold grade inputs
        self.grade_inputs = {}

        # Display the courses with input fields for grades
        for course_name, course_code, credit in self.courses:
            course_label = toga.Label(f'{course_code}: {course_name} - Credits: {credit}', style=Pack(padding=(5, 0)))
            grade_input = toga.TextInput(placeholder='Enter grade (e.g., A+)', style=Pack(flex=1, padding=(0, 5)))
            self.grade_inputs[course_code] = grade_input
            
            # Add the label and input to a row
            row = toga.Box(style=Pack(direction=ROW, padding=5))
            row.add(course_label)
            row.add(grade_input)
            main_box.add(row)

        # Button to calculate CGPA
        calculate_button = toga.Button(
            'Calculate CGPA',
            on_press=self.calculate_cgpa,
            style=Pack(padding=10)
        )

        # Display result
        self.result_label = toga.Label('CGPA will be displayed here', style=Pack(padding=10))

        # Add components to main box
        main_box.add(calculate_button)
        main_box.add(self.result_label)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def grade_to_points(self, grade):
        """Converts letter grades to grade points."""
        grade_map = {
            'A+': 4.0,
            'A': 3.75,
            'A-': 3.5,
            'B+': 3.25,
            'B': 3.0,
            'B-': 2.75,
            'C+': 2.5,
            'C': 2.25,
            'D': 2.0,
            'F': 0.0
        }
        return grade_map.get(grade, 0.0)

    def calculate_cgpa(self, widget):
        total_points = 0
        total_credits = 0

        for course_name, course_code, credit in self.courses:
            grade = self.grade_inputs[course_code].value
            if grade:  # Only calculate if grade is entered
                grade_points = self.grade_to_points(grade)
                total_points += grade_points * credit
                total_credits += credit

        if total_credits == 0:
            cgpa = 0.0
        else:
            cgpa = total_points / total_credits

        self.result_label.text = f'Your CGPA is: {cgpa:.2f}'

def main():
    return CGPACalculator()

if __name__ == '__main__':
    main().main_loop()
