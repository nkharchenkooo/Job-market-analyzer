import csv 

def load_data(filename):
    jobs = []
    
    with open (filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
    
        for row in reader:
            jobs.append(row)
        
    return jobs
    
    
    
def calculate_average_salary(jobs):
    total = 0
    
    for job in jobs:
        total += float(job["Annual Salary (USD)"])
    return round(total/ len(jobs), 2)
    
def find_highest_salary(jobs):
    highest = jobs[0]
    
    for job in jobs:
        if float(job["Annual Salary (USD)"]) > float(highest["Annual Salary (USD)"]):
            highest = job
    return highest
    
def count_job_title (jobs):
    title_count = {}
    
    for job in jobs:
        title = job["Job Title"]
        if title in title_count:
            title_count[title] += 1
        else:
            title_count [title] = 1
    return title_count
    
def search_by_location(jobs, location):
    result = []
    
    for job in jobs:
        if location.lower()in job["Location"].lower():
            result.append(job)
    return result
    
def search_by_level(jobs, level):
    results = []
    
    for job in jobs:
        if level.lower() in job["Level"].lower():
            results.append(job)
    return results
    
def search_by_skills(jobs):
    skill = input("Enter skill: ").strip().lower()
    
    for job in jobs:
        if skill in job["Skills"].lower():
            print(job)
            
def count_by_level(jobs):
    counts = {}
    
    for job in jobs:
        level = job["Level"]
        if level not in counts:
            counts[level] = 1
        else:
            counts[level] +=1
    print(counts)
    
def print_jobs(jobs):
    if len(jobs)==0:
        print("No job found")
    else:
        for job in jobs:
            print("-----------------------")
            print("Title:", job["Job Title"])
            print("Company:" , job["Company"])
            print("Location", job["Location"])
            print("Level:", job["Level"])
            print("Salary:", job["Annual Salary (USD)"])
            print("Skills:", job["Skills"])
    


def main():
    
    filename = "job.csv"
    jobs = load_data(filename)
    
    while True:
        
        print("\n**********Job Market Analyzer**********")
        print("1 . Show total number of jobs")
        print("2. Show average salary")
        print("3. Show highest salary job")
        print("4. Show job title counts")
        print("5. Search job by location")
        print("6. Search job by level")
        print("7. Show all jobs")
        print("8. Search by skills")
        print("9. Count jobs by level")
        print("10. Exit")
        
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            print(f"Total jobs analyzed: {len(jobs)}")
        elif choice == "2":
            average_salary = calculate_average_salary(jobs)
            print(f"Average salary: ${average_salary: .2f}")
            
        elif choice == "3":
            highest = find_highest_salary(jobs)
            print("Highest salary job: ")
            print([highest])
        elif choice == "4":
            title_counts = count_job_title(jobs)
            for title, count in title_counts.items():
                print(f"{title}: {count}")
        elif choice == "5":
            location = input("Enter Location: ")
            results = search_by_location(jobs, location)
            print_jobs(results)
            
        elif choice == "6":
            level = input("Enter level: Entry, Junior, Mid, or Senior: ")
            results = search_by_level(jobs, level)
            print_jobs(results)
        elif choice == "7":
            print_jobs(jobs)
        elif choice== "8":
            search_by_skills(jobs)
        elif choice == "9":
            count_by_level(jobs)
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choise. Please enter a number from 1 to 10")
            
            
main()
        
        
        
        
    
