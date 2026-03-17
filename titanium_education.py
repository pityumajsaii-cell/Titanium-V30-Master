import datetime

class ApexAcademy:
    def __init__(self):
        self.courses = {
            "AI-MASTERCLASS": "Hogyan építs AI birodalmat (Titanium módszer)",
            "LEVIATHAN-MARKETING": "Vírusmarketing és automata értékesítés",
            "FINANCE-FREEDOM": "Arbitrázs és kripto-automatizáció"
        }
        self.owner = "Majsai István"

    def enroll_student(self, student_name, course_id):
        if course_id in self.courses:
            cert_id = f"CERT-{datetime.datetime.now().strftime('%Y%m%d')}-001"
            print(f"🎓 {student_name} beiratkozott: {self.courses[course_id]}")
            return cert_id
        return None

if __name__ == "__main__":
    ApexAcademy()
    print("✅ Oktatási modul üzemkész.")
