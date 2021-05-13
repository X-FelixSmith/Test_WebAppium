import _thread
import logging
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


#
def loop(nloop, nsec, lock):
    logging.info(f"start loop{nloop} at " + ctime())
    sleep(nsec)
    logging.info(f"end loop{nloop} at " + ctime())
    lock.release()


def main():
    logging.info("start all at " + ctime())

    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass
    logging.info("end all at " + ctime())


# def loop():
#     logging.info("start loop0 at " + ctime())
#
#     sleep(4)
#
#     logging.info("end loop0 at " + ctime())
#
#
# def loop1():
#     logging.info("start loop1 at " + ctime())
#
#     sleep(2)
#
#     logging.info("end loop1 at " + ctime())


if __name__ == "__main__":
    main()
