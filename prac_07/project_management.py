"""
Estimate: 60 minutes
Actual:   70 minutes
"""
import datetime
from prac_07.project import Project


def main():
    print("Welcome to Pythonic Project Management")
    initial_file = 'project_management.txt'
    projects = load_projects(initial_file)
    print(f"Loaded {len(projects)} projects from {initial_file}")

    menu = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
            "- (F)ilter projects by date)\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")

    print(menu)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'L':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 'S':
            filename = input("Enter filename to save: ")
            save_projects(projects, filename)
            print("Projects saved")
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects(projects)
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            update_project(projects)
        else:
            print("Invalid choice.")

        print(menu)
        choice = input(">>> ").upper()

    print("Would you like to save to projects.txt? no, I think not.")
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            file.readline()  # Skip header
            for line in file:
                parts = line.strip().split('\t')
                name = parts[0]
                start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                priority = int(parts[2])
                estimate = float(parts[3])
                completion_percentage = int(parts[4])
                projects.append(Project(name, start_date, priority, estimate, completion_percentage))
    except FileNotFoundError:
        print("File not found.")
    return projects


def save_projects(projects, filename):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(" ", project)

    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(" ", project)


def filter_projects(projects):
    try:
        date_string = input("Show projects that start after date (dd/mm/yyyy): ")
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        for project in sorted(projects, key=lambda x: x.start_date):
            if project.start_date >= filter_date:
                print(project)
    except ValueError:
        print("Invalid date format.")


def add_project(projects):
    name = input("Let's add a new project\nName: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, estimate, completion_percentage))


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)

    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)


main()
