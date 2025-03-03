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