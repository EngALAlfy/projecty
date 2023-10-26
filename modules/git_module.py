from openpyxl import Workbook
from github import Auth
from github import Github
import pathlib


def get_repos():
    auth = Auth.Token("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")
    g = Github(auth=auth)
    repos = g.get_user().get_repos()
            
    return repos

# Load the workbook
workbook = Workbook()

repos_worksheet = workbook.active
    
# header
repos_worksheet[f"C{4}"] = "Name"
repos_worksheet[f"D{4}"] = "Full Name"
repos_worksheet[f"E{4}"] = "URL"
repos_worksheet[f"F{4}"] = "Private"
repos_worksheet[f"G{4}"] = "Owner"
        
print("Loading....")
for index,repo in enumerate(get_repos()):
    if repo.owner.name == "ALALFY APPS":
        repos_worksheet[f"C{index+5}"] = repo.name
        repos_worksheet[f"D{index+5}"] = repo.full_name
        repos_worksheet[f"E{index+5}"] = repo.url
        repos_worksheet[f"F{index+5}"] = repo.private
        repos_worksheet[f"G{index+5}"] = repo.owner.name
# Save the workbook
workbook.save(f'{pathlib.Path(__file__).parent.resolve()}/repos_output.xlsx')  # This will save the modified file

# Close the workbook
workbook.close()
print("Done")