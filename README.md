
# Android Connections Forensics

This software enables a forensic investigator to map each connection to its originating process.

It doesn't require root privliges on the system, but do require adb & USB debugging.
# Supported OS

ACF works currently only on Linux (Ubuntu 14.04)


# Installation
    git clone https://github.com/CyberHatcoil/ACF.git
    cd ACF
    pip install -r requirments.txt

# Usage

Make sure you device is connected, usb debugging is enabled and authorized.

    adb devices

To run Acf:

    python acf.py -d [Device serial number]

Filter by process name match:

    python acf.py -d [Device serial number] -f facebook

Filter by process owner:

    python acf.py -d [Device serial number] -u user
    python acf.py -d [Device serial number] -u system
    python acf.py -d [Device serial number] -u root

# Output
ACF create 3 different output types:

1. console output - live connections

2. acm-log file - live connections

3. metadata file - external IP's metadata results

acm-log example:
<img src="http://i.imgur.com/CkRp6LV.png" />

#Metadata Plugins
Acf extract metadata to every external IP address.

Current Plugins:

1. IP Info - geolocation, provider etc..

2. IP Rep - alienvault ip blacklist database.

3. VirusTotal - virustotal ip lookup.

4. Whois

# Contact Us

itaykrk [ [ AT ] ]gmail.com
