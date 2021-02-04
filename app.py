import psutil
import time

def main():
    tracked_processes = ["Spotify.exe"]
    start_time = time.time()
    # time limit in seconds
    max_time = 5
    while True:
        try:
            for proc in psutil.process_iter(['name']):
                for pname in tracked_processes:
                    if proc.info['name'] == pname and time.time() - start_time > max_time:
                        print(f"Killing {pname} because time limit was reached")
                        proc.kill()

            time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting")
            break
if __name__ == "__main__":
    main()