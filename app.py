import psutil
import time

def main():
    # process names should not have leading or trailing spaces
    # each element is array with process name and time elapsed
    tracked_processes = []
    try:
        with open("times.txt") as f:
            for line in f:
                tracked_processes.append([line.split(" ")[0], float(line.split(" ")[1])])
    except:
        print("Save file missing or corrupted")
        tracked_processes = [["Spotify.exe", 0]]
    print(tracked_processes)
    last_time = time.time()
    # time limit in seconds
    max_time = 5
    while True:
        try:
            for proc in psutil.process_iter(['name']):
                for process in tracked_processes:
                    # match name
                    if proc.info['name'] == process[0]:
                        # kill the process if time limit exceeded
                        print(time.time() - last_time + process[1])
                        if time.time() - last_time + process[1]> max_time:
                            print(f"Killing {process[0]} because time limit was reached")
                            proc.kill()
                        # add to the elapsed time
                        process[1] += time.time() - last_time
            # reset last_time
            last_time = time.time()
            time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting")
            # save state
            with open("times.txt", "w") as f:
                for process in tracked_processes:
                    f.write(f"{process[0].strip()} {time.time() - last_time + process[1]}\n")
            break
if __name__ == "__main__":
    main()