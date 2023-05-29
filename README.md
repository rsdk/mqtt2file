# Simple MQTT to CSV logger
For use with a raspberry pi and a MQTT Broker like Mosquitto.

Two logging Modes are available:
MQTT Topic Prefix or Topic List
## MQTT Topic Prefix
All MQTT Topics with a definable Prefix will be logged to daily CSV Files. 

## MQTT Topic List
Add Topics to the List in topics.py

## CSV Filenames
The file Name is determined by the MQTT Topic and the date.

Example (energydata is the Prefix) :
`energydata/fridge/power -> energydata.fridge.power_2023-05-15.csv`

CSV example:
```
2023-05-25T09:54:17.757944,19.16118581488867
2023-05-25T09:54:17.773440,13.628220241093041
```
## Todo
- Better installation
## Install
copy files tp `/home/pi/scripts/mqtt2file`
### Poetry
1. Install requirement Rust
`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
2. Install requirement Openssl Lib `sudo apt install libssl-dev`
3. Install Poetry `curl -sSL https://install.python-poetry.org | python3 -`
3. create directories in `/home/pi/` `mkdir energydata/csv`

### Install as Systemd Service
1. `cp mqtt2file.service /etc/systemd/system/`
2. `sudo systemctl daemon-reload`
3. `sudo systemctl enable mqtt2file.service`
4. `sudo systemctl start mqtt2file.service`

## Configure
1. Set MQTTHOST in mqtt2file.py
2. Set MQTTTOPICPREFIX in mqtt2file.py
