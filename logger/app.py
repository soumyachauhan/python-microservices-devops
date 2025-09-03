import time

def log_writer():
    with open("app.log", "a") as f:
        while True:
            message = "Logger running...\n"
            f.write(message)
            f.flush()
            print(message, end="")   
            time.sleep(10)

if __name__ == "__main__":
    log_writer()