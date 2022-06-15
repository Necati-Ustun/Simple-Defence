import subprocess
import time
import winsound
import smtp

mailService = smtp.SmtpMailService()


class MITMHunter:

    def mitm_hunter(self):

        run = True
        while run:
            choice = input("Press enter for detect arp-spoofing attack >")

            if choice == "Q" or choice == "q":
                run = False
            else:
                while True:
                    subprocess.call("arp -a 192.168.43.1")   # bağlı olduğunuz switch yada router cihazınızın ip adresi
                    get_output = subprocess.getoutput("arp -a 192.168.43.1")
                    output_log = open("Logs.txt", "w")
                    output_log.write(get_output)
                    output_log.close()
                    log = open("Logs.txt", "r")
                    if log.mode == "r":
                        contents = log.read()
                        if "gateway mac address" in contents:  # bağlı olduğunuz gateway'in mac adresi
                            print("ARP POISONING: FALSE")
                        elif "gateway mac address" != contents: # bağlı olduğunuz gateway'in mac adresi
                            print("[!] ARP POISONING DETECTED!")
                            winsound.PlaySound("redalarm", winsound.SND_FILENAME)
                            mailService.send_mail("ARP-Spoof Attack Detected!",
                                              f"Man in the middle info : {contents}")

                            break
                    time.sleep(10)
