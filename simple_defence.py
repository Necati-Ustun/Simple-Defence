import honeypot
import pyfiglet
import mitm_hunter
import sniffer
import log_analyzer

sniffer = sniffer
honeypotService = honeypot
mitmHunter = mitm_hunter.MITMHunter
logAnalyzer = log_analyzer


def menu():
    ascii_banner = pyfiglet.figlet_format("Simple Defence")
    print(ascii_banner)
    print("[*] Necati Üstün\n")
    print("[1] Network Sniffer\n"
          "[2] MITM Hunter\n"
          "[3] Honeypot\n"
          "[4] Log Analyzer\n"
          "[Q] Quit")


def main():
    stop = True
    menu()

    while stop:

        choice = input("Select your choice >")
        if choice == "1":
            sniffer.sniffing("Wi-Fi")
        elif choice == "2":
            mitmHunter.mitm_hunter(mitmHunter)
        elif choice == "3":
            honeypot.honeypot_enable()
        elif choice == "4":
            log_analyzer.read_pcap()
        elif choice == "q" or choice == "Q":
            stop = False
        else:
            menu()


if __name__ == '__main__':
    main()




