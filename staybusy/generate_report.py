import pandas as pd
import datetime

# Load internship data (replace with actual data source)
def load_data(file_path):
    return pd.read_csv(file_path)

# Filter multinational companies
def filter_multinational(df):
    return df[df['is_multinational'] == True]

# Generate email template
def generate_email(name, company, position, contact_email):
    return f"""\n**To:** {contact_email}\n**Subject:** Interest in {position} Internship at {company}\n\nDear {name},\n\nI hope this email finds you well. I am writing to express my interest in the {position} internship at {company}.\n\nI have a strong background in [your field of expertise] and am eager to contribute to your team. I would love to discuss how my skills align with this opportunity.\n\nWould you be available for a brief conversation regarding this role? Please let me know a time that works for you.\n\nBest regards,\n[Your Name]\n[Your Email]\n[Your LinkedIn]\n"""

# Generate Markdown report
def generate_report(df, field, center, radius, output_file="internship_report.md"):
    date_generated = datetime.date.today().strftime("%Y-%m-%d")
    multinational_df = filter_multinational(df)
    
    with open(output_file, "w") as f:
        f.write(f"# Internship Report – {field} Opportunities in {center} ({radius} km radius)\n")
        f.write(f"\n📅 **Report Date:** {date_generated}\n")
        f.write(f"📍 **Search Location:** {center}, within {radius} km\n")
        f.write(f"🏢 **Companies Verified:** {len(multinational_df)}\n")
        f.write(f"📌 **Internships Found:** {len(df)}\n")
        f.write("\n---\n")
        
        f.write("## 1. Internship Listings\n")
        for _, row in df.iterrows():
            f.write(f"\n- **Company:** {row['company']}\n")
            f.write(f"  - **Job Title:** {row['title']}\n")
            f.write(f"  - **Location:** {row['location']}\n")
            f.write(f"  - **Apply:** [Link]({row['apply_link']})\n")
            f.write(f"  - **Multinational:** {'✅ Yes' if row['is_multinational'] else '❌ No'}\n")
        
        f.write("\n---\n")
        f.write("## 2. Draft Outreach Emails\n")
        for _, row in multinational_df.iterrows():
            email_template = generate_email("Hiring Manager", row['company'], row['title'], row['contact_email'])
            f.write(email_template + "\n---\n")
        
    print(f"Report generated: {output_file}")

# Example usage (update with actual file path)
file_path = "internships.csv"  # Replace with actual CSV file
internships_df = load_data(file_path)
generate_report(internships_df, field="HR", center="Padova", radius=50)

