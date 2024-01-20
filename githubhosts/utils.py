from pathlib import Path
from typing import List, Tuple
import ping3
from datetime import datetime

def write_hosts(hosts:List[Tuple[str,str]]):
    with open(Path(__file__).parent / 'hosts', 'w') as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for host in hosts:
            f.write(f"{host[0]} {host[1]}\n")
        f.write(f"# Update Time: {now}")
        

def ip_ping(ip:str)->int:
    """
    测试一个ip的联通性，返回延迟毫秒
    """
    try:
        delay = ping3.ping(ip, timeout=1)
        if not delay:
            return -1
        return int(delay*1000)
    except ping3.exceptions.PingError:
        return -1



