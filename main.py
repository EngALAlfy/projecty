import crayons
import openpyxl
import inflect

def get_plural(word):
    p = inflect.engine()
    return p.plural(word)

projects_location = "./projects"

user_input = input(crayons.blue("Enter a modules spreated by (,) (or 'q' to quit): "))

if user_input == 'q':
    exit(0)

user_input = user_input.split(",")
modules = [{"name": value.capitalize(),"plural":get_plural(value.capitalize())} for value in user_input]

for module in modules:
    module_time = input(crayons.blue(f"{module['plural']}: Expected time in hours: "))
    module_curd = input(crayons.blue(f"{module['plural']}: CURD ? [yes]: "))
    module_generate = input(crayons.blue(f"{module['plural']}: Generate Models,Request,Controllers etc ? [yes]: "))
    if(module_generate == "yes" or not module_generate):
        module_generate = True
    if(module_curd == "yes" or not module_generate):
        module_generate = True
    module["time"] = module_time
    module["curd"] = module_curd
    module["generate"] = module_generate
    
print(crayons.red("Collecting modules finished"))
print(crayons.yellow("Generating modules tasks"))



tasks = []
for module in modules:
    if(module["curd"] == True):
        tasks.append({"name":f"{module['plural']}: create item","time":int(module['time'])/5})
        tasks.append({"name":f"{module['plural']}: Update item","time":int(module['time'])/5})
        tasks.append({"name":f"{module['plural']}: Delete item","time":int(module['time'])/5})
        tasks.append({"name":f"{module['plural']}: List items","time":int(module['time'])/5})
        tasks.append({"name":f"{module['plural']}: Show item","time":int(module['time'])/5})
    else:
        tasks.append({"name":f"{module['plural']}","time":int(module['time'])})

# Load the workbook
workbook = openpyxl.load_workbook('template.xlsx')

tasks_worksheet = workbook["tasks"]
modules_worksheet = workbook["modules"]

# Access a specific cell and set its value
for index,task in enumerate(tasks):
    tasks_worksheet[f"C{index+5}"] = task["name"]
    tasks_worksheet[f"D{index+5}"].number_format = '[hh]:mm'
    tasks_worksheet[f"D{index+5}"] = task["time"]
    
for index,module in enumerate(modules):
    modules_worksheet[f"C{index+5}"] = module["plural"]
    modules_worksheet[f"D{index+5}"].number_format = '[hh]:mm'
    modules_worksheet[f"D{index+5}"] = module["time"]
# Save the workbook
workbook.save('output.xlsx')  # This will save the modified file

# Close the workbook
workbook.close()
