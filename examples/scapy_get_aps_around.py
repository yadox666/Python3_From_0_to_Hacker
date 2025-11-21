from scapy.all import *
import json
from scapy.layers.dot11 import Dot11, Dot11Beacon

# Path to the JSON file with OUI data
OUI_JSON_FILE = "oui_list.json"

# Wi-Fi interface to use for scanning (e.g., "wlan0")
INTERFACE = "wlan0mon"

# Load the OUI data from the JSON file
def load_oui_data():
    try:
        with open(OUI_JSON_FILE, "r") as f:
            oui_data = json.load(f)
            # Convert the OUI list to a dictionary for faster lookup
            return {entry["oui"]: entry["organization"] for entry in oui_data}
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading OUI data: {e}")
        return {}


# Extract the OUI part (first three octets) from a BSSID
def get_oui_from_bssid(bssid):
    return "".join(bssid.split(":")[:3]).upper()


# Callback function for processing packets
def packet_handler(packet, oui_lookup):
    # Check if the packet is a beacon frame from an AP
    if packet.haslayer(Dot11Beacon):
        bssid = packet[Dot11].addr2  # Get the BSSID (MAC address of the AP)
        ssid = packet[Dot11Elt].info.decode() if packet[Dot11Elt].info else "Hidden SSID"
        oui = get_oui_from_bssid(bssid)  # Extract OUI part of the BSSID
        organization = oui_lookup.get(oui, "Unknown")  # Lookup the organization

        # Print AP information
        print(f"SSID: {ssid}, BSSID: {bssid}, Organization: {organization}")

# Main function
def main():
    # Load the OUI data
    oui_lookup = load_oui_data()
    if not oui_lookup:
        print("OUI data could not be loaded.")
        return

    print("Starting Wi-Fi scan... (Press Ctrl+C to stop)")

    # Start sniffing for 802.11 beacon frames on the specified interface
    sniff(iface=INTERFACE, prn=lambda pkt: packet_handler(pkt, oui_lookup), store=0)

if __name__ == "__main__":
    main()
