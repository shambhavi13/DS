
#### SUPERMARKET OPTIMIZATION

To run the code:

``bash
python market_opt.py
``


Following arguments are supported:
``bash
--data_directory : retail data directory
--log_directory : log file directory where results are logged
--support : sigma value defaulted to 4
--size_threshold: threshold value defaulted to 3 (support is equal and greater than threshold support)
``

you can pass args like

``bash
python market_opt.py --support=4
``

This method takes about 20-25 minutes depending on the computer.