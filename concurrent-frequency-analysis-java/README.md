# Concurrent Frequency Analysis — Java

A multithreaded Java project that reads text data, counts fixed-length subsequences, and merges frequency tables concurrently.

The implementation uses Java threads together with a monitor built from `ReentrantLock` and `Condition` to coordinate access to shared data.

## Structure

- `Frekvenstabell.java` — frequency table and merge operation.
- `Subsekvensregister.java` — stores frequency tables and reads subsequences from files.
- `Monitor.java` — thread-safe access to the shared register.
- `Lesetrad.java` — reader thread.
- `Flettetrad.java` — merge thread.
- `KlarGjorData.java` — main program.

## Run

```bash
cd src
javac *.java
java KlarGjorData <path-to-metadata-file>
```

The data files used by the original assignment are not included in this repository.
