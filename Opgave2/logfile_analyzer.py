def open_logfile(file_path:str = "Opgave2/app_log.txt")->list[str]:
    try:
        with open(file_path, "r") as log_file:
            logs = []
            for line in log_file:
                logs.append(line.strip())
            return logs
    except:
        print("Could not read file!")
        return []

def main():
    logs = open_logfile()

if __name__ == "__main__":
    main()