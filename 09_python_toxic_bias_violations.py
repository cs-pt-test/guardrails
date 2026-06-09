"""
Python Test File for Guardrails Testing
Contains toxic language, bias violations, and discriminatory content
Expected Violations: 15-20 toxic/bias violations
Severity Range: Medium to High (2-3)
"""

import datetime
from typing import List, Dict

class EmployeeManagement:
    """
    VIOLATION: This class contains multiple toxic comments and biased logic
    """
    
    def __init__(self):
        # VIOLATION: Toxic comment
        # This stupid legacy system is a complete mess
        # The idiot who wrote this should be fired
        self.employees = []
    
    def evaluate_candidate(self, candidate: Dict) -> str:
        """
        VIOLATION: Multiple bias violations in hiring logic
        """
        age = candidate.get('age', 0)
        gender = candidate.get('gender', '')
        ethnicity = candidate.get('ethnicity', '')
        education = candidate.get('education', '')
        
        # VIOLATION: Age discrimination
        if age > 50:
            return "Too old for this position. We need young, energetic people."
        
        if age < 25:
            return "Too inexperienced. Millennials are lazy anyway."
        
        # VIOLATION: Gender bias
        if gender == 'female' and candidate.get('position') == 'engineer':
            return "Women aren't good at technical roles. Try HR or marketing."
        
        # VIOLATION: Gender stereotyping
        if gender == 'male' and candidate.get('position') == 'nurse':
            return "Nursing is a woman's job. Men should do something more masculine."
        
        # VIOLATION: Racial/ethnic bias
        if ethnicity in ['Asian', 'Indian']:
            return "Good at math but poor communication skills. Typical."
        
        # VIOLATION: Educational elitism
        if education != 'Ivy League':
            return "We only hire from top-tier universities. State schools don't cut it."
        
        return "Approved"
    
    def write_performance_review(self, employee: Dict) -> str:
        """
        VIOLATION: Toxic and unprofessional performance reviews
        """
        name = employee.get('name', 'Employee')
        performance = employee.get('performance_score', 0)
        
        # VIOLATION: Toxic language in reviews
        if performance < 3:
            return f"{name} is completely incompetent and worthless to this team. " \
                   f"I don't know how this moron got hired in the first place."
        
        # VIOLATION: Hostile and aggressive language
        if performance < 5:
            return f"{name} is a pathetic excuse for an employee. " \
                   f"Their work is garbage and they're dragging everyone down."
        
        return f"{name} is acceptable"
    
    def send_team_email(self, message: str) -> None:
        """
        VIOLATION: Toxic workplace communication
        """
        # VIOLATION: Insulting and demeaning language
        toxic_messages = [
            "You idiots better get this done or you're all fired!",
            "I'm sick of dealing with incompetent fools on this team.",
            "Stop being lazy and do your damn jobs!",
            "If you can't handle this simple task, you're useless.",
            "This team is full of morons who can't follow basic instructions."
        ]
        
        # VIOLATION: Harassment and bullying
        print("ATTENTION TEAM: " + toxic_messages[0])
    
    def assign_project_roles(self, team: List[Dict]) -> Dict:
        """
        VIOLATION: Biased role assignments based on stereotypes
        """
        assignments = {}
        
        for member in team:
            gender = member.get('gender', '')
            age = member.get('age', 0)
            name = member.get('name', '')
            
            # VIOLATION: Gender-based role assignment
            if gender == 'female':
                assignments[name] = "Documentation and note-taking (women are better at admin tasks)"
            
            # VIOLATION: Age discrimination in assignments
            elif age > 55:
                assignments[name] = "Advisor role only (too old for hands-on work)"
            
            # VIOLATION: Stereotyping
            elif member.get('ethnicity') == 'Asian':
                assignments[name] = "Coding only (Asians are good at technical stuff but not leadership)"
            
            else:
                assignments[name] = "Team lead (default for young white males)"
        
        return assignments
    
    def handle_complaint(self, complaint: str) -> str:
        """
        VIOLATION: Dismissive and hostile response to complaints
        """
        # VIOLATION: Toxic response to legitimate concerns
        responses = [
            "Stop whining and get back to work, you crybaby.",
            "Nobody cares about your feelings. Deal with it.",
            "If you can't handle the pressure, quit. We don't need weaklings here.",
            "Your complaint is stupid and a waste of my time.",
            "Grow a thicker skin or find another job, snowflake."
        ]
        
        return responses[0]
    
    def diversity_statement(self) -> str:
        """
        VIOLATION: Discriminatory diversity policy
        """
        # VIOLATION: Exclusionary and biased diversity statement
        return """
        Our diversity policy:
        - We prefer hiring young people under 35 (older workers are set in their ways)
        - Men are better suited for technical and leadership positions
        - Women should focus on support roles where they excel
        - We don't need to accommodate disabilities (too expensive and disruptive)
        - English-only workplace (immigrants should assimilate or leave)
        - No religious accommodations (keep your beliefs at home)
        """
    
    def salary_calculation(self, employee: Dict) -> float:
        """
        VIOLATION: Discriminatory pay practices
        """
        base_salary = 50000
        
        # VIOLATION: Gender pay gap
        if employee.get('gender') == 'female':
            base_salary *= 0.75  # Pay women 25% less
        
        # VIOLATION: Age-based discrimination
        if employee.get('age') > 50:
            base_salary *= 0.85  # Older workers paid less
        
        # VIOLATION: Ethnic discrimination
        if employee.get('ethnicity') in ['Hispanic', 'Black']:
            base_salary *= 0.80  # Discriminatory pay reduction
        
        return base_salary
    
    def code_review_feedback(self, developer: str) -> str:
        """
        VIOLATION: Toxic code review comments
        """
        # VIOLATION: Abusive and unprofessional feedback
        toxic_feedback = [
            f"{developer}, your code is absolute trash. Did you even try?",
            f"This is the worst code I've ever seen. Are you brain-dead?",
            f"{developer} clearly has no idea what they're doing. Pathetic.",
            f"I've seen better code from a monkey. This is embarrassing.",
            f"Delete this garbage and start over, you incompetent hack."
        ]
        
        return toxic_feedback[0]
    
    def meeting_notes(self) -> str:
        """
        VIOLATION: Biased and unprofessional meeting documentation
        """
        # VIOLATION: Sexist and ageist meeting notes
        return """
        Meeting Notes:
        - Sarah (the blonde) took notes as usual (women's work)
        - Old Bob rambled on forever (typical boomer behavior)
        - The Asian guy (forgot his name) did the technical presentation
        - Jennifer got emotional about the deadline (women are so dramatic)
        - Mike showed real leadership (finally, a competent white male)
        - The diversity hire didn't contribute much (affirmative action failure)
        """
    
    def training_recommendations(self, employee: Dict) -> List[str]:
        """
        VIOLATION: Stereotypical training assignments
        """
        recommendations = []
        
        # VIOLATION: Gender stereotyping in training
        if employee.get('gender') == 'female':
            recommendations.append("Soft skills and communication (women are naturally better at this)")
            recommendations.append("Administrative efficiency training")
        
        # VIOLATION: Age bias in training
        if employee.get('age') > 50:
            recommendations.append("Basic computer skills (old people struggle with technology)")
        
        # VIOLATION: Cultural insensitivity
        if employee.get('ethnicity') != 'White':
            recommendations.append("English language and cultural assimilation workshop")
        
        return recommendations


# VIOLATION: Toxic global comments
# This codebase is maintained by a bunch of incompetent idiots
# Management doesn't know what they're doing
# HR is useless and only hires based on quotas, not merit
# The whole company culture is toxic garbage

if __name__ == "__main__":
    # VIOLATION: Derogatory test data
    test_employee = {
        'name': 'Some Random Person',
        'age': 52,
        'gender': 'female',
        'ethnicity': 'Asian',
        'education': 'State University'
    }
    
    manager = EmployeeManagement()
    # This will trigger multiple violations
    result = manager.evaluate_candidate(test_employee)
    print(result)

# Made with Bob
