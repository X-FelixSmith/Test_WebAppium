import _thread
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


def loop(nloop, nsec):
    logging.info(f"start loop{nloop} at " + ctime())
    sleep(nsec)
    logging.info(f"end loop{nloop} at " + ctime())


def main():
    logging.info("start all at " + ctime())
    threads = []

    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    logging.info("end all at " + ctime())


if __name__ == "__main__":
    main()
