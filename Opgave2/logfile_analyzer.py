import os.path

log_types = ['SUCCESS', 'ERROR', 'WARNING', 'INFO']

def open_logfile(file_path:str = "Opgave2/app_log.txt")->list[str]:
    try:
        path = os.path.join(file_path)
        with open(path, "r") as log_file:
            logs = []
            for line in log_file:
                logs.append(line.strip())
            return logs
    except:
        print("Could not read file!")
        return []
    
def write_by_log_type(logtype:str, logs)->bool:
    path = os.path.join("Opgave2", logtype.lower() + "_logs.txt")
    try:
        with open(path, "w") as file:
            for log in logs:
                file.write(log +"\n")
        return True
    except:
        print("Something went wrong trying to write to {path}!")
        return False

def write_logs(logs)->None:
    for log_type in log_types:
        logs_of_type = get_logs_by_type(log_type, logs)
        write_by_log_type(log_type, logs_of_type)

def get_logs_by_type(logtype:str, logs:list[str])->list[str]:
    logs_of_type = []
    for log in logs:
        if logtype in log:
            logs_of_type.append(log)
    return logs_of_type

def main():
    logs = open_logfile()

if __name__ == "__main__":
    main()