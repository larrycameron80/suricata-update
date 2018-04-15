index = {'sources': {'oisf/trafficid': {'vendor': 'OISF', 'license': 'MIT', 'url': 'https://raw.githubusercontent.com/jasonish/suricata-trafficid/master/rules/traffic-id.rules', 'min-version': '4.0.0', 'support-url': 'https://redmine.openinfosecfoundation.org/', 'summary': 'Suricata Traffic ID ruleset'}, 'ptresearch/attackdetection': {'vendor': 'Positive Technologies', 'description': u'The Attack Detection Team searches for new vulnerabilities and 0-days, reproduces it and creates PoC exploits to understand how these security flaws work and how related attacks can be detected on the network layer. Additionally, we are interested in malware and hackers\u2019 TTPs, so we develop Suricata rules for detecting all sorts of such activities.\n', 'license': 'Custom', 'url': 'https://raw.githubusercontent.com/ptresearch/AttackDetection/master/pt.rules.tar.gz', 'license-url': 'https://raw.githubusercontent.com/ptresearch/AttackDetection/master/LICENSE', 'summary': 'Positive Technologies Attack Detection Team ruleset'}, 'sslbl/ssl-fp-blacklist': {'url': 'https://sslbl.abuse.ch/blacklist/sslblacklist.rules', 'vendor': 'Abuse.ch', 'license': 'Non-Commercial', 'summary': 'Abuse.ch SSL Blacklist'}, 'et/open': {'url': 'https://rules.emergingthreats.net/open/suricata-%(__version__)s/emerging.rules.tar.gz', 'vendor': 'Proofpoint', 'license': 'MIT', 'summary': 'Emerging Threats Open Ruleset'}, 'scwx/security': {'vendor': 'Secureworks', 'description': 'Broad ruleset composed of malware rules and other security-related countermeasures, and curated by the Secureworks Counter Threat Unit research team.\n', 'license': 'Commercial', 'url': 'https://ws.secureworks.com/ti/ruleset/%(secret-code)s/Suricata_suricata-security_latest.tgz', 'summary': 'Secureworks suricata-security ruleset.', 'min-version': '2.0.9', 'subscribe-url': 'https://www.secureworks.com/contact/ (Please reference CTU Countermeasures)', 'parameters': {'secret-code': {'prompt': 'Secureworks Threat Intelligence Authentication Token'}}}, 'scwx/malware': {'vendor': 'Secureworks', 'description': 'High-fidelity, high-priority ruleset composed mainly of malware-related countermeasures and curated by the Secureworks Counter Threat Unit research team.\n', 'license': 'Commercial', 'url': 'https://ws.secureworks.com/ti/ruleset/%(secret-code)s/Suricata_suricata-malware_latest.tgz', 'summary': 'Secureworks suricata-malware ruleset.', 'min-version': '2.0.9', 'subscribe-url': 'https://www.secureworks.com/contact/ (Please reference CTU Countermeasures)', 'parameters': {'secret-code': {'prompt': 'Secureworks Threat Intelligence Authentication Token'}}}, 'et/pro': {'replaces': ['et/open'], 'vendor': 'Proofpoint', 'description': 'Proofpoint ET Pro is a timely and accurate rule set for detecting and blocking advanced threats\n', 'license': 'Commercial', 'url': 'https://rules.emergingthreatspro.com/%(secret-code)s/suricata-%(__version__)s/etpro.rules.tar.gz', 'summary': 'Emerging Threats Pro Ruleset', 'subscribe-url': 'https://www.proofpoint.com/us/threat-insight/et-pro-ruleset', 'parameters': {'secret-code': {'prompt': 'Emerging Threats Pro access code'}}}}, 'version': 1}