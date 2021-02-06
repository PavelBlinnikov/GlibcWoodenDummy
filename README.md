This repository can help you figure out what attacks work for your libc and what not.<br />The only dependency is ```patchelf```

```
export MALLOC_CHECK_=0
make all
python main_checker.py
```
