import csv

print("IT Job Eligibility Checker Bot")

while True:
    print("\n---Candidate Info---")

    name = input("Name: ")
    skills = input("Skills (Python, JavaScript, SQL): ").lower().split(",")
    skills = [s.strip() for s in skills]

    cgpa = input("CGPA: ")
    experience = input("Experience: ")

    print("\nCompanies:")
    print("1. Netsol")
    print("2. Descon")
    print("3. PepsiCo")

    company = input("Apply for (Netsol/Descon/Pepsico): ").lower()

    try:
        cgpa = float(cgpa)
    except:
        cgpa = 0

    result = ""
    score = 0
    reason = ""

    # Netsol
    if company == "netsol":
        if cgpa >= 3.0:
            score += 50
        else:
            reason += "Low CGPA. "

        if "python" in skills or "javascript" in skills:
            score += 50
        else:
            reason += "Missing Python/JavaScript. "

        if score == 100:
            result = "ELIGIBLE for Netsol"
        else:
            result = "Not Eligible for Netsol"

    # Descon
    elif company == "descon":
        if cgpa >= 2.8:
            score += 50
        else:
            reason += "Low CGPA. "

        if any(skill in skills for skill in ["engineering", "autocad", "civil"]):
            score += 50
        else:
            reason += "Missing engineering skills. "

        if score == 100:
            result = "ELIGIBLE for Descon"
        else:
            result = "Not Eligible for Descon"

    # PepsiCo
    elif company == "pepsico":
        if cgpa >= 2.5:
            score += 50
        else:
            reason += "Low CGPA. "

        if any(skill in skills for skill in ["management", "communication", "excel"]):
            score += 50
        else:
            reason += "Missing business skills. "

        if score == 100:
            result = "ELIGIBLE for PepsiCo"
        else:
            result = "Not Eligible for PepsiCo"

    else:
        result = "Invalid company selected"

    print(f"\n{name}: {result}")
    print(f"Score: {score}%")

    if reason:
        print("Reason:", reason)

    # Save to CSV file
    with open("candidates_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, cgpa, ",".join(skills), experience, company, score, result])

    again = input("\nCheck another candidate? (yes/no): ").lower()
    if again == "no":
        break

print("Good luck with your career!")