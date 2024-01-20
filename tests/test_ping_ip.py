from githubhosts.ali import AliPing
from githubhosts.utils import ip_ping

def test_ip_ping():
    assert ip_ping('114.114.114.114') >= 0 and ip_ping('114.114.114.114') < 1000
    assert ip_ping('127.0.0.2') == -1
    
def test_ali_get_ip():
    ali_ping = AliPing()
    all_ips = ali_ping.get_all_ip("github.com")
    assert len(all_ips) != 0

    valid_ips =[i for i in all_ips if ip_ping(i)>0]
    assert len(valid_ips) != 0