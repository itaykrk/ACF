import urllib3
from metadata import MetadataPlugin


class IpRepPlugin(MetadataPlugin):
    def __init__(self):
        MetadataPlugin.__init__(self)
        self.name = "IpRep"
        self._reputation_list = self.get_rep_list()
        self._is_rep_list = True

    def run(self):
        if not self._is_rep_list:
            return ""
        res = ""
        if self._dst_ip in self._reputation_list:
            res = "Blacklisted by AlienVault reputation data"
        return res

    def get_rep_list(self):
        alientvault_resp = ""
        try:
            req = urllib3.Request(
                'http://reputation.alienvault.com/reputation.data')
            req.add_header(
                'User-agent',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
            response = urllib3.urlopen(req)
            alientvault_resp = response.read()
        except Exception as e:
            self._is_rep_list = False
        return alientvault_resp
