def analyze_port(port):
    risks = {
        21: ("High", "FTP insecure che. Use SFTP."),
        22: ("Medium", "SSH secure che pan strong password joiye."),
        23: ("High", "Telnet unsafe che. Avoid karo."),
        80: ("Low", "HTTP che pan encrypted nathi."),
        443: ("Low", "HTTPS secure communication che."),
        3389: ("High", "RDP attack mate vulnerable che.")
    }

    if port in risks:
        return risks[port]
    else:
        return ("Unknown", "No major risk.")